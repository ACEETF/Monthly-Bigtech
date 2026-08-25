# -*- coding: utf-8 -*-
"""openpyxl이 생성한 워크북에 수식 결과값(캐시)을 주입한다.

openpyxl은 수식을 문자열로만 기록하므로 캐시값이 없어 Excel 외의 뷰어
(미리보기, pandas, 일부 모바일 앱)에서 빈 칸으로 보인다. 이 스크립트는
`formulas` 패키지로 전체 워크북을 실제 평가한 뒤 각 수식 셀에 <v> 값을
삽입한다. 수식 자체는 그대로 남으므로 입력값을 바꾸면 정상 재계산된다.

사용법: python3 scripts/inject_cached_values.py <파일.xlsx>
오류(#REF!, #DIV/0! 등)가 하나라도 있으면 종료코드 1로 실패한다.
"""
import re
import shutil
import sys
import zipfile
from xml.sax.saxutils import escape

import formulas


def evaluate(path):
    xl = formulas.ExcelModel().loads(path).finish()
    sol = xl.calculate()
    values, errors = {}, []
    key_re = re.compile(r"^'\[.*?\]([^']+)'!([A-Z]+\d+)$")
    for k, v in sol.items():
        m = key_re.match(k)
        if not m:
            continue
        sheet, ref = m.group(1).upper(), m.group(2)
        try:
            val = v.value[0, 0]
        except Exception:
            continue
        val = val.item() if hasattr(val, "item") else val
        values.setdefault(sheet, {})[ref] = val
        if isinstance(val, str) and val.startswith("#"):
            errors.append(f"{sheet}!{ref} = {val}")
    return values, errors


def sheet_name_map(zf):
    """xl/worksheets/sheetN.xml → 시트명 (rels 속성 순서에 무관하게 파싱)"""
    wb = zf.read("xl/workbook.xml").decode("utf-8")
    rels = zf.read("xl/_rels/workbook.xml.rels").decode("utf-8")
    rid_to_target = {}
    for tag in re.findall(r"<Relationship\b[^>]*/?>", rels):
        rid = re.search(r'Id="([^"]+)"', tag)
        tgt = re.search(r'Target="([^"]+)"', tag)
        if rid and tgt:
            t = tgt.group(1).lstrip("/")
            rid_to_target[rid.group(1)] = t if t.startswith("xl/") else "xl/" + t
    out = {}
    for tag in re.findall(r"<sheet\b[^>]*/?>", wb):
        name = re.search(r'name="([^"]+)"', tag)
        rid = re.search(r'r:id="([^"]+)"', tag)
        if name and rid and rid.group(1) in rid_to_target:
            out[rid_to_target[rid.group(1)]] = name.group(1)
    return out


CELL_RE = re.compile(r"<c\b[^>]*/>|<c\b[^>]*>.*?</c>", re.S)


def patch_sheet(xml, cell_values):
    def repl(m):
        cell = m.group(0)
        fm = re.search(r"<f[^>]*>(.*?)</f>|<f[^>]*/>", cell, re.S)
        if not fm:
            return cell
        rm = re.search(r'\br="([A-Z]+\d+)"', cell)
        if not rm or rm.group(1) not in cell_values:
            return cell
        val = cell_values[rm.group(1)]
        if val is None or (isinstance(val, str) and val == ""):
            return cell
        cell = re.sub(r"<v\s*/>|<v>.*?</v>", "", cell, flags=re.S)
        if isinstance(val, bool):
            head, vtag = ' t="b"', "<v>%d</v>" % int(val)
        elif isinstance(val, (int, float)):
            head, vtag = "", "<v>%s</v>" % repr(float(val))
        else:
            head, vtag = ' t="str"', "<v>%s</v>" % escape(str(val))
        cell = re.sub(r'\s+t="[^"]*"', "", cell, count=1)
        cell = re.sub(r"^<c\b", "<c" + head, cell)
        return cell.replace("</c>", vtag + "</c>")

    return CELL_RE.sub(repl, xml)


def main(path):
    values, errors = evaluate(path)
    total = sum(len(v) for v in values.values())
    print(f"평가된 셀: {total}개 / 오류: {len(errors)}개")
    for e in errors:
        print("  ERROR", e)
    if errors:
        return 1

    src = path + ".orig"
    shutil.move(path, src)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(
        path, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        names = sheet_name_map(zin)
        patched = 0
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename in names:
                sheet = names[item.filename].upper()
                if sheet in values:
                    xml = data.decode("utf-8")
                    new = patch_sheet(xml, values[sheet])
                    if new != xml:
                        patched += 1
                    data = new.encode("utf-8")
            zout.writestr(item, data)
    shutil.os.remove(src)
    print(f"값이 주입된 시트: {patched}개 → {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

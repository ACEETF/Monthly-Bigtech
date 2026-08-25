# -*- coding: utf-8 -*-
"""적립식 투자 복리효과 시뮬레이션 워크북 생성

산출물: 투자시뮬레이션/적립식투자_복리효과_시뮬레이션.xlsx
모든 수치는 엑셀 수식으로 작성되어 '가정' 시트의 입력값을 바꾸면 전체가 재계산됨.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.comments import Comment

FONT = "맑은 고딕"

# ── 스타일 ────────────────────────────────────────────────────────────────
def F(size=10, bold=False, color="000000"):
    return Font(name=FONT, size=size, bold=bold, color=color)

TITLE     = F(16, True, "1F3864")
SUBTITLE  = F(10, False, "595959")
H_SECTION = F(12, True, "1F3864")
H_TBL     = F(10, True, "FFFFFF")
NORMAL    = F(10)
INPUT     = F(10, False, "0000FF")     # 하드코딩 입력값
LINKED    = F(10, False, "008000")     # 타 시트 참조
EMPH      = F(11, True, "C00000")
NOTE      = F(9, False, "808080")

FILL_HDR   = PatternFill("solid", fgColor="1F3864")
FILL_INPUT = PatternFill("solid", fgColor="FFFF00")
FILL_BAND  = PatternFill("solid", fgColor="F2F2F2")
FILL_HILI  = PatternFill("solid", fgColor="FFF2CC")
FILL_GOOD  = PatternFill("solid", fgColor="E2EFDA")
FILL_BAD   = PatternFill("solid", fgColor="FCE4E4")

thin = Side(style="thin", color="BFBFBF")
BOX  = Border(left=thin, right=thin, top=thin, bottom=thin)

WON = '#,##0;(#,##0);-'
PCT = '0.0%;(0.0%);-'
MUL = '0.00"배"'
YR  = '0"년"'
AGE = '0"세"'

def put(ws, ref, value, font=NORMAL, fmt=None, fill=None, align=None, border=True, wrap=False):
    c = ws[ref]
    c.value = value
    c.font = font
    if fmt:   c.number_format = fmt
    if fill:  c.fill = fill
    if border: c.border = BOX
    c.alignment = Alignment(horizontal=align or ("left" if isinstance(value, str) and not str(value).startswith("=") else "right"),
                            vertical="center", wrap_text=wrap)
    return c

def header_row(ws, row, labels, start_col=2, widths=None):
    for i, lab in enumerate(labels):
        c = ws.cell(row=row, column=start_col + i, value=lab)
        c.font = H_TBL
        c.fill = FILL_HDR
        c.border = BOX
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 30

def set_widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w

def section(ws, ref, text):
    c = ws[ref]; c.value = text; c.font = H_SECTION
    return c

wb = Workbook()

# ════════════════════════════════════════════════════════════════════════
# 1. 가정 (Assumptions)
# ════════════════════════════════════════════════════════════════════════
a = wb.active
a.title = "가정"
a.sheet_view.showGridLines = False
set_widths(a, {"A": 2, "B": 26, "C": 18, "D": 6, "E": 62})

a["B2"] = "적립식 투자 복리효과 시뮬레이션"; a["B2"].font = TITLE
a["B3"] = "노란색 음영 + 파란색 글씨 셀만 수정하시면 모든 시트가 자동으로 재계산됩니다."
a["B3"].font = SUBTITLE

section(a, "B5", "■ 기본 가정")
header_row(a, 6, ["항목", "값", "", "설명"])
a.merge_cells("D6:E6")

rows = [
    ("월 납입액 (원)",     500000,      WON, True,  "기본 시나리오의 매월 적립 금액"),
    ("연 수익률",          0.05,        PCT, True,  "세전·보수 차감 전 기대수익률 (연 5% 가정)"),
    ("월 수익률",          "=C8/12",    '0.0000%', False, "연 수익률 ÷ 12 (월복리 환산)"),
    ("연 환산 복리계수",   "=(1+C9)^12", '0.0000', False, "1년간 월복리 누적 배수 = (1+월수익률)^12"),
]
r = 7
for label, val, fmt, is_input, desc in rows:
    put(a, f"B{r}", label, F(10, True))
    put(a, f"C{r}", val, INPUT if is_input else NORMAL, fmt, FILL_INPUT if is_input else None, align="right")
    put(a, f"D{r}", "", border=False)
    put(a, f"E{r}", desc, NOTE, align="left", wrap=True)
    a.merge_cells(f"D{r}:E{r}")
    r += 1

section(a, "B12", "■ 연령 가정")
header_row(a, 13, ["항목", "값", "", "설명"])
a.merge_cells("D13:E13")
age_rows = [
    ("빠른 시작 연령",  30, AGE, True, "시나리오 A: 일찍 시작하는 투자자"),
    ("늦은 시작 연령",  40, AGE, True, "시나리오 B: 10년 늦게 시작하는 투자자"),
    ("은퇴(목표) 연령", 60, AGE, True, "두 시나리오 모두 이 연령에 투자를 종료"),
]
r = 14
for label, val, fmt, is_input, desc in age_rows:
    put(a, f"B{r}", label, F(10, True))
    put(a, f"C{r}", val, INPUT, fmt, FILL_INPUT, align="right")
    put(a, f"D{r}", "", border=False)
    put(a, f"E{r}", desc, NOTE, align="left", wrap=True)
    a.merge_cells(f"D{r}:E{r}")
    r += 1

section(a, "B18", "■ 계산 방식 및 유의사항")
notes = [
    "① 적립 방식: 매월 말 정액 납입(기말급 연금, ordinary annuity), 월복리 재투자 가정.",
    "② 최종자산 = 월납입액 × [ (1+월수익률)^납입개월수 − 1 ] ÷ 월수익률",
    "③ 납입원금 = 월납입액 × 납입개월수,  투자수익 = 최종자산 − 납입원금",
    "④ 연 5% 수익률은 사용자가 제시한 가정치이며 특정 상품의 확정수익률이 아닙니다.",
    "⑤ 세금(배당소득세·양도소득세), 판매보수·운용보수, 매매비용, 물가상승률은 반영하지 않았습니다.",
    "⑥ 실제 수익률은 매년 변동하므로 본 자료는 복리 구조를 설명하기 위한 예시입니다.",
    "⑦ 투자원금 손실이 발생할 수 있으며 과거·가정 수익률이 미래 수익률을 보장하지 않습니다.",
]
r = 19
for n in notes:
    c = a.cell(row=r, column=2, value=n)
    c.font = NOTE if r > 20 else F(9, False, "404040")
    c.alignment = Alignment(horizontal="left", vertical="center")
    a.merge_cells(f"B{r}:E{r}")
    r += 1

a["C7"].comment = Comment("사용자 제시 가정: 월 50만원 정액 적립", "시뮬레이션")
a["C8"].comment = Comment("사용자 제시 가정: 연 수익률 5% (월복리 환산 적용)", "시뮬레이션")

# 공통 참조
PMT = "가정!$C$7"
RM  = "가정!$C$9"
AGE_E, AGE_L, AGE_R = "가정!$C$14", "가정!$C$15", "가정!$C$16"

def fv(pmt, n):
    """기말급 연금 미래가치 수식 문자열"""
    return f"{pmt}*((1+{RM})^({n})-1)/{RM}"

def pmt_needed(target, n):
    """목표자산 달성에 필요한 월납입액"""
    return f"({target})/(((1+{RM})^({n})-1)/{RM})"

# ════════════════════════════════════════════════════════════════════════
# 2. 1_기간별비교
# ════════════════════════════════════════════════════════════════════════
s = wb.create_sheet("1_기간별비교")
s.sheet_view.showGridLines = False
set_widths(s, {"A": 2, "B": 14, "C": 12, "D": 14, "E": 16, "F": 16, "G": 18, "H": 14, "I": 12, "J": 2})

s["B2"] = "① 월 50만원 적립 · 연 5% 가정 — 기간별 결과"; s["B2"].font = TITLE
s["B3"] = "같은 금액을 넣어도 '기간'이 길어질수록 투자수익이 원금을 압도합니다."
s["B3"].font = SUBTITLE

header_row(s, 5, ["구분", "납입기간", "납입개월", "월 납입액(원)", "납입원금(원)",
                  "투자수익(원)", "최종자산(원)", "수익/원금", "자산배수"])

periods = [10, 20, 30]
first = 6
for i, yrs in enumerate(periods):
    r = first + i
    band = FILL_BAND if i % 2 else None
    put(s, f"B{r}", f"{yrs}년 투자", F(10, True), fill=band, align="center")
    put(s, f"C{r}", yrs, INPUT, YR, FILL_INPUT, align="center")
    put(s, f"D{r}", f"=C{r}*12", NORMAL, '#,##0"개월"', band)
    put(s, f"E{r}", f"={PMT}", LINKED, WON, band)
    put(s, f"F{r}", f"=E{r}*D{r}", NORMAL, WON, band)
    put(s, f"G{r}", f"=H{r}-F{r}", NORMAL, WON, band)
    put(s, f"H{r}", "=" + fv(f"E{r}", f"D{r}"), F(10, True), WON, band)
    put(s, f"I{r}", f"=G{r}/F{r}", NORMAL, PCT, band)
    put(s, f"J{r}", f"=H{r}/F{r}", NORMAL, MUL, band)

s["B10"] = "핵심 메시지"; s["B10"].font = H_SECTION
msgs = [
    ('=" · 10년 → 30년으로 기간이 3배가 되면 납입원금은 3배지만, 최종자산은 "&TEXT(H8/H6,"0.0")&"배가 됩니다."'),
    ('=" · 30년 투자 시 최종자산의 "&TEXT(G8/H8,"0.0%")&"가 원금이 아닌 \'투자수익\'입니다. (10년 투자 시에는 "&TEXT(G6/H6,"0.0%")&")"'),
    ('=" · 마지막 10년(20년차→30년차)에만 자산이 "&TEXT(H8-H7,"#,##0")&"원 늘어납니다. 이는 첫 10년 증가분("&TEXT(H6,"#,##0")&"원)의 "&TEXT((H8-H7)/H6,"0.0")&"배입니다."'),
]
r = 11
for m in msgs:
    c = s.cell(row=r, column=2, value=m)
    c.font = F(10, False, "C00000") if r == 13 else F(10)
    c.alignment = Alignment(horizontal="left", vertical="center")
    s.merge_cells(f"B{r}:J{r}")
    r += 1

# 차트: 원금 vs 수익 누적막대
ch = BarChart()
ch.type = "col"; ch.grouping = "stacked"; ch.overlap = 100
ch.title = "기간별 납입원금 vs 투자수익 (월 50만원 · 연 5%)"
ch.y_axis.title = "금액(원)"; ch.x_axis.title = "투자기간"
ch.height, ch.width = 9, 18
data = Reference(s, min_col=6, max_col=7, min_row=5, max_row=8)
cats = Reference(s, min_col=2, min_row=6, max_row=8)
ch.add_data(data, titles_from_data=True); ch.set_categories(cats)
s.add_chart(ch, "B16")

# ════════════════════════════════════════════════════════════════════════
# 3. 2_시작시점비교
# ════════════════════════════════════════════════════════════════════════
t = wb.create_sheet("2_시작시점비교")
t.sheet_view.showGridLines = False
set_widths(t, {"A": 2, "B": 20, "C": 14, "D": 14, "E": 16, "F": 16, "G": 18, "H": 18, "I": 16, "J": 14, "K": 18})

t["B2"] = "② 30세 시작 vs 40세 시작 — 10년의 값어치"; t["B2"].font = TITLE
t["B3"] = "모두 60세까지 월 50만원(연 5%)을 적립했을 때의 결과입니다."
t["B3"].font = SUBTITLE

section(t, "B5", "■ 시작 연령별 결과 (60세 종료 기준)")
header_row(t, 6, ["시작 연령", "납입기간", "납입개월", "월 납입액(원)", "납입원금(원)",
                  "투자수익(원)", "60세 최종자산(원)", "30세 시작 대비 부족액(원)", "30세 시작 대비 달성률"])

start_ages = [30, 35, 40, 45, 50]
base_r = 7
for i, ag in enumerate(start_ages):
    r = base_r + i
    hi = FILL_HILI if ag in (30, 40) else (FILL_BAND if i % 2 else None)
    put(t, f"B{r}", ag, F(10, True) if ag in (30, 40) else NORMAL, AGE, hi, align="center")
    put(t, f"C{r}", f"={AGE_R}-B{r}", NORMAL, YR, hi, align="center")
    put(t, f"D{r}", f"=C{r}*12", NORMAL, '#,##0"개월"', hi)
    put(t, f"E{r}", f"={PMT}", LINKED, WON, hi)
    put(t, f"F{r}", f"=E{r}*D{r}", NORMAL, WON, hi)
    put(t, f"G{r}", f"=H{r}-F{r}", NORMAL, WON, hi)
    put(t, f"H{r}", "=" + fv(f"E{r}", f"D{r}"), F(10, True), WON, hi)
    put(t, f"I{r}", f"=H{r}-$H${base_r}", NORMAL, WON, hi)
    put(t, f"J{r}", f"=H{r}/$H${base_r}", NORMAL, PCT, hi)

section(t, "B14", "■ 늦게 시작한 사람이 '따라잡으려면' 얼마를 더 내야 하나?")
t["B15"] = "60세 시점 자산을 30세 시작(월 50만원)과 똑같이 맞추기 위해 필요한 월 납입액입니다."
t["B15"].font = SUBTITLE
header_row(t, 16, ["시작 연령", "납입기간", "따라잡기 필요 월납입액(원)", "월 50만원 대비 배수",
                   "월 추가부담액(원)", "총 납입원금(원)", "30세 시작 대비 추가 납입원금(원)", "그래도 남는 투자수익 차이(원)"])

catch_r = 17
for i, ag in enumerate(start_ages[1:], start=1):
    r = catch_r + i - 1
    src = base_r + i
    hi = FILL_HILI if ag == 40 else (FILL_BAND if i % 2 else None)
    put(t, f"B{r}", f"=$B${src}", F(10, True) if ag == 40 else NORMAL, AGE, hi, align="center")
    put(t, f"C{r}", f"=$C${src}", NORMAL, YR, hi, align="center")
    put(t, f"D{r}", "=" + pmt_needed(f"$H${base_r}", f"$D${src}"), F(10, True, "C00000"), WON, hi)
    put(t, f"E{r}", f"=D{r}/{PMT}", F(10, True), MUL, hi)
    put(t, f"F{r}", f"=D{r}-{PMT}", NORMAL, WON, hi)
    put(t, f"G{r}", f"=D{r}*$D${src}", NORMAL, WON, hi)
    put(t, f"H{r}", f"=G{r}-$F${base_r}", NORMAL, WON, hi)
    put(t, f"I{r}", f"=($H${base_r}-G{r})-($H${base_r}-$F${base_r})", NORMAL, WON, hi)

t["B22"] = "핵심 메시지"; t["B22"].font = H_SECTION
msgs2 = [
    '=" · 30세에 시작하면 60세에 "&TEXT(H7,"#,##0")&"원, 40세에 시작하면 "&TEXT(H9,"#,##0")&"원입니다. 10년 늦은 대가는 "&TEXT(-I9,"#,##0")&"원입니다."',
    '=" · 40세 시작자가 30세 시작자를 따라잡으려면 월 "&TEXT(D18,"#,##0")&"원, 즉 "&TEXT(E18,"0.00")&"배를 넣어야 합니다."',
    '=" · 그 결과 납입원금만 "&TEXT(H18,"#,##0")&"원을 더 부담하게 됩니다. 10년 먼저 시작했다면 내지 않아도 될 돈입니다."',
    '=" · 50세에 시작하면 월 "&TEXT(D20,"#,##0")&"원("&TEXT(E20,"0.00")&"배)이 필요합니다. 늦어질수록 따라잡기 부담은 기하급수적으로 커집니다."',
]
r = 23
for m in msgs2:
    c = t.cell(row=r, column=2, value=m)
    c.font = F(10, True, "C00000") if r in (24, 25) else F(10)
    c.alignment = Alignment(horizontal="left", vertical="center")
    t.merge_cells(f"B{r}:K{r}")
    r += 1

ch2 = BarChart()
ch2.type = "col"
ch2.title = "시작 연령별 60세 최종자산 (월 50만원 · 연 5%)"
ch2.y_axis.title = "60세 최종자산(원)"; ch2.x_axis.title = "시작 연령"
ch2.height, ch2.width = 9, 18
d2 = Reference(t, min_col=8, min_row=6, max_row=11)
c2 = Reference(t, min_col=2, min_row=7, max_row=11)
ch2.add_data(d2, titles_from_data=True); ch2.set_categories(c2)
ch2.legend = None
t.add_chart(ch2, "B29")

ch3 = BarChart()
ch3.type = "col"
ch3.title = "따라잡기 위해 필요한 월 납입액"
ch3.y_axis.title = "월 납입액(원)"; ch3.x_axis.title = "시작 연령"
ch3.height, ch3.width = 9, 18
d3 = Reference(t, min_col=4, min_row=16, max_row=20)
c3 = Reference(t, min_col=2, min_row=17, max_row=20)
ch3.add_data(d3, titles_from_data=True); ch3.set_categories(c3)
ch3.legend = None
t.add_chart(ch3, "H29")

# ════════════════════════════════════════════════════════════════════════
# 4. 3_적게빨리vs많이늦게
# ════════════════════════════════════════════════════════════════════════
u = wb.create_sheet("3_적게빨리vs많이늦게")
u.sheet_view.showGridLines = False
set_widths(u, {"A": 2, "B": 30, "C": 22, "D": 22, "E": 20, "F": 2})

u["B2"] = "③ 적은 금액이라도 빨리 vs 많은 금액을 늦게"; u["B2"].font = TITLE
u["B3"] = "'금액'보다 '시간'이 강하다는 것을 보여주는 세 가지 비교입니다. (연 5% · 60세 종료)"
u["B3"].font = SUBTITLE

def compare_block(ws, top, title, label_a, label_b,
                  pmt_a, months_a, pmt_b, months_b,
                  fv_a_formula, fv_b_formula, note):
    section(ws, f"B{top}", title)
    header_row(ws, top + 1, ["구분", label_a, label_b, "차이 (A − B)"], start_col=2)
    rows_def = [
        ("월 납입액(원)",   pmt_a,    pmt_b,    WON),
        ("납입 개월수",     months_a, months_b, '#,##0"개월"'),
        ("총 납입원금(원)", f"=C{top+2}*C{top+3}", f"=D{top+2}*D{top+3}", WON),
        ("투자수익(원)",    f"=C{top+6}-C{top+4}", f"=D{top+6}-D{top+4}", WON),
        ("60세 최종자산(원)", fv_a_formula, fv_b_formula, WON),
    ]
    for i, (lab, va, vb, fmt) in enumerate(rows_def):
        r = top + 2 + i
        is_last = (i == len(rows_def) - 1)
        fl = FILL_HILI if is_last else (FILL_BAND if i % 2 else None)
        fnt = F(10, True) if is_last else NORMAL
        put(ws, f"B{r}", lab, F(10, True), fill=fl)
        put(ws, f"C{r}", va, fnt, fmt, fl)
        put(ws, f"D{r}", vb, fnt, fmt, fl)
        put(ws, f"E{r}", f"=C{r}-D{r}", fnt, fmt, fl)
    put(ws, f"B{top+7}", "결론", F(10, True, "FFFFFF"), fill=FILL_HDR)
    c = ws.cell(row=top + 7, column=3, value=note)
    c.font = F(10, True, "C00000")
    c.alignment = Alignment(horizontal="left", vertical="center")
    c.border = BOX
    ws.merge_cells(start_row=top + 7, start_column=3, end_row=top + 7, end_column=5)
    ws.row_dimensions[top + 7].height = 22

# 비교 1: 30세 월30만 30년  vs  40세 월50만 20년
compare_block(
    u, 5,
    "■ 비교 1 : 30세부터 '월 30만원' 30년  vs  40세부터 '월 50만원' 20년",
    "A. 30세 시작 · 월 30만원", "B. 40세 시작 · 월 50만원",
    300000, f"=({AGE_R}-{AGE_E})*12", f"={PMT}", f"=({AGE_R}-{AGE_L})*12",
    "=" + fv("C7", "C8"), "=" + fv("D7", "D8"),
    '="A가 원금을 "&TEXT(D9-C9,"#,##0")&"원 적게 넣고도 최종자산은 "&TEXT(C11-D11,"#,##0")&"원 더 많습니다."'
)
u["C7"].font = INPUT; u["C7"].fill = FILL_INPUT

# 비교 2: 30세 월50만 10년만 납입 후 20년 거치 vs 40세 월50만 20년 납입
section(u, "B15", "■ 비교 2 : 30세부터 '10년만' 넣고 멈추기  vs  40세부터 '20년 내내' 넣기")
header_row(u, 16, ["구분", "A. 30~40세 10년 납입 후 20년 거치", "B. 40~60세 20년 납입", "차이 (A − B)"], start_col=2)
defs2 = [
    ("월 납입액(원)",      f"={PMT}", f"={PMT}", WON),
    ("납입 개월수",        f"=({AGE_L}-{AGE_E})*12", f"=({AGE_R}-{AGE_L})*12", '#,##0"개월"'),
    ("추가 거치 개월수",   f"=({AGE_R}-{AGE_L})*12", 0, '#,##0"개월"'),
    ("총 납입원금(원)",    "=C17*C18", "=D17*D18", WON),
    ("투자수익(원)",       "=C22-C20", "=D22-D20", WON),
    ("60세 최종자산(원)",  "=(" + fv("C17", "C18") + f")*(1+{RM})^C19", "=" + fv("D17", "D18"), WON),
]
for i, (lab, va, vb, fmt) in enumerate(defs2):
    r = 17 + i
    is_last = (i == len(defs2) - 1)
    fl = FILL_HILI if is_last else (FILL_BAND if i % 2 else None)
    fnt = F(10, True) if is_last else NORMAL
    put(u, f"B{r}", lab, F(10, True), fill=fl)
    put(u, f"C{r}", va, fnt, fmt, fl)
    put(u, f"D{r}", vb, fnt, fmt, fl)
    put(u, f"E{r}", f"=C{r}-D{r}", fnt, fmt, fl)
put(u, "B23", "결론", F(10, True, "FFFFFF"), fill=FILL_HDR)
c = u.cell(row=23, column=3,
           value='="A는 B의 절반("&TEXT(C20/D20,"0.0%")&")만 납입하고 10년간 손을 뗐는데도 최종자산이 "&TEXT(C22-D22,"#,##0")&"원 더 많습니다."')
c.font = F(10, True, "C00000"); c.alignment = Alignment(horizontal="left", vertical="center"); c.border = BOX
u.merge_cells("C23:E23"); u.row_dimensions[23].height = 22

# 비교 3: 손익분기 — 40세 시작이 30세 월30만원을 따라잡으려면
section(u, "B26", "■ 비교 3 : 40세 시작자가 '30세 · 월 30만원'을 따라잡으려면?")
header_row(u, 27, ["항목", "값", "해설", ""], start_col=2)
u.merge_cells("D27:E27")
defs3 = [
    ("30세 · 월 30만원의 60세 자산(원)", "=C11", WON, "비교 1의 A 시나리오 결과"),
    ("40세 시작자의 납입 개월수",        f"=({AGE_R}-{AGE_L})*12", '#,##0"개월"', "40세부터 60세까지"),
    ("따라잡기 필요 월납입액(원)",       "=" + pmt_needed("C28", "C29"), WON, "30세 월 30만원과 동일한 자산을 만들기 위한 금액"),
    ("30만원 대비 배수",                 "=C30/C7", MUL, "10년 늦은 만큼 매월 이만큼 더 넣어야 함"),
    ("40세 시작자의 총 납입원금(원)",    "=C30*C29", WON, "필요 월납입액 × 납입 개월수"),
    ("30세 시작자의 총 납입원금(원)",    "=C9", WON, "월 30만원 × 360개월"),
    ("추가로 부담해야 하는 원금(원)",    "=C32-C33", WON, "같은 결과를 얻기 위해 더 내야 하는 돈"),
]
for i, (lab, val, fmt, desc) in enumerate(defs3):
    r = 28 + i
    hi = FILL_HILI if r in (30, 34) else (FILL_BAND if i % 2 else None)
    fnt = F(10, True, "C00000") if r in (30, 34) else NORMAL
    put(u, f"B{r}", lab, F(10, True), fill=hi)
    put(u, f"C{r}", val, fnt, fmt, hi)
    put(u, f"D{r}", desc, NOTE, align="left")
    put(u, f"E{r}", "", fill=hi)
    u.merge_cells(f"D{r}:E{r}")

u["B36"] = "핵심 메시지"; u["B36"].font = H_SECTION
msgs3 = [
    '=" · 30세에 월 30만원으로 시작한 사람을 40세에 따라잡으려면 월 "&TEXT(C30,"#,##0")&"원("&TEXT(C31,"0.00")&"배)이 필요하고, 원금은 "&TEXT(C34,"#,##0")&"원을 더 넣어야 합니다."',
    ' · 즉, "얼마를 넣느냐"보다 "언제 시작하느냐"가 결과를 더 크게 좌우합니다.',
    ' · 시작이 늦어질수록 필요한 금액은 산술적으로가 아니라 기하급수적으로 늘어납니다. 지금 소액이라도 시작하는 것이 최선의 전략입니다.',
]
r = 37
for m in msgs3:
    c = u.cell(row=r, column=2, value=m)
    c.font = F(10, True, "C00000") if r == 37 else F(10)
    c.alignment = Alignment(horizontal="left", vertical="center")
    u.merge_cells(f"B{r}:E{r}")
    r += 1

# ════════════════════════════════════════════════════════════════════════
# 5. 4_연도별추이
# ════════════════════════════════════════════════════════════════════════
v = wb.create_sheet("4_연도별추이")
v.sheet_view.showGridLines = False
set_widths(v, {"A": 2, "B": 10, "C": 10, "D": 22, "E": 22, "F": 22, "G": 26, "H": 2})

v["B2"] = "④ 연령별 자산 추이 (30세 → 60세)"; v["B2"].font = TITLE
v["B3"] = "네 가지 시나리오의 연말 평가금액입니다. 그래프의 '벌어지는 간격'이 곧 시간의 힘입니다."
v["B3"].font = SUBTITLE

header_row(v, 5, ["연령", "경과연수",
                  "A. 30세 시작 월50만",
                  "B. 40세 시작 월50만",
                  "C. 30세 시작 월30만",
                  "D. 30~40세 월50만 후 거치"])

AF = "가정!$C$10"   # 연 환산 복리계수 (1+월수익률)^12
YRFV = f"((1+{RM})^12-1)/{RM}"   # 1년치 월적립의 연말 가치계수

start_row = 6
n_years = 31   # 30세~60세
for i in range(n_years):
    r = start_row + i
    band = FILL_BAND if i % 2 else None
    put(v, f"B{r}", f"={AGE_E}+{i}", NORMAL, AGE, band, align="center")
    put(v, f"C{r}", i, NORMAL, YR, band, align="center")
    if i == 0:
        for col in "DEFG":
            put(v, f"{col}{r}", 0, NORMAL, WON, band)
    else:
        p = r - 1
        # A: 30세~60세 월 50만원
        put(v, f"D{r}",
            f'=D{p}*{AF}+IF(AND(B{r}>{AGE_E},B{r}<={AGE_R}),{PMT},0)*{YRFV}', NORMAL, WON, band)
        # B: 40세~60세 월 50만원
        put(v, f"E{r}",
            f'=E{p}*{AF}+IF(AND(B{r}>{AGE_L},B{r}<={AGE_R}),{PMT},0)*{YRFV}', NORMAL, WON, band)
        # C: 30세~60세 월 30만원
        put(v, f"F{r}",
            f"=F{p}*{AF}+IF(AND(B{r}>{AGE_E},B{r}<={AGE_R}),'3_적게빨리vs많이늦게'!$C$7,0)*{YRFV}", NORMAL, WON, band)
        # D: 30세~40세만 월 50만원 납입 후 거치
        put(v, f"G{r}",
            f'=G{p}*{AF}+IF(AND(B{r}>{AGE_E},B{r}<={AGE_L}),{PMT},0)*{YRFV}', NORMAL, WON, band)

last = start_row + n_years - 1
put(v, f"B{last+2}", "60세 시점 요약", F(11, True, "FFFFFF"), fill=FILL_HDR)
put(v, f"C{last+2}", "", fill=FILL_HDR)
for col in "DEFG":
    put(v, f"{col}{last+2}", f"={col}{last}", F(11, True), WON, FILL_HILI)
v.merge_cells(f"B{last+2}:C{last+2}")

put(v, f"B{last+3}", "총 납입원금", F(10, True))
put(v, f"C{last+3}", "", border=True)
put(v, f"D{last+3}", f"={PMT}*({AGE_R}-{AGE_E})*12", NORMAL, WON)
put(v, f"E{last+3}", f"={PMT}*({AGE_R}-{AGE_L})*12", NORMAL, WON)
put(v, f"F{last+3}", f"='3_적게빨리vs많이늦게'!$C$7*({AGE_R}-{AGE_E})*12", NORMAL, WON)
put(v, f"G{last+3}", f"={PMT}*({AGE_L}-{AGE_E})*12", NORMAL, WON)
v.merge_cells(f"B{last+3}:C{last+3}")

put(v, f"B{last+4}", "원금 1원당 최종자산", F(10, True))
put(v, f"C{last+4}", "", border=True)
for col in "DEFG":
    put(v, f"{col}{last+4}", f"={col}{last+2}/{col}{last+3}", F(10, True, "C00000"), MUL)
v.merge_cells(f"B{last+4}:C{last+4}")

lc = LineChart()
lc.title = "연령별 자산 추이 (연 5% 가정)"
lc.y_axis.title = "평가금액(원)"; lc.x_axis.title = "연령"
lc.height, lc.width = 11, 24
ld = Reference(v, min_col=4, max_col=7, min_row=5, max_row=last)
lcat = Reference(v, min_col=2, min_row=6, max_row=last)
lc.add_data(ld, titles_from_data=True); lc.set_categories(lcat)
for ser in lc.series:
    ser.smooth = False
v.add_chart(lc, "I5")

# ════════════════════════════════════════════════════════════════════════
# 6. 요약 (맨 앞으로)
# ════════════════════════════════════════════════════════════════════════
z = wb.create_sheet("요약", 0)
z.sheet_view.showGridLines = False
set_widths(z, {"A": 2, "B": 34, "C": 20, "D": 20, "E": 20, "F": 24, "G": 2})

z["B2"] = "적립식 투자, 왜 '빨리' 시작해야 하는가"; z["B2"].font = TITLE
z["B3"] = "월 50만원 · 연 수익률 5% · 월복리 재투자 가정 (세금·보수 미반영)"
z["B3"].font = SUBTITLE

section(z, "B5", "한눈에 보기 ①  같은 돈, 다른 시간")
header_row(z, 6, ["구분", "10년", "20년", "30년", "비고"])
sum1 = [
    ("납입원금(원)",  "='1_기간별비교'!F6", "='1_기간별비교'!F7", "='1_기간별비교'!F8", "월 50만원 × 개월수"),
    ("투자수익(원)",  "='1_기간별비교'!G6", "='1_기간별비교'!G7", "='1_기간별비교'!G8", "복리로 불어난 금액"),
    ("최종자산(원)",  "='1_기간별비교'!H6", "='1_기간별비교'!H7", "='1_기간별비교'!H8", "원금 + 투자수익"),
    ("수익이 차지하는 비중", "=C8/C9", "=D8/D9", "=E8/E9", "기간이 길수록 급증"),
]
for i, (lab, c1, c2, c3, note) in enumerate(sum1):
    r = 7 + i
    fmt = PCT if i == 3 else WON
    fl = FILL_HILI if i == 2 else (FILL_BAND if i % 2 else None)
    fnt = F(11, True) if i == 2 else LINKED
    put(z, f"B{r}", lab, F(10, True), fill=fl)
    for col, val in zip("CDE", (c1, c2, c3)):
        put(z, f"{col}{r}", val, fnt, fmt, fl)
    put(z, f"F{r}", note, NOTE, align="left")

section(z, "B13", "한눈에 보기 ②  10년 늦게 시작하면?")
header_row(z, 14, ["구분", "30세 시작", "40세 시작", "차이", "비고"])
sum2 = [
    ("60세 최종자산(원)", "='2_시작시점비교'!H7", "='2_시작시점비교'!H9", "=C15-D15", "둘 다 월 50만원 · 60세 종료"),
    ("총 납입원금(원)",   "='2_시작시점비교'!F7", "='2_시작시점비교'!F9", "=C16-D16", "40세 시작자는 원금도 적음"),
    ("따라잡기 필요 월납입액(원)", "='2_시작시점비교'!E7", "='2_시작시점비교'!D18", "=D17-C17", "40세 시작자가 동일 자산을 만들려면"),
    ("→ 월 납입 배수",    1, "='2_시작시점비교'!E18", "=D18-C18", "10년의 공백을 메우는 비용"),
    ("→ 추가 납입원금(원)", 0, "='2_시작시점비교'!H18", "=D19-C19", "일찍 시작했다면 안 냈을 돈"),
]
for i, (lab, c1, c2, c3, note) in enumerate(sum2):
    r = 15 + i
    fmt = MUL if i == 3 else WON
    fl = FILL_HILI if i in (0, 2) else (FILL_BAND if i % 2 else None)
    fnt = F(11, True) if i in (0, 2) else NORMAL
    put(z, f"B{r}", lab, F(10, True), fill=fl)
    put(z, f"C{r}", c1, fnt if not isinstance(c1, str) else (LINKED if str(c1).startswith("='") else fnt), fmt, FILL_GOOD if i in (0, 2) else fl)
    put(z, f"D{r}", c2, fnt, fmt, FILL_BAD if i in (0, 2) else fl)
    put(z, f"E{r}", c3, NORMAL, fmt, fl)
    put(z, f"F{r}", note, NOTE, align="left")

section(z, "B21", "한눈에 보기 ③  적게 빨리 vs 많이 늦게")
header_row(z, 22, ["비교", "A (빨리 시작)", "B (늦게 시작·많이)", "A − B", "결론"])
sum3 = [
    ("① 30세 월30만(30년) vs 40세 월50만(20년) — 최종자산",
     "='3_적게빨리vs많이늦게'!C11", "='3_적게빨리vs많이늦게'!D11", "=C23-D23",
     "적게 넣어도 A 승"),
    ("   └ 총 납입원금",
     "='3_적게빨리vs많이늦게'!C9", "='3_적게빨리vs많이늦게'!D9", "=C24-D24",
     "A가 원금도 더 적음"),
    ("② 30세 10년만 납입 후 거치 vs 40세 20년 납입 — 최종자산",
     "='3_적게빨리vs많이늦게'!C22", "='3_적게빨리vs많이늦게'!D22", "=C25-D25",
     "절반만 넣고 멈춰도 A 승"),
    ("   └ 총 납입원금",
     "='3_적게빨리vs많이늦게'!C20", "='3_적게빨리vs많이늦게'!D20", "=C26-D26",
     "A는 B의 절반"),
]
for i, (lab, c1, c2, c3, note) in enumerate(sum3):
    r = 23 + i
    fl = FILL_HILI if i % 2 == 0 else None
    fnt = F(10, True) if i % 2 == 0 else NORMAL
    put(z, f"B{r}", lab, F(10, True) if i % 2 == 0 else F(10, False, "595959"), fill=fl, align="left")
    put(z, f"C{r}", c1, fnt, WON, FILL_GOOD if i % 2 == 0 else fl)
    put(z, f"D{r}", c2, fnt, WON, FILL_BAD if i % 2 == 0 else fl)
    put(z, f"E{r}", c3, fnt, WON, fl)
    put(z, f"F{r}", note, F(9, True, "C00000") if i % 2 == 0 else NOTE, align="left")

section(z, "B28", "결론")
concl = [
    '="1. 시간이 곧 수익이다 : 월 50만원 30년 투자 시 최종자산 "&TEXT(E9,"#,##0")&"원 중 "&TEXT(E10,"0.0%")&"가 투자수익입니다."',
    '="2. 10년의 지각비 : 40세 시작자가 30세 시작자를 따라잡으려면 매월 "&TEXT(D17,"#,##0")&"원("&TEXT(D18,"0.00")&"배), 원금은 "&TEXT(D19,"#,##0")&"원을 더 넣어야 합니다."',
    '="3. 금액보다 시점 : 30세에 월 30만원이 40세에 월 50만원을 이깁니다. 원금을 "&TEXT(D24-C24,"#,##0")&"원 덜 넣고도 "&TEXT(C23-D23,"#,##0")&"원을 더 법니다."',
    '="4. 시작이 전부 : 30세부터 10년만 넣고 20년간 방치해도, 40세부터 20년 내내 넣은 것보다 "&TEXT(C25-D25,"#,##0")&"원 앞섭니다."',
    "5. 지금 할 일 : 금액을 완벽하게 정하려다 미루지 말 것. 소액이라도 오늘 시작하는 것이 가장 큰 수익률 개선입니다.",
]
r = 29
for m in concl:
    c = z.cell(row=r, column=2, value=m)
    c.font = F(10, True, "1F3864") if r < 33 else F(10, True, "C00000")
    c.alignment = Alignment(horizontal="left", vertical="center")
    z.merge_cells(f"B{r}:F{r}")
    z.row_dimensions[r].height = 20
    r += 1

put(z, "B36", "※ 연 5%는 사용자 제시 가정치이며 확정수익률이 아닙니다. 세금·보수·물가상승률 미반영. 투자원금 손실이 발생할 수 있습니다.",
    F(9, False, "808080"), align="left", border=False)
z.merge_cells("B36:F36")

for ws in wb.worksheets:
    ws.sheet_view.zoomScale = 100

out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "투자시뮬레이션")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "적립식투자_복리효과_시뮬레이션.xlsx")
wb.save(out)
print(out)

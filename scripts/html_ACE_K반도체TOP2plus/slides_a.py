# -*- coding: utf-8 -*-
from build_html import slide, img, logo, FOOT2, pageno

CSS_A = r"""
/* ---- cover ---- */
.cover{padding:0;display:block;background:var(--dark)}
.cover .top{position:relative;height:62%;padding:34px 46px}
.cover .rule{position:absolute;left:46px;right:46px;top:88px;height:1px;background:#5a5a5a}
.cover .redn{position:absolute;right:46px;top:34px;text-align:right;color:#e23b2f;font-size:14.5px;
  font-weight:800;line-height:1.6;letter-spacing:-.4px}
.cover .pills{position:absolute;right:46px;top:104px;display:flex;gap:9px}
.cover .pills span{display:inline-block;padding:7px 15px;border-radius:5px;font-size:17px;font-weight:800;color:#fff}
.cover .pills .brown{background:#7c4323}
.cover .pills .bl{background:#6e91b7}
.cover .datepill{display:inline-block;margin-top:38px;background:var(--blue);color:#fff;
  border-radius:40px;padding:11px 30px;font-size:26px;font-weight:800;letter-spacing:-.6px}
.cover .brand{margin-top:34px;font-size:62px;font-weight:800;color:#7ea1c8;letter-spacing:-1px;line-height:1}
.cover .name{margin-top:6px;font-size:62px;font-weight:800;color:#fff;letter-spacing:-2.4px;line-height:1.1}
.cover .ticker{position:absolute;right:100px;top:296px;background:var(--blue);color:#fff;
  border-radius:40px;padding:9px 26px;font-size:24px;font-weight:700}
.cover .sub{margin-top:52px;font-size:22px;font-weight:700;color:#e9e9e9;letter-spacing:-.6px}
.cover .sub em{font-style:normal;color:#8fb0d4}
.cover .band{height:38%;background:var(--blue);color:#fff;padding:20px 46px 14px}
.cover .band ul{margin:0;padding:0;list-style:none}
.cover .band li{font-size:13.4px;line-height:1.72;padding-left:19px;position:relative;letter-spacing:-.35px}
.cover .band li::before{content:"※";position:absolute;left:0;font-size:11px;top:1px}
.cover .band .sig{margin-top:14px;font-size:13.4px}
.cover .ace-logo{top:32px;left:46px;right:auto}
/* ---- contents ---- */
.contents{padding:0}
.contents .big{position:absolute;left:56px;top:50%;transform:translateY(-50%);
  font-size:86px;font-weight:800;letter-spacing:-3px;color:#333}
.contents .list{position:absolute;left:57%;right:56px;top:11%;bottom:9%;display:flex;flex-direction:column}
.contents .row{flex:1;display:flex;align-items:center;gap:38px;border-bottom:1px solid #ececec}
.contents .row:last-child{border-bottom:1px solid #ececec}
.contents .row .n{font-size:15px;font-weight:800;color:var(--blue)}
.contents .row .lbl{font-size:31px;font-weight:800;letter-spacing:-1.4px}
/* ---- s3 ---- */
.s3 .lead{text-align:center;font-size:23px;font-weight:700;letter-spacing:-.8px;margin:2px 0 8px}
.s3 .lead mark{background:#dbe6f3;color:inherit;padding:2px 4px}
.s3 .lead b{color:var(--blue-d)}
.s3 .prod{text-align:center;font-size:34px;font-weight:800;letter-spacing:-1.4px;margin:6px 0 26px}
.s3 .cards{display:flex;gap:22px;flex:1;align-items:stretch}
.s3 .card{flex:1;border:1px solid #dcdcdc;border-radius:2px;padding:34px 16px 16px;position:relative;
  display:flex;flex-direction:column;align-items:center;text-align:center}
.s3 .num{position:absolute;top:-21px;left:50%;transform:translateX(-50%);width:42px;height:42px;
  border-radius:50%;background:#6f93bb;color:#fff;font-size:22px;font-weight:800;
  display:flex;align-items:center;justify-content:center;border:3px solid #fff;
  box-shadow:0 0 0 1px #b9c9dc}
.s3 .card h4{font-size:20.5px;font-weight:800;color:var(--blue-d);margin:2px 0 0;line-height:1.35;letter-spacing:-.7px}
.s3 .card .ill{flex:1;display:flex;align-items:center;justify-content:center;padding:8px 0}
.s3 .card .ill img{max-height:150px;max-width:88%;object-fit:contain}
.s3 .card ul{margin:0;padding:0;list-style:none;font-size:15px;line-height:1.5;letter-spacing:-.4px}
.s3 .card li{margin-top:8px;text-align:center}
.s3 .card li::before{content:"• "}
.s3 .card li.hl{color:var(--blue-d);font-weight:800}
/* ---- s7 composition ---- */
.s7 .box{border:1px solid #cfcfcf;border-radius:3px;flex:1;position:relative;padding:30px 26px 24px;
  display:flex;flex-direction:column}
.s7 .box .cap{position:absolute;top:-11px;left:22px;background:#fff;padding:0 8px;font-size:17px;font-weight:800}
.s7 .logos{display:flex;align-items:flex-end;height:44px;position:relative;margin-bottom:6px}
.s7 .logos img{height:26px}
.s7 .brk{height:12px;border-left:1px solid #555;border-right:1px solid #555;border-top:1px solid #555;
  margin:0 0 6px}
.s7 .bar{display:flex;height:56px;font-size:20px;font-weight:800;color:#fff}
.s7 .bar div{display:flex;align-items:center;justify-content:center;letter-spacing:-.6px}
.s7 .eq{display:flex;align-items:center;gap:14px;margin-top:26px;flex:1}
.s7 .eq .c{flex:1;background:#e9f0f8;border-radius:12px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;padding:16px}
.s7 .eq .c.solid{background:#5b83ad;color:#fff}
.s7 .eq .c .big{font-size:33px;font-weight:800;color:var(--blue-d);letter-spacing:-1.2px;text-align:center;line-height:1.25}
.s7 .eq .c.solid .big{color:#fff}
.s7 .eq .c .sm{font-size:15px;font-weight:700;color:#3c3c3c;white-space:nowrap}
.s7 .eq .op{font-size:38px;font-weight:800;color:#333}
/* ---- s11 ---- */
.s11 .lead{font-size:19px;letter-spacing:-.5px;margin:0 0 12px 6px}
.s11 .strip{display:flex;background:#eaf1f8;border-radius:4px;padding:11px 8px;gap:0;margin-bottom:14px}
.s11 .strip .it{flex:1;display:flex;align-items:center;gap:12px;padding:0 14px;font-size:14.5px;
  line-height:1.4;letter-spacing:-.4px}
.s11 .strip .it+.it{border-left:1px solid #c9d7e6}
.s11 .strip img{width:36px;height:36px;object-fit:contain}
.s11 .strip b{color:var(--blue-d)}
.s11 .hdr{width:330px;margin:0 auto 0;background:#5b83ad;color:#fff;border-radius:8px;text-align:center;
  font-size:22px;font-weight:800;padding:8px 0;letter-spacing:-.8px}
.s11 .conn{height:26px;position:relative;margin:0 0 2px}
.s11 .conn::before{content:"";position:absolute;left:25%;right:25%;top:12px;height:1px;background:#9aa8b8}
.s11 .conn span{position:absolute;top:12px;width:1px;height:14px;background:#9aa8b8}
.s11 .two{display:flex;gap:18px;flex:1;min-height:0}
.s11 .col{flex:1;border:1px solid #dcdcdc;border-radius:4px;overflow:hidden;display:flex;flex-direction:column}
.s11 .col>h5{margin:0;padding:7px 0;text-align:center;font-size:18px;font-weight:800;color:#fff;letter-spacing:-.6px}
.s11 .col.blue>h5{background:#5b83ad}
.s11 .col.red>h5{background:#f2413a}
.s11 .inner{padding:12px;display:flex;flex-direction:column;gap:9px;flex:1}
.s11 .row{display:flex;align-items:center;gap:10px}
.s11 .row .rk{width:28px;height:28px;border-radius:50%;background:#5b83ad;color:#fff;font-size:15px;
  font-weight:800;display:flex;align-items:center;justify-content:center;flex:0 0 28px}
.s11 .row.r .rk{background:#f2413a}
.s11 .row .lg{width:84px;display:flex;align-items:center;justify-content:center}
.s11 .row .lg img{max-width:100%;max-height:36px;object-fit:contain}
.s11 .row .wt{background:#dbe6f3;border-radius:3px;padding:6px 0;width:74px;text-align:center;
  font-size:16px;font-weight:800}
.s11 .row.r .wt{background:#fde3e1}
.s11 .row ul{margin:0;padding:0 0 0 4px;list-style:none;font-size:13.2px;line-height:1.45;flex:1;letter-spacing:-.35px}
.s11 .row li{position:relative;padding-left:11px}
.s11 .row li::before{content:"•";position:absolute;left:0}
.s11 .sub{background:#fdeeed;border-radius:5px;padding:8px 10px;margin-top:2px}
.s11 .sub h6{margin:0 0 6px;text-align:center;font-size:15.5px;font-weight:800}
.s11 .sub .g3{display:flex}
.s11 .sub .g3>div{flex:1;padding:0 8px;font-size:12.8px;line-height:1.5}
.s11 .sub .g3>div+div{border-left:1px solid #f0b9b5}
.s11 .sub .g3 b{display:block;font-size:14px;margin-bottom:3px}
.s11 .sub .g3 li{position:relative;padding-left:10px;list-style:none}
.s11 .sub .g3 ul{margin:0;padding:0}
.s11 .sub .g3 li::before{content:"•";position:absolute;left:0}
.s11 .note{display:flex;align-items:center;gap:12px;border-radius:6px;padding:9px 12px;margin-top:auto;
  font-size:13.8px;line-height:1.5;letter-spacing:-.4px}
.s11 .note.b{background:#e9f0f8}
.s11 .note.r{background:#fdeeed}
.s11 .note img{width:44px;height:44px;object-fit:contain}
.s11 .note b{color:var(--blue-d)}
.s11 .note.r b{color:#e0342a}
"""

# ---------------------------------------------------------------- 1. cover
_cover_items = [
 '본 자료는 상품이해를 돕기 위하여 판매회사에 제공되는 자료입니다.',
 '본 자료에 기재된 운용계획 및 전략은 시장상황 및 가격변동 등에 따라 변경될 수 있습니다.',
 '본 상품은 예금자보호법에 따라 보호되지 않습니다.',
 '본 상품은 자산가격 변동, 신용등급 하락 등에 따라 투자원금의 손실(0~100%)이 발생할 수 있으며, 그 손실은 투자자에게 귀속됩니다.',
 '분배금은 발생 및 금액이 고정적이지 않으며, 분배금 지급과는 별도로 보유자산이 하락할 경우 원금손실이 발생할 수 있습니다.',
 '투자하시기 전에 반드시 (간이)투자설명서 및 집합투자규약을 읽어보시기 바랍니다.',
 '금융상품판매업자는 이 금융투자상품에 관하여 충분히 설명할 의무가 있으며, 투자자는 투자에 앞서 그러한 설명을 충분히 들으시기 바랍니다.',
 '과거의 운용실적이 미래의 수익을 보장하지는 않습니다.',
 '증권거래비용, ETF거래수수료 및 기타비용 등이 추가로 발생할 수 있습니다.',
 '집합투자재산은 자본시장법에 의하여 신탁업자에게 안전하게 보관·관리되고 있습니다.',
]
slide(1, 'ACE K반도체TOP2+ (표지)', f"""
<div class="top">
  {logo(dark=True)}
  <div class="redn">[판매사 사내한] [고객 교부 금지]<br>*퇴직 (DC, IRP) 연금 70%, 개인연금 및 ISA 100% 한도로 투자 가능</div>
  <div class="rule"></div>
  <div class="pills"><span class="brown">퇴직연금</span><span class="bl">개인연금</span></div>
  <div class="datepill">2026.06.23 상장</div>
  <div class="brand">ACE</div>
  <div class="name">K반도체TOP2+</div>
  <div class="ticker">0210A0</div>
  <div class="sub">상품 제안서- <em>2026년 6월</em></div>
</div>
<div class="band">
  <ul>{''.join(f'<li>{t}</li>' for t in _cover_items)}</ul>
  <div class="sig">한국투자신탁운용 금융소비자보호 총괄책임자 심의필</div>
</div>""", cls='cover')

# ---------------------------------------------------------------- 2. contents
_toc = [('01','투자 포인트'),('02','기초지수 소개'),('03','ETF 상품 안내'),('04','투자 유의사항')]
slide(2, 'Contents', f"""
{logo()}
<div class="big">Contents</div>
<div class="list">
  {''.join(f'<div class="row"><span class="n">{n}</span><span class="lbl">{l}</span></div>' for n,l in _toc)}
</div>""", cls='contents')

# ---------------------------------------------------------------- 3. 주요 투자 포인트
slide(3, '주요 투자 포인트', f"""
{logo()}
<p class="eyebrow">ACE K반도체TOP2+</p>
<h1 class="t">주요 투자 포인트</h1>
<p class="lead"><mark><b>삼성·SK</b> 반도체 핵심주 <b>90%</b>에 <b>기판</b> 성장성까지 더한 K반도체 압축 투자</mark></p>
<p class="prod">ACE K반도체TOP2+</p>
<div class="cards">
  <div class="card"><div class="num">1</div>
    <h4>메모리 사이클 지속과<br>대형주 중심 장세</h4>
    <div class="ill">{img('p3-ill1')}</div>
    <ul><li>AI 수요 확대와 공급 병목에 따른 메모리 업황 지속 가능성 강화</li>
        <li class="hl">대형 핵심주 중심 수혜 기대</li></ul>
  </div>
  <div class="card"><div class="num">2</div>
    <h4>삼성·SK 반도체 핵심주<br>약 90% 초압축 투자</h4>
    <div class="ill">{img('p3-ill2')}</div>
    <ul><li>삼성전자/SK하이닉스/삼성전기/SK스퀘어 상위 4종목 중심 포트폴리오</li>
        <li class="hl">삼성·SK그룹 반도체 관련 주가 노출도 약 90% 확대</li></ul>
  </div>
  <div class="card"><div class="num">3</div>
    <h4>AI 반도체의 다음 성장축,<br>기판까지 투자</h4>
    <div class="ill">{img('p3-ill3')}</div>
    <ul><li>AI반도체 고성능화에 따른 기판 중요도 확대</li>
        <li>삼성전기를 필두로한 <b class="blue">기판 관련주 편입으로 성장성 플러스 알파로 추구</b></li></ul>
  </div>
</div>
<div class="foot-red"><p>※ 상기 운용구조 및 전략은 예시이며, 실제 운용에서는 당사 사정 또는 시장상황 변동 등에 따라 변경될 수 있습니다.</p></div>
""", cls='s3')

# ---------------------------------------------------------------- 4
slide(4, '메모리 사이클은 지속된다: 수요 측면', f"""
{logo()}
<p class="eyebrow">① 메모리 사이클 지속과 대형주 중심 장세</p>
<h1 class="t">메모리 사이클은 지속된다: 수요 측면</h1>
<div class="callout">
  <div class="hd"><span><b>AI</b> 수요 확대는 메모리 수요 확대로 연결</span></div>
  <ul>
    <li>빅테크의 AI 투자 확대는 메모리 수요의 구조적 증가를 뒷받침</li>
    <li>AI Agent 시대에는 GPU뿐 아니라 CPU 및 주변 메모리 수요도 확대</li>
    <li>AI 반도체 수요 확산은 메모리 업황의 지속 가능성을 높이는 요인</li>
  </ul>
</div>
<div class="body"><div class="panel" style="flex:1">
  <div class="cols" style="flex:1">
    <div style="display:flex;flex-direction:column">
      <div class="panel-t">빅테크 AI CAPEX 추이(분기)</div>
      <div class="figure">{img('p4-chart1')}</div>
      <div class="src">* 자료: The Wall Street Journal</div>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="panel-t">2026년 OpenRouter 토큰 사용량</div>
      <div class="figure">{img('p4-chart2')}</div>
      <div class="src">* 자료: MacroMicro, OpenRouter</div>
    </div>
  </div>
</div></div>
{FOOT2}{pageno(4)}""")

# ---------------------------------------------------------------- 5
_lta = [
 ('4/23','SK하이닉스','클라우드·AI<br>빅테크 다수','1분기 컨콜 — 다년 LTA 요청 급증,<br>“공급 제약으로 전부 수용 불가”','N년'),
 ('4/30','삼성전자','일부 고객사<br>(NDA 비공개)','1분기 컨콜 —<br>“일부 고객과 다년 공급계약 완료” 공식화','N년'),
 ('4월 말<br>~<br>5월 초','샌디스크','고객 5곳<br>(비공개)','LTA 총 5건 체결 · FY27 공급 물량 1/3 이상 확정','최대 5년<br>물량·<br>가격 확정'),
 ('6/8','SK하이닉스<br>(SK그룹)','엔비디아','AI 팩토리용 차세대 메모리 공동개발 + 다년 공급 계약<br>“멀티 플랫폼·그룹 포괄 최초 사례”','N년<br>(2년+)<br>연장 옵션'),
]
_lead = [
 ('표준 팹 1기','투자 $100억+ · 건설인력 7,000명 · 장비 1,200대 규모','3~4년<br><span class="nb">완공까지</span>','인텔 공식<br>자료'),
 ('업계 표준 추정','가동까지 3~5년 · 손익분기 8~10년<br>→ 증설 의사결정 자체가 보수화','3~5년<br><span class="nb">가동까지</span>','업계 분석'),
 ('그린필드 ①<br>TSMC 애리조나','2020년 발표 → Fab1 양산 2025년 전후 · Fab 2 2026.4 완공 → 2027년 하반기 양산','5년+<br><span class="nb">발표 → 양산</span>','TSMC·<br>보도'),
 ('그린필드 ②<br>SK하이닉스 용인','클러스터 착수(부지 조성)부터 첫 공장 Y1 가동<br>(2027년 말)까지','8년<br><span class="nb">착수 → 가동</span>','한국은행·<br>보도'),
 ('범용 D램 라인','건설 18~24개월 + 수율 램프업 6~12개월<br>→ 지금 착공해도 양산은 2028년','2~3년<br><span class="nb">착공 → 양산</span>','업계 분석'),
 ('확정 신공장 일정','용인 Y1·마이크론 신공장 2027년 하반기<br>→ 삼성 평택 P5 2028년 본격 기여','2H27~<br><span class="nb">공급 기여 시작</span>','한국은행<br>(2026.4)'),
]
slide(5, '메모리 사이클은 지속된다: 공급 측면', f"""
{logo()}
<p class="eyebrow">① 메모리 사이클 지속과 대형주 중심 장세</p>
<h1 class="t">메모리 사이클은 지속된다: 공급 측면</h1>
<div class="callout">
  <div class="hd"><span>메모리 업황의 지속성을 높이는 공급 병목과 장기공급계약</span></div>
  <ul>
    <li>장기공급계약 확대는 메모리 기업 실적 가시성을 높이는 요인</li>
    <li>단기간에 확대되기 어려운 메모리 생산능력</li>
    <li><b>수요는 빠르게 늘고 공급은 천천히 늘어나는 구조</b></li>
  </ul>
</div>
<div class="body"><div class="panel" style="flex:1">
  <div class="cols" style="flex:1">
    <div style="display:flex;flex-direction:column">
      <div class="panel-t">LTA 계약 사례</div>
      <table class="t s5">
        <thead><tr><th style="width:12%">발표<br>시점</th><th style="width:16%">공급사</th>
          <th style="width:17%">계약 상대</th><th>핵심 내용</th><th class="box" style="width:17%">기간·조건</th></tr></thead>
        <tbody>{''.join(f'<tr><td class="b">{a}</td><td class="b">{b}</td><td>{c}</td><td class="l">{d}</td><td class="box blue b">{e}</td></tr>' for a,b,c,d,e in _lta)}</tbody>
      </table>
      <div class="src">* 자료: 각사 자료 종합</div>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="panel-t">공장 증설에 필요한 리드타임_기업별 데이터</div>
      <table class="t s5 tight">
        <thead><tr><th style="width:20%">구분</th><th>내용</th><th class="box" style="width:20%">리드타임</th><th style="width:16%">출처</th></tr></thead>
        <tbody>{''.join(f'<tr><td>{a}</td><td>{b}</td><td class="box blue b">{c}</td><td>{d}</td></tr>' for a,b,c,d in _lead)}</tbody>
      </table>
      <div class="src">* 자료: 각사 및 언론사 종합</div>
    </div>
  </div>
</div></div>
{FOOT2}{pageno(5)}""")

# ---------------------------------------------------------------- 6
_rank_l = [('1','삼성전자','709조원',1),('2','SK하이닉스','473조원',1),('3','LG에너지솔루션','86조원',0),
           ('4','삼성바이오로직스','78조원',0),('5','삼성전자우','72조원',0),('6','현대차','60조원',0),
           ('7','HD현대중공업','53조원',0),('8','SK스퀘어','48조원',1),('9','한화에어로스페이스','48조원',0),
           ('10','두산에너빌리티','48조원',0)]
_rank_r = [('1','삼성전자','1882조원',1),('2','SK하이닉스','1578조원',1),('3','SK스퀘어','167조원',1),
           ('4','삼성전자우','163조원',1),('5','삼성전기','147조원',1),('6','현대차','130조원',0),
           ('7','LG에너지솔루션','92조원',0),('8','삼성생명','78조원',0),('9','삼성물산','69조원',0),
           ('10','HD현대중공업','64조원',0)]
def _rank(rows):
    body = ''.join(f'<tr class="{"hi" if h else ""}"><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c,h in rows)
    return f'<table class="t rk"><thead><tr><th style="width:22%">순위</th><th>종목명</th><th style="width:32%">시가총액</th></tr></thead><tbody>{body}</tbody></table>'
slide(6, 'K반도체 장세의 중심은 대형 핵심주', f"""
{logo()}
<p class="eyebrow">① 메모리 사이클 지속과 대형주 중심 장세</p>
<h1 class="t">K반도체 장세의 중심은 대형 핵심주</h1>
<div class="callout">
  <div class="hd"><span>메모리 업황 개선의 수혜는 대형 핵심주에 집중</span></div>
  <ul>
    <li>K반도체 장세는 대형 메모리 대표주 중심으로 전개</li>
    <li>유동성, 시가총액, 수급 측면에서 핵심 대형주의 우위 지속 가능</li>
    <li><b>삼성전자·SK하이닉스에서 삼성전기·SK스퀘어까지 주도주 확장</b></li>
  </ul>
</div>
<div class="body"><div class="panel" style="flex:1">
  <div class="cols" style="flex:1">
    <div style="flex:1.05;display:flex;flex-direction:column">
      <div class="panel-t">삼성전자·SK하이닉스가 주도한 한국 증시</div>
      <div class="figure">{img('p6-chart')}</div>
      <div class="src">- 자료 : Bloomberg, 한국투자신탁운용, 기준일: 2024년 12월 31일 ~ 2026년 5월 15일</div>
    </div>
    <div style="flex:1.15;display:flex;flex-direction:column">
      <div class="panel-t">국내 상장 기업 시가총액 순위 변화</div>
      <div style="display:flex;align-items:center;gap:8px;flex:1">
        {_rank(_rank_l)}
        <div style="color:#4d78ad;font-size:22px">&#9654;</div>
        {_rank(_rank_r)}
      </div>
      <div class="src">* 자료: 한국거래소 정보데이터시스템. 좌측: 2025.12.30 기준 / 우측: 2026.06.09 기준</div>
    </div>
  </div>
</div></div>
{FOOT2}{pageno(6)}""")

CSS_A += r"""
table.t.s5 th{font-size:12.4px;padding:6px 4px}
table.t.s5 td{font-size:11.9px;line-height:1.38;padding:6px 5px}
table.t.s5 .box{border-left:1.6px solid #5b83ad;border-right:1.6px solid #5b83ad}
table.t.s5 thead .box{border-top:1.6px solid #5b83ad;background:#dbe6f3}
table.t.s5 tbody tr:last-child .box{border-bottom:1.6px solid #5b83ad}
table.t.s5 .nb{font-weight:400;color:#3b3b3b;font-size:11.6px}
table.t.rk td{font-size:12.8px;padding:5px 4px}
table.t.rk th{font-size:13px}
"""

# ---------------------------------------------------------------- 7
slide(7, '삼성·SK 반도체 핵심주에 90% 초압축 투자', f"""
{logo()}
<p class="eyebrow">② 삼성·SK 반도체 핵심주 90% 초압축 투자</p>
<h1 class="t">삼성·SK 반도체 핵심주에 90% 초압축 투자</h1>
<div class="callout">
  <div class="hd"><span>삼성 45% + SK 45%, 반도체 핵심주 90% 집중</span></div>
  <ul>
    <li>상위 4종목만으로 삼성·SK 반도체 핵심주 90% 구성</li>
    <li>핵심 종목 집중으로 K반도체 상승에 대한 민감도 제고</li>
    <li>메모리 대표주 + 그룹 반도체 핵심주 조합</li>
  </ul>
</div>
<div class="body"><div class="box">
  <div class="cap">ACE K반도체TOP2+ 구성</div>
  <div class="logos">
    <div style="width:33%">{img('p7-logo-samsung', style='height:24px')}</div>
    <div style="width:38%;text-align:center">{img('p7-logo-skhynix', style='height:34px')}</div>
  </div>
  <div class="brk"></div>
  <div class="bar">
    <div style="flex:25;background:#33417f">삼성전자 25.0%</div>
    <div style="flex:18.3;background:#6f7fbe">삼성전기 18.3%</div>
    <div style="flex:25;background:#f2413a">SK하이닉스 25.0%</div>
    <div style="flex:19.5;background:#fbc3bd;color:#2b2b2b">SK스퀘어 19.5%</div>
    <div style="flex:12;background:#b9c4d2;color:#3d3d3d;font-size:13px">소형주 ~12%</div>
  </div>
  <div class="eq">
    <div class="c"><div class="big">삼성그룹 약 45%</div><div class="sm">삼성전자 25% + 삼성전기 18.3%</div></div>
    <div class="op">+</div>
    <div class="c"><div class="big">SK그룹 약 45%</div><div class="sm">SK하이닉스 25% + SK스퀘어 19.5%</div></div>
    <div class="op">=</div>
    <div class="c solid"><div class="big">핵심 4종목<br>약 90%</div></div>
  </div>
</div></div>
{FOOT2}{pageno(7)}""", cls='s7')

# ---------------------------------------------------------------- 8
slide(8, '핵심 4종목으로 K반도체 상승 탄력 확대', f"""
{logo()}
<p class="eyebrow">② 삼성·SK 반도체 핵심주 90% 초압축 투자</p>
<h1 class="t">핵심 4종목으로 K반도체 상승 탄력 확대</h1>
<div class="callout">
  <div class="hd"><span>K반도체 주도주 확장으로 성과 탄력 보완</span></div>
  <ul>
    <li>삼성전자·SK하이닉스는 국내 AI 메모리 사이클의 핵심 수혜주</li>
    <li>SK스퀘어는 SK하이닉스 지분가치, 삼성전기는 반도체 기판·AI 서버 부품 성장성을 반영</li>
    <li><b>메모리 대표주에 확장 수혜주를 결합</b></li>
  </ul>
</div>
<div class="body"><div class="panel" style="flex:1">
  <div class="panel-t">예상 시뮬레이션 성과</div>
  <div class="figure">{img('p8-chart')}</div>
  <div class="src" style="line-height:1.6">
    · 자료: FnGuide, 2026.05.29 기준<br>
    · 주: 상기 성과는 가정 포트폴리오의 예시 성과이며, 실제 비교지수 성과 및 상품 운용성과와 다를 수 있습니다. 분배금 재투자를 가정한 세전 수익률입니다. (보수 미반영)<br>
    <span style="padding-left:1.1em">‘삼성전자 25 : SK하이닉스 25: 삼성전기 20: SK스퀘어 20’ 성과는 100%로 환산한 성과입니다.</span>
  </div>
</div></div>
{FOOT2}{pageno(8)}""")

# ---------------------------------------------------------------- 9
slide(9, 'K반도체의 다음 성장축, 기판', f"""
{logo()}
<p class="eyebrow">③ K반도체의 다음 성장축, 기판까지 투자</p>
<h1 class="t">K반도체의 다음 성장축, 기판</h1>
<div class="callout">
  <div class="hd"><span><b>AI</b> 반도체가 고도화될수록 기판은 더 중요해진다</span></div>
  <ul>
    <li>기판은 칩과 메인보드를 연결하고 전기 신호·전력을 전달하는 핵심 부품</li>
    <li>AI 반도체는 고성능화될수록 대면적화·고다층화 진행중</li>
    <li>따라서, GPU, HBM, CPU, ASIC 등 다양한 칩을 안정적으로 연결하기 위해 고부가 기판 필요</li>
    <li class="plain">→ FC-BGA, PCB, SOCAMM 등 관련 기판 수요 확대 가능</li>
  </ul>
</div>
<div class="body"><div class="panel" style="flex:1">
  <div class="cols" style="flex:1">
    <div style="display:flex;flex-direction:column">
      <div class="panel-t">AI 발전 할수록 신규 칩(기판) 수요 확대</div>
      <div class="figure">{img('p9-left')}</div>
      <div class="src">· 자료: : 삼성증권</div>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="panel-t">글로벌 패키지 기판 업체 합산 CapEx 컨센서스 추이</div>
      <div class="figure">{img('p9-right')}</div>
      <div class="src">· 자료: : 각사, Im증권, 2026.05.26기준</div>
    </div>
  </div>
</div></div>
{FOOT2}{pageno(9)}""")

# ---------------------------------------------------------------- 10
slide(10, 'AI 기판 핵심 플레이어: 삼성전기', f"""
{logo()}
<p class="eyebrow">③ K반도체의 다음 성장축, 기판까지 투자</p>
<h1 class="t">AI 기판 핵심 플레이어: 삼성전기</h1>
<div class="callout">
  <div class="hd nobullet" style="font-size:22px">글로벌 MLCC 점유율 2위, AI 가속기용 FC-BGA 핵심 공급사 - AI·전장 수요로 사상 최대 실적 경신</div>
  <ul style="margin-top:4px">
    <li>AI 서버·데이터센터 투자 확대로 고온·고용량 MLCC와 AI 가속기용 FC-BGA 수요 동시 폭증</li>
    <li>FC-BGA 판가 인상 + 생산 거점 풀가동 근접, 증설 투자 검토 → 기판 사업 고성장(기판소재 부문 영업이익 2026E 전년 대비 약 +185% 전망)</li>
    <li>MLCC, IT용 대비 산업·전장용 고부가 비중 확대 + 수주잔고(BB율) 1.2~1.3로 공급 부족·가격 인상 환경 조성</li>
    <li>2026년 1분기 매출 3조 2,091억 원, 영업이익 2,806억 원 기록. 창사 이래 최초 분기 매출 3조 원 돌파 및 역대 최대 분기 매출 달성</li>
    <li>유리기판·로봇용 액추에이터 등 신사업으로 중장기 성장축 확대</li>
  </ul>
</div>
<div class="body">
  <div class="cols" style="flex:1">
    <div style="display:flex;flex-direction:column">
      <div class="panel-t ul">삼성전기 AI 기판 사업 비중 확대</div>
      <div class="figure">{img('p10-donut')}</div>
      <div class="src" style="text-align:center">- 자료 : 삼성전기, 한국투자신탁운용, 기준일: 1Q26</div>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="panel-t ul">패키지솔루션(FC-BGA) 매출·증감률 추이</div>
      <div class="figure">{img('p10-chart2')}</div>
      <div class="src" style="text-align:center">- 자료 : 삼성전기, 대신증권 추정, 기준일: 2026년 5월 1일</div>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="panel-t ul">전사 영업이익 및 증감률 추이</div>
      <div class="figure">{img('p10-chart3')}</div>
      <div class="src" style="text-align:center">- 자료 : 삼성전기, 대신증권 추정, 기준일: 2026년 5월 1일</div>
    </div>
  </div>
</div>
{FOOT2}{pageno(10)}""")

# ---------------------------------------------------------------- 11
slide(11, '메모리 70% + 기판 30%, K반도체 핵심 수혜 투자', f"""
{logo()}
<p class="eyebrow">③ K반도체의 다음 성장축, 기판까지 투자</p>
<h1 class="t" style="font-size:47px">메모리 70%+기판 30%, K반도체 핵심 수혜 투자</h1>
<p class="lead">삼성·SK 핵심주 약 90%에 집중하고, 반도체 기판 성장성까지 함께 반영</p>
<div class="strip">
  <div class="it">{img('p11-icon1')}<span>삼성전자·SK하이닉스·SK스퀘어로<br><b>메모리 반도체 약 70% 구성</b></span></div>
  <div class="it">{img('p11-icon2')}<span>삼성전기와 기판 소형주로<br><b>반도체 기판 약 30% 구성</b></span></div>
  <div class="it">{img('p11-icon3')}<span>기판 소형주는<br><b>FC-BGA 제조·장비·검사 밸류체인 중심</b></span></div>
</div>
<div class="hdr">삼성·SK 핵심주 약 90% 비중</div>
<div class="conn"><span style="left:25%"></span><span style="right:25%"></span></div>
<div class="two">
  <div class="col blue"><h5>메모리 반도체 약 70%</h5>
    <div class="inner">
      <div class="row"><div class="rk">1</div><div class="lg">{img('p11-samsung')}</div><div class="wt">25.00%</div>
        <ul><li>메모리(DRAM·NAND) + 파운드리</li><li>글로벌 종합 반도체 기업</li></ul></div>
      <div class="row"><div class="rk">2</div><div class="lg">{img('p11-skhynix')}</div><div class="wt">25.00%</div>
        <ul><li>HBM 핵심 기업</li><li>AI 메모리 핵심</li><li>글로벌 종합 반도체 기업</li></ul></div>
      <div class="row"><div class="rk">3</div><div class="lg">{img('p11-sksquare')}</div><div class="wt">19.49%</div>
        <ul><li>SK하이닉스 지분 20% 보유</li><li>AI 메모리 업황 수혜 기대</li></ul></div>
      <div class="note b">{img('p11-brain')}<span>AI 메모리 사이클의 중심인 삼성전자·SK하이닉스와<br>SK하이닉스 지분가치 노출인 SK스퀘어로<br><b>메모리 반도체 비중 약 70% 구성</b></span></div>
    </div>
  </div>
  <div class="col red"><h5>반도체 기판 약 30%</h5>
    <div class="inner">
      <div class="row r"><div class="rk">4</div><div class="lg">{img('p11-samsungem')}</div><div class="wt">18.28%</div>
        <ul><li>MLCC, 기판(FC-BGA), 카메라 모듈 등 AI 서버 부품 핵심</li></ul></div>
      <div class="sub">
        <h6>반도체 소형주 약 10%</h6>
        <div class="g3">
          <div><b>FC-BGA 기판 제조</b><ul><li>심텍</li><li>코리아써키트</li><li>티엘비</li><li>해성디에스</li></ul></div>
          <div><b>FC-BGA 기판 생산장비</b><ul><li>태성</li></ul></div>
          <div><b>검사장비</b><ul><li>기가비스</li></ul></div>
        </div>
      </div>
      <div class="note r">{img('p11-chart-icon')}<span>삼성전기와 기판 소형주를 통해<br><b>FC-BGA 제조·장비·검사 밸류체인까지 반영</b></span></div>
    </div>
  </div>
</div>
{FOOT2}
<div class="src r" style="position:absolute;right:78px;bottom:24px">- 자료 : 한국투자신탁운용, 기준일: 2026년 6월 15일</div>
{pageno(11)}""", cls='s11')

# ---------------------------------------------------------------- 12
_pf = [
 (1,'삼성전자','25.00%','메모리(DRAM·NAND) + 파운드리 · 글로벌 종합 반도체 기업',1),
 (2,'SK하이닉스','25.00%','HBM 핵심 기업 · AI 메모리 핵심 · 글로벌 종합 반도체 기업',1),
 (3,'SK스퀘어','19.49%','SK하이닉스 지분 20% 보유 · AI 메모리 업황 수혜 기대',1),
 (4,'삼성전기','18.28%','MLCC · 기판(FC-BGA) · 카메라 모듈 등 AI 서버 부품 핵심',1),
 (5,'기가비스','4.62%','AOI(내부 회로 패턴 검사) 검사 장비, AOR(기판 수리) 장비 제조 기업',0),
 (6,'심텍','4.10%','메모리 모듈기판(Module PCB), 패키지(Package Substrate) 기판 제조 기업',0),
 (7,'코리아써키트','0.90%','MLB, HDI, 반도체 패키지 기판 제조 기업',0),
 (8,'태성','0.89%','PCB 기판 세정·식각(습식) 공정 장비 제조 기업',0),
 (9,'티엘비','0.86%','메모리 모듈 PCB(DDR5·SOCAMM), AI 서버용 고부가 기판 제조 기업',0),
 (10,'해성디에스','0.85%','리드 프레임, 패키지 기판(BGA) · 차량용 기판 제조 기업',0),
]
_rows12 = ''
for i,(n,nm,w,desc,hi) in enumerate(_pf):
    c = ' class="hi"' if hi else ''
    extra = ''
    if i == 0:
        extra = ('<td rowspan="4" class="grp lb">삼성/SK*<br>핵심주<br>약 90% 비중</td>'
                 '<td rowspan="4" class="grp lb2">메모리<br>반도체<br>약 70%</td>')
    if i == 4:
        extra = ('<td rowspan="6" class="grp g1">반도체 소형주<br>약 10%</td>'
                 '<td rowspan="6" class="grp g2">반도체 기판<br>약 30%</td>')
    _rows12 += (f'<tr{c}><td class="no">{n}</td><td class="nm">{nm}</td><td class="wt">{w}</td>'
                f'<td class="ds">{desc}</td>{extra}</tr>')
slide(12, 'ACE K반도체TOP2+ ETF 예상포트폴리오', f"""
{logo()}
<p class="eyebrow">ACE ETF</p>
<h1 class="t">ACE K반도체TOP2+ ETF 예상포트폴리오</h1>
<div class="body" style="margin-top:6px;flex-direction:column"><table class="t pf">
  <thead><tr><th style="width:5%"></th><th style="width:13%">종목명</th><th style="width:10%">비중</th>
    <th>내용</th><th colspan="2" style="width:24%">구분</th></tr></thead>
  <tbody>{_rows12}</tbody>
</table></div>
<div class="src r" style="line-height:1.9;margin-top:4px">* 자료: 한국투자신탁운용, 2026.05.29 기준<br>* 광고시점 및 미래에는 이와 다를 수 있음</div>
<div class="foot-red"><p>※ 상기 운용구조 및 전략은 예시이며, 실제 운용에서는 당사 사정 또는 시장상황 변동 등에 따라 변경될 수 있습니다.</p></div>
{pageno(12)}""", cls='s12')

CSS_A += r"""
.s12 table.pf{font-size:14.5px}
.s12 table.pf th{background:#efefef;font-size:16px;padding:9px 4px;border-bottom:none}
.s12 table.pf td{border-bottom:1px solid #f0f0f0;padding:13px 6px}
.s12 table.pf tr.hi td{background:#6290be;color:#fff;border-bottom:1px solid #fff;font-weight:800}
.s12 table.pf tr.hi td.grp{color:#2b2b2b;font-weight:400}
.s12 table.pf td.ds{font-size:14px}
.s12 table.pf tr.hi td.ds{font-size:14px;font-weight:800}
.s12 table.pf td.lb{background:#dbe6f3;width:12%;line-height:1.5}
.s12 table.pf td.lb2{background:#e9f1f9;width:12%;line-height:1.5}
.s12 table.pf td.g1{background:#dedede;line-height:1.5}
.s12 table.pf td.g2{background:#e6e6e6;line-height:1.5}
"""

CSS_A += r'''
table.t.s5.tight td{padding:5px 5px;font-size:11.7px}
'''

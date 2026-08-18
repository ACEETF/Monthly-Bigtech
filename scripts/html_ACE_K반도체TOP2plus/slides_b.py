# -*- coding: utf-8 -*-
from build_html import slide, img, logo, FOOT2, pageno

CSS_B = r"""
/* ---- section divider ---- */
.divider{background:var(--dark);color:#fff;padding:0;display:block;position:relative}
.divider .wm{position:absolute;left:1%;top:47%;transform:translateY(-50%);font-size:400px;
  font-weight:800;color:#3d3d3d;letter-spacing:6px;line-height:.86;user-select:none}
.divider .ttl{position:absolute;left:78px;top:50%;transform:translateY(-50%);font-size:66px;
  font-weight:800;letter-spacing:-2.6px;line-height:1.32}
.divider .kicker{position:absolute;left:56%;top:49.5%;transform:translateY(-50%);font-size:20px;
  font-weight:700;letter-spacing:3px;color:#dcdcdc}
.divider .kicker b{color:#6c9bd2;font-weight:700}
.divider .ace-logo{left:60px;bottom:56px;top:auto;right:auto;width:118px}
/* ---- s14 ---- */
.s14{flex-direction:row;gap:24px;padding-top:52px}
.s14 .left{width:272px;flex:0 0 272px;display:flex;flex-direction:column}
.s14 .left h1{font-size:48px;font-weight:800;letter-spacing:-2px;margin:0;line-height:1.16}
.s14 .steps{margin-top:auto;margin-bottom:70px;position:relative}
.s14 .step{background:#efefef;border-radius:14px;padding:16px 12px;text-align:center;font-size:15.5px;
  line-height:1.5;letter-spacing:-.4px;position:relative;margin-bottom:44px}
.s14 .step:last-child{margin-bottom:0}
.s14 .step .no{position:absolute;left:22px;top:-16px;font-size:26px;font-weight:800;color:#fff;
  -webkit-text-stroke:1.6px #9dc3e6;letter-spacing:1px}
.s14 .step::after{content:"";position:absolute;left:50%;bottom:-38px;width:2px;height:32px;background:#8fadcf}
.s14 .step:last-child::after{display:none}
.s14 .arrowhead{position:absolute;left:calc(50% - 6px);bottom:-8px;width:0;height:0;
  border-left:6px solid transparent;border-right:6px solid transparent;border-top:9px solid #4b6c96}
.s14 .right{flex:1;min-width:0;display:flex;flex-direction:column}
.s14 .idxname{text-align:center;font-size:20px;font-weight:800;color:var(--blue-d);padding:9px 0 11px;
  border-top:2px solid #3c3c3c;letter-spacing:-.8px}
table.idx{width:100%;border-collapse:collapse;font-size:12.3px;letter-spacing:-.35px}
table.idx td{border:1px solid #e6e6e6;padding:5px 10px;vertical-align:middle;line-height:1.45}
table.idx td.k{background:#f4f4f4;text-align:center;font-weight:800;width:104px}
table.idx td.k2{background:#f4f4f4;text-align:center;font-weight:800;width:80px}
table.idx ul{margin:0;padding:0;list-style:none}
table.idx li{position:relative;padding-left:13px;margin:2px 0}
table.idx li::before{content:"•";position:absolute;left:0}
table.idx li.d{padding-left:26px}
table.idx li.d::before{content:none}
table.idx a{color:#2f6fb5}
"""

def divider(no, num, title, page_title):
    slide(no, page_title, f"""
<div class="wm">{num}</div>
<div class="ttl">{title}</div>
<div class="kicker"><b>ACE</b> K반도체TOP2+ <b>ETF</b></div>
{logo(dark=True)}""", cls='divider')

divider(13, '02', '기초지수<br>소개', '02 기초지수 소개')

# ---------------------------------------------------------------- 14
slide(14, '기초지수 개요', f"""
{logo()}
<div class="left">
  <h1>기초지수<br>개요</h1>
  <div class="steps">
    <div class="step"><span class="no">01</span>유니버스 조건 충족 기업 선별</div>
    <div class="step"><span class="no">02</span>(1) 시장 대표종목 2종목 선정<br>(2) AI반도체 테마 적합성 분석<br>(키워드 유사도) → 8종목 선별<div class="arrowhead"></div></div>
    <div class="step"><span class="no">03</span>최종 선별된 10개 기업<br>투자 비중 확정</div>
  </div>
</div>
<div class="right">
  <div class="idxname">KRX K-AI 반도체TOP2+ 지수(시장가격)</div>
  <table class="idx">
    <tr><td class="k">지수 소개</td><td colspan="3" class="b">한국거래소 유가증권시장 및 코스닥 상장된 보통주 중 AI 반도체 산업과 관련성 높은 10개 종목으로 구성된 지수</td></tr>
    <tr><td class="k">산출기관</td><td>한국거래소</td><td class="k">산출 기준일 / 가격</td><td>2020.01.15 / 1,000pt</td></tr>
    <tr><td class="k">산출시간</td><td colspan="3">한국시간 기준 9:00~15:30</td></tr>
    <tr><td class="k">지수 정보 웹사이트</td><td colspan="3"><a href="https://www.akrostec.com/indices" target="_blank" rel="noopener">https://www.akrostec.com/indices</a></td></tr>
    <tr><td class="k" rowspan="4">지수<br>설명</td><td class="k2">유니버스</td><td colspan="2">
      <ul><li>거래소: 한국거래소 유가증권시장, 코스닥 시장 보통주</li>
          <li>우량 조건: 시가총액 1조원 이상, 3개월 평균 일 거래대금 10억원 이상</li>
          <li>산업 기준 (AICS Primary기준): Machinery Manufacturing, Computer and Electronic Product Manufacturing</li></ul></td></tr>
    <tr><td class="k2">종목<br>선정방법</td><td colspan="2">
      <ul><li>키워드 정의: AI Semiconductor</li>
          <li><b>Step 1) 시장 대표 종목 선정 (2종목)</b> : 유니버스 내 시가총액 상위 2개 종목을 편입</li>
          <li><b>Step 2) 테마 유사도 상위 종목 선정 (8종목)</b></li>
          <li class="d"><b>- 1차 필터링 (키워드 절대 유사도)</b>: LLM 유사도 스코어 1 이상 종목 선별 (10개 미만 시 0.5점까지 확대)</li>
          <li class="d"><b>- 2차 최종 선별 (키워드 상대 순위)</b>: 1차 필터링 통과 종목 중 LLM 유사도 순위 상위 8개 확정</li></ul></td></tr>
    <tr><td class="k2">투자비중</td><td colspan="2">
      <ul><li>유동시가총액 + 키워드 가중 혼합 방식</li>
          <li>고정 비중: 시장 대표 종목 2개 종목 25% 우선 배정</li>
          <li>잔여 비중: 3~10위 종목은 <u>종합 점수</u> 가중치로 배분 (개별 비중 최대 20%, 최소 0.5% 제한)</li>
          <li>(참고) <u>종합 점수</u> = 키워드 점수 * 0.3 + 유동시총 점수 * 0.7</li></ul></td></tr>
    <tr><td class="k2">정기변경</td><td colspan="2">
      <ul><li>종목 변경 및 비중 변경: 연 4회 (3, 6, 9, 12월 마지막 영업일 D) 기준, D+10</li>
          <li>특별 비중 변경: 개별 종목 비중이 3영업일 연속 30% 초과할 경우, 1 영업일 후 비중 축소 실시</li></ul></td></tr>
  </table>
  <div class="src r" style="margin-top:10px">자료: 한국투자신탁운용, Akros Technologies</div>
</div>
<div class="foot-gray" style="left:330px;color:#8a8a8a;font-size:12.5px">
  <p>※ 상기 내용은 특정일 기준의 비교지수 정보를 기재한 것이며, 자세한 사항은 지수 웹사이트를 참고하시기 바랍니다.</p>
  <p>※ 실제 포트폴리오는 운용전략 및 시장상황 변동 등에 따라 달라질 수 있습니다.</p>
</div>
{pageno(14)}""", cls='s14')

CSS_B += r"""
table.perf{width:100%;border-collapse:collapse;font-size:15px;margin-top:6px}
table.perf th{padding:9px 4px;font-weight:800;text-align:center;border-top:1.6px solid #8b3a3a;
  border-bottom:1px solid #dcdcdc}
table.perf td{padding:9px 4px;text-align:center;border-bottom:1px solid #ededed}
table.perf td.k{font-weight:800;width:12%}
table.perf td.k2{font-weight:800;width:16%;text-align:center}
table.perf tr:last-child td{border-bottom:1.2px solid #c9c9c9}
.perf-foot{color:#8a8a8a;font-size:12.5px;line-height:1.7}
"""

def perf_slide(no, title, chart, rows, head, src, page):
    body = ''
    for i,(grp, name, vals) in enumerate(rows):
        g = f'<td class="k" rowspan="2">{grp}</td>' if grp else ''
        body += f'<tr>{g}<td class="k2">{name}</td>' + ''.join(f'<td>{v}</td>' for v in vals) + '</tr>'
    slide(no, title, f"""
{logo()}
<p class="eyebrow">ACE K반도체TOP2+ ETF</p>
<h1 class="t">{title}</h1>
<div class="body" style="flex-direction:column;margin-top:2px">
  <div class="panel" style="padding:10px 14px 6px">
    <div class="figure">{img(chart)}</div>
  </div>
  <table class="perf">
    <thead><tr><th style="width:12%"></th><th style="width:16%"></th>{''.join(f'<th>{h}</th>' for h in head)}</tr></thead>
    <tbody>{body}</tbody>
  </table>
  <div class="src r" style="margin-top:8px">· 자료: {src}</div>
</div>
<div class="foot-gray">
  <p>※ 본 자료에 기재된 운용전략 및 전망은 시장상황 변동 등에 따라 변경될 수 있으며, 상기의 운용실적이 미래의 수익을 보장하는 것은 아닙니다.</p>
  <p>※ 본 자료 중 예측 및 전망에 관한 자료는 참고자료이며 향후의 결과를 보증하는 것은 아닙니다.</p>
</div>
{pageno(page)}""")

perf_slide(15, 'KRX K-AI 반도체TOP2+ 지수 성과 (1)', 'p15-chart',
  [('성과','기초지수',['57.28%','91.07%','282.58%','523.46%','681.72%','760.18%']),
   (None,'코스피200',['35.34%','43.87%','142.39%','212.20%','269.84%','322.58%']),
   ('변동성','기초지수',['70.37%','77.23%','63.33%','57.48%','51.93%','48.56%']),
   (None,'코스피200',['56.79%','63.61%','49.82%','43.73%','38.89%','34.94%'])],
  ['1M','3M','6M','9M','1Y','산출이후'],
  '한국거래소, 한국투자신탁운용, 기준일: 2020.01.15~2026.05.29', 15)

perf_slide(16, 'KRX K-AI 반도체TOP2+ 지수 성과 (2)', 'p16-chart',
  [('성과','기초지수',['-34.26%','73.67%','-6.04%','156.36%','100.40%']),
   (None,'코스피200',['-26.40%','23.53%','-11.85%','90.70%','58.96%']),
   ('변동성','기초지수',['25.59%','26.86%','33.75%','37.17%','67.51%']),
   (None,'코스피200',['18.64%','15.20%','20.44%','22.57%','53.76%'])],
  ['2022년','2023년','2024년','2025년','2026년 YTD'],
  '한국거래소, 한국투자신탁운용, 기준일: 2021.12.30~2026.05.29', 16)

divider(17, '03', 'ETF<br>상품 안내', '03 ETF 상품 안내')

# ---------------------------------------------------------------- 18
CSS_B += r"""
.s18{flex-direction:row;gap:26px;padding-top:56px}
.s18 .left{width:290px;flex:0 0 290px}
.s18 .left h1{font-size:52px;font-weight:800;letter-spacing:-2.4px;margin:0}
.s18 .right{flex:1;min-width:0;display:flex;flex-direction:column}
.s18 .prod{text-align:center;font-size:24px;font-weight:800;padding:10px 0 12px;border-top:2px solid #3c3c3c;
  letter-spacing:-.8px}
table.etf{width:100%;border-collapse:collapse;font-size:14px;letter-spacing:-.35px}
table.etf td{border-bottom:1px solid #e9e9e9;padding:8px 16px;line-height:1.5;vertical-align:middle}
table.etf td.k{background:#f4f4f4;text-align:center;font-weight:800;width:32%;border-right:1px solid #e9e9e9}
table.etf .fee th{background:#f4f4f4;font-size:14px;font-weight:800;padding:8px 4px;text-align:center;
  border-bottom:1px solid #e9e9e9}
table.etf .fee td{text-align:center;padding:10px 4px;border-bottom:none}
table.etf .sub{width:100%;border-collapse:collapse}
"""
slide(18, 'ETF개요', f"""
{logo()}
<div class="left"><h1>ETF개요</h1></div>
<div class="right">
  <div class="prod">ACE K반도체TOP2+</div>
  <table class="etf">
    <tr><td class="k">펀드명</td><td>한국투자 ACE K반도체TOP2+증권상장지수투자신탁(주식)</td></tr>
    <tr><td class="k">상품 컨셉</td><td>유가증권시장, 코스닥시장 상장 보통주 중 AI 반도체와의 연관성, 시가총액을 고려하여 선정된 10종목으로 구성</td></tr>
    <tr><td class="k">기초지수명</td><td class="b">KRX K-AI 반도체TOP2+ 지수</td></tr>
    <tr><td class="k">지수 산출기관</td><td>한국거래소 (Akros Technologies 공동 개발)</td></tr>
    <tr><td class="k">펀드유형</td><td>증권- 주식형, 개방형, 추가형, 공모형</td></tr>
    <tr><td class="k">환노출여부</td><td>해당사항 없음</td></tr>
    <tr><td class="k">주요투자대상</td><td>국내 주식에 주로 (60% 이상) 투자</td></tr>
    <tr><td class="k">설정환매</td><td>설정: 제 2영업일(T+1) 기준가격 적용 제 3영업일(T+2) 납입<br>환매: 제 2영업일(T+1) 기준가격 적용 제 3영업일(T+2) 지급</td></tr>
    <tr><td class="k">분배금지급기준일</td><td>1, 4, 7, 10월 마지막영업일 및 회계기간 종료일</td></tr>
    <tr><td class="k">1좌당 가격</td><td>10,000원 (예정)</td></tr>
    <tr><td class="k">AP/LP</td><td>한국투자증권, 키움증권</td></tr>
    <tr><td class="k">신탁업자</td><td>HSBC</td></tr>
    <tr><td class="k">총보수(연)</td><td style="padding:0">
      <table class="sub fee">
        <tr><th>총보수(연)</th><th>집합투자업자</th><th>AP/LP</th><th>신탁업자</th></tr>
        <tr><td>0.39%</td><td>0.369%</td><td>0.001%</td><td>0.010%</td></tr>
      </table></td></tr>
  </table>
  <div class="src r" style="margin-top:14px">자료: 한국투자신탁운용</div>
  <div class="foot-gray" style="position:static;margin-top:6px">
    <p>※ 증권거래비용, ETF 거래 수수료 및 기타비용 등이 추가로 발생할 수 있습니다.</p>
  </div>
</div>
{pageno(18)}""", cls='s18')

# ---------------------------------------------------------------- 19~21 appendix
def appendix(no, title, head, bullets, panels, page):
    lis = ''
    for b in bullets:
        lis += f'<li>{b}</li>'
    cols = ''
    for t, im, src in panels:
        cols += (f'<div style="display:flex;flex-direction:column"><div class="panel-t ul">{t}</div>'
                 f'<div class="figure">{img(im)}</div>'
                 f'<div class="src" style="text-align:center">{src}</div></div>')
    slide(no, title, f"""
{logo()}
<p class="eyebrow">Appendix</p>
<h1 class="t">{title}</h1>
<div class="callout">
  <div class="hd nobullet" style="font-size:22px">{head}</div>
  <ul style="margin-top:4px">{lis}</ul>
</div>
<div class="body p3"><div class="cols" style="flex:1">{cols}</div></div>
{FOOT2}{pageno(page)}""")

appendix(19, '글로벌 메모리 시장의 대장 : 삼성전자',
 '글로벌 메모리 시장 점유율 1위, HBM 시장 점유율 2위의 명실상부 메모리 대장주',
 ['추론용 AI 시장 본격화, AI 서버 수요 증가와 데이터센터 투자 확대 등으로 DRAM, NAND 등 AI 전용 뿐만 아니라 범용 메모리의 수요 폭증',
  '그러나 고부가가치인 HBM 우선 생산으로 공급 부족, ASP 상승 지속되며 범용 메모리 CAPA(생산능력)가 가장 큰 삼성전자에 가장 큰 수혜 <span class="mini">(노무라 증권, 2025년 12월 말)</span>',
  '이에 따라 1Q26 사상 최대 분기 매출(133.9조원) 달성 및 DS(반도체) 부문 영업이익 53.7조원(OPM 66%) 달성',
  'HBM4 세계 최초 양산 및 엔비디아 최초 납품으로 HBM 경쟁력 확대 및 TSMC CoWoS 공정 병목으로 인한 파운드리 낙수효과 기대'],
 [('삼성전자 1Q26 사업 부문별 영업이익 비중','p19-donut','- 자료 : 삼성전자, 한국투자신탁운용, 기준일: 1Q26'),
  ('삼성전자 DS부문 실적 추이 및 전망','p19-chart2','- 자료 : 삼성전자, 한국투자증권 추정, 기준일: 2026년 5월 20일'),
  ('삼성전자 영업이익 및 ROE 추이','p19-chart3','- 자료 : 삼성전자, NH투자증권 추정, 기준일: 2026년 5월 21일')], 19)

appendix(20, 'HBM 시장 부동의 1위 : SK하이닉스',
 '전체 메모리 시장 1위 자리까지 위협하는 HBM 시장 점유율 1위 대장주',
 ['DRAM, NAND, HBM 전 제품군의 수익성 동반 상승이 지속되며 1Q26 사상 최초 분기 매출 50조원 돌파와 함께 영업이익률(OPM) 71.5% 달성',
  'DRAM 공급 부족에 따른 ASP 상승과 빅테크들의 자체 AI칩(ASIC), 추론향 CPU 수요 강세 등이 지속되며 HBM 포함 메모리 전반의 강세 지속 전망<br><span class="mini" style="padding-left:1.2em">(*ASP : 판매된 제품, 서비스 1단위당 평균 가격)</span>',
  '최근 삼성전자 HBM4 최초 양산 등 위협에도 기존 계약 물량 기반으로 엔비디아 HBM4 공급망 내 약 60% 비중 확보 전망 <span class="mini">(KB증권, 2026년 4월 1일)</span>',
  '2026년 7~8월 미국 ADR 상장이 예상됨에 따라 마이크론 대비 상대적 저평가 매력 부각과 필라델피아 반도체 지수 편입에 따른 패시브 펀드 수급 기대'],
 [('SK하이닉스 1Q26 사업 부문별 영업이익 비중','p20-donut','- 자료 : SK하이닉스, 한국투자신탁운용, 기준일: 1Q26<br>* HBM은 1Q26 증권사 종합 추정치 평균인 DRAM 전체의 15% 적용'),
  ('SK하이닉스 DRAM 부문 추이 및 전망','p20-chart2','- 자료 : SK하이닉스, 한국투자증권 추정, 기준일: 2026년 5월 20일'),
  ('SK하이닉스 영업이익 및 ROE 추이','p20-chart3','- 자료 : SK하이닉스, NH투자증권 추정, 기준일: 2026년 5월 22일')], 20)

appendix(21, 'SK하이닉스를 품은 AI 메모리 지주: SK스퀘어',
 'SK하이닉스 지분 약 20% 보유 투자지주 - AI·HBM 호황으로 NAV 급증, 적극적 밸류업·주주환원으로 할인율 축소',
 ['NAV의 95% 이상이 SK하이닉스 지분 가치 → AI·HBM 메모리 호황의 직접 수혜 (SK하이닉스 2026년 영업이익 컨센서스 약 165조로 급상승)',
  '2025년 연결 순이익 약 8.8조 원(사상 최대, 대부분 SK하이닉스 지분법 이익), 주당 NAV 약 95.7만 원(2026.02 기준)',
  '밸류업 추진: 2028년까지 NAV 할인율 30% 이하·PBR 1배 이상 목표, 2027년 목표(할인율 50% 이하)는 이미 조기 달성(2026.03 기준 약 46%)',
  '첫 배당 포함 2026년 약 3,100억 원 주주환원(현금배당+자사주 매입·소각), 중간배당 DPS 1,550원',
  '11번가·원스토어·티맵모빌리티 등 비핵심 자산 유동화로 투자 재원 확보 및 포트폴리오 AI 반도체 중심 재편'],
 [('NAV 구성 (자산별 비중)','p21-donut','- 자료 : SK스퀘어, 한국투자신탁운용, 기준일: 1Q26'),
  ('NAV, 주가 및 할인율 추이','p21-chart2','- 자료 : SK스퀘어, DB증권, 한국투자신탁운용, 기준일: 1Q26'),
  ('SK하이닉스 및 SK스퀘어 주가 추이','p21-chart3','- 자료 : SK스퀘어, NH투자증권, 한국투자신탁운용, 기준일: 1Q26')], 21)

CSS_B += r"""
.mini{font-size:12.5px;color:#4a4a4a}
"""

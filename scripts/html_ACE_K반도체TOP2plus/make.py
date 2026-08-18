# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_html as B
from css import CSS
import slides_a, slides_b, slides_c

CSS_ALL = CSS + slides_a.CSS_A + slides_b.CSS_B + slides_c.CSS_C

SECTIONS = [(1,2,'표지 · 목차'),(3,12,'01 투자 포인트'),(13,16,'02 기초지수 소개'),
            (17,21,'03 ETF 상품 안내'),(22,35,'04 투자 유의사항')]

slides = sorted(B.SLIDES, key=lambda s: s[0])
assert [s[0] for s in slides] == list(range(1,36)), [s[0] for s in slides]

toc = ''
for a, b, label in SECTIONS:
    toc += f'<h4>{label}</h4>'
    for no, title, cls, _ in slides:
        if a <= no <= b:
            toc += f'<a href="#s{no}" data-i="{no}"><span class="n">{no:02d}</span>{title}</a>'

body = ''
for no, title, cls, html in slides:
    body += (f'<div class="holder" id="s{no}" data-i="{no}">'
             f'<section class="slide {cls}">{html}</section></div>\n')

JS = r"""
const slides=[...document.querySelectorAll('.holder')];
const links=[...document.querySelectorAll('nav.toc a')];
const W=1170,H=810;
function fit(){
  const main=document.querySelector('main');
  const avail=main.clientWidth-4;
  const s=Math.min(1.6,avail/W);
  document.documentElement.style.setProperty('--s',s);
  slides.forEach(h=>{h.style.height=(H*s)+'px'});
}
window.addEventListener('resize',fit);fit();
const io=new IntersectionObserver(es=>{
  es.forEach(e=>{if(e.isIntersecting){
    const i=e.target.dataset.i;
    links.forEach(l=>l.classList.toggle('on',l.dataset.i===i));
    document.getElementById('cnt').textContent=i+' / 35';
  }});
},{rootMargin:'-45% 0px -45% 0px'});
slides.forEach(s=>io.observe(s));
function go(d){
  const y=window.scrollY+window.innerHeight*0.35;
  let idx=slides.findIndex(s=>s.offsetTop+s.offsetHeight>y);
  if(idx<0)idx=slides.length-1;
  const t=Math.max(0,Math.min(slides.length-1,idx+d));
  slides[t].scrollIntoView({behavior:'smooth',block:'start'});
}
document.getElementById('prev').onclick=()=>go(-1);
document.getElementById('next').onclick=()=>go(1);
addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT')return;
  if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(1)}
  if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(-1)}
  if(e.key==='Home'){e.preventDefault();slides[0].scrollIntoView({behavior:'smooth'})}
  if(e.key==='End'){e.preventDefault();slides[34].scrollIntoView({behavior:'smooth'})}
});
document.getElementById('toggle').onclick=()=>{
  document.body.classList.toggle('no-toc');fit();
};
"""

PRINT_CSS = r"""
@media print{
  body{background:#fff}
  .topbar,nav.toc{display:none!important}
  .wrap{padding:0;display:block}
  main{gap:0}
  .holder{height:auto!important;page-break-after:always;break-after:page;display:block}
  .slide{transform:none!important;box-shadow:none;margin:0 auto}
  @page{size:1170px 810px;margin:0}
}
@media (max-width:1080px){
  nav.toc{display:none}
}
body.no-toc nav.toc{display:none}
"""

html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ACE K반도체TOP2+ 상품 제안서 (2026년 6월)</title>
<meta name="description" content="한국투자신탁운용 ACE K반도체TOP2+ ETF 상품 제안서 HTML 버전">
<style>{CSS_ALL}{PRINT_CSS}</style>
</head>
<body>
<div class="topbar">
  <span class="tt">ACE K반도체TOP2+ 상품 제안서</span>
  <span class="sub">2026년 6월 · 한국투자신탁운용</span>
  <span class="spacer"></span>
  <button id="toggle">목차 접기/펼치기</button>
  <button id="prev">◀ 이전</button>
  <span class="counter" id="cnt">1 / 35</span>
  <button id="next">다음 ▶</button>
  <button onclick="window.print()">인쇄 / PDF</button>
</div>
<div class="wrap">
  <nav class="toc">{toc}</nav>
  <main>
{body}  </main>
</div>
<script>{JS}</script>
</body>
</html>
"""
open(B.OUT,'w',encoding='utf-8').write(html)
print('wrote', B.OUT, round(len(html.encode())/1024/1024,2),'MB')

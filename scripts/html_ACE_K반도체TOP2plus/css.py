CSS = r"""
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;padding:0}
:root{
  --blue:#557daa; --blue-d:#3f6396; --blue2:#6290be; --blue-lt:#deebf7;
  --thead:#dfe9f1; --dark:#303030; --callout:#f1f2f1; --ink:#1f1f1f;
  --red:#e8362c; --gray:#dedede; --line:#d9d9d9; --eyebrow:#648ab1;
  --s:1;
}
body{
  background:#1b1d22; color:#e8e8ea;
  font-family:"Pretendard","Pretendard Variable","Noto Sans KR","Apple SD Gothic Neo",
              "Malgun Gothic","맑은 고딕",system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing:antialiased;
}
/* ---------- shell ---------- */
.topbar{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:14px;
  padding:10px 18px;background:rgba(20,22,26,.92);backdrop-filter:blur(8px);
  border-bottom:1px solid #2c2f36}
.topbar .tt{font-size:14px;font-weight:700;letter-spacing:-.2px}
.topbar .sub{font-size:12px;color:#8d93a0}
.topbar .spacer{flex:1}
.topbar button{background:#2a2e37;color:#dfe3ea;border:1px solid #3a3f4a;border-radius:6px;
  padding:5px 10px;font-size:12px;cursor:pointer;font-family:inherit}
.topbar button:hover{background:#343945}
.counter{font-size:12px;color:#9aa1ae;min-width:56px;text-align:center}
.wrap{display:flex;align-items:flex-start;gap:18px;padding:16px}
nav.toc{position:sticky;top:60px;width:216px;flex:0 0 216px;max-height:calc(100vh - 78px);
  overflow:auto;background:#22252b;border:1px solid #2f333b;border-radius:10px;padding:8px}
nav.toc h4{margin:10px 8px 6px;font-size:11px;letter-spacing:.09em;color:#7d838f;text-transform:uppercase}
nav.toc a{display:block;padding:5px 9px;border-radius:6px;color:#c3c8d2;text-decoration:none;
  font-size:12.5px;line-height:1.35}
nav.toc a:hover{background:#2c313a;color:#fff}
nav.toc a.on{background:var(--blue);color:#fff}
nav.toc a .n{display:inline-block;width:22px;color:#767d8a;font-size:11px}
nav.toc a.on .n{color:#dbe6f3}
main{flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:22px}
.holder{width:100%;display:flex;justify-content:center;scroll-margin-top:58px}
/* ---------- slide canvas ---------- */
.slide{
  width:1170px;height:810px;flex:0 0 auto;background:#fff;color:var(--ink);
  position:relative;overflow:hidden;transform:scale(var(--s));transform-origin:top center;
  box-shadow:0 10px 34px rgba(0,0,0,.45);border-radius:2px;
  padding:34px 54px 68px;display:flex;flex-direction:column;
  font-size:16px;line-height:1.45;letter-spacing:-.2px;word-break:keep-all;
}
.slide.dark{background:var(--dark);color:#fff}
.ace-logo{position:absolute;top:26px;right:44px;width:104px;height:auto}
.slide.dark .ace-logo{top:auto}
.pageno{position:absolute;right:46px;bottom:26px;font-size:13.5px;color:#c0c0c0}
.eyebrow{font-size:19px;font-weight:800;color:var(--eyebrow);letter-spacing:-.4px;margin:0 0 2px}
h1.t{font-size:45px;font-weight:800;letter-spacing:-2px;margin:6px 0 20px;color:#1a1a1a;line-height:1.1}
h1.t.sm{font-size:40px}
.callout{background:var(--callout);border-radius:5px;padding:16px 26px 18px}
.callout .hd{font-size:23px;font-weight:800;color:var(--blue);letter-spacing:-.8px;margin-bottom:9px;
  display:flex;gap:10px}
.callout .hd::before{content:"•";color:#1a1a1a;font-weight:700}
.callout .hd.nobullet{display:block}
.callout .hd.nobullet::before{content:none}
.callout ul{margin:0;padding:0;list-style:none}
.callout li{font-size:18.5px;line-height:1.55;padding-left:16px;position:relative;letter-spacing:-.45px}
.callout li::before{content:"-";position:absolute;left:2px;color:#3a3a3a}
.callout li.plain{padding-left:34px}
.callout li.plain::before{content:none}
.callout li b{font-weight:800}
.callout small{font-size:12.5px;color:#555}
.body{flex:1;display:flex;min-height:0;margin-top:16px}
.foot-red{position:absolute;left:54px;bottom:24px;color:var(--red);font-size:11.5px;line-height:1.6}
.foot-red p{margin:0}
.foot-gray{position:absolute;left:54px;bottom:26px;color:#7d7d7d;font-size:12px;line-height:1.7}
.foot-gray p{margin:0}
.src{font-size:12px;color:#555;margin-top:6px}
.src.r{text-align:right}
/* panels */
.panel{border:1px solid var(--line);border-radius:4px;padding:14px 16px 12px;display:flex;
  flex-direction:column;min-width:0}
.panel-t{font-size:18.5px;font-weight:800;text-align:center;letter-spacing:-.6px;margin-bottom:8px}
.panel-t.ul{border-bottom:1.5px solid #9db3cd;padding-bottom:7px}
.figure{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}
.figure img{max-width:100%;max-height:100%;object-fit:contain}
.cols{display:flex;gap:16px;width:100%}
.cols>*{flex:1;min-width:0}
/* tables */
table.t{width:100%;border-collapse:collapse;font-size:13.5px;letter-spacing:-.3px}
table.t th{background:var(--thead);font-weight:800;padding:7px 6px;text-align:center;
  border-bottom:1px solid #c8d4e0}
table.t td{padding:6px 8px;text-align:center;border-bottom:1px solid #ececec;vertical-align:middle}
table.t td.l{text-align:left}
table.t tr.hi td{background:#eaf1f8;font-weight:800}
.blue{color:var(--blue-d)}
.b{font-weight:800}
.red{color:#e0342a}
/* risk tables */
table.risk{width:100%;border-collapse:collapse;font-size:10.1px;line-height:1.46;letter-spacing:-.35px}
table.risk th{font-size:12.5px;font-weight:800;padding:7px 4px;border-top:1.6px solid #3c3c3c;
  border-bottom:1px solid #c9c9c9;text-align:center}
table.risk td{padding:5px 9px;border-bottom:1px solid #e6e6e6;vertical-align:top;color:#2c2c2c}
table.risk td.k{width:132px;text-align:center;font-weight:800;font-size:11.4px;vertical-align:middle;
  letter-spacing:-.6px;padding:6px 4px}
table.risk td p{margin:0}
table.risk td .ind1{padding-left:2.2em;text-indent:-1.1em}
table.risk td .ind2{padding-left:3.6em;text-indent:-1.1em}
table.risk td .ind3{padding-left:5.0em;text-indent:-1.1em}
table.risk .rd{color:#e0342a;font-weight:700}
h2.risk-t{font-size:44px;font-weight:800;letter-spacing:-2px;margin:0}
h3.risk-s{font-size:23px;font-weight:800;color:var(--blue);margin:12px 0 16px;letter-spacing:-.8px}
.p3 .panel-t{font-size:17px;letter-spacing:-.9px}
"""

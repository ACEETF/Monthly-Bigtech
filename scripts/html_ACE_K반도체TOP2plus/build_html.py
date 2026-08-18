# -*- coding: utf-8 -*-
"""ACE K반도체TOP2+ 상품제안서 PDF -> 단일 HTML 변환 빌더."""
import base64, os, io, json

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
OUT = 'ACE_K반도체TOP2plus_상품제안서.html'  # 출력 경로

_cache = {}
def img(name, cls='', style='', alt=''):
    if name not in _cache:
        for ext, mime in (('webp', 'image/webp'), ('png', 'image/png')):
            p = os.path.join(ASSETS, f'{name}.{ext}')
            if os.path.exists(p):
                _cache[name] = f"data:{mime};base64," + base64.b64encode(open(p, 'rb').read()).decode()
                break
        else:
            raise FileNotFoundError(name)
    c = f' class="{cls}"' if cls else ''
    s = f' style="{style}"' if style else ''
    return f'<img{c}{s} src="{_cache[name]}" alt="{alt}">'

def logo(dark=False):
    return img('logo-dark' if dark else 'logo-light', cls='ace-logo', alt='ACE ETF')

FOOT2 = ('<div class="foot-red">'
         '<p>※ 상기 운용구조 및 전략은 예시이며, 실제 운용에서는 당사 사정 또는 시장상황 변동 등에 따라 변경될 수 있습니다.</p>'
         '<p>※ 분배금은 발생 및 금액이 고정적이지 않으며, 분배금 지급과는 별도로 보유자산이 하락할 경우 원금손실이 발생할 수 있습니다.</p>'
         '</div>')
RISK_FOOT = ('<div class="foot-gray">'
             '<p>※ 상기 투자위험은 본 자료 작성시점 현재 중요하다고 판단되는 위험을 기재한 것이므로 향후 운용과정 등에서 예측되지 아니하는 위험이 추가적으로 발생할 수 있습니다.</p>'
             '<p>※ 보다 상세한 투자위험은 정식 투자설명서의 “10. 집합투자기구의 투자위험”을 참고하여 주시기 바랍니다.</p>'
             '</div>')

def pageno(n):
    return f'<div class="pageno">{n}</div>'

SLIDES = []
def slide(no, title, html, cls=''):
    SLIDES.append((no, title, cls, html))

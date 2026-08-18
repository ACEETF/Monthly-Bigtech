# ACE K반도체TOP2+ 상품제안서 HTML 빌더

원본 PDF(`ACE_K반도체TOP2+.pdf`, 35p, 780×540pt)를 단일 HTML 파일로 변환하는 스크립트 모음입니다.
결과물: 저장소 루트의 `ACE_K반도체TOP2plus_상품제안서.html` (이미지 base64 내장, 외부 의존성 없음)

## 구성
| 파일 | 역할 |
|---|---|
| `crop.py` | 원본 PDF에서 차트·일러스트·로고 영역을 잘라 `assets/*.webp` 생성 |
| `build_html.py` | 슬라이드 등록 헬퍼, 이미지 base64 인라인, 공통 푸터 |
| `css.py` | 공통 스타일(슬라이드 캔버스 1170×810px, 표/콜아웃/위험표) |
| `slides_a.py` | 표지 · 목차 · 01 투자 포인트 (p1~12) |
| `slides_b.py` | 02 기초지수 소개 · 03 ETF 상품 안내 (p13~21) |
| `slides_c.py` | 04 투자 유의사항 (p22~35) |
| `make.py` | 목차·네비게이션·인쇄 CSS를 붙여 최종 HTML 출력 |

## 실행
```bash
pip install pymupdf pillow
python crop.py     # 원본 PDF 경로는 crop.py 상단 SRC 상수에서 지정
python make.py     # HTML 생성 (출력 경로는 build_html.py의 OUT 상수)
```

## 참고
- 원본 PDF는 텍스트가 아웃라인 처리되어 있어 본문은 육안 판독 후 재입력했습니다.
- 차트·일러스트 등 벡터 그래픽은 해당 영역만 잘라 WebP로 삽입했고, 표·본문·레이아웃은 HTML/CSS로 재구성했습니다.

import pymupdf, io, json, os
from PIL import Image

SRC = 'ACE_K반도체TOP2+.pdf'  # 원본 PDF 경로
doc=pymupdf.open(SRC)
OUT='assets'; os.makedirs(OUT, exist_ok=True)

# (name, page(1-based), coarse box in PDF pt, tighten?)
REGIONS = [
 ('p3-ill1', 3, (86,285,203,396), False),
 ('p3-ill2', 3, (322,282,470,394), False),
 ('p3-ill3', 3, (553,288,714,397), False),
 ('p4-chart1', 4, (25,255,400,472), True),
 ('p4-chart2', 4, (405,259,748,470), True),
 ('p6-chart', 6, (22,252,400,478), True),
 ('p7-logo-samsung', 7, (40,258,130,280), True),
 ('p7-logo-skhynix', 7, (342,256,418,290), True),
 ('p8-chart', 8, (37,252,735,452), True),
 ('p9-left', 9, (35,255,383,472), True),
 ('p9-right', 9, (401,255,722,462), True),
 ('p10-donut', 10, (35,258,266,470), True),
 ('p10-chart2', 10, (269,258,516,470), True),
 ('p10-chart3', 10, (526,258,762,470), True),
 ('p11-icon1', 11, (38,137,75,175), True),
 ('p11-icon2', 11, (281,136,318,174), True),
 ('p11-icon3', 11, (513,136,549,174), True),
 ('p11-samsung', 11, (76.6,271.3,148.1,308.1), False),
 ('p11-skhynix', 11, (78.7,323.8,150.2,348.7), False),
 ('p11-samsungem', 11, (457.6,271.3,529.1,307.3), False),
 ('p11-brain', 11, (62,417,108,468), True),
 ('p11-chart-icon', 11, (437,417,483,468), True),
 ('p11-sksquare', 11, (78,358,150,414), False),
 ('p15-chart', 15, (25,112,750,361), True),
 ('p16-chart', 16, (25,112,750,361), True),
 ('p19-donut', 19, (54,254,250,470), True),
 ('p19-chart2', 19, (269,255,516,472), True),
 ('p19-chart3', 19, (530,255,758,472), True),
 ('p20-donut', 20, (48,254,255,462), True),
 ('p20-chart2', 20, (268,255,516,472), True),
 ('p20-chart3', 20, (526,255,758,472), True),
 ('p21-donut', 21, (34,252,266,472), True),
 ('p21-chart2', 21, (272,252,505,472), True),
 ('p21-chart3', 21, (521,252,767,472), True),
 ('p34-flow', 34, (294,205,754,316), True),
]

SCALE=3.4
meta={}
for name,pno,box,tighten in REGIONS:
    page=doc[pno-1]
    # render whole page once per call (cheap enough)
    clip=pymupdf.Rect(*box)
    pix=page.get_pixmap(matrix=pymupdf.Matrix(SCALE,SCALE), clip=clip)
    img=Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
    if tighten:
        # find non-white bbox
        gray=img.convert('L').point(lambda v: 0 if v>246 else 255)
        bb=gray.getbbox()
        if bb:
            pad=int(3*SCALE)
            l=max(0,bb[0]-pad); t=max(0,bb[1]-pad)
            r=min(img.width,bb[2]+pad); b=min(img.height,bb[3]+pad)
            img=img.crop((l,t,r,b))
    # downscale to max width 1400
    if img.width>1400:
        img=img.resize((1400,int(img.height*1400/img.width)), Image.LANCZOS)
    p=os.path.join(OUT,name+'.webp')
    img.save(p,'WEBP',quality=86,method=6)
    meta[name]={'w':img.width,'h':img.height,'bytes':os.path.getsize(p)}
    print(name, img.width, img.height, os.path.getsize(p))
json.dump(meta,open('assets_meta.json','w'),indent=1)
print('total bytes', sum(v['bytes'] for v in meta.values()))

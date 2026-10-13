# 홈 화면 아이콘 생성: 판넬 바탕 위에 a접점 기호 + 전기가 흐르는 주황 전선
from PIL import Image, ImageDraw
import os
S = 2048  # 크게 그린 뒤 줄여서 매끄럽게
BG, RAIL, INK, WIRE, SCREW = (29, 38, 43), (44, 56, 63), (240, 244, 245), (240, 140, 26), (207, 214, 217)

def thick(d, a, b, w, c):
    d.line([a, b], fill=c, width=int(w))
    for p in (a, b):
        d.ellipse([p[0]-w/2, p[1]-w/2, p[0]+w/2, p[1]+w/2], fill=c)

def draw():
    im = Image.new('RGB', (S, S), BG)
    d = ImageDraw.Draw(im)
    u = S / 1024
    # DIN 레일
    d.rectangle([0, 470*u, S, 560*u], fill=RAIL)
    for i in range(9):
        x = (60 + i*115)*u
        d.rounded_rectangle([x, 500*u, x+60*u, 530*u], radius=15*u, fill=BG)
    W = 46*u
    x = 420*u
    # 위쪽 선 + 단자
    thick(d, (x, 150*u), (x, 300*u), W, INK)
    d.ellipse([x-48*u, 300*u, x+48*u, 396*u], outline=INK, width=int(34*u), fill=BG)
    # 아래 단자 + 접점 날(살짝 벌어진 a접점)
    d.ellipse([x-48*u, 610*u, x+48*u, 706*u], outline=INK, width=int(34*u), fill=BG)
    thick(d, (x+28*u, 622*u), (x+190*u, 380*u), W, INK)
    # 아래로 흐르는 주황 전선 → 오른쪽 단자로
    d.line([(x, 706*u), (x, 760*u)], fill=WIRE, width=int(W))
    pts = []
    import math
    p0, p1, p2, p3 = (x, 760*u), (x, 900*u), (740*u, 900*u), (740*u, 760*u)
    for t in [i/60 for i in range(61)]:
        mt = 1-t
        pts.append((mt**3*p0[0]+3*mt*mt*t*p1[0]+3*mt*t*t*p2[0]+t**3*p3[0], mt**3*p0[1]+3*mt*mt*t*p1[1]+3*mt*t*t*p2[1]+t**3*p3[1]))
    for a, b in zip(pts, pts[1:]):
        thick(d, a, b, W, WIRE)
    # 오른쪽 나사 단자
    cx, cy, r = 740*u, 700*u, 62*u
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=SCREW, outline=(89, 100, 106), width=int(10*u))
    d.line([(cx-34*u, cy), (cx+34*u, cy)], fill=(89, 100, 106), width=int(14*u))
    d.line([(cx, cy-34*u), (cx, cy+34*u)], fill=(89, 100, 106), width=int(14*u))
    return im

im = draw()
out = os.path.join(os.path.dirname(__file__), '..', 'icons')
for name, size in [('icon-512.png', 512), ('icon-192.png', 192), ('apple-touch-icon.png', 180), ('favicon-32.png', 32)]:
    im.resize((size, size), Image.LANCZOS).save(os.path.join(out, name), optimize=True)
print('icons ok')

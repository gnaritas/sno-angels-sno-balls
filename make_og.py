#!/usr/bin/env python3
"""Render og.png (1200x630) — hand-drawn 'fresh snow' card for Sno Angels SNO Balls.
Cream-snow field, berry-plum ink, storefront pink mound on a mint cone, drifting
flake marks. Palette from the shop's own remodeled building (pink/white/green,
Community Impact 2026-10-21). Layout zones are disjoint by construction; brand-line
width is measured with asserts (fork of the coastal painter, 2026-11-25)."""
from PIL import Image, ImageDraw, ImageFont
import math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public", "og.png")
W, H = 1200, 630
SNOW = (253, 247, 244)   # fresh snow cream
INK = (59, 34, 48)       # deep berry-plum
BERRY = (178, 58, 94)
BERRY_DK = (142, 44, 72)
PINK = (239, 159, 188)   # storefront pink
PINK_LT = (250, 205, 222)
MINT = (62, 157, 120)    # storefront green
MINT_DK = (35, 102, 78)

def F(size, bold=False):
    name = "Georgia Bold.ttf" if bold else "Georgia.ttf"
    return ImageFont.truetype("/System/Library/Fonts/Supplemental/" + name, size)

def M(size):
    return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)

def tw(d, t, f, tr=0):
    total = 0
    for ch in t:
        total += f.getlength(ch) + tr
    return total - tr

def text(d, x, y, t, f, fill, tr=0):
    cx = x
    for ch in t:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += f.getlength(ch) + tr

def center(d, y, t, f, fill, tr=0):
    text(d, (W - tw(d, t, f, tr)) // 2, y, t, f, fill, tr)

img = Image.new("RGB", (W, H), SNOW)
d = ImageDraw.Draw(img)
random.seed(1701)

# snow-drift field: soft tinted mound arcs along the bottom band
for i in range(3):
    rr = 780 - i * 90
    cy = H + 250 - i * 40
    shade = (222, 240, 231) if i % 2 == 0 else (244, 232, 236)
    d.ellipse((-W // 2 + i * 120, cy - rr, W + W // 2 - i * 120, cy + rr), fill=shade)

# drifting flakes (line-stars) kept above the brand line and out of the mound column
for _ in range(24):
    x, y = random.choice((random.randint(44, 330), random.randint(860, 1156))), random.randint(28, 140)
    r = random.choice((6, 8, 10))
    c = random.choice((PINK, MINT, (203, 182, 191)))
    for ang in (0, 45, 90, 135):
        dx, dy = r * math.cos(math.radians(ang)), r * math.sin(math.radians(ang))
        d.line([(x - dx, y - dy), (x + dx, y + dy)], fill=c, width=2)

# brand rope: pink over mint, top and mirrored bottom
d.rectangle((0, 0, W - 1, 3), fill=PINK)
d.rectangle((0, 3, W - 1, 6), fill=MINT)
d.rectangle((0, H - 6, W - 1, H - 4), fill=MINT)
d.rectangle((0, H - 3, W - 1, H - 1), fill=PINK)
# double frame: ink outer, berry inner
d.rectangle((26, 26, W - 27, H - 27), outline=INK, width=1)
d.rectangle((34, 34, W - 35, H - 35), outline=BERRY, width=3)

center(d, 74, "NEW ORLEANS-STYLE SNO BALLS", M(24), MINT_DK, tr=10)
center(d, 112, "DRIVE-THRU · OLD TOWN TOMBALL, TEXAS", M(21), MINT_DK, tr=7)

# big brand line, measured; vertical separation from the mound column is checked, not x-ban
h1 = "Sno Angels SNO Balls"
for px in (84, 80, 76, 72, 68, 64, 60):
    wd = tw(d, h1, F(px, True))
    if wd <= 1060:
        break
else:
    raise SystemExit("og: h1 too wide")
cx0 = (W - wd) // 2
assert cx0 >= 34 + 24 and cx0 + wd <= W - 35 - 24, "og: h1 frame collision (%d -> %d..%d)" % (wd, cx0, cx0 + wd)
# mound top edge at the title's right x (ellipse rx110 ry77.5 center (1050, 382.5))
_r = max(0.0, 1.0 - ((min(cx0 + wd, 1050) - 1050) / 110.0) ** 2) if cx0 + wd >= 940 else 1.0
_mound_top = 382.5 - 77.5 * math.sqrt(_r) if cx0 + wd >= 940 else 9999
_title_bottom = 162 + px * 1.17
assert _title_bottom <= _mound_top - 30, "og: h1/mound collision (bottom %d vs mound top %d)" % (_title_bottom, _mound_top)
d.text((cx0, 162), h1, font=F(px, True), fill=INK)

# snowball mound art (right column, y>=250): pink snow mound on a mint cone
mx, my = 1050, 345
d.ellipse((mx - 110, my - 95, mx + 110, my + 60), fill=PINK)                      # mound body
d.polygon([(mx - 62, my + 30), (mx + 62, my + 30), (mx, my + 175)], fill=MINT)   # cone
for k in range(5):                                                                 # syrup drips
    x0 = mx - 48 + k * 24
    d.line([(x0, my - 68), (x0, my - 44 - (k % 2) * 12)], fill=BERRY, width=4)
for sx, sy in ((-40, -34), (0, -52), (44, -30)):                                   # scoop dimples
    d.ellipse((mx + sx - 16, my + sy - 16, mx + sx + 16, my + sy + 16), fill=PINK_LT)
for yy in (my + 65, my + 100, my + 135):                                           # cone hatch, width follows taper
    hw = 62 * (my + 175 - yy) / 145.0
    d.line([(mx - hw, yy), (mx + hw, yy)], fill=MINT_DK, width=2)

# feature rules + lines (centered text, all widths end short of the mound column)
y = 296
d.line([(60, y), (900, y)], fill=BERRY, width=2)
assert tw(d, "MIX UP TO 3 FLAVORS FROM 50+", M(26), 6) <= 870
center(d, 332, "MIX UP TO 3 FLAVORS FROM 50+", M(26), INK, tr=6)
assert tw(d, "ICE CREAM STUFFED · SWEET CREAM FLOAT", M(22), 5) <= 870
center(d, 370, "ICE CREAM STUFFED · SWEET CREAM FLOAT", M(22), BERRY_DK, tr=5)
assert tw(d, "KOSHER · DYE-FREE · SUGAR-FREE CHOICES", M(22), 5) <= 870
center(d, 406, "KOSHER · DYE-FREE · SUGAR-FREE CHOICES", M(22), MINT_DK, tr=5)

assert tw(d, "525 W MAIN ST · TOMBALL TX 77375", M(25), 8) <= 900
center(d, H - 148, "525 W MAIN ST · TOMBALL TX 77375", M(25), INK, tr=8)
assert tw(d, "MAIN & MAGNOLIA · PARKING IN BACK", M(20), 6) <= 870
center(d, H - 106, "MAIN & MAGNOLIA · PARKING IN BACK", M(20), BERRY_DK, tr=6)

y = H - 64
d.line([(430, y), (W - 430, y)], fill=MINT, width=2)

img.save(OUT, "PNG")
print("wrote", OUT, img.size, "| h1 px", px, "wd", wd, "@ x", cx0)

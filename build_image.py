#!/usr/bin/env python3
"""Build entry.png: a newspaper front page summing up 18 Nov 2026 world news.

Drawn programmatically with PIL (no photos, no AI generation, no network):
crisp vector text and shapes only, so nothing is garbled at any size.
Run:  python3 build_image.py   (writes entry.png next to this script)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/noto"

SERIF_BLACK = os.path.join(FONT_DIR, "NotoSerif-Black.ttf")
SERIF_BOLD = os.path.join(FONT_DIR, "NotoSerif-Bold.ttf")
SANS_BLACK = os.path.join(FONT_DIR, "NotoSans-Black.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")

W, H = 1024, 1024
PAGE = (251, 249, 244)       # warm off-white paper
INK = (20, 20, 20)          # near-black
MUTE = (90, 90, 86)          # footer grey
RULE = (20, 20, 20)
FAINT = (180, 175, 165)      # light rule
RED = (179, 38, 30)
BLUE = (26, 79, 138)
TEAL = (14, 107, 92)
PURPLE = (91, 45, 142)
AMBER = (178, 106, 0)
GREEN = (46, 107, 46)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(g, text, ft, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if g.textlength(trial, font=ft) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(g, x, y, text, ft, max_w, leading, color=INK):
    """Draw wrapped paragraph; returns y just below the last line."""
    for line in wrap(g, text, ft, max_w):
        g.text((x, y), line, font=ft, fill=color)
        y += leading
    return y


def hrule(g, x0, x1, y, width=2, color=RULE):
    g.line([(x0, y), (x1, y)], fill=color, width=width)


def burst(g, cx, cy, r, color):
    """Simple 8-point starburst (drawn shape, lead-story icon)."""
    import math
    outer = []
    for i in range(16):
        ang = math.pi * i / 8 - math.pi / 2
        rad = r if i % 2 == 0 else r * 0.45
        outer.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    g.polygon(outer, fill=color)


def circles3(g, x, y, r, colors):
    for i, c in enumerate(colors):
        g.ellipse([x + i * (2 * r + 6), y, x + i * (2 * r + 6) + 2 * r,
                   y + 2 * r], fill=c, outline=INK, width=2)


def chip(g, x, y, s, color):
    """Compact chip: rounded square with an inner die, no pins (pins would
    reach into the headline below)."""
    g.rounded_rectangle([x, y, x + s, y + s], radius=6, fill=color,
                        outline=INK, width=2)
    inner = s // 3
    g.rectangle([x + inner, y + inner, x + s - inner, y + s - inner],
                outline=(255, 255, 255), width=2)


def coin(g, x, y, r, color):
    """Euro coin: filled circle with a white bold euro sign."""
    g.ellipse([x, y, x + 2 * r, y + 2 * r], fill=color,
              outline=INK, width=2)
    f = font(SANS_BOLD, r + 6)
    g.text((x + r, y + r - 2), "€", font=f, fill=(255, 255, 255),
           anchor="mm")


def chart_up(g, x, y, w, h, color):
    pts = [(x, y + h), (x + w * 0.3, y + h * 0.65),
           (x + w * 0.55, y + h * 0.75), (x + w * 0.8, y + h * 0.3),
           (x + w, y + h * 0.08)]
    g.line(pts, fill=color, width=6, joint="curve")
    g.polygon([(x + w - 12, y + h * 0.08), (x + w + 2, y + h * 0.08),
               (x + w, y + h * 0.08 - 10)], fill=color)


def skyline(g, x, y, w, h, color):
    bars = [(0, 0.55), (0.18, 0.30), (0.38, 0.62), (0.56, 0.22),
            (0.74, 0.48), (0.88, 0.35)]
    bw = w / len(bars)
    for i, (fx, fh) in enumerate(bars):
        bx = x + i * bw + 2
        g.rectangle([bx, y + h * fh, bx + bw - 4, y + h], fill=color)


def main():
    img = Image.new("RGB", (W, H), PAGE)
    g = ImageDraw.Draw(img)
    M = 44  # margin
    X0, X1 = M, W - M

    # ---- Masthead ----
    f_mast = font(SERIF_BLACK, 62)
    g.text((W // 2, 34), "THE WORLD IN ONE DAY", font=f_mast, fill=INK,
           anchor="ma")
    hrule(g, X0, X1, 118, width=3)
    f_date = font(SANS_BOLD, 30)
    g.text((W // 2, 130), "Wednesday, 18 November 2026", font=f_date,
           fill=INK, anchor="ma")
    hrule(g, X0, X1, 176, width=1, color=FAINT)

    # ---- Lead story: Iran hits Kuwait and Bahrain ----
    y = 196
    f_kick = font(SANS_BLACK, 22)
    g.text((X0, y), "MIDDLE EAST  •  CONFLICT", font=f_kick, fill=RED)
    burst(g, X1 - 34, y + 26, 30, RED)
    y += 36
    f_lead = font(SERIF_BLACK, 47)
    y = para(g, X0, y, "Iran Hits U.S. Base in Kuwait, Strikes Bahrain Again",
             f_lead, X1 - X0 - 90, 54)
    y += 8
    f_sum = font(SANS, 24)
    y = para(g, X0, y,
             "Tehran's drones target Ali Al Salem air base and Bahrain "
             "again, a day after U.S. jets struck a missile site on Iran's "
             "Qeshm Island; both Gulf states report interceptions.",
             f_sum, X1 - X0, 32)
    y += 14
    hrule(g, X0, X1, y, width=2)

    # ---- Grid: 4 stories, 2 x 2 ----
    stories = [
        ("DIPLOMACY  •  ASIA", BLUE,
         "Trump Lands in Shenzhen; Xi and Putin Meet",
         "The three leaders prepare trilateral talks at the APEC summit, "
         "set for Thursday.",
         lambda px, py: circles3(g, px, py + 2, 11, [RED, (255, 210, 63), BLUE])),
        ("TECHNOLOGY", TEAL,
         "Nvidia Board Rules Out Huang's Return",
         "Chair Harvey Jones says the board will not reinstate its "
         "co-founder; CFO Colette Kress stays interim chief.",
         lambda px, py: chip(g, px + 4, py + 2, 26, TEAL)),
        ("EUROPE  •  UKRAINE", PURPLE,
         "EU Proposes €45bn Ukraine Loan for 2027",
         "€20bn for the budget and €25bn for arms, repaid only once "
         "Russia pays reparations.",
         lambda px, py: coin(g, px + 4, py, 13, PURPLE)),
        ("ECONOMY  •  U.S.", AMBER,
         "Fed Minutes Point to More Hikes",
         "Nearly all officials expect further rises if inflation stays "
         "hot; the October hold was 10–2.",
         lambda px, py: chart_up(g, px, py + 10, 56, 20, AMBER)),
    ]
    gy = y + 18
    col_w = (X1 - X0 - 28) // 2
    row_h = 196
    for i, (kicker, color, head, summ, icon) in enumerate(stories):
        cx = X0 + (i % 2) * (col_w + 28)
        cy = gy + (i // 2) * (row_h + 14)
        g.text((cx, cy), kicker, font=font(SANS_BLACK, 20), fill=color)
        icon(cx + col_w - 70, cy - 4)
        yy = cy + 32
        f_h = font(SERIF_BOLD, 29)
        yy = para(g, cx, yy, head, f_h, col_w, 35)
        yy += 4
        yy = para(g, cx, yy, summ, font(SANS, 22), col_w, 29, color=(60, 60, 58))
        if i % 2 == 0:
            g.line([(cx + col_w + 14, cy), (cx + col_w + 14, cy + row_h - 8)],
                   fill=FAINT, width=1)
    gy2 = gy + 2 * row_h + 14
    hrule(g, X0, X1, gy2, width=2)

    # ---- Bottom story: GTA VI ----
    y = gy2 + 16
    g.text((X0, y), "CULTURE  •  GAMES", font=font(SANS_BLACK, 20), fill=GREEN)
    skyline(g, X1 - 84, y - 2, 80, 44, GREEN)
    y += 32
    f_h = font(SERIF_BOLD, 30)
    g.text((X0, y), "GTA VI Unlocks First in New Zealand", font=f_h, fill=INK)
    y += 40
    y = para(g, X0, y,
             # One line on purpose: a second line would run into the footer.
             "The game goes live region by region from midnight local time; "
             "early reviews arrive.",
             font(SANS, 22), X1 - X0, 29, color=(60, 60, 58))
    hrule(g, X0, X1, y + 12, width=1, color=FAINT)

    # ---- Footer ----
    f_foot = font(SANS, 18)
    g.text((W // 2, H - 44),
           "Six stories from 18 November 2026  •  As reported by wire services",
           font=f_foot, fill=MUTE, anchor="ma")

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    size = os.path.getsize(out)
    print(f"wrote {out}: {img.size[0]}x{img.size[1]}, {size} bytes")


if __name__ == "__main__":
    main()

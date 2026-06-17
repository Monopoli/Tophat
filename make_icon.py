"""
Generates assets/tophat.ico (multi-resolution Windows icon) and
assets/tophat.png (standalone preview / source image) for the TopHat app.

Drawn at high resolution (1024px) and downsampled with LANCZOS for clean
anti-aliased edges at every icon size Windows asks for.

Run once: python assets/make_icon.py
"""
from PIL import Image, ImageDraw

S = 1024  # working canvas size; final sizes are downsampled from this

# Palette pulled from app.py's existing dark theme so the icon matches
# the app's own UI rather than introducing a new color scheme.
INK     = (18, 18, 24, 255)    # near-black crown/brim (matches BG "#14141c")
OUTLINE = (90, 90, 122, 255)   # FG3-ish lavender-grey, for edge definition on dark taskbars
BAND    = (91, 155, 213, 255)  # ACC accent blue ("#5b9bd5") used for links/addresses in-app
BAND_HI = (130, 184, 230, 255) # lighter sheen line on the band

def make_base():
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    cx = S // 2

    # ── Brim (wide, flat ellipse) ───────────────────────────────────────
    brim_box = (S*0.07, S*0.70, S*0.93, S*0.92)
    d.ellipse(brim_box, fill=INK, outline=OUTLINE, width=10)

    # ── Crown sides ──────────────────────────────────────────────────────
    crown_box = (S*0.27, S*0.20, S*0.73, S*0.79)
    d.rounded_rectangle(crown_box, radius=int(S*0.05), fill=INK,
                         outline=OUTLINE, width=10)

    # ── Crown top cap (rounds off the top of the cylinder) ─────────────
    cap_box = (S*0.27, S*0.145, S*0.73, S*0.30)
    d.ellipse(cap_box, fill=INK, outline=OUTLINE, width=10)

    # ── Band near the base of the crown ─────────────────────────────────
    band_top, band_bot = S*0.595, S*0.69
    d.rectangle((S*0.275, band_top, S*0.725, band_bot), fill=BAND)
    d.line((S*0.275, band_top + S*0.012, S*0.725, band_top + S*0.012),
           fill=BAND_HI, width=int(S*0.012))

    return img

def main():
    base = make_base()
    base.save("assets/tophat.png")

    sizes = [16, 24, 32, 48, 64, 128, 256]
    base.save(
        "assets/tophat.ico",
        sizes=[(s, s) for s in sizes],
    )
    print("Wrote assets/tophat.png and assets/tophat.ico")

if __name__ == "__main__":
    main()

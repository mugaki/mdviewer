"""
Crop the main icon from the reference image and generate icon.ico.
"""
from PIL import Image
import sys

SRC    = "icon_src.png"  # 変換元画像のパスを指定してください
SIZES  = [16, 32, 48, 64, 128, 256]


def main():
    src = Image.open(SRC).convert("RGBA")
    W, H = src.size
    print(f"Source image: {W}x{H}")

    # Already a clean single icon — center-crop to square
    side = min(W, H)
    x0 = (W - side) // 2
    y0 = (H - side) // 2
    icon = src.crop((x0, y0, x0 + side, y0 + side))

    icon.save(
        "icon.ico",
        format="ICO",
        sizes=[(s, s) for s in SIZES],
    )
    print("icon.ico created.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

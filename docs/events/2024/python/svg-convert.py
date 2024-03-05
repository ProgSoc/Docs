from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os
import sys

if __name__ == "__main__":
  prefix = sys.argv[1] if len(sys.argv) > 1 else "."
  for fname in os.listdir(prefix):
    if fname.endswith(".svg"):
      renderPM.drawToFile(
        svg2rlg(f"{prefix}/{fname}"),
        fname.replace(".svg", ".png"),
        fmt="PNG",
        backend='_renderPM'
      )

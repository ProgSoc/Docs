from svg_turtle import SvgTurtle
from math import cos, sin
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Spiro:
  def __init__(self, r, accel = 1.0, child = None):
    self._rotation = 0
    self._radius = r
    self._accel = accel
    self._child = child

  def turn(self, angle):
    self._rotation += angle * self._accel
    if self._child is not None:
      self._child.turn(-1 * angle * self._radius / self._child._radius)

  def pos(self):
    x = self._radius * cos(self._rotation)
    y = self._radius * sin(self._rotation)
    if self._child is not None:
      child_coords = self._child.pos()
      x += child_coords[0]
      y += child_coords[1]
    return (x, y)

def spirograph(spiros=[(127,1.5),(128,1.5)], width=512, height=512):
  t = SvgTurtle(width, height)
  t.getscreen().bgcolor(0.9, 0.9, 1.0)
  s = None
  for (r,a) in reversed(spiros):
    s = Spiro(r, a, s)
  t.teleport(*s.pos())
  for _ in range(2048):
    s.turn(0.1)
    t.goto(s.pos())
  return t.to_svg()

def simple_text(txt):
  return "".join(c for c in txt.lower().replace("-", " ") if c in 'abcdefghijklmnopqrstuvwxyz0123456789 ')

soup = BeautifulSoup(urlopen("https://progsoc.org/blog/"), "html.parser")
for ele in soup.select(".post-card-title"):
  name = "-".join(simple_text(ele.text).split())
  with open(f"_{name}.svg", "w") as f:
    f.write(spirograph(list(map(lambda w: (len(w) * 10, 1.5), name.split("-")))))

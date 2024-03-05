import turtle as t
from math import cos, sin

class Spiro:
  def __init__(self, radius, rotation = 0.0, child = None):
    self._radius = radius
    self._rotation = rotation
    self._child = child
  def turn(self, angle):
    self._rotation += angle
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

s = Spiro(
  5, 0,
  child=Spiro(
    63, 0
  )
)
t.penup()
t.goto(s.pos())
t.pendown()

while True:
  s.turn(0.1)
  t.goto(s.pos())

t.mainloop()

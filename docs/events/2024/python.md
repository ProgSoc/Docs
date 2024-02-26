---
title: "Beginners' Python (2024)"
date: 2024-02-28
tags:
  - Workshop
  - Python
---

# Beginners' Python (2024)

## Setting Up

See the [installation section on the TFM Python page](../../tfm/python.md#installation).

## Background

### History

### Why Python?

## Fundamentals

### Hello, World!

```python
$ python

>>> print("Hello, World!")
Hello, World!
```

### Data Types

```python
print(2)

print(4.2)

print(4 - 2)

print(5 / 2)

print(0.1 + 0.3)

print(True)

print(False)

print([1, 2, 3])

print((1, 2, 3))

print({1, 1, 2, 3, 5, 8, 13})

print(3 in {1, 5, 3, 9})

print({ "key": "value" })
```

### Operators

```python
1 + 1
2 * 2
3 - 3
4 / 4
5 % 5
6 // 4
(2 + 3) * 4
```

### Variables

```python
a = 2
b = 8
c = a - b
print(c)
```

### Input

```python
print("Hi I'm PyBot!")
name = input("What's your name? ")
print("Hi", name)
# print(f"Hi {name}! Nice to meet you.")

x = int(input("Enter a number: "))
print("You entered:", x)
```

### Conditions

```python
x = int(input())
if x % 15 == 0:
  print("FizzBuzz")
elif x % 5 == 0:
  print("Buzz")
elif x % 3 == 0:
  print("Fizz)
else:
  print(x)
```

### Repetition

```python
for i in range(10):
  print(i)

for i in range(10, 0, -2):
  print(i)

items = [1, 3, 8, 2]
for x in items:
  print(x)

values = []
while (x := int(input("Enter number:"))) != 999:
  values.append(x)
print(sum(values))
```

### Exceptions

```python
try:
  pass
except Error as e:
  pass
finally:
  pass
```

### Encapsulation

```python
def add(a, b):
  return a + b

class Vehicle:
  def __init__(self, name):
    self._name = name

  def introduce(self):
    print(f"This is a {self._name}.")

class Car:
  pass
```

## Modules

```python
import random
from random import randint
from random import *
import numpy as np
from numpy import sqrt as sq
```

```sh
$ pip install numpy
```

## Trivia

```
global scope keyword

for else loops

mutable default arguments
```

## Into Practice

```python
# turtle plot spirograph
```

## Automation / Web Server

```python
# file renaming

# web scrape / re-present uts wayfinding
```

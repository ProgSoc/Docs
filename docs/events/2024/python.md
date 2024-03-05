---
title: "Beginners' Python (2024)"
date: 2024-02-28
tags:
    - Workshop
    - Python
    - Beginners' Series
---

# Beginners' Python (2024)

## 🏗️ Setting Up

See the [installation section on the TFM Python page](../../tfm/python.md#installation).

## 🖼️ Background

### Audience's Background

* Have you ever done any programming/coding?
* If so:
    * What programming language(s) did you use?
    * If one of them was Python:
        * Awesome! Hopefully this is somewhat familiar to you, but enjoy the refresher nonetheless.
    * Otherwise:
        * Well, another one to add to your repertoire!
* Otherwise:
    * Enjoy learning how to program!
    * Try typing in `print("Hello, World!")` into `python`

### History

<https://en.wikipedia.org/wiki/History_of_Python>
<http://python-history.blogspot.com/2009/01/personal-history-part-1-cwi.html>

* Written initially by Guido van Rossum in 1989/1990, working at CWI (Government research centre for computer science and mathematics).
* Made public on Usenet in February 1991.
* Version 1.0 release in January 1994. This marked the start of wider "Open Source" development with more external contributors.
* Version 2.0 release in October 2000, used as a tool in building and compiling C and C++ source code for many years - more capabable and compatible than shell scripts yet still simple.
* Version 3.0 release in December 2008, breaking backwards compatibility with Python 2. Simplified and made the language more consistent, removing accumulated messyness.

### Why Python?

<http://python-history.blogspot.com/2009/01/introduction-and-overview.html>

* Quick for prototyping small solutions
    * Dynamic typing means you don't have to fuss over extra variable labelling like in C, Java, etc
* Extensive standard library of code
* Large collection of third-party modules
* Simple to learn the basics, good for non-programmers
* Used widely in Data Science, Dev-Ops scripting, Web Servers.
    * Google's first web crawler was written in Python
    * Reddit, DropBox, YouTube, Spotify are all largely written in Python
    * A useful 'glue' language to join other systems together
* Has many features inspired from other programming languages, learning Python is a great stepping stone to learning many others

## 🥋 Fundamentals

You can also refer to [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) for extra guidance.

### Hello, World!

1. Open up your CMD / Command Prompt (Windows), or Terminal (Unix),
2. At the prompt, type `python` and hit `Enter`:
    * You'll go into interactive mode, also known as the Read-Evaluate-Print-Loop (REPL),
    * This is sort of like a calculator, you can type instructions in but they won't be saved - you'll have to type them all in again if you want to continue your work again later.

```python
$ python

>>> print("Hello, World!")
Hello, World!
```

Congratulations, that's your first line of Python code in this workshop! (And technically too, of Batch or Bash to launch Python. Sssneaky! 🐍)

### Data Types

Without data, your program may as well not exist at all. It's what your computer works with in order to actually produce (occasionally 😉) useful output.

#### 'Primitives'

All progamming languages have a group of base level data-types, known as ['primitives'](https://en.wikipedia.org/wiki/Language_primitive), that you process in your code and use to assemble more complex data-structures.

As we work through the examples below, have a go at typing them into the REPL as-is; but also on the inside of that `print(...)` thing we saw earlier. Anything you want to display goes inside the round-brackets.

```python
$ python

>>> 0
>>> print(0)
```

##### Whole Numbers (Integers)

Let's start by looking at numbers.

As you may know, computers are made to work with numbers, ***really well***. But, they don't count how we do with digits 0 to 9. They use a different system; in particular, the [binary (or base-2) system](https://en.wikipedia.org/wiki/Binary_number) with only 0 or 1, which is represented physically by an off or on electrical signal.

Thankfully, we don't have do conversion in our heads in order to write programs that computers understand - that's what programming languages are for. We can instead type notation known as ['literals'](https://en.wikipedia.org/wiki/Literal_(computer_programming)) and that is converted for us.

Have a go at typing in the values below into the REPL, to see how they are interpreted:

```python
1
10
-5
0x7F
0b101
0o664
```

##### Text (Strings)

> *This heading says "Text"! But you just said computers work with numbers?*

That's right.

> *Is this some kind of trick?!*

Actually, it kind of is... Text in programming languages is actually just a bunch of numbers.

> *Sure.. but the code further down clearly says `"A Pie"` and not `1, 3, 14159`! So what's going on? 🤔*

Each of those numbers are used to represent individual letters, or more formally 'characters'. For modern computers, those numbers are assigned to specific characters by the [Unicode Consortium](https://home.unicode.org/). In the past (and still for the first 128 characters) these numbers were assigned according to [ASCII](https://en.wikipedia.org/wiki/ASCII).

> *For more of the history and specifics, read about ['ANSI'](https://en.wikipedia.org/wiki/ANSI_character_set) and [character encoding](https://en.wikipedia.org/wiki/Character_encoding).*

What's important here is that all the characters are *strung* together in lines of text, making what us programmers call *strings!*

> *More accurately, strings in programming languages are represented with [UTF-8](https://en.wikipedia.org/wiki/UTF-8) or [UTF-16](https://en.wikipedia.org/wiki/UTF-16) code-units (bytes/octets and 16-bit words respectively).*

Here's how we can represent them in Python code, in that literal notation from earlier:

```python
'A Pie'
"Hi Guido!"
'Hello, but from single quotes.'
'This is \'quoted\'-string-ception!!! "Nice"'
'This one has a\nnewline in it.'
'And now \x20 triple space'
"""This is an incredibly long string, at least it's trying to be.
So long that it's now across two lines"""
'''Ditto
with
single \
quotes'''
"Aha! But also\
with normal quotes"
```

Perhaps you noticed those odd `\` backslashes. They form [escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences), and are used to insert special non-typable characters into text in your Python code.

You'll mostly only ever need to know a couple: `\"` or `\'` when you want to use quotes inside a string, `\n` for starting more text on a new line, and `\\` for including a backslash by itself.

##### Decimals (Floating-Point Numbers)

Back to numbers, modern computers store decimal numbers in a special way to make computation efficient. It's called 'floating' point (reffering to the decimal-dot) because you can change how many decimal places of precision you represent a number with. Some old computers only did decimals to a fixed number of places (like 2.01, 2.10) because they were manually doing the base-10 arithmetic which was slow.

They're simple enough to use in Python, just put a decimal-point in your number with at least one digit afterwards and you know have a floating-point number, or *float*.

```python
3.14159
-9.8
```

Because of the way floats are represented, you can have negative-zero and  infinity. There's also a special value called `nan`, short for 'Not-A-Number'.

```python
0.0
-0.0
float('-inf')
float('inf')
float('nan')
```

> *If you want a great example of how floating-point numbers work inside your computer, have a tinker with the [Float Toy](https://evanw.github.io/float-toy/). The particular format today's computers use is [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).*

##### Booleans

Last but not least of the primitives is booleans. These are named for English Logician [George Boole](https://en.wikipedia.org/wiki/George_Boole), and represent the binary conditions `True` and `False` - most often the result of comparing numbers.

```python
True
False
```

#### Collections

Now we've seen the most fundamental building blocks of Python programs, let's step up a level.

Collections are data structures that hold other data, each with their own special properties and ways of using them.

##### Lists

These are the most basic data structure, containing an ordered list of values. In Python, it is a list of anything, of any size - including more lists.

```python
[1, 2, 3]
['one', 2, 'four', 8.2, False]
['apple', 'orange', ['rapsberry', 'blueberry', ['pineapple']]]
```

We can get the size of a list by using `len()` similarly to `print()`:

```python
len([1, 2, 3])
```

You can request to get a specific an item from a list, using 'index' notation, where 0 is the first item, and specially -1 counts from the end:

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][-1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][-2]
```

You can also request copies of the list, but with only certain parts, known as 'slice' notation:

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][0:1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][1:3]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][1:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][:5]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][::-1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9][2:7:-3]
```

> *Lists are similar to "Arrays" as known in other programming languages; but arrays normally only contain the same type of item at a fixed size, or vectors which can additinally be resized.*

##### Dictionaries

These allow you to store away values for use again with a lookup index called a key.

```python
{ "key": "value" }
{ "a": 123, "b": 52 }
{ 1: 5 }
```

Just like lists, you can use index notation to get a certain item but inside the square brackets is the "key" you want the "value" of:

```python
{ "joe": 5000, "jim": 2700 }["joe"]
```

##### Tuples

These are like lists, but have a fixed size, so are useful for storing things like like coorinates:

```
(1,)
(3, 7)
(1, 5, 12.0)
("a", 45, 3.0, True)
(1, 3, 5)[2]
(1, 2, 7)[::-1]
```

##### Sets

The final simple data type, and work the same way as they do in maths. They contain an unordered collection of distinct items.

```python
{ 1 }
{ 1, 2, 1 }
{ 1, "2", 1.0, "1" }
```

### Operators

<https://docs.python.org/3/library/operator.html#mapping-operators-to-functions>

0.1 + 0.3 show quirk of floating point numbers

```python
1 + 1
2 * 2
3 - 3
4 / 4
5 % 5
6 // 4
(2 + 3) * 4
[1, 2] + [3]
(1, 2) + (3,)
==
!=
>
<
>=
<=
+=
*=
-=
/=
in
and
or
not
is
=
:=
```

### Variables

Now we're moving out of calculator territory. We can interact with results easier than the memory stack M+.

```python
a = 2
b = 8
c = a - b
print(c)

conventional_python_snake_case
PascalCase
camelCase
```

### Input

* input()
* int / casting
* f-strings
* print is a str-conversion, comma for space separated

```python
print("Hi I'm PyBot!")
name = input("What's your name? ")
print("Hi", name)
# print(f"Hi {name}! Nice to meet you. I calculated your name is {len(name)} characters long!")

x = int(input("Enter a number: "))
print("You entered:", x)
```

#### Type-Casting / Conversion

```python
int()
str()
float()
list()
tuple()
set()
dict()
```

### Conditions

```python
if input("What's the password? ") == "password":
    print("Correct! Here's your super secret password: password1")
else:
    print("Wrong! Either you mistyped, forgot, or someone is hacking you!")

x = int(input())
if x % 15 == 0:
    print("FizzBuzz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 == 0:
    print("Fizz")
else:
    print(x)
```

### Repetition (Loops)

* break
* continue

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

for i in range(100):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
```

### Functions

```python
def add(a, b):
    return a + b

def add(a, b=1):
    return a + b

def add(a, *args, **kwargs):
    pass

def complex_add(a, b):
    return (a[0] + b[0], a[1] + b[1])
```

### Modules

```python
import random
from random import randint
from random import *
import numpy as np
from numpy import sqrt as sq
```

#### Installing Modules from PyPI

```sh
$ pip install numpy
```

## 🔬 Advanced Python

### External Interaction

```python
with open("file.txt") as f:
    print(f.read())
```

### Complex Numbers

### Classes

```python
class Vehicle:
    def __init__(self, name):
        self._name = name

    def introduce(self):
        print(f"This is a {self._name}.")

class Car:
    pass
```

### Exceptions (Error Handling)

try opening a file, fail.
repeat logic twice, show complelling use of functions

```python
try:
    pass
except Error as e:
    pass
finally:
    pass
```

### Lambda Expressions

### List Comprehension

[i for i in range(10)]

### Iterables

```python
map(fn, iter)
filter(fn, iter)
[*iter]
{**iterkv}
```

### Structural Pattern Matching

```python
match <expression>:
    case <pattern> [<if guard>]:
        ...
```

### Generators / Coroutines

### Esoterics

* global/nonlocal scope keyword
* for else loops
* mutable default arguments

## ⛩️ Into Practice

### ProcSoc Turtle

![The ProgSoc Logo drawn using the Turtle Python library](./python/turtle-logo.png)

### Spirograph Turtle

### Automation and Scripting

```
pip install svg-turtle beautifulsoup4 svglib "reportlab<4"
```

Bulk file creation and renaming

<https://beautiful-soup-4.readthedocs.io/en/latest/>

Scrape ProgSoc Blog, Use Length of words in blog titles to generate a unique spiro for each post

### Web Server

UTS Wayfinding scraper

### More?

* Django / Flask
* Numpy / Matplotlib

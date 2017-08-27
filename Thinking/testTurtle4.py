import turtle
import math


def pie_chart(t, length, n):
    a = (180 - (360 / n))/2
    b = 360 / n
    in_length = (length / 2) / (math.cos(a / 180 * math.pi))
    # t.lf(b)
    for i in range(n):
        t.fd(length)
        draw_in_length(t, a, in_length)
        t.lt(a + b)
    t.pu()
    t.fd(in_length * 4 + 10)
    t.pd()


def draw_in_length(t, a, in_length):
    t.lt(180 - a)
    t.fd(in_length)
    t.lt(180)
    t.fd(in_length)


t = turtle.Turtle()
t.delay = 0.5
pie_chart(t, 200, 15)
pie_chart(t, 50, 9)
turtle.mainloop()
print(math.sin(math.pi / 6))

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()


def polypie(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle / 2)
        t.lt(angle)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(2 * y)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180 - angle)


# bob = turtle.Turtle()
#
# bob.pu()
# bob.bk(130)
# bob.pd()
#
# # draw polypies with various number of sides
# size = 40
# draw_pie(bob, 5, size)
# draw_pie(bob, 6, size)
#
#
# bob.hideturtle()
# turtle.mainloop()

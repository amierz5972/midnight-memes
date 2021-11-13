#from app import student_overall, course_overall
from random import randint

def range_set_finder(s: int, c: float) -> list[int]:
    if s - c >= 11:
        return [0, 70, 90, 95, 98, 100]
    elif s - c < 11 and s - c >= -5:
        return [0, 15, 40, 70, 90, 100]
    elif s - c < -5:
        return [0, 3, 10, 40, 80, 100]

def lgnv(rs: list[int]) -> float:
    g = randint(1, 100)
    if g >= rs[0] and g < rs[1]:
        return 4.0
    elif g >= rs[1] and g < rs[2]:
        return 3.0
    elif g >= rs[2] and g < rs[3]:
        return 2.0
    elif g >= rs[3] and g < rs[4]:
        return 1.0
    elif g >= rs[4] and g < rs[5]:
        return 0.0

def rs_avg(ar: list[float]) -> float:
    assert len(ar) != 0
    sum = 0
    for x in ar:
        sum += x
    return sum / len(ar)
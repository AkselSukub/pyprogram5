#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def are_points_symmetric(m1, m2):
    x1, y1 = m1
    x2, y2 = m2

    symmetric_x = x1 == x2
    symmetric_y = y1 == y2

    if symmetric_x and symmetric_y:
        return "Точки симметричны относительно обеих осей."
    elif symmetric_x:
        return "Точки симметричны относительно оси Oy."
    elif symmetric_y:
        return "Точки симметричны относительно оси Ox."
    else:
        return "Точки не симметричны относительно осей."

def main():
    m1 = tuple(map(float, input("Введите координаты точки M1 (x1 y1): ").split()))
    m2 = tuple(map(float, input("Введите координаты точки M2 (x2 y2): ").split()))

    result = are_points_symmetric(m1, m2)
    print(result)

if __name__ == "__main__":
    main()
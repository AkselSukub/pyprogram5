#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    n = int(input("Введите число карандашей (N <= 10): "))

    if n <= 0 or n > 10:
        print("Пожалуйста, введите число от 1 до 10.")
    else:
        if n == 1:
            print(f"Я купил {n} карандаш.")
        elif 2 <= n <= 4:
            print(f"Я купил {n} карандаша.")
        else:
            print(f"Я купил {n} карандашей.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_special_numbers():
    special_numbers = []

    for number in range(100, 1000):
        digit_sum = sum(int(digit) for digit in str(number))
        digit_product = 1
        for digit in str(number):
            digit_product *= int(digit)

        if digit_sum == digit_product:
            special_numbers.append(number)

    return special_numbers

def main():
    result = find_special_numbers()

    if result:
        print("Трехзначные натуральные числа, сумма цифр которых равна их произведению:")
        print(result)
    else:
        print("Таких чисел нет.")

if __name__ == "__main__":
    main()
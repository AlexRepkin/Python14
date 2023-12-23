#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_two(a):
    """Выполнение функции проходит успешно, однако переменная x локальная."""

    x = 2
    return a + x


def add_four(a):
    """
    Выполнение функции проходит успешно, ведь
    переменная x глобальная для вложенной функции
    """

    x = 2

    def add_some():
        print("x = " + str(x))
        return a + x
    return add_some()


def mul(a):

    def helper(b):
        return a * b
    return helper


if __name__ == '__main__':
    print(add_two(3))
    print(add_four(5))
    new_mul5 = mul(5)  # Создание функции-аналога
    print(new_mul5(2))  # Передача данных сразу вложенной функции, а внешней всегда передаётся 5
    # Получение ошибки, так как x - локальная переменная в функции add_two.
    print(x)

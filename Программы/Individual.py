#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Внутренняя функция увеличивает полученное значение на 3."""


def calculaion():

    def plus_3(value):
        return value + 3
    return plus_3


if __name__ == '__main__':
    cnt = calculaion()
    k = int(input("Good day! Please, enter value: "))
    print("According to our calculations, answer is - ", cnt(k))

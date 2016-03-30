# coding=utf-8

# Первый практикум
# Задача 1.1

from __future__ import print_function
from __future__ import division
import numpy as np
import utils


def f(x, a):
    """Возвращает значение функции из искомого уравнения ƒ(x, a) = 0 """
    return np.fabs(x * (x - a)) - a * np.log(x)


def phi(x, a):
    """Вовзвращает значение функции сжимающего отоброжения"""
    if a < 0:  # a in (-inf, 0)
        return np.exp(x * (x - a) / a)
    elif 0 <= a <= 1:
        raise ValueError("alpha не должна лежать в отрезке [0, 1]")
    elif 1 < a:  # a in (1, inf)
        if x < a:
            return np.sqrt(a * (x - np.log(x)))  # x in (1, a)
        else:
            return a * np.log(x) / x + a  # x in (a, inf)
    else:
        raise AssertionError("Unhandled case with a=%s and x=%s" % (a, x))


def root_with_negative_alpha(alpha):
    """Поиск корня при отрицательных альфа"""
    if alpha > 0:
        raise ValueError('alpha не может быть отрицательной')

    x0 = 1 / 2

    print('')
    print('Поиск корня при отрицательной альфа')
    print('Параметр альфа: %f' % alpha)
    print('Ищем корень x в интервале (0, 1)')
    print('Начальное приближение x0: %f' % x0)
    print('==============================')

    solve_and_print(alpha=alpha, x0=x0)


def root_with_positive_alpha(alpha):
    root_less_than_positive_alpha(alpha)
    root_greater_than_positive_alpha(alpha)


def root_less_than_positive_alpha(alpha):
    """Поиск корня меньшего чем положительная альфа"""
    if alpha <= 1:
        raise ValueError('alpha должна быть больше 1.')

    # x0 = (1 + np.log(alpha)) / 2
    x0 = 1 + (alpha - 1) * (6 / 7)

    print('')
    print('Поиск корня при 1 < root < a')
    print('Параметр альфа: %f' % alpha)
    print('Ищем корень x в интервале (%f, %f)' % (1, alpha))
    print('Начальное приближение x0: %f' % x0)
    print('==============================')

    solve_and_print(alpha=alpha, x0=x0)


def root_greater_than_positive_alpha(alpha):
    """Поиск корня большего чем положительная альфа"""
    if alpha <= 1:
        raise ValueError('alpha должна быть больше 1.')

    x0 = alpha + np.log(alpha)

    print('')
    print('Поиск корня при 1 < a < root')
    print('Параметр альфа: %f' % alpha)
    print('Ищем корень x в интервале (%f, inf)' % alpha)
    print('Начальное приближение x0: %f' % x0)
    print('==============================')

    solve_and_print(alpha=alpha, x0=x0)


def solve_and_print(alpha, x0):
    (root, step) = utils.modified_fixed_point(phi, [x0], args=np.array([alpha]), xtol=1e-9, maxiter=1000)

    print('кол-во сделанных шагов: %d' % step)
    print('корень: %f' % root)
    print('итерация в корне: %f' % phi(root, alpha))
    print('значение в корне: %e' % f(root, alpha))
    print('')


def solve(alpha):
    print('Поиск корней при альфа:', alpha)

    if alpha < 0:
        return root_with_negative_alpha(alpha)
    elif alpha == 0:
        print("При альфа=0 корень x=0")
    elif 0 < alpha < 1:
        print("Нет корней при alpha из интервала (0, 1)")
    elif alpha == 1:
        print("При альфа=1 корень x=1")
    elif 1 < alpha:
        return root_with_positive_alpha(alpha)
    else:
        raise AssertionError("Unhandled case with a=%s" % alpha)


def main():
    solve(alpha=4.5)


if __name__ == "__main__":
    main()

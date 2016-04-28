# coding=utf-8

# Третий практикум
# Задача 3.3
# Задачи класического вариационного исчисления и задачи Лагранжа

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from scipy import integrate
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


# noinspection SpellCheckingInspection
def dfdt(t, y, u, alpha):
    x1 = y[0]
    x2 = y[1]
    p1 = y[2]
    p2 = y[3]

    # Output from ODE function must be a COLUMN vector, with n rows
    n = len(y)
    # noinspection SpellCheckingInspection
    dydt = np.zeros((n, 1))
    dydt[0] = x2
    dydt[1] = -x1 * np.exp(-alpha * x1) + u
    dydt[2] = p2 * np.exp(-alpha * x1) - alpha * p2 * x1 * np.exp(-alpha * x1)
    dydt[3] = -x2 * p1
    return dydt


# def func():


def main():
    a = 1


if __name__ == "__main__":
    main()

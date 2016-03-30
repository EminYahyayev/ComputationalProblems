# coding=utf-8

# Второй практикум
# Задача 2.1
# Расчитать траекторию

from __future__ import print_function
from __future__ import division
from scipy.integrate import ode
import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    x1 = y[0]
    y1 = y[1]
    x2 = y[2]
    y2 = y[3]

    # Output from ODE function must be a COLUMN vector, with n rows
    n = len(y)
    # noinspection SpellCheckingInspection
    dydt = np.zeros((n, 1))
    dydt[0] = x2
    dydt[1] = y2
    dydt[2] = x1 * (y1 * y1 - 1)
    dydt[3] = y1 * (x1 * x1 - 1)
    return dydt


def solve(alpha):
    # Initial conditions
    y0 = np.zeros((4, 1))
    y0[0] = alpha
    y0[1] = 1
    y0[2] = 0
    y0[3] = 0

    # Time grid for integration
    t0 = 0
    tF = 50
    num_steps = 1000
    tt = np.linspace(t0, tF, num_steps)
    # Setup list ot hold solutions
    yy = np.array(y0)

    solver = ode(f)
    solver.set_integrator('dopri5')
    solver.set_initial_value(y0, t0)

    # Integrate
    for t in tt[1:]:
        r = solver.integrate(t)
        # print("Solution ", r)
        yy = np.append(yy, r, axis=1)
        if not solver.successful():
            print("WARNING: Integration not successful!")

    # print(tt)
    # print(yy)

    plt.figure(1)
    plt.plot(tt, yy[0], 'b', label='x(t)')
    plt.plot(tt, yy[1], 'g', label='y(t)')
    plt.legend(loc='best')

    plt.xlabel('t')
    plt.title('ODE Solution with alpha=%.2f' % alpha)
    plt.grid()
    plt.show()


def main():
    alpha1 = 0.5
    alpha2 = 0.1

    solve(alpha=alpha1)


if __name__ == "__main__":
    main()
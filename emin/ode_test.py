import numpy as np
from scipy import integrate


def solver(y, t):
    return [y[1], -2 * y[0] - y[1]]


def main():
    a_t = np.arange(0, 25.0, 0.01)
    asol = integrate.odeint(solver, [1, 0], a_t)
    astack = np.c_[a_t, asol[:, 0], asol[:, 1]]
    np.savetxt('approx.csv', astack, delimiter=',', header='t, y, yd', comments='')


if __name__ == '__main__':
    main()

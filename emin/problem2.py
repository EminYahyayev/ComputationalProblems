# coding=utf-8

# Второй практикум
# Задача 2.1
# Расчитать траекторию

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

debug = True


# noinspection PyUnusedLocal
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
    dydt[2] = x1 * (y1 ** 2 - 1)
    dydt[3] = y1 * (x1 ** 2 - 1)
    return dydt


# noinspection SpellCheckingInspection
def solout(t, y):
    if debug:
        print('Solout: t=%.5f, x=%.5f, y=%.5f' % (t, y[0], y[1]))


# def solve_plot(alpha, eps=1e-7):
#     # Initial conditions
#     y0 = np.zeros((4, 1))
#     y0[0] = alpha  # x(0)
#     y0[1] = 1  # y(0)
#     y0[2] = 0  # dxdt(0)
#     y0[3] = 0  # dydt(0)
#
#     # Time grid for integration
#     t0 = 0
#     tF = 50
#     num_steps = 500
#     tt = np.linspace(t0, tF, num_steps)
#     # Setup list ot hold solutions
#     yy = np.array(y0)
#
#     solver = integrate.ode(f)
#     solver.set_integrator('dop853', rtol=eps, atol=eps, nsteps=1000)
#     # solver.set_solout(solout)
#     solver.set_initial_value(y0, t0)
#
#     # Integrate
#     for t in tt[1:]:
#         r = solver.integrate(t)
#         # print("Solution ", r)
#         yy = np.append(yy, r, axis=1)
#         if not solver.successful():
#             print('WARNING: Integration not successful at %f!' % t)
#
#     # print(tt)
#     # print(yy)
#
#     plt.figure(1)
#     plt.plot(tt, yy[0], 'b', label='x(t)')
#     plt.plot(tt, yy[1], 'g', label='y(t)')
#     plt.legend(loc='best')
#
#     plt.title('Alpha = %.2f' % alpha)
#     plt.xlabel('t')
#     plt.ylabel('f(t)')
#     plt.grid()
#     plt.show()


def get_solver(alpha, eps=1e-7):
    # Initial conditions
    t0 = 0
    y0 = np.zeros((4, 1))
    y0[0] = alpha  # x(0)
    y0[1] = 1  # y(0)
    y0[2] = 0  # dxdt(0)
    y0[3] = 0  # dydt(0)

    solver = integrate.ode(f)
    solver.set_integrator('dopri5', rtol=eps, nsteps=5000)
    solver.set_initial_value(y0, t0)

    return solver


def solve(t, alpha, eps=1e-7, output=False):
    solver = get_solver(alpha, eps=eps)
    y = solver.integrate(t)
    if not solver.successful():
        raise RuntimeError('WARNING: Integration not successful at eps=%.0e, t=%.2f!' % (eps, t))

    if output:
        # print('Solution: t=%.2f, eps=%.0e, (x(t), y(t)) = (%.8e, %.8e)' % (t, eps, y[0], y[1]))
        print('y[1]=%.14f\\\\y[2]=%.14f\\\\y[3]=%.14f\\\\y[4]=%.14f' % (y[0], y[1], y[2], y[3]))

    return y


def print_values_row(t, alpha, eps):
    print('t=%.1f' % t)
    for e in eps:
        y = solve(t, alpha, eps=e)
        print('&\\centering')
        print('y[1]=%.14f\\\\y[2]=%.14f\\\\y[3]=%.14f\\\\y[4]=%.14f' % (y[0], y[1], y[2], y[3]))

    print('&\\\\')


def print_values_table(t, alpha, eps):
    print('\n')
    print('\\begin{table} \\centering')
    print('\\parbox{15cm}{\caption{Результаты Вычислений при альфа=%.1f}\\label{Ts0Sib}}' % alpha)
    print('\\begin{tabular}{| p{1.5cm} || p{4.5cm} | p{4.5cm} | p{4.5cm}l |}')
    print('	\\hline\\hline')
    print('t & \\centering $\\varepsilon_1=1e-7$ \n'
          '&\\centering$\\varepsilon_2=1e-9$ \n'
          '&\\centering $\\varepsilon_3=1e-11$  \n'
          '& \\\\')

    for tt in t:
        print('\\hline')
        print_values_row(tt, alpha, eps)

    print('\\hline\\hline\\end{tabular}\\end{table}')


def print_delta_row(y1, y2, y3, y4):
    print('$\\Delta$y[1]=%.8e\\\\$\\Delta$y[2]=%.8e\\\\\n$\\Delta$y[3]=%.8e\\\\$\\Delta$y[4]=%.8e' % (y1, y2, y3, y4))


def print_delta_row_relative(y1, y2, y3, y4):
    print(
        '$\\Delta$y[1]=%2.4f\\\\$\\Delta$y[2]=%2.4f\\\\\n$\\Delta$y[3]=%2.4f\\\\$\\Delta$y[4]=%2.4f' % (y1, y2, y3, y4))


def print_errors_row(t, alpha, eps):
    y1 = solve(t, alpha=alpha, eps=eps[0])
    y2 = solve(t, alpha=alpha, eps=eps[1])
    y3 = solve(t, alpha=alpha, eps=eps[2])

    print('t=%.1f' % t)
    print('&\\centering')
    print_delta_row(y1[0] - y2[0],
                    y1[1] - y2[1],
                    y1[2] - y2[2],
                    y1[3] - y2[3])
    print('&\\centering')
    print_delta_row(y2[0] - y3[0],
                    y2[1] - y3[1],
                    y2[2] - y3[2],
                    y2[3] - y3[3])
    print('&\\centering')
    print_delta_row_relative((y1[0] - y2[0]) / (y2[0] - y3[0]),
                             (y1[1] - y2[1]) / (y2[1] - y3[1]),
                             (y1[2] - y2[2]) / (y2[2] - y3[2]),
                             (y1[3] - y2[3]) / (y2[3] - y3[3]))

    print("&\\\\")


def print_errors_table(t, alpha, eps):
    print('\n')
    print('\\begin{table} \\centering')
    print('\\parbox{15cm}{\caption{Результаты Вычислений при альфа=%.1f}\\label{Ts0Sib}}' % alpha)
    print('\\begin{tabular}{| p{1.5cm} || p{4.5cm} | p{4.5cm} | p{3cm}l |}')
    print('	\\hline\\hline')
    print('t & \\centering $y_1-y_2$ \n'
          '&\\centering $y_2-y_3$ \n'
          '&\\centering $\\frac{y_1-y_2}{y_2-y_3}$  \n'
          '& \\\\')

    for tt in t:
        print("\\hline")
        print_errors_row(tt, alpha, eps)

    print('\\hline\\hline\\end{tabular}\\end{table}')


def main():
    tf = 50
    t = [tf / 4, tf * 2 / 4, tf * 3 / 4, tf]
    # t = [tf / 8, tf * 2 / 8, tf * 3 / 8, tf * 4 / 8, tf * 5 / 8, tf * 6 / 8, tf * 7 / 8, tf]
    eps = [1e-7, 1e-9, 1e-11]
    alpha = [0.1, 0.5]

    integrate.odeint()

    print_values_table(t, alpha[1], eps)
    print_errors_table(t, alpha[1], eps)


if __name__ == "__main__":
    main()

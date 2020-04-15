import math
import numpy as np


def f(valor):
    interno = math.sin(2 * valor) + 4 * valor ** 2 + 3 * valor
    return pow(interno, 2)


def x(a, xIni, xFim):
    return ((xIni + xFim) / 2) + ((xFim - xIni) / 2) * a


def doisPontos(xIni, xFim):
    a1 = -np.sqrt(3) / 3
    a2 = np.sqrt(3) / 3
    w = 1
    somatorio = w * f(x(a1, xIni, xFim)) + w * f(x(a2, xIni, xFim))
    resultado = ((xFim - xIni) / 2) * somatorio

    print("%1.7f\n" % resultado)


def tresPontos(xIni, xFim):
    a1 = -np.sqrt(3 / 5)
    a2 = 0
    a3 = np.sqrt(3 / 5)

    w1 = 5 / 9
    w2 = 8 / 9
    w3 = 5 / 9

    somatorio = w1 * f(x(a1, xIni, xFim)) + w2 * f(x(a2, xIni, xFim)) + w3 * f(x(a3, xIni, xFim))
    resultado = ((xFim - xIni) / 2) * somatorio

    print("%1.7f\n" % resultado)


def quatroPontos(xIni, xFim):
    a1 = np.sqrt((3 - 2 * np.sqrt(6 / 5)) / 7)
    a2 = -np.sqrt((3 - 2 * np.sqrt(6 / 5)) / 7)
    a3 = np.sqrt((3 + 2 * np.sqrt(6 / 5)) / 7)
    a4 = -np.sqrt((3 + 2 * np.sqrt(6 / 5)) / 7)

    w1 = (18 + np.sqrt(30)) / 36
    w2 = (18 + np.sqrt(30)) / 36
    w3 = (18 - np.sqrt(30)) / 36
    w4 = (18 - np.sqrt(30)) / 36

    somatorio = w1 * f(x(a1, xIni, xFim)) + w2 * f(x(a2, xIni, xFim)) + w3 * f(x(a3, xIni, xFim)) + w4 * f(
        x(a4, xIni, xFim))
    resultado = ((xFim - xIni) / 2) * somatorio

    print("%1.7f\n" % resultado)


doisPontos(0, 1)

tresPontos(0, 1)

quatroPontos(0, 1)

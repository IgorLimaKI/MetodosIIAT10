import math
import numpy as np

# Valor exato da integral do polinomio
VALOR_EXATO = 17.8764703
# Tolerância defina na lista
TOLERANCIA = 0.000001
# Quantidade de passos que será incrementado
INCREMENTO = 1


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

    return resultado


def tresPontos(xIni, xFim):
    a1 = -np.sqrt(3 / 5)
    a2 = 0
    a3 = np.sqrt(3 / 5)

    w1 = 5 / 9
    w2 = 8 / 9
    w3 = 5 / 9

    somatorio = w1 * f(x(a1, xIni, xFim)) + w2 * f(x(a2, xIni, xFim)) + w3 * f(x(a3, xIni, xFim))
    resultado = ((xFim - xIni) / 2) * somatorio

    return resultado


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

    return resultado


def resolver(xIni, xFim, pontos):
    resultado = 0
    numeroParticoes = 0
    while erroRelativo(resultado) > TOLERANCIA:
        resultado = 0
        numeroParticoes = numeroParticoes + 1
        deltax = (xFim - xIni) / numeroParticoes
        xIniAtual = xIni
        xFimAtual = xIniAtual + deltax
        if pontos == 2:
            for i in range(numeroParticoes):
                resultado = resultado + doisPontos(xIniAtual, xFimAtual)
                xIniAtual = xFimAtual
                xFimAtual = xIniAtual + deltax
        if pontos == 3:
            for i in range(numeroParticoes):
                resultado = resultado + tresPontos(xIniAtual, xFimAtual)
                xIniAtual = xFimAtual
                xFimAtual = xIniAtual + deltax
        if pontos == 4:
            for i in range(numeroParticoes):
                resultado = resultado + quatroPontos(xIniAtual, xFimAtual)
                xIniAtual = xFimAtual
                xFimAtual = xIniAtual + deltax

    return resultado, numeroParticoes


def erroRelativo(aproximado):
    return abs(aproximado - VALOR_EXATO) / VALOR_EXATO


# resolver(0, 1, 1, 4)

def main():
    for i in range(3):
        res, ite = resolver(0, 1, i + 2)
        print(
            'Total de particoes para formula de {} pontos: {} iteracoes'.format(res, ite))
        print('************************************************************')


if __name__ == '__main__':
    print('************************** CALCULANDO **************************')
    main()

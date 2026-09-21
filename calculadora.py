"""Operacoes matematicas basicas para reutilizacao em outros arquivos."""


def somar(a, b):
    """Retorna a soma de dois valores."""
    return a + b


def subtrair(a, b):
    """Retorna a diferenca entre dois valores."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de dois valores."""
    return a * b


def dividir(a, b):
    """Divide a por b e retorna None quando b e zero."""
    if b == 0:
        return None
    return a / b
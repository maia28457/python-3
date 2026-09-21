"""Funcoes estatisticas opcionais da atividade."""

from collections import Counter


def media(valores):
    """Retorna a media aritmetica de uma sequencia."""
    if not valores:
        raise ValueError("A lista de valores nao pode estar vazia.")
    return sum(valores) / len(valores)


def mediana(valores):
    """Retorna o valor central de uma sequencia ordenada."""
    if not valores:
        raise ValueError("A lista de valores nao pode estar vazia.")
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2


def moda(valores):
    """Retorna uma lista com os valores que mais se repetem."""
    if not valores:
        raise ValueError("A lista de valores nao pode estar vazia.")
    frequencias = Counter(valores)
    maior_frequencia = max(frequencias.values())
    return [valor for valor, frequencia in frequencias.items()
            if frequencia == maior_frequencia]
"""Script principal: demonstra a reutilizacao dos modulos da atividade."""

import calculadora
import estatistica as est
from utilidades import (
    adicionar_item_seguro,
    caixa,
    converter_temperatura,
    ficha_aluno,
    validar_senha,
)


def fatorial(numero):
    """Retorna o fatorial de um numero inteiro nao negativo."""
    if numero < 0:
        raise ValueError("O fatorial nao existe para numeros negativos.")
    if numero <= 1:
        return 1
    return numero * fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    """Monta um relatorio usando parametros posicionais e nomeados."""
    separador = config.get("separador", "\n")
    cabecalho = config.get("cabecalho", True)
    partes = [titulo] if cabecalho else []
    partes.extend(str(linha) for linha in linhas)
    return separador.join(partes)


def main():
    print("Calculadora")
    print("Soma:", calculadora.somar(8, 2))
    print("Subtracao:", calculadora.subtrair(8, 2))
    print("Multiplicacao:", calculadora.multiplicar(8, 2))
    print("Divisao:", calculadora.dividir(8, 2))
    print("Divisao por zero:", calculadora.dividir(8, 0))

    print("\nUtilidades")
    print("25 C em F:", converter_temperatura(25, "C", "F"))
    print("Senha valida:", validar_senha("Python123"))
    print("Total da caixa:", caixa(10.5, 4.5, 5))
    print("Ficha:", ficha_aluno(nome="Ana", idade=20, curso="Python"))

    lista_original = ["caderno", "caneta"]
    lista_nova = adicionar_item_seguro(lista_original, "borracha")
    print("Lista original:", lista_original)
    print("Lista nova:", lista_nova)

    valores = [2, 3, 3, 7, 9]
    print("\nEstatistica")
    print("Media:", est.media(valores))
    print("Mediana:", est.mediana(valores))
    print("Moda:", est.moda(valores))
    print("Fatorial de 5:", fatorial(5))
    print(relatorio("Relatorio", "Modulos importados", "Funcoes executadas"))


if __name__ == "__main__":
    main()
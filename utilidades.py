"""Funcoes reutilizaveis dos exercicios praticos."""


def converter_temperatura(valor, origem, destino):
    """Converte temperaturas entre Celsius, Fahrenheit e Kelvin."""
    origem = origem.upper()
    destino = destino.upper()

    if origem == destino:
        return valor

    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        raise ValueError("Escala de origem invalida. Use C, F ou K.")

    if destino == "C":
        return celsius
    if destino == "F":
        return celsius * 9 / 5 + 32
    if destino == "K":
        return celsius + 273.15
    raise ValueError("Escala de destino invalida. Use C, F ou K.")


def validar_senha(senha):
    """Verifica se a senha tem 8 caracteres, maiuscula, minuscula e numero."""
    return (
        len(senha) >= 8
        and any(caracter.isupper() for caracter in senha)
        and any(caracter.islower() for caracter in senha)
        and any(caracter.isdigit() for caracter in senha)
    )


def caixa(*precos):
    """Recebe varios precos e retorna o total da compra."""
    return sum(precos)


def ficha_aluno(**dados):
    """Recebe dados nomeados e retorna uma ficha formatada do aluno."""
    nome = dados.get("nome", "Nao informado")
    idade = dados.get("idade", "Nao informada")
    curso = dados.get("curso", "Nao informado")
    return f"Nome: {nome} | Idade: {idade} | Curso: {curso}"


def adicionar_item_seguro(lista, item):
    """Retorna uma nova lista com item, preservando a lista original."""
    nova_lista = lista.copy()
    nova_lista.append(item)
    return nova_lista


# Versoes equivalentes em Portugal (comentadas):
#
# Conversor de temperatura:
# def conversor_temperatura(valor, origem, destino):
#     # A logica e a mesma; apenas os nomes podem seguir o portugues europeu.
#     if origem == "C" and destino == "F":
#         return valor * 9 / 5 + 32
#     return valor
#
# Validador de palavra-passe:
# def validar_palavra_passe(palavra_passe):
#     return len(palavra_passe) >= 8 and any(
#         caracter.isdigit() for caracter in palavra_passe
#     )
#
# Caixa:
# def caixa_portugal(*precos):
#     # Em Portugal, "precos" continua representando varios precos.
#     return sum(precos)
#
# Ficha do aluno:
# def ficha_do_aluno(**dados):
#     nome = dados.get("nome", "Nao indicado")
#     curso = dados.get("curso", "Nao indicado")
#     return f"Nome: {nome} | Curso: {curso}"
#
# Lista segura:
# def acrescentar_item_seguro(lista, item):
#     nova_lista = lista.copy()
#     nova_lista.append(item)
#     return nova_lista
import random
import string


def gerar_senha(tamanho=12):
    """
    Gera uma senha aleatória com letras maiúsculas, minúsculas, números e caracteres especiais.
    :param tamanho: Tamanho da senha gerada.
    :return: Senha gerada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    senha = gerar_senha(tamanho)
    print(f"Sua senha segura é: {senha}")

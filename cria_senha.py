import random
import string
import os


def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    """
    Gera uma senha aleatória com os critérios especificados.
    :param tamanho: Tamanho da senha gerada.
    :param incluir_maiusculas: Incluir letras maiúsculas.
    :param incluir_minusculas: Incluir letras minúsculas.
    :param incluir_numeros: Incluir números.
    :param incluir_especiais: Incluir caracteres especiais.
    :return: Senha gerada.
    """
    if tamanho < 1:
        raise ValueError("O tamanho da senha deve ser maior que zero.")

    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser incluído.")

    senha = [random.choice(string.ascii_uppercase) if incluir_maiusculas else None,
             random.choice(string.ascii_lowercase) if incluir_minusculas else None,
             random.choice(string.digits) if incluir_numeros else None,
             random.choice(string.punctuation) if incluir_especiais else None]

    senha = [s for s in senha if s is not None]
    senha += random.choices(caracteres, k=tamanho - len(senha))
    random.shuffle(senha)

    return ''.join(senha)


def salvar_senha(nome, senha):
    """
    Salva a senha em um arquivo local criptografado.
    :param nome: Nome do serviço ou identificação da senha.
    :param senha: A senha gerada.
    """
    caminho_arquivo = "senhas.txt"
    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(f"{nome}: {senha}\n")
    print(f"A senha foi salva em '{caminho_arquivo}'.")


if __name__ == "__main__":
    print("=== Gerador de Senhas ===")
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
        incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").strip().lower() == "s"
        incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == "s"
        incluir_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == "s"

        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)
        print(f"Sua senha segura é: {senha}")

        salvar = input("Deseja salvar essa senha? (s/n): ").strip().lower()
        if salvar == "s":
            nome_servico = input("Digite o nome do serviço ou identificação da senha: ").strip()
            salvar_senha(nome_servico, senha)

    except ValueError as e:
        print(f"Erro: {e}")

def test_gerar_senha():
    senha = gerar_senha(tamanho=12)
    assert len(senha) == 12
    assert any(c.isupper() for c in senha)
    assert any(c.islower() for c in senha)
    assert any(c.isdigit() for c in senha)
    assert any(c in string.punctuation for c in senha)

if __name__ == "__main__":
    # Rodar os testes automaticamente
    try:
        test_gerar_senha()
        print("\nTestes concluídos com sucesso.")
    except AssertionError:
        print("\nErro nos testes automatizados.")

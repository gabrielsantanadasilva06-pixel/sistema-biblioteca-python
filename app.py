# ----imports-----
import json
import os

# ----funções de arquivos-----


def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ===================
# carregamento
# ===================


livros = carregar_dados("livros.json")

# ==============================
# LOGIN
# ==============================
while True:

    print("1 - cadastrar livros ")
    print("2 - listar livros")
    print("3 - buscar livros")
    print("4 - remover livros")
    print("5 - sair")

    opcao = input("escolha: ")

# cadastrar livros
    if opcao == "1":
        titulo = input("titulo: ")
        autor = input("autor: ")
        publicado = input("data de publicação: ")

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano de publicação": publicado
        }
        livros.append(livro)
        salvar_dados("livros.json", livros)
        print("livro cadastrado!")


# listagem de livros
    if opcao == "2":
        if not livros:
            print("Livro não cadastrado!")
            print("cadastre um novo livro na opção 1")
        else:

            for livro in livros:
                print(f"titulo: {livro['titulo']}")
                print(f"autor: {livro['autor']}")
                print(f"ano de publicação: {livro['ano de publicação']}")
                print("-" * 30)

# busca de livros cadastrados
    if opcao == "3":
        if not livros:
            print("Nenhum livro cadastrado para buscar.")
        else:
            termo = input("Digite o título ou autor para buscar: ").lower()
            encontrados = []

            for livro in livros:
                if termo in livro['titulo'].lower() or termo in livro['autor'].lower():
                    encontrados.append(livro)

            if encontrados:
                print(f"\n--- {len(encontrados)} livro(s) encontrado(s) ---")
                for livro in encontrados:
                    print(
                        f"Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano de publicação']}")
                print("-" * 30)
            else:
                print("Nenhum livro encontrado com esse termo.")

# remover de livros
    if opcao == "4":
        if not livros:
            print("A lista está vazia!")
        else:
            nome_para_remover = input(
                "Digite o título exato do livro para remover: ").lower()

            # Busca o livro primeiro para confirmar se ele existe
            livro_encontrado = None
            for livro in livros:
                if livro["titulo"].lower() == nome_para_remover:
                    livro_encontrado = livro
                    break

            if livro_encontrado:
                print(
                    f"\nLivro encontrado: {livro_encontrado['titulo']} - Autor: {livro_encontrado['autor']}")
                confirmar = input(
                    "Tem certeza que deseja remover este livro? (s/n): ").lower()

                if confirmar == 's':
                    # Cria a nova lista sem o livro removido
                    livros = [l for l in livros if l["titulo"].lower()
                              != nome_para_remover]
                    salvar_dados("livros.json", livros)
                    print("Livro removido com sucesso!")
                else:
                    print("Remoção cancelada.")
            else:
                print("Livro não encontrado.")

# sair do sistema
    if opcao == "5":
        print("bliblioteca virtual encerrada com sucesso.")
        print("tenha um bom dia!")
        break

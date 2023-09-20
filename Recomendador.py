filmes = {
    1: {"titulo": "Matrix", "categoria": "Ação", "avaliacao": 4.5, "favorito": False, "assistido": False},
    2: {"titulo": "Interestelar", "categoria": "Ficção Científica", "avaliacao": 4.8, "favorito": False, "assistido": False},
    3: {"titulo": "Pantera Negra", "categoria": "Ação", "avaliacao": 4.3, "favorito": False, "assistido": False},
    4: {"titulo": "Cidade de Deus", "categoria": "Drama", "avaliacao": 4.7, "favorito": False, "assistido": False},
    5: {"titulo": "Breaking Bad", "categoria": "Drama", "avaliacao": 4.9, "favorito": False, "assistido": False},
    6: {"titulo": "Vingadores: Ultimato", "categoria": "Ação", "avaliacao": 4.9, "favorito": False, "assistido": False},
    7: {"titulo": "Mad Max: Estrada da Fúria", "categoria": "Ação", "avaliacao": 4.7, "favorito": False, "assistido": False},
    8: {"titulo": "Superbad", "categoria": "Comédia", "avaliacao": 4.1, "favorito": False, "assistido": False},
    9: {"titulo": "Se Beber, Não Case!", "categoria": "Comédia", "avaliacao": 4.0, "favorito": False, "assistido": False},
    10: {"titulo": "Forrest Gump", "categoria": "Drama", "avaliacao": 4.8, "favorito": False, "assistido": False},
    11: {"titulo": "O Poderoso Chefão", "categoria": "Drama", "avaliacao": 4.9, "favorito": False, "assistido": False},
    12: {"titulo": "Blade Runner 2049", "categoria": "Ficção Científica", "avaliacao": 4.6, "favorito": False, "assistido": False},
    13: {"titulo": "A Origem", "categoria": "Ficção Científica", "avaliacao": 4.7, "favorito": False, "assistido": False},
    14: {"titulo": "Toy Story", "categoria": "Animação", "avaliacao": 4.5, "favorito": False, "assistido": False},
    15: {"titulo": "Procurando Nemo", "categoria": "Animação", "avaliacao": 4.4, "favorito": False, "assistido": False},
    16: {"titulo": "O Iluminado", "categoria": "Terror", "avaliacao": 4.6, "favorito": False, "assistido": False},
    17: {"titulo": "Invocação do Mal", "categoria": "Terror", "avaliacao": 4.3, "favorito": False, "assistido": False},
    18: {"titulo": "Diário de uma Paixão", "categoria": "Romance", "avaliacao": 4.3, "favorito": False, "assistido": False},
    19: {"titulo": "Orgulho e Preconceito", "categoria": "Romance", "avaliacao": 4.2, "favorito": False, "assistido": False},
    20: {"titulo": "Harry Potter e a Pedra Filosofal", "categoria": "Fantasia", "avaliacao": 4.7, "favorito": False, "assistido": False},
    21: {"titulo": "O Senhor dos Anéis: A Sociedade do Anel", "categoria": "Fantasia", "avaliacao": 4.8, "favorito": False, "assistido": False},
    22: {"titulo": "Seven: Os Sete Crimes Capitais", "categoria": "Suspense", "avaliacao": 4.6, "favorito": False, "assistido": False},
    23: {"titulo": "Psicose", "categoria": "Suspense", "avaliacao": 4.5, "favorito": False, "assistido": False},
    24: {"titulo": "A 13ª Emenda", "categoria": "Documentário", "avaliacao": 4.8, "favorito": False, "assistido": False},
    25: {"titulo": "A Marcha dos Pingüins", "categoria": "Documentário", "avaliacao": 4.3, "favorito": False, "assistido": False},
}
usuarios = {}


def listar_filmes() -> None:
    for filme_id, filme_info in filmes.items():
        print(f"ID: {filme_id} - Título: {filme_info['titulo']} - Categoria: {filme_info['categoria']} - Avaliação da crítica: {filme_info['avaliacao']}")


def registrar_usuario(nome: str) -> None:
    """
    Esta função adiciona um novo usuário ao dicionário "usuarios"

    Args:
        nome: Recebe o nome do novo usuário
    """
    usuarios[nome] = {
        "avaliacoes": {},
        "filmes_assistidos": {},
        "filmes_favoritos": {}
    }


def listar_usuarios():
    """
        Esta função lista todos os usuários registrados
    """
    print("Lista de usuários registrados:")
    for usuario, chave in usuarios.items():
        print(f"""
        Nome: {usuario}
        Avaliações: {chave["avaliacoes"]}
        Filmes assistidos: {chave["filmes_assistidos"]}
        Filmes favoritos: {chave["filmes_favoritos"]}
""")


def avaliar_filme(usuario_nome: str, filme_id: int, avaliacao: float) -> None:
    """
      Esta função avalia determinado filme no dicionario do usuário selecionado

      Args:
          usuario_nome: Recebe o nome do usuário
          filme_id: Recebe o identificador do filme
          avaliacao: Recebe a nota
      """
    usuario = usuarios.get(usuario_nome)
    filme = filmes.get(filme_id)
    if usuario and filme:
        if 1 <= avaliacao <= 5:
            usuario["avaliacoes"][filme_id] = avaliacao
            print(f"\nAvaliação do filme '{filme['titulo']}' por {usuario_nome} atualizada para {avaliacao}")
        else:
            print("\nAvaliação deve ser um valor entre 1 e 5.")
    else:
        print("\nUsuário ou filme não encontrado.")


def favoritar_filme(usuario_nome: str, filme_id: int) -> None:
    """
    Esta função marca determinado filme como assistido no dicionario do usuário selecionado

    Args:
        usuario_nome: Recebe o nome do usuário
        filme_id: Recebe o identificador do filme

    """
    usuario = usuarios.get(usuario_nome)
    filme = filmes.get(filme_id)
    if usuario and filme:
        if not filme['favorito']:
            filme['favorito'] = True
            usuario["filmes_favoritos"][filme_id] = filme['titulo']
            print(f"\nFilme '{filme['titulo']}' adicionado aos favoritos de {usuario_nome}.")
        else:
            print("\nEste filme já está nos favoritos.")
    else:
        print("\nUsuário ou filme não encontrado.")


def marcar_assistido(usuario_nome: str, filme_id: int) -> None:
    """
    Esta função marca determinado filme como assistido no dicionario do usuário selecionado

    Args:
        usuario_nome: Recebe o nome do usuário
        filme_id: Recebe o identificador do filme
    """
    usuario = usuarios.get(usuario_nome)
    filme = filmes.get(filme_id)
    if usuario and filme:
        if not filme['assistido']:
            filme['assistido'] = True
            usuario["filmes_assistidos"][filme_id] = filme['titulo']
            print(f"\nFilme '{filme['titulo']}' marcado como assistido por {usuario_nome}.")
        else:
            print("\nEste filme já foi assistido anteriormente.")
    else:
        print("\nUsuário ou filme não encontrado.")


def filtrar_categoria(filtrar: str):
    """
    Esta função filtra os filmes por categoria.

    Args:
        filtrar (string): Informa a categoria de filme a ser buscado na listagem dos filmes.

    Returns:
        string: Puxa as informações dos filmes de acordo com a categoria digitada,

    Exemplo:
        filtrar_categoria(drama)
        ID: 4 - Título: Cidade de Deus - Categoria: Drama - Avaliação: 4.7
    """

    for chave, valor in filmes.items():

        if filtrar in valor['categoria']:
            print(f"ID: {chave} - Título: {valor['titulo']} - Categoria: {valor['categoria']} - Avaliação: {valor['avaliacao']}")

        elif filtrar not in ["Ação", "Drama", "Comédia", "Ficção Científica", "Animação", "Terror", "Romance", "Fantasia", "Suspense", "Documentário"]:
            print("\nA categoria digitada não consta na relação dos filmes.")
            break



while True:
    opcao = int(input("""
Digite a opção desejada:

1) Listar filmes
2) Registrar usuário
3) Listar usuários
4) Avaliar filme
5) Favoritar filme
6) Marcar como assistido
7) Filtrar por categoria
0) Sair

Digite a opção desejada: """))

    match opcao:
        case 1:
            listar_filmes()

        case 2:
            nome = str(input("Digite o seu nome de usuário: "))
            registrar_usuario(nome)
            print(f"\nUsuário {nome} registrado com sucesso!")

        case 3:
            listar_usuarios()

        case 4:
            listar_usuarios()
            usuario_nome = str(input("\nDigite o nome do usuário: "))
            listar_filmes()
            filme_id = int(input("\nDigite o ID do filme à ser avaliado: "))
            avaliacao = float(input("\nDigite a nota: "))
            avaliar_filme(usuario_nome, filme_id, avaliacao)

        case 5:
            listar_usuarios()
            usuario_nome = str(input("\nDigite o nome do usuário: "))
            listar_filmes()
            filme_id = int(input("\nDigite o ID do filme à ser favoritado: "))
            favoritar_filme(usuario_nome, filme_id)

        case 6:
            listar_usuarios()
            usuario_nome = str(input("\nDigite o nome do usuário: "))
            listar_filmes()
            filme_id = int(input("\nDigite o ID do filme à ser avaliado: "))
            marcar_assistido(usuario_nome, filme_id)

        case 7:
            filtrar = str(input("Digite a categoria desejada: ")).capitalize()
            filtrar_categoria(filtrar)

        case _:
            break

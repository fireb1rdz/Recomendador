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


def listar_filmes():
    for filme_id, filme_info in filmes.items():
        print(f"ID: {filme_id} - Título: {filme_info['titulo']} - Categoria: {filme_info['categoria']} - Avaliação da crítica: {filme_info['avaliacao']}")











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
            print("A categoria digitada não consta na relação dos filmes.")
            break


filtrar = input("Digite a categória que você deseja filtrar: ").title()
filtrar_categoria(filtrar)

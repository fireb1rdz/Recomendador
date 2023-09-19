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
usuarios = {
    1: {
        "nome": "Alice",
        "avaliacoes": {},
        "filmes_assistidos": {},
        "filmes_favoritos": {},
    },
    2: {
        "nome": "Bob",
        "avaliacoes": {},
        "filmes_assistidos": {},
        "filmes_favoritos": {},
    },

}

def listar_filmes():
    for filme_id, filme_info in filmes.items():
        print(
            f"ID: {filme_id} - Título: {filme_info['titulo']} - Categoria: {filme_info['categoria']} - Avaliação da crítica: {filme_info['avaliacao']}")












"""

Avaliar filmes

"""
def avaliar_filme(usuario_nome, filme_id, avaliacao):
    usuario = usuarios.get(usuario_nome)
    filme = filmes.get(filme_id)
    if usuario and filme:
        if 1 <= avaliacao <= 5:
            usuario["avaliacoes"][filme_id] = avaliacao
            print(f"Avaliação do filme '{filme['titulo']}' por {usuario['nome']} atualizada para {avaliacao}.")
        else:
            print("Avaliação deve ser um valor entre 1 e 5.")
    else:
        print("Usuário ou filme não encontrado.")


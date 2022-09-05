class Livro:
    def __init__(self, titulo, autor, genero, qnt_pag, ano_publi, editora, concluido=False):
        self.__titulo = titulo
        self.__autor = autor
        self.genero = genero
        self.qnt_pag = qnt_pag
        self.ano_publi = ano_publi
        self.editora = editora
        self.concluido = concluido


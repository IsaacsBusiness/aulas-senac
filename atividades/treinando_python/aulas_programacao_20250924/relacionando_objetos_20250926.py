class Aluno:
    def __init__(self, nome, id_aluno):
        self.nome = nome
        self.id_aluno = id_aluno
        self.cursos = []

    def apresentar(self) -> str:
        print(f"Aluno: {self.nome}, ID: {self.id_aluno}")


class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionarAluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        if not self.alunos:
            return "Nenhum aluno matriculado."
        return [aluno.nome for aluno in self.alunos]


def main():
    # Criando alunos
    aluno1 = Aluno("Ana", 1)
    aluno2 = Aluno("Bruno", 2)

    # Criando curso
    curso_python = Curso("Python para Iniciantes", "PY101")

    # Adicionando alunos ao curso
    curso_python.adicionarAluno(aluno1)
    curso_python.adicionarAluno(aluno2)

    # Listando alunos do curso
    print(f"Curso: {curso_python.nome} ({curso_python.codigo})")
    print("Alunos matriculados:")
    alunos = curso_python.listar_alunos()
    if isinstance(alunos, list):
        for nome in alunos:
            print(f"- {nome}")
    else:
        print(alunos)


main()

from datetime import datetime
from typing import List


class Nota:
    def __init__(self, valor: float, observacao: str = ""):
        self.valor = valor
        self.observacao = observacao

    def __str__(self):
        return f"Nota: {self.valor}, Observação: {self.observacao}"


class Matricula:
    def __init__(self, id_matricula: int, aluno, disciplina, data_matricula: datetime):
        self.id = id_matricula
        self.aluno = aluno
        self.disciplina = disciplina
        self.data_matricula = data_matricula
        self.notas = []
        self.nota = None  # Nota associada à matrícula

    def associarNota(self, nota: Nota):
        self.nota = nota
        f"\nNota associada à matrícula {self.id} na disciplina {self.disciplina.nome}."

    def __str__(self):
        return f"Matrícula {self.id}: {self.aluno.nome} em {self.disciplina.nome}, Data: {self.data_matricula.strftime('%Y-%m-%d')}"


class Disciplina:
    def __init__(self, nome: str, codigo: int, vagas: int = 10):
        self.nome = nome
        self.codigo = codigo
        self.vagas = vagas
        self.alunos_matriculados: List[Matricula] = []
        self.professor = None

    def registrarAluno(self, matricula: Matricula) -> bool:
        if self.vagas > len(self.alunos_matriculados):
            self.alunos_matriculados.append(matricula)
            print(
                f"\nAluno {matricula.aluno.nome} registrado na disciplina {self.nome}."
            )
            return True
        else:
            print(f"Não há vagas disponíveis na disciplina {self.nome}.")
            return False

    def atribuirProfessor(self, professor):
        self.professor = professor
        print(f"\nProfessor {professor.nome} atribuído à disciplina {self.nome}.")

    def __str__(self):
        return f"Disciplina {self.nome} (Código: {self.codigo}, Vagas: {self.vagas})"


class Aluno:
    def __init__(self, nome: str, id_aluno: int):
        self.nome = nome
        self.id = id_aluno
        self.matriculas: List[Matricula] = []

    def matricular(self, disciplina: Disciplina, sistema) -> bool:
        return sistema.registrar_em_disciplina(self, disciplina)

    def visualizar_relatorio(self) -> str:
        relatorio = f"Relatório de {self.nome}:"
        for matricula in self.matriculas:
            nota_str = matricula.nota.valor if matricula.nota else "Sem nota registrada"
            relatorio += f"\n{matricula.disciplina.nome}: {nota_str}"
        return relatorio


class Professor:
    def __init__(self, nome: str, id_professor: int):
        self.nome = nome
        self.id = id_professor
        self.disciplinas: List[Disciplina] = []

    def atribuir_disciplina(self, disciplina: Disciplina):
        disciplina.atribuirProfessor(self)
        self.disciplinas.append(disciplina)

    def inserir_nota(self, matricula: Matricula, valor: float, observacao: str = ""):
        nota = Nota(valor, observacao)
        matricula.associarNota(nota)

    def visualizar_relatorio(self) -> str:
        relatorio = f"Relatório do Professor(a) {self.nome}:"
        for disciplina in self.disciplinas:
            relatorio += f"\nDisciplina: {disciplina.nome}"
            for matricula in disciplina.alunos_matriculados:
                nota_str = (
                    matricula.nota.valor if matricula.nota else "Sem nota registrada"
                )
                relatorio += f"\nAluno: {matricula.aluno.nome}, Nota: {nota_str}"
        return relatorio


class SistemaEscolar:
    def __init__(self):
        self.alunos: List[Aluno] = []
        self.disciplinas: List[Disciplina] = []
        self.professores: List[Professor] = []
        self.matriculas: List[Matricula] = []
        self.contador_matriculas = 0

    def matricula_aluno(self, nome: str, id_aluno: int) -> Aluno:
        aluno = Aluno(nome, id_aluno)
        self.alunos.append(aluno)
        print(f"\nAluno {aluno.nome} matriculado ao sistema.")
        return aluno

    def registrar_em_disciplina(self, aluno: Aluno, disciplina: Disciplina) -> bool:
        if disciplina not in self.disciplinas:
            print(f"Disciplina {disciplina.nome} não encontrada no sistema.")
            return False

        self.contador_matriculas += 1
        matricula = Matricula(
            self.contador_matriculas, aluno, disciplina, datetime.now()
        )
        if disciplina.registrarAluno(matricula):
            aluno.matriculas.append(matricula)
            self.matriculas.append(matricula)

            # Simular aprovação automática pelo administrador
            print(f"Administrador aprovou a matrícula {matricula.id}.")
            return True
        return False

    def adicionar_disciplina(
        self, nome: str, codigo: int, vagas: int = 10
    ) -> Disciplina:
        disciplina = Disciplina(nome, codigo, vagas)
        self.disciplinas.append(disciplina)
        return disciplina

    def adicionar_professor(self, nome: str, id_professor: int) -> Professor:
        professor = Professor(nome, id_professor)
        self.professores.append(professor)
        return professor


# Exemplo de uso do sistema
def main():
    sistema = SistemaEscolar()

    # Adicionar disciplinas
    matematica = sistema.adicionar_disciplina("Matemática", 101, vagas=2)
    historia = sistema.adicionar_disciplina("História", 102, vagas=2)

    # Adicionar professores
    prof_ana = sistema.adicionar_professor("Ana", 1)
    prof_ana.atribuir_disciplina(matematica)

    prof_beto = sistema.adicionar_professor("Beto", 2)
    prof_beto.atribuir_disciplina(historia)

    # Matricular alunos
    aluno1 = sistema.matricula_aluno("João", 1)
    aluno2 = sistema.matricula_aluno("Maria", 2)

    # Alunos se matriculam em disciplinas
    aluno1.matricular(matematica, sistema)
    aluno2.matricular(matematica, sistema)
    aluno2.matricular(historia, sistema)

    # Professores inserem notas
    for matricula in matematica.alunos_matriculados:
        prof_ana.inserir_nota(matricula, 9.5, "Ótimo desempenho")

    # Visualizar relatórios
    print("\nRelatórios:")
    print(aluno1.visualizar_relatorio())
    print("\nRelatórios:")
    print(aluno2.visualizar_relatorio())
    print("\nRelatório do professor:")
    print(prof_ana.visualizar_relatorio())
    print("\nRelatório do professor:")
    print(prof_beto.visualizar_relatorio())


if __name__ == "__main__":
    main()

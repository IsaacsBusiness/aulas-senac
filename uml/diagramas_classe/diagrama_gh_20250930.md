```mermaid
classDiagram
    class SistemaGestaoHospitalar {
        +gerenciarPacientes() void
        +gerenciarConsultas() void
        +gerenciarInternacoes() void
        +gerenciarFaturamento() void
    }

    class BancoDeDados {
        +salvar(objeto: Object) void
        +buscar(id: String) Object
        +atualizar(objeto: Object) void
        +deletar(id: String) void
    }

    class Pessoa {
        -id: String
        -nome: String
        -dataNascimento: Date
        -endereco: String
    }

    class Paciente {
        +historicoMedico: String
        +agendarConsulta() void
        +solicitarInternacao() void
    }

    class Funcionario {
        -matricula: String
        -cargo: String
        -departamento: String
    }

    class Usuario {
        -login: String
        -senha: String
        -perfilAcesso: String
    }

    class Medico {
        -crm: String
        -especialidade: String
        +realizarConsulta() void
        +prescreverMedicamento() void
    }

    class Enfermeiro {
        -coren: String
        +administrarMedicamento() void
        +registrarObservacao() void
    }

    class Consulta {
        -dataHora: DateTime
        -sintomas: String
        -diagnostico: String
    }

    class Internacao {
        -dataEntrada: Date
        -dataSaida: Date
        -leito: String
    }

    class Leito {
        -numero: String
        -tipo: String
        -disponivel: Boolean
    }

    class Prontuario {
        -historico: String
    }

    class Procedimento {
        -data: Date
        -medicoResponsavel: Medico
    }

    class Exame {
        -tipoExame: String
        -resultado: String
    }

    class Faturamento {
        -valorTotal: Double
        -statusPagamento: String
        +gerarConta() Conta
    }

    class Conta {
        -id: String
        -servicosPrestados: List<Servico>
        -valor: Double
    }

    class Servico {
        -descricao: String
        -valor: Double
    }

    class Estoque {
        -itens: Map<Medicamento, Integer>
        +adicionarItem(medicamento: Medicamento, quantidade: int) void
        +removerItem(medicamento: Medicamento, quantidade: int) void
    }

    class Medicamento {
        -nome: String
        -descricao: String
        -estoque: int
    }

    %% =========================
    %% HERANÇA
    %% =========================
    Paciente --|> Pessoa
    Funcionario --|> Pessoa
    Medico --|> Funcionario
    Enfermeiro --|> Funcionario
    Usuario --|> Funcionario
    Procedimento --|> Servico
    Exame --|> Servico

    %% =========================
    %% ASSOCIAÇÕES COM MULTIPLICIDADE
    %% =========================
    Medico "1" --> "*" Consulta : realiza
    Paciente "1" --> "*" Consulta : possui
    Paciente "1" --> "*" Internacao : é_internado
    Internacao "1" --> "1" Leito : ocupa
    Faturamento "1" --> "*" Conta : gera
    Conta "1" --> "*" Servico : inclui
    Funcionario "1" --> "0..1" Usuario : pode_ter

    %% =========================
    %% AGREGAÇÃO
    %% =========================
    Paciente "1" o-- "1" Prontuario : possui
    Prontuario o-- "*" Consulta
    Prontuario o-- "*" Internacao
    Prontuario o-- "*" Procedimento
    Prontuario o-- "*" Exame

    %% =========================
    %% COMPOSIÇÃO
    %% =========================
    Estoque "1" *-- "*" Medicamento : contém

    %% =========================
    %% DEPENDÊNCIAS
    %% =========================
    SistemaGestaoHospitalar ..> BancoDeDados : <<usa>>
    SistemaGestaoHospitalar ..> Paciente : <<usa>>
    SistemaGestaoHospitalar ..> Consulta : <<usa>>
    SistemaGestaoHospitalar ..> Internacao : <<usa>>
    SistemaGestaoHospitalar ..> Faturamento : <<usa>>
 
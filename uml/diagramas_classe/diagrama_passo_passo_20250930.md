```mermaid
classDiagram

class Paciente{
    -id: int
    -nome: str
    -telefone: str
    -email: str
    +agendarConsulta()
    +solicitarCancelamento()
}

class Medico{
    -id: int
    -nome: str
    -crm: str
    -especialidade: str
    +checarAgendamento()
    +realizarConsulta()
}

class Consulta{
    -data: date
    -hora: time
    +confirmarConsulta()
    +cancelarConsulta()
}

class Pessoa{
    -id: int
    -nome: str
    +visitarHospital()
    +utilizarBanheiro()
}

Paciente --> Consulta
Medico --> Consulta

Paciente --|> Pessoa
Medico --|> Pessoa
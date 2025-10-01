```mermaid
sequenceDiagram
    participant Paciente
    participant Recepcionista
    participant SGH as SGH (Interface)
    participant Agendamento as Módulo de Agendamento
    participant BD as Banco de Dados
    participant Medico as Médico

    Paciente ->> Recepcionista: Solicita agendamento
    Recepcionista ->> SGH: Solicita horários do Médico
    SGH ->> Agendamento: Requisita disponibilidade
    Agendamento ->> BD: Consulta horários disponíveis do Médico
    BD -->> Agendamento: Retorna horários disponíveis
    Agendamento -->> SGH: Horários disponíveis
    SGH -->> Recepcionista: Exibe horários disponíveis
    Recepcionista ->> SGH: Seleciona e confirma horário
    SGH ->> Agendamento: Registrar consulta
    Agendamento ->> BD: Salvar consulta na agenda
    BD -->> Agendamento: Confirma registro
    Agendamento ->> Medico: Atualiza agenda
    Agendamento -->> SGH: Confirma agendamento
    SGH -->> Recepcionista: Retorna confirmação
    Recepcionista -->> Paciente: Informa agendamento realizado

    alt Paciente ou Médico não encontrados
        SGH -->> Recepcionista: Notifica erro (não encontrado)
        Recepcionista -->> Paciente: Informa falha no agendamento
    end
    alt Horário já ocupado
        BD -->> Agendamento: Horário indisponível
        Agendamento -->> SGH: Notifica conflito
        SGH -->> Recepcionista: Informa indisponibilidade
        Recepcionista -->> Paciente: Solicita escolher outro horário
    end
import MonitoramentoVagas

eventos = []

def adicionarEvento(nome, vagas, usuarios, tipoVeiculo, data, liberarVeiculos):
    evento = (nome, data, vagas, liberarVeiculos)
    eventos.append(evento)

    MonitoramentoVagas.reservarVagas(vagas,usuarios, tipoVeiculo, nome)

def listarEventos():
    saida = ""

    for evento in eventos:
        saida+= "\n"
        saida+= "Nome: " +evento[0] + "\n"
        saida+=  "Data: " +evento[1] + "\n"
        saida+= "Vagas: " +evento[2] + "\n"
        saida += "Liberação de Veículos: " + evento[3]

    saida+= "\n"
    return saida



def main():

    executando = True
    while executando:

        print("1.Cadastrar eventos ")
        print("2.Listar eventos ")
        print("3.Voltar ao menu anterior ")

        opcao = int(input("> "))

        if opcao == 1:
            nome = input("Informe um nome para o evento: ")
            tipoVaga = input(
                "Informe o tipo de estacionamento \n(c) Carro \n(m) Moto \n(o) Onibus \n(r) Reservadas \n> ")
            if tipoVaga not in ("c", "m", "o", "r"):
                print("Tipo de estacionamento inválido")
                executando = False
            data = input("Informe a data do evento: ")
            vagas = input("Informe as vagas desejadas: ")
            usuarios = input("Informe os usuários para as vagas: ")
            liberarVeiculo = input("Deseja liberar entrada de veículos para este evento? S/N ")

            adicionarEvento(nome,vagas,usuarios,tipoVaga,data, liberarVeiculo)
            print("Evento cadastrado com sucesso!")
        elif opcao == 2:

            print(listarEventos())

        elif opcao == 3:
            executando = False
        else:
            print("opção invalida")

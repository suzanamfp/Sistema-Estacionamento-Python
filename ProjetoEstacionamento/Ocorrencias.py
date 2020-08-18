import datetime
ocorrencias = {}

def adicionarOcorrencia(codigo, tipoVaga, tipoOcorrencia, ocorrencia ):
    data = datetime.datetime.now()
    data = str(data)
    dataBR = data[8:10] + "/" + data[5:7] + "/" + data[0:4]

    if tipoVaga == "c":
        tipoVaga = "Carro"
    elif tipoVaga == "m":
        tipoVaga = "Moto"
    elif tipoVaga == "o":
        tipoVaga = "Onibus"
    elif tipoVaga == "r":
        tipoVaga = "Vagas reservadas"

    if tipoOcorrencia == "s":
        tipoOcorrencia = "Sinistro"
    elif tipoOcorrencia == "f":
        tipoOcorrencia = "Furto ou Assalto"
    elif tipoOcorrencia == "e":
        tipoOcorrencia = "Estacionamento Indevido"
    elif tipoOcorrencia == "i":
        tipoOcorrencia = "Inundação"
    elif tipoOcorrencia == "d":
        tipoOcorrencia = "Dano ao veiculo"
    elif tipoOcorrencia == "o":
        tipoOcorrencia = "Outros"

    ocorrencia = (codigo, tipoVaga, tipoOcorrencia, ocorrencia, dataBR )
    ocorrencias[codigo] = ocorrencia

def listarOcorrenciasporData(data, tipoVaga):
    listaOcorrencias = ocorrencias.values()
    saida =""
    for ocorrencia in listaOcorrencias:
        if data == ocorrencia[4] and tipoVaga == ocorrencia[1][0].lower():
            saida += "Codigo: " + ocorrencia[0] +" Tipo de ocorrencia: " + ocorrencia[2] +"\n"
    return saida

def main():

    executando = True
    while executando:

        print("1.Cadastrar ocorrencia ")
        print("2.Listar ocorrencias por data ")
        print("3.Voltar ao menu anterior ")

        opcao = int(input("> "))

        if opcao == 1:
            codigo = input("Informe um codigo para ocorrencia: ")
            tipoVaga = input("Informe o tipo de estacionamento \n(c) Carro \n(m) Moto \n(o) Onibus \n(r) Reservadas \n> ")
            if tipoVaga not in ("c","m","o","r"):
                print("Tipo de estacionamento invalido")
                executando = False
            tipoOcorrencia = input("Tipo de ocorrencia: \n(s) Sinistro \n(f) Furto ou Assalto \n(e) Estacionamento indevido \n(i) Inundação \n(d) Dano ao veiculo \n(o) Outros \n> ")
            if tipoOcorrencia not in ("s","f","e","i","d","o"):
                print("Tipo de ocorrencia invalida")
                executando = False
            ocorrencia = input("Informe a ocorrencia: ")
            adicionarOcorrencia(codigo,tipoVaga,tipoOcorrencia,ocorrencia)
        elif opcao == 2:
            data = input("Informe a data para pesquisa: ")
            tipoVaga = input("Informe o tipo de estacionamento \n(c) Carro \n(m) Moto \n(o) Onibus \n(r) Reservadas \n> ")
            print(listarOcorrenciasporData(data,tipoVaga))
        elif opcao == 3:
            executando = False
        else:
            print("opção invalida")
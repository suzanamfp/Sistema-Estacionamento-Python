import MonitoramentoVagas
import Ocorrencias
import Eventos
import BancoDeDados
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors


def relatorioFuncionarios():

    rel_funcionarios = []
    BancoDeDados.cur.execute("SELECT * FROM public.funcionario")
    rows = BancoDeDados.cur.fetchall()
    pdf = SimpleDocTemplate("Listagem de Funcionários.pdf")
    table = Table(rows)
    ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black)])
    table.setStyle(ts)
    rel_funcionarios.append(table)
    pdf.build(rel_funcionarios)

def relatorioVeiculos():

    rel_veiculos = []
    BancoDeDados.cur.execute("SELECT * FROM public.veiculo")
    rows = BancoDeDados.cur.fetchall()
    pdf = SimpleDocTemplate("Listagem de Veículos.pdf")
    table = Table(rows)
    ts = TableStyle([("GRID", (0, 0), (-1, -1), 2, colors.black)])
    table.setStyle(ts)
    rel_veiculos.append(table)
    pdf.build(rel_veiculos)

def checarLoginFuncEstacionamento(uf,sf):

    while True:
        uf = str(input("Digite seu usuário: "))
        while uf != 'estacionamento':
            uf = str(input("Digite seu usuário: "))
        if uf == 'estacionamento':
            sf = str(input("Digite sua senha: "))
            while sf != '123':
                sf = str(input("Digite sua senha: "))
            if sf == '123':
                return True
        else:
            return False

def checarLoginFuncRH(ur,sr):

    while True:
        ur = str(input("Digite seu usuário: "))
        while ur != 'rh':
            ur = str(input("Digite seu usuário: "))
        if ur == 'rh':
            sr = str(input("Digite sua senha: "))
            while sr != '456':
                sr = str(input("Digite sua senha: "))
            if sr == '456':
                return True
        else:
            return False

def checarLoginGestor(ug,sg):

    while True:
        ug = str(input("Digite seu usuário: "))
        while ug != 'gestor':
            ug = str(input("Digite seu usuário: "))
        if ug == 'gestor':
            sg = str(input("Digite sua senha: "))
            while sg != '789':
                sg = str(input("Digite sua senha: "))
            if sg == '789':
                return True
        else:
            return False

def cadastrarFuncionario(funcionario, vetorLinhaFuncionario):
    quantFuncionario = int(input("Quantos funcionários você quer cadastrar? "))
    if quantFuncionario !=0:
        i = 0
        while i< quantFuncionario:
            for linha in range(0, quantFuncionario):
                for coluna in range(0, quantFuncionario):
                    nome = input ("Digite o nome do funcionário: ")
                    matricula = input ("Digite a matrícula do funcionário: ")
                    senha = input("Digite sua senha: ")
                    vetorLinhaFuncionario.append(nome)
                    vetorLinhaFuncionario.append(matricula)
                    vetorLinhaFuncionario.append(senha)
                    BancoDeDados.cur.execute(BancoDeDados.queryCadFuncionario, vetorLinhaFuncionario)
                    BancoDeDados.con.commit()
                    i = i+1
                funcionario.append(vetorLinhaFuncionario)
        print(funcionario)
    else:
        return 0

def cadastrarVeiculo(veiculo, vetorLinhaVeiculo):
    quantVeiculo = int(input("Quantos veiculos deseja cadastrar? "))
    if quantVeiculo != 0:
        i = 0
        while i < quantVeiculo:
            for linha in range(0,quantVeiculo):
                for coluna in range(0,quantVeiculo):
                    nome = input("Digite o nome do aluno: ")
                    matricula = input("Digite a matricula do aluno: ")
                    curso = input("Digite o curso do aluno: ")
                    placa = input("Digite a placa do carro: ")
                    vaga = input("Vaga especial? (S/N) ")
                    vetorLinhaVeiculo.append(nome)
                    vetorLinhaVeiculo.append(matricula)
                    vetorLinhaVeiculo.append(curso)
                    vetorLinhaVeiculo.append(placa)
                    vetorLinhaVeiculo.append(vaga)
                    BancoDeDados.cur.execute(BancoDeDados.queryCadVeiculo, vetorLinhaVeiculo)
                    BancoDeDados.con.commit()
                    i = i + 1
                veiculo.append(vetorLinhaVeiculo)
        print(veiculo)
    else:
        return 0


#funcionalidades do funcionario do estacionamento
def funcEstacionamento(veiculo, vetorLinhaVeiculo, removerVeiculo, listarVeiculo):

    print("1. Cadastrar novos veiculos")
    print("2. Listar veículos")
    print("3. Remover veículos")
    print("4. Monitorar o estacionamento")
    print("5. Cadastrar ocorrencia no estacionamento")
    print("6. Cadastrar eventos no estacionamento ")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
        if cadastrarVeiculo(veiculo, vetorLinhaVeiculo, removerVeiculo) != 0:
            print("Veículo cadastrado com sucesso!")
    elif opcao == "2":
        MonitoramentoVagas.listarVeiculo()
    elif opcao == "3":
        if removerVeiculo(removerVeiculo) != 0:
            print("Veículo removido com sucesso!")
    elif opcao == "4":
        MonitoramentoVagas.main(False)
    elif opcao == "5":
        Ocorrencias.main()
    elif opcao == "6":
        Eventos.main()
    elif opcao == "0":
        print("sair!")
        return 0

#funcionalidades do funcionario do RH
def funcRH(funcionario, vetorLinhaFuncionario, permissaoAE):

    print("1. Cadastrar novos funcionários")
    print("2. Permitir acesso para área especial")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
        if cadastrarFuncionario(funcionario, vetorLinhaFuncionario) != 0:
            print("Funcionario cadastrado com sucesso!")
    elif opcao == "2":
        MonitoramentoVagas.mainRh()
    elif opcao == "0":
        print("sair!")
        return 0

#funcionalidades do gestor
def gestor(relatorio):

    print("1. Monitorar estacionamento")
    print("2. Visualizar relatório")
    print("3. Adicionar usuários com permissão")
    print("4. Gerenciar eventos no estacionamento")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
        MonitoramentoVagas.main(True)
    elif opcao == "2":
        print("1. Relatório de Veículos ")
        print("2. Relatório de Funcionários ")
        print("3. Sair")
        selecionar = input("_")
        if selecionar == "1":
            relatorioVeiculos()
        elif selecionar == "2":
            relatorioFuncionarios()
        elif selecionar == "3":
            print("sair!")
            return 0
    elif opcao == "3":
        MonitoramentoVagas.mainRh()
    elif opcao == "4":
        Eventos.main()

    elif opcao == "0":
        print("sair!")
        return 0

#funcao principal que ira chamar o menu principal e guardar todos os vetores
def main():

    veiculo = []
    vetorLinhaVeiculo = []
    removerVeiculo = []
    funcionario = []
    vetorLinhaFuncionario = []
    permissaoAE = []
    relatorio = []
    areaEspecial = []
    listarVeiculo = []

    uf = 'estacionamento'
    sf = '123'
    ur = 'rh'
    sr = '456'
    ug = 'gestor'
    sg = '789'

    while True:
        print("Bem-vindo ao Morais Parking! Por favor, identifique-se e faça seu login.")
        print("1. Funcionario do Estacionamento")
        print("2. Funcionario do RH")
        print("3. Gestor")
        print("0. Sair")

        opcao = input("_")
        if opcao == "1":
            if checarLoginFuncEstacionamento(uf, sf) != 0:
                print("Login realizado com sucesso!")
                if funcEstacionamento(veiculo, vetorLinhaVeiculo, removerVeiculo, listarVeiculo) != 0:
                    print()
                else:
                    break

        elif opcao == "2":
            if checarLoginFuncRH(ur, sr) != 0:
                print("Login realizado com sucesso!")
                if funcRH(funcionario, vetorLinhaFuncionario, permissaoAE) != 0:
                    print()
                else:
                    break

        elif opcao == "3":
            if checarLoginGestor(ug, sg) != 0:
                print("Login realizado com sucesso!")
                if gestor(relatorio) != 0:
                    print()
                else:
                    break

        elif opcao == "0":
            print("sair!")
            return 0

main()
import time

precoKwh = 1.86
potencia = 7
valorMin = 5


registroDeSessoes = []
sessaoAtual = None
contID = 1



def inicioSessao():
    global sessaoAtual, contID

    if sessaoAtual is not None:
        print('Já existe uma sessão em andamento!')
        return

    sessaoAtual = {
        'id': contID,
        'início': time.time(),
        'fim': None,
        'energia': 0,
        'status': 'ativa',
        'valor': 0
    }

    print(f'Sessão {contID} iniciada.')
    contID += 1

def fimSessao():
    global sessaoAtual

    if sessaoAtual is None:
        print('Não há sessão ativa!')
        return

    sessaoAtual['fim'] = time.time()

    tempoSeg = sessaoAtual['fim'] - sessaoAtual['início']
    tempoHrs = tempoSeg / 3600

    energia = potencia * tempoHrs
    sessaoAtual['energia'] = energia

    valor = calculoCobranca(energia, tempoHrs)
    sessaoAtual["valor"] = valor

    sessaoAtual['status'] = 'encerrada'

    registroDeSessoes.append(sessaoAtual.copy())

    print('\nSessão encerrada!')
    print(f'Tempo: {tempoHrs:.2f}h')
    print(f'Energia: {energia:.2f}kWh')
    print(f'Valor: R${valor:.2f}')

    sessaoAtual = None



def calculoCobranca(energia, tempo):
    valor = energia * precoKwh

    if valor < valorMin:
            valor = valorMin

    #Taxa se passar de 3 horas
    if tempo > 3:
        valor += 2

    return valor


def mostrarRegsitro():
    if not registroDeSessoes:
        print('Nenhuma sessão registrada!')
        return

    for s in registroDeSessoes:
        print('-' * 40)
        print(f'ID: {s["id"]}')
        print(f'Energia: {s["energia"]:.2f}kWh')
        print(f'Valor: R${s["valor"]:.2f}')
        print(f'Status: {s["status"]}')
        print('-' * 40)



def menuEscolha():
    while True:
        print('\n1 - Iniciar sessão')
        print('2 - Encerrar sessão')
        print('3 - Ver registro de sessões')
        print('4 - Sair')

        escolha = int(input('Escolha: '))

        if escolha == 1:
            inicioSessao()
        elif escolha == 2:
            fimSessao()
        elif escolha == 3:
            mostrarRegsitro()
        elif escolha == 4:
            break
        else:
            print('Opção inválida!')



menuEscolha()







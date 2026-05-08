Explicando a lógica do código:

Primeira linha ("import time") -> Este módulo é utilizado para capturar o tempo atual do sistema.
Ele é essencial para calcular a duração da sessão de recarga.

1º Bloco -> Declarando as variáveis fixas:
"precoKwh": preço por kWh consumido (R$ 1,86).
"potencia": potência do carregador (7 kW).
"valorMin": valor mínimo cobrado por sessão (R$ 5,00).

2º Bloco -> Declarando as variáveis simples e compostas: 
"registroDeSessoes": lista que armazena todas as sessões finalizadas.
"sessaoAtual": guarda a sessão em andamento.
"contID": contador automático de IDs para cada sessão.

3º Bloco -> Declara a função "inicioSessao()", que:
Verifica se já existe uma sessão ativa.
Se existir, impede iniciar outra.
Caso contrário:
Cria um dicionário com os dados da sessão.
Registra o horário de início.
Define status como "ativa".
Incrementa o ID.

4º Bloco -> Declarando a função "fimSessao()", que:
Verifica se existe uma sessão ativa.
Registra o horário de término.
Calcula o tempo da sessão:
segundos -> horas.
Calcula a energia consumida:
"energia = potencia × tempo".
Calcula o valor da cobrança (chama outra função).
Atualiza o status para "encerrada".
Salva a sessão no histórico.
Exibe os dados da sessão.

5º Bloco -> Declarando a função "calculoCobranca()", que:
Calcula o valor base:
"valor = energia * precoKwh"
Aplica valor mínimo:
"if valor < valorMin:
    valor = valorMin"
Aplica taxa extra:
Se a sessão durar mais de 3 horas → + R$2
Retorna o valor final.

6º Bloco -> Declarando a função "mostrarRegsitro()", que:
Verifica se existem sessões registradas.
Caso não exista, exibe mensagem.
Caso exista:
Percorre a lista de sessões.
Exibe:
ID
Energia consumida
Valor cobrado
Status

7º Bloco -> Declarando a função "mostrarRegsitro()", que:
Executa um loop infinito (while True).
Exibe opções para o usuário:
"Iniciar sessão
Encerrar sessão
Ver registros
Sair"
Captura a escolha do usuário.
Executa a função correspondente.

Última linha ("menuEscolha()") -> Executa a função "menuEscolha()", que consequentemente inicia o sistema, até o usuário escolher a opção "Sair".

Resumo geral:
Usuário inicia uma sessão.
O sistema registra o tempo.
Usuário encerra a sessão.
O sistema:
calcula duração
calcula energia
calcula valor
Os dados são armazenados para consulta futura.




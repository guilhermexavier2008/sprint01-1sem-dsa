Explicando a lógica do código:

Primeira linha ("import time") -> Este módulo é utilizado para capturar o tempo atual do sistema.
Ele é essencial para calcular a duração da sessão de recarga.

1º Bloco -> Declarando as variáveis fixas:
precoKwh: preço por kWh consumido (R$ 1,86)
potencia: potência do carregador (7 kW)
valorMin: valor mínimo cobrado por sessão (R$ 5,00)

2º Bloco -> Declarando as variáveis simples e compostas: 
registroDeSessoes: lista que armazena todas as sessões finalizadas
sessaoAtual: guarda a sessão em andamento
contID: contador automático de IDs para cada sessão

3º Bloco -> Declara a função inicioSessao(), que:
Verifica se já existe uma sessão ativa
Se existir, impede iniciar outra
Caso contrário:
Cria um dicionário com os dados da sessão
Registra o horário de início
Define status como "ativa"
Incrementa o ID

4º Bloco -> Declarando a função fimSessao(), que:
Verifica se existe uma sessão ativa
Registra o horário de término
Calcula o tempo da sessão:
segundos -> horas
Calcula a energia consumida:
energia = potencia × tempo
Calcula o valor da cobrança (chama outra função)
Atualiza o status para "encerrada"
Salva a sessão no histórico
Exibe os dados da sessão

5º Bloco -> 

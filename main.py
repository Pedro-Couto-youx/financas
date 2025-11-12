from datetime import datetime
from utils import value, date, category, account, tipoTransaction, payment, tags, listing
import pandas as pd
menu =''
transacao = None
transacoes = pd.DataFrame()

while menu != 0: #Nas opções, futuramente fazer um menu opcional organizado caso seja necessário
    menu = (int(input("""                                 ===  DurelliLedger ===
                        1- Adicionar transação
                        2- Listar transações
                        3- Editar transações
                        4- Excluir transação
                        5- Relatórios
                        0- Sair""")))
    if menu == 1:
        data= date()
        tipo = tipoTransaction()
        descricao = str(input('Insira uma descrição para esta transação:  [Opcional]'))
        categoria = category(tipo)
        conta = account()
        valor = value()
        formaPagamento = payment()
        tag = tags(tipo, categoria)
        criadoEm = datetime.today()

        transacao = {
                'DATA': data,
                'TIPO' : tipo,
                'DESCRICAO' : descricao,
                'CATEGORIA' : categoria,
                'CONTA' : conta,
                'VALOR' : valor,
                'FORMA DE PAGAMENTO' : formaPagamento,
                'TAG' : tag,
                'CRIADO EM' : criadoEm
        }
        dadosNovos= pd.DataFrame(transacao)
        transacoes= pd.concat([transacoes, dadosNovos])
        coluna_nome = 'data'
        transacoes.iloc[2][coluna_nome] = valor-novo


    if menu == 2:
        listing(transacao)
    
    if menu == 3:

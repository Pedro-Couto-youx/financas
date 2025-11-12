from datetime import datetime
from utils import value, date, category, account, tipoTransaction, payment, tags
menu =''



while menu != 0:
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
        tag = tags(categoria, tipo)
        criadoEm = datetime.today()
    if menu == 2:
        list(EXTRATO)
    
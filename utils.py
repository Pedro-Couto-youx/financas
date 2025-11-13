import datetime
import pandas as pd
from unidecode import unidecode

def removerAcento(a):
    semacento= unidecode(a)
    print(semacento)
    return semacento

def value():
    while True:
        try:
            valorTransacao = float(input('Digite o valor da transação: [Valores nulos não são aceitos]'))

            if valorTransacao<=0:
                 print(f'Caro usuário, números neutros são inválidos! Por favor insira um valor maior que zero!')
            else:
                print('Valor registrado com sucesso')
                return valorTransacao
        except ValueError:
            print('Entrada inválida, por favor digite um numero válido')
    




def date():
    while True:
        try:
            data = input('Em que data foi feita a transação? ')
            dataCorreta = datetime.datetime.strptime(data, "%d/%m/%Y")
            print('Data registrada com sucesso')
            return dataCorreta
        except ValueError:
            print(f'Caro usuário, sua data não é válida, por favor insira uma data válida')

def tipoTransaction():
    tipoTransacao = str(input('Qual o tipo da transação? [Receita| Despesa]').upper()).strip()
    tipoTransacaoCorrigida = removerAcento(tipoTransacao)
    while tipoTransacaoCorrigida != 'RECEITA' and tipoTransacaoCorrigida != 'DESPESA':
        print('Caro usuário, por favor insira um tipo válido! ')
        tipoTransacao = str(input('Qual o tipo da transação? [Receita| Despesa]').upper())
        tipoTransacaoCorrigida = removerAcento(tipoTransacao)
    return tipoTransacaoCorrigida

def list(e):
    print(e)

#FUTURAMENTE PODERIAMOS ADICIONAR NOVAS CATEGORIAS, COMO RECEITAS E DESPESAS EMPRESARIAIS, TRANSFERÊNCIA ENTRE CONTAS ETC...
def category(tipoTransacaoCorrigida):
    if tipoTransacaoCorrigida == 'RECEITA':
        categoriasReceitas= ['SALARIO', 'VENDAS DE PRODUTOS', 'PRESTACAO DE SERVICOS', 'INVESTIMENTOS', 'REEMBOLSOS', 'OUTRAS RECEITAS']
        categoriaTransacao = str(input('Insira a categoria da transação: SALÁRIO, VENDAS DE PRODUTOS, PRESTACAO DE SERVICOS, INVESTIMENTOS, REEMBOLSOS, OUTRAS RECEITAS').upper())
        categoriaTransacaoCorrigida = removerAcento(categoriaTransacao)
        if categoriaTransacaoCorrigida not in categoriasReceitas:
            print('Caro usuário, por favor insira uma categoria de receitas válidas [SALÁRIO, VENDAS DE PRODUTOS, PRESTACAO DE SERVICOS, INVESTIMENTOS, REEMBOLSOS, OUTRAS RECEITAS]')
            categoriaTransacao = str(input('Insira a categoria da transação: SALÁRIO, VENDAS DE PRODUTOS, PRESTACAO DE SERVICOS, INVESTIMENTOS, REEMBOLSOS, OUTRAS RECEITAS').upper())
    if tipoTransacaoCorrigida == 'DESPESA':
        categoriasDespesas = ['ALIMENTAÇÃO', 'MORADIA', 'TRANSPORTE', 'SAÚDE', 'EDUCAÇÃO', 'LAZER', 'ROUPAS', 'HIGIENE PESSOAL', 'CONTAS', 'IMPOSTOS', 'DOAÇÕES']
        categoriaTransacao = str(input('Insira a categoria da transação: [ALIMENTAÇÃO, MORADIA, SAUDE, EDUCAÇÃO LAZER, ROUPAS, HIGIENE PESSOAL, CONTAS, IMPOSTOS, DOACOES]').upper())
        categoriaTransacaoCorrigida = removerAcento(categoriaTransacao)
        if categoriaTransacaoCorrigida not in categoriasDespesas:
                print('Caro usuário, por favor insira uma categoria de despesas válidas [ALIMENTAÇÃO, MORADIA, TRANSPORTE, SAÚDE, EDUCAÇÃO, LAZER, ROUPAS, HIGIENE PESSOAL, CONTAS, IMPOSTOS, DOACOES]')
                categoriaTransacao = str(input('Insira a categoria da transação: [ALIMENTAÇÃO, MORADIA, SAUDE, EDUCAÇÃO LAZER, ROUPAS, HIGIENE PESSOAL, CONTAS, IMPOSTOS, DOACOES]').upper())
                categoriaTransacaoCorrigida = removerAcento(categoriaTransacao)
    return categoriaTransacaoCorrigida

def account(): #FUTURAMENTE ADAPTAR PARA CONTAS EMPRESARIAIS
    tiposContas = ['CONTA CORRENTE', 'CONTA POUPANÇA', 'DINHEIRO VIVO', 'CARTÃO DE CRÉDITO', 'INVESTIMENTOS', 'CARTEIRA DIGITAL', 'OUTROS']
    contaTransacao = str(input('Digite o tipo de sua conta bancária: [CONTA CORRENTE, CONTA POUPANÇA, DINHEIRO VIVO, CARTÃO DE CŔEDITO, INVESTIMENTOS, CARTEIRA DIGITAL, OUTROS]').upper())
    if contaTransacao not in tiposContas:
        print('Caro usuário, por favor insira um tipo de conta válido: [CONTA CORRENTE, CONTA POUPANÇA, DINHEIRO VIVO, CARTÃO DE CŔEDITO, INVESTIMENTOS, CARTEIRA DIGITAL, OUTROS]')
        contaTransacao = str(input('Digite o tipo de sua conta bancária: [CONTA CORRENTE, CONTA POUPANÇA, DINHEIRO VIVO, CARTÃO DE CŔEDITO, INVESTIMENTOS, CARTEIRA DIGITAL, OUTROS]').upper())
    else: 
        print('Tipo de conta bancária registrado com sucesso!')
    return contaTransacao

def payment():
    tiposPagamentos = ['DINHEIRO', 'CARTAO DE DÉBITO', 'CARTÃO DE CRÉDITO', 'PIX', 'TRANSFERÊNCIA', 'TED', 'DOC', 'CHEQUE', 'PAYPAL', 'PICPAY', 'MERCADO PAGO', 'GOOGLE PAY', 'APPLE PAY', 'CRYPTO']
    formaPagamento = str(input('Insira a forma de pagamento da transação: [DINHEIRO, CARTAO DE DÉBITO, CARTÃO DE CRÉDITO, PIX, TRANSFERÊNCIA, TED, DOC, CHEQUE, PAYPAL, PICPAY, MERCADO PAGO, GOOGLE PAY, APPLE PAY, CRYPTO]').upper())
    if formaPagamento not in tiposPagamentos:
        print('Caro usuário, por favor insira uma forma de pagamento válida!')
        formaPagamento = str(input('Insira a forma de pagamento da transação: [DINHEIRO, CARTAO DE DÉBITO, CARTÃO DE CRÉDITO, PIX, TRANSFERÊNCIA, TED, DOC, CHEQUE, PAYPAL, PICPAY, MERCADO PAGO, GOOGLE PAY, APPLE PAY, CRYPTO]').upper())
    return formaPagamento

def tags(tipoTransacao, categoriaTransacao): #FUTURAMENTE DIVIDIR AS TAGS ENTRE TIPOS DE PESSOAS EX: ADULTOS, CRIANÇAS, ADOLESCENTES
    if tipoTransacao == 'DESPESA':
        if categoriaTransacao == 'ALIMENTAÇÃO':
            alimentacao = ['SUPERMERCADO', 'COMPRA MENSAL', 'PROMOÇÃO']
            tag= str(input('Adicione uma tag para esta transação: [SUPERMERCADO, COMPRA MENSAL, PROMOCAO]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in alimentacao:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [SUPERMERCADO, COMPRA MENSAL, PROMOÇÃO]'))
                tagCorrigida= removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'MORADIA':
            moradia = ['ALUGUEL', 'CONDOMINIO', 'IPTU', 'SEGURO RESIDENCIAL', 'FINANCIAMENTO', 'PRESTACAO DA CASA']
            tag= str(input('Adicione uma tag para esta transação: [ALUGUEL, CONDOMINIO, IPTU, SEGURO RESIDENCIAL, FINANCIAMENTO, PRESTACAO DA CASA]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in moradia:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag= str(input('Adicione uma tag para esta transação: [ALUGUEL, CONDOMINIO, IPTU, SEGURO RESIDENCIAL, FINANCIAMENTO, PRESTACAO DA CASA]').upper())
                tagCorrigida = removerAcento(tag)
                return print('Tag adicionada com sucesso!')
            


        if categoriaTransacao == 'TRANSPORTE':
            transporte = ['COMBUSTIVEL', 'ESTACIONAMENTO', 'PEDAGIO', 'SEGURO VEICULAR', 'IPVA', 'LICENCIAMENTO', 'FINANCIAMENTO DO CARRO']
            tag= str(input('Adicione uma tag para esta transação: [COMBUSTIVEL, ESTACIONAMENTO, PEDAGIO, SEGURO VEICULAR, IPVA, LICENCIAMENTO, FINANCIAMENTO DO CARRO]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in transporte:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag= str(input('Adicione uma tag para esta transação: [COMBUSTIVEL, ESTACIONAMENTO, PEDAGIO, SEGURO VEICULAR, IPVA, LICENCIAMENTO, FINANCIAMENTO DO CARRO]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'SAÚDE':
            saude = ['CONSULTA MEDICA', 'EXAMES LABORATORIAIS', 'MEDICAMENTOS', 'HOSPITALIZACAO', 'CIRURGIA', 'ANESTESIA', 'EMERGENCIA', 'MATERIAIS HOSPITALARES', 'DENTISTA', 'LIMPEZA DENTARIA', 'ORTODONTIA', 'PROTESE DENTARIA', 'CIRURGIA BUCAL', 'OCULOS', 'LENTES DE CONTATO', 'CONSULTA OFTAMOLOGISTA', 'EXAME DE VISAO', 'APARELHO AUDITIVO', 'TERAPIA', 'PSICOLOGO', 'NUTRICIONISTA', 'ACADEMIA', 'PILATES', 'FISIOTERAPIA', 'MASSAGEM', 'CHECKUP ANUAL', 'PLANO DE SAUDE', 'PLANO ODONTO', 'SEGURO SAUDE', 'COPARTICIPACAO', 'VACINAS']
            tag= str(input('Adicione uma tag para esta transação: [CONSULTA MEDICA, EXAMES LABORATORIAIS, MEDICAMENTOS, HOSPITALIZACAO, CIRURGIA, ANESTESIA, EMERGENCIA, MATERIAIS HOSPITALARES, DENTISTA, LIMPEZA DENTARIA, ORTODONTIA, PROTESE DENTARIA, CIRURGIA BUCAL, OCULOS, LENTES DE CONTATO, CONSULTA OFTAMOLOGISTA, EXAME DE VISAO, APARELHO AUDITIVO, TERAPIA, PSICOLOGO, NUTRICIONISTA, ACADEMIA, PILATES, FISIOTERAPIA, MASSAGEM, CHECKUP ANUAL, PLANO DE SAUDE, PLANO ODONTO, SEGURO SAUDE, COPARTICIPACAO, VACINAS]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in saude:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag= str(input('Adicione uma tag para esta transação: [CONSULTA MEDICA, EXAMES LABORATORIAIS, MEDICAMENTOS, HOSPITALIZACAO, CIRURGIA, ANESTESIA, EMERGENCIA, MATERIAIS HOSPITALARES, DENTISTA, LIMPEZA DENTARIA, ORTODONTIA, PROTESE DENTARIA, CIRURGIA BUCAL, OCULOS, LENTES DE CONTATO, CONSULTA OFTAMOLOGISTA, EXAME DE VISAO, APARELHO AUDITIVO, TERAPIA, PSICOLOGO, NUTRICIONISTA, ACADEMIA, PILATES, FISIOTERAPIA, MASSAGEM, CHECKUP ANUAL, PLANO DE SAUDE, PLANO ODONTO, SEGURO SAUDE, COPARTICIPACAO, VACINAS]').upper())
                tagCorrigida= removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'EDUCAÇÃO':
            educacao = ['MENSALIDADE ESCOLAR', 'MENSALIDADE FACULDADE', 'CURSO TÉCNICO', 'MATERIAL DIDATICO', 'UNIFORME', 'TRANSPORTE ESCOLAR', 'ALIMENTACAO ESCOLAR', 'TAXA DE MATRICULA', 'TAXA DE RECUPERAÇÃO', 'AULAS DE REFORÇO', 'CURSOS ONLINE', 'CURSOS PROFISSIONALIZANTES', 'CERTIFICACAO', 'INSCRICAO EM EVENTOS', 'MATERIAL DO CURSO', 'PLATAFORMA DE ASSINATURA', 'LIVROS', 'REVISTAS ACADEMICAS', 'EBOOKS', 'CRECHE', 'ATIVIDADE EXTRACURRICULAR', 'PASSEIO ESCOLAR', 'PALESTRAS', 'MENTORIA', 'COACHING']
            tag = str(input('Adicione uma tag para esta transação: [MENSALIDADE ESCOLAR, MENSALIDADE FACULDADE, CURSO TÉCNICO, MATERIAL DIDATICO, UNIFORME, TRANSPORTE ESCOLAR, ALIMENTACAO ESCOLAR, TAXA DE MATRICULA, TAXA DE RECUPERAÇÃO, AULAS DE REFORÇO, CURSOS ONLINE, CURSOS PROFISSIONALIZANTES, CERTIFICACAO, INSCRICAO EM EVENTOS, MATERIA DO CURSO, PLATAFORMA DE ASSINATURA, LIVROS, REVISTAS ACADEMICAS, EBOOKS, CRECHE, ATIVIDADE EXTRACURRICULAR, PASSEIO ESCOLAR, PALESTRAS, MENTORIA, COACHING ').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in educacao:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [MENSALIDADE ESCOLAR, MENSALIDADE FACULDADE, CURSO TÉCNICO, MATERIAL DIDATICO, UNIFORME, TRANSPORTE ESCOLAR, ALIMENTACAO ESCOLAR, TAXA DE MATRICULA, TAXA DE RECUPERAÇÃO, AULAS DE REFORÇO, CURSOS ONLINE, CURSOS PROFISSIONALIZANTES, CERTIFICACAO, INSCRICAO EM EVENTOS, MATERIA DO CURSO, PLATAFORMA DE ASSINATURA, LIVROS, REVISTAS ACADEMICAS, EBOOKS, CRECHE, ATIVIDADE EXTRACURRICULAR, PASSEIO ESCOLAR, PALESTRAS, MENTORIA, COACHING ').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'LAZER':
            lazer = ['CINEMA', 'TEATRO', 'SHOWS', 'EVENTOS', 'MUSEUS', 'PARQUE', 'STREAMING', 'GAMES', 'RESTAURANTE', 'BAR', 'CAFETERIA', 'DELIVERY', 'CHURRASCO', 'FESTAS', 'VIAGEM', 'AIRBNB', 'FOTOGRAFIAS', 'JARDINAGEM', 'ANIMAIS DE ESTIMACAO', 'CLUBE', 'ACADEMIA']
            tag = str(input('Adicione uma tag para esta transação: [CINEMA, TEATRO, SHOWS, EVENTOS, MUSEUS, PARQUE, STREAMING, GAMES, RESTAURANTE, BAR, CAFETERIA, DELIVERY, CHURRASCO, FESTAS, VIAGEM, AIRBNB, FOTOGRAFIAS, JARDINAGEM, ANIMAIS DE ESTIMACAO, CLUBE, ACADEMIA]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in lazer:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [CINEMA, TEATRO, SHOWS, EVENTOS, MUSEUS, PARQUE, STREAMING, GAMES, RESTAURANTE, BAR, CAFETERIA, DELIVERY, CHURRASCO, FESTAS, VIAGEM, AIRBNB, FOTOGRAFIAS, JARDINAGEM, ANIMAIS DE ESTIMACAO, CLUBE, ACADEMIA]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida
            

        if categoriaTransacao == 'ROUPAS':
            roupas = ['ROUPAS CASUAL', 'ROUPAS DE TRABALHO', 'ROUPAS ESPORTIVAS', 'ROUPAS DE FESTA', 'ROUPAS INFANTIS', 'ROUPAS DE INVERNO', 'CALCADOS', 'BOLSAS', 'CINTOS', 'RELOGIOS', 'JOIAS', 'BONES', 'OCULOS', 'LUVAS', 'LAVANDERIA', 'COSTURA', 'TINTURARIA', 'LIMPEZA DE CALCADOS']
            tag = str(input('Adicione uma tag para esta transação: [ROUPAS CASUAL, ROUPAS DE TRABALHO, ROUPAS ESPORTIVAS, ROUPAS DE FESTA, ROUPAS INFANTIS, ROUPAS DE INVERNO, CALCADOS, BOLSAS, CINTOS, RELOGIOS, JOIAS, BONES, OCULOS, LUVAS, LAVANDERIA, COSTURA, TINTURARIA, LIMPEZA DE CALCADOS').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in roupas:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [ROUPAS CASUAL, ROUPAS DE TRABALHO, ROUPAS ESPORTIVAS, ROUPAS DE FESTA, ROUPAS INFANTIS, ROUPAS DE INVERNO, CALCADOS, BOLSAS, CINTOS, RELOGIOS, JOIAS, BONES, OCULOS, LUVAS, LAVANDERIA, COSTURA, TINTURARIA, LIMPEZA DE CALCADOS').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'HIGIENE PESSOAL':
            higiene = ['SABONETE', 'SHAMPOO', 'CONDICIONADOR', 'DESODORANTE', 'CREME DENTAL', 'FIO DENTAL', 'ESCOVA DE DENTE', 'PAPEL HIGIENICO', 'ABSORVENTES', 'LENCOS UMIDOS', 'CREMES', 'CORTE DE CABELO', 'BARBEIRO', 'MANICURE', 'PEDICURE', 'DEPILACAO', 'PRODUTOS PARA SKINCARE', 'MAQUIAGEM', 'PERFUME', 'COSMETICOS', 'SPA', 'TOALHAS', 'ROUPAS DE BANHO', 'ESCOVA DE CABELO', 'LAMINAS DE BARBEAR', 'ITENS DE BANHEIRO']
            tag = str(input('Adicione uma tag para esta transação: [SABONETE, SHAMPOO, CONDICIONADOR, DESODORANTE, CREME DENTAL, FIO DENTAL, ESCOVA DE DENTE, PAPEL HIGIENICO, ABSORVENTES, LENCOS UMIDOS, CREMES, CORTE DE CABELO, BARBEIRO. MANICURE, PEDICURE, DEPILACAO, PRODUTOS PARA SKINCARE, MAQUIAGEM, PERFUME, COSMETICOS, SPA, TOALHAS, ROUPAS DE BANHO, ESCOVA DE CABELO, LAMINA DE BARBEAR, ITENS DE BANHEIRO]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in higiene:
                print('Caro usuario, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [SABONETE, SHAMPOO, CONDICIONADOR, DESODORANTE, CREME DENTAL, FIO DENTAL, ESCOVA DE DENTE, PAPEL HIGIENICO, ABSORVENTES, LENCOS UMIDOS, CREMES, CORTE DE CABELO, BARBEIRO. MANICURE, PEDICURE, DEPILACAO, PRODUTOS PARA SKINCARE, MAQUIAGEM, PERFUME, COSMETICOS, SPA, TOALHAS, ROUPAS DE BANHO, ESCOVA DE CABELO, LAMINA DE BARBEAR, ITENS DE BANHEIRO]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'CONTAS':
            contas = ['ENERGIA', 'AGUA', 'GAS', 'INTERNET', 'CELULAR', 'ESGOTO', 'LIXO', 'ANUIDADE', 'JUROS', 'MULTAS', 'EMPRESTIMO', 'FINANCIAMENTO', 'SEGURO', 'LIMPEZA', 'SEGURANCA RESIDENCIAL']
            tag = str(input('Adicione uma tag para esta transação: [ENERGIA, AGUA, GAS, INTERNET, CELULAR, ESGOTO, LIXO, ANUIDADE, JUROS, MULTAS, EMPRESTIMO, FINANCIAMENTO, SEGURO, LIMPEZA, SEGURANCA RESIDENCIAL]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in contas:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [ENERGIA, AGUA, GAS, INTERNET, CELULAR, ESGOTO, LIXO, ANUIDADE, JUROS, MULTAS, EMPRESTIMO, FINANCIAMENTO, SEGURO, LIMPEZA, SEGURANCA RESIDENCIAL').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida
                
        if categoriaTransacao == 'IMPOSTOS':
            impostos = ['ITR', 'IMPOSTO DE RENDA', 'INSS', 'CONTRIBUICAO SINDICAL', 'TAXA AUTONOMO', 'RETENCAO FONTE', 'MEI', 'ICMS', 'ISS', 'IPI', 'IOF', 'TARIFAS FISCAIS']
            tag = str(input('Adicione uma tag para esta transação: [ITR, IMPOSTO DE RENDA, INSS, CONTRIBUICAO SINDICAL, TAXA AUTONOMO, RETENCAO FONTE, MEI, ICMS, ISS IPI, IOF, TARIFAS FISCAIS]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in impostos:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [ITR, IMPOSTO DE RENDA, INSS, CONTRIBUICAO SINDICAL, TAXA AUTONOMO, RETENCAO FONTE, MEI, ICMS, ISS IPI, IOF, TARIFAS FISCAIS]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'DOACOES':
            doacoes = ['AJUDA PARA FAMILIA', 'AJUDA PRA AMIGOS', 'PRESENTEAMENTOS', 'SOCORRO EMERGENCIAL', 'IGREJA', 'INSTITUICAO DE CARIDADE', 'PROJETO SOCIAL', 'ORFANATO', 'INSTITUICAO DE ANIMAIS', 'INSITITUICAO DE SAUDE', 'MEIO AMBIENTE', 'EDUCACAO']
            tag = str(input('Adicione uma tag para esta transação: [AJUDA PARA FAMILIA, AJUDA PARA AMIGOS, PRESENTEAMENTOS, SOCORRO EMERGENCIAL, IGREJA, INSTITUICAO DE CARIDADE, PROJETO SOCIAL, ORFANATO, INSTITUICAO DE ANIMAIS, INSTITUICAO DE SAUDE, MEIO AMBIENTE, EDUCACAO]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in doacoes:
                print('Caro usuário, por favor digite uma tag válida para esta categoria')
                tag = str(input('Adicione uma tag para esta transação: [AJUDA PARA FAMILIA, AJUDA PARA AMIGOS, PRESENTEAMENTOS, SOCORRO EMERGENCIAL, IGREJA, INSTITUICAO DE CARIDADE, PROJETO SOCIAL, ORFANATO, INSTITUICAO DE ANIMAIS, INSTITUICAO DE SAUDE, MEIO AMBIENTE, EDUCACAO]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida

    if tipoTransacao == 'RECEITA':
        categoriaTransacao = category(tipoTransacao)
        if categoriaTransacao == 'SALARIO':
            salario = ['EMPRESA', 'TRABALHO']
            tag = str(input('Digite uma tag para esta transação: [EMPRESA, TRABALHO]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in salario:
                print('Caro usuário, por favor insira uma tag válida para esta categoria')
                tag = str(input('Digite uma tag para esta transação: [EMPRESA, TRABALHO]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida

        if categoriaTransacao == 'VENDA DE PRODUTOS':
            venda= ['ALIMENTOS', 'ROUPAS', 'ARTESANATO', 'ELETRONICOS', 'COSMETICOS', 'ACESSORIOS', 'DIGITAL']
            tag = str(input('Digite uma tag para esta transação: [ALIMENTOS, ROUPAS, ARTESANATO , ELETRONICOS ,COSMETICOS , ACESSORIOS, DIGITAL]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in venda:
                print('Caro usuário, por favor insira uma tag válida para esta categoria')
                tag = str(input('Digite uma tag para esta transação: [ALIMENTOS, ROUPAS, ARTESANATO , ELETRONICOS ,COSMETICOS , ACESSORIOS, DIGITAL]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida

        if categoriaTransacao == 'PRESTACAO DE SERVICOS':
            prestacao = ['CONSULTORIA', 'DESIGN', 'MANUTENÇÃO', 'AULAS', 'BELEZA', 'TRANSPORTE', 'FREELANCER', 'SUPORTE', 'ENTREGA']
            tag = str(input('Digite uma tag para esta transação: [CONSULTORIA, DESIGN, MANUTENÇÃO, AULAS, BELEZA, TRANSPORTE, FREELANCER, SUPORTE, ENTREGA]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in prestacao:
                print('Caro usuário, por favor insira uma tag válida para esta categoria')
                tag = str(input('Digite uma tag para esta transação: [CONSULTORIA, DESIGN, MANUTENÇÃO, AULAS, BELEZA, TRANSPORTE, FREELANCER, SUPORTE, ENTREGA]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida
                

        if categoriaTransacao == 'INVESTIMENTOS':
            investimentos = ['RENDA FIXA', 'RENDA VARIAVEL', 'TESOURO DIRETO', 'ACOES', 'FUNDOS IMOBILIARIOS', 'CRIPTO', 'CDB', 'POUPANCA', 'ETFs']
            tag = str(input('Digite uma tag para esta transação: [RENDA FIXA, RENDA VARIAVEL, TESOURO DIRETO, ACOES, FUNDOS IMOBILIARIOS, CRIPTO, CDB, POUPANCA, ETFs]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in investimentos:
                print('Caro usuário, por favor insira uma tag válida para esta categoria')
                tag = str(input('Digite uma tag para esta transação: [RENDA FIXA, RENDA VARIAVEL, TESOURO DIRETO, ACOES, FUNDOS IMOBILIARIOS, CRIPTO, CDB, POUPANCA, ETFs]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida


        if categoriaTransacao == 'REEMBOLSOS':
            reembolsos = ['EMPRESA', 'PLANO DE SAUDE', 'CLIENTE', 'AMIGO', 'GOVERNO', 'LOJA', 'BANCARIO']
            tag = str(input('Digite uma tag para esta transação: [EMPRESA, PLANO DE SAUDE, CLIENTE, AMIGO, GOVERNO, LOJA, BANCARIO]').upper())
            tagCorrigida = removerAcento(tag)
            if tagCorrigida not in reembolsos:
                print('Caro usuário, por favor insira uma tag válida para esta categoria')
                tag = str(input('Digite uma tag para esta transação: [EMPRESA, PLANO DE SAUDE, CLIENTE, AMIGO, GOVERNO, LOJA, BANCARIO]').upper())
                tagCorrigida = removerAcento(tag)
                return tagCorrigida
            
def listing(transacao):
    if transacao == None:
        print('Por favor, insira uma transação válida antes de listar')
    else:
        print(transacao)


def update(dataframe):
    while True:
        if dataframe.empty:
            print('Caro usuário, por favor adicione uma transação primeiro')
            break

        indice = int(input('Digite o id de sua transação: '))
        while indice < 0 or indice > (dataframe.shape[0] - 1):
            print('Digite um id válido')
            indice = int(input('Digite o id de sua transação: '))

        colunas = ['DATA', 'TIPO', 'DESCRICAO', 'CATEGORIA', 'CONTA', 'VALOR', 'FORMA DE PAGAMENTO', 'TAG', 'CRIADO EM']
        coluna = str(input('Digite qual coluna você deseja editar: [DATA, TIPO, DESCRICAO, CATEGORIA, CONTA, VALOR, FORMA DE PAGAMENTO, TAG, CRIADO EM]').upper())
        colunaCorrigida = removerAcento(coluna)

        if colunaCorrigida not in colunas:
            print('Caro usuário, por favor digite uma coluna presente na tabela')
            indice = int(input('Digite o id de sua transação: '))
            coluna = str(input('Digite qual coluna você deseja editar: [DATA, TIPO, DESCRICAO, CATEGORIA, CONTA, VALOR, FORMA DE PAGAMENTO, TAG, CRIADO EM]').upper())
            colunaCorrigida = removerAcento(coluna)

        if colunaCorrigida == 'DATA':
            while True:
                try:
                    data = input('Qual data você deseja atribuir à transação? [XX/XX/XXXX] ')
                    data = datetime.datetime.strptime(data, "%d/%m/%Y")
                    print('Data alterada com sucesso')
                    dataframe.loc[indice,coluna] = data
                    print('Edição concluída')
                    print(dataframe.iloc[indice])
                except ValueError:
                    print(f'Caro usuário, sua data não é válida, por favor insira uma data válida')

        if colunaCorrigida == 'TIPO':
            tipoLista = ['RECEITA', 'DESPESA']
            tipo = str(input('Qual tipo você deseja atribuir à transação? [RECEITA|DESPESA]').upper())
            tipoCorrigido = removerAcento(tipo)
            if tipoCorrigido not in tipoLista:
                print('Caro usuário, por favor insira um tipo válido!')
                tipo = str(input('Qual tipo você deseja atribuir à transação? [RECEITA|DESPESA]').upper())
                tipoCorrigido = removerAcento(tipo)
            dataframe.iloc[indice][coluna] = tipoCorrigido
            print('Tipo alterado com sucesso')
            print(dataframe.iloc[indice])

        if colunaCorrigida == 'DESCRICAO':
            descricao = str(input('Qual descrição você deseja atribuir à transação? '))
            dataframe.iloc[indice][coluna] = descricao
            print('Descrição alterada com sucesso')
            print(dataframe.iloc[indice])
        
        if colunaCorrigida == 'CATEGORIA':
            tiposCategoria = ['RECEITA', 'DESPESA']
            categoriasReceitas = ['SALÁRIO', 'VENDAS DE PRODUTOS', 'PRESTACAO DE SERVICOS', 'INVESTIMENTOS', 'REEMBOLSOS', 'OUTRAS RECEITAS']
            categoriasDespesas = ['ALIMENTAÇÃO', 'MORADIA', 'TRANSPORTE', 'SAÚDE', 'EDUCAÇÃO', 'LAZER', 'ROUPAS', 'HIGIENE PESSOAL', 'CONTAS', 'IMPOSTOS', 'DOAÇÕES']
            tipo = str(input('Qual o tipo da categoria? [RECEITA|DESPESA]').upper)
            tiposCategoriaCorrigido= removerAcento(tipo)

            if tiposCategoriaCorrigido not in tiposCategoria:
                print('Caro usuário, digite um tipo de categoria válido!')
                tipo = str(input('Qual o tipo da categoria? [RECEITA|DESPESA]'))
                tiposCategoriaCorrigido = removerAcento(tipo)

            if tiposCategoriaCorrigido == 'RECEITA':
                categoria = str(input('Qual categoria você deseja atribuir à transação: [SALARIO, VENDAS DE PRODUTOS, PRESTACAO DE SERVICOS, INVESTIMENTOS, REEMBOLSOS, OUTRAS RECEITAS]').upper())
                categoriaCorrigida = removerAcento(categoria)
                if categoriaCorrigida not in categoriasReceitas:
                    print('Caro usuário, por favor insira uma categoria válida para o tipo receitas')
                    categoria = str(input('Qual categoria você deseja atribuir à transação: [SALARIO, VENDAS DE PRODUTOS, PRESTACAO DE SERVICOS, INVESTIMENTOS, REEMBOLSOS, OUTRAS RECEITAS]').upper())
                    categoriaCorrigida = removerAcento(categoria)

            if tiposCategoriaCorrigido == 'DESPESA':
                categoria = str(input('Qual categoria você deseja atribuir  à transação: [ALIMENTACAO, MORADIA, TRANSPORTE, SAUDE, EDUCACAO, LAZER, ROUPAS, HIGIENE PESSOAL, CONTAS, IMPOSTOS, DOACOES]').upper())
                categoria= removerAcento(categoria)
                if categoriaCorrigida not in categoriasDespesas:
                    print('Caro usuário, por favor insira uma categoria válida para o tipo despesas')
                    categoria = str(input('Qual categoria você deseja atribuir  à transação: [ALIMENTACAO, MORADIA, TRANSPORTE, SAUDE, EDUCACAO, LAZER, ROUPAS, HIGIENE PESSOAL, CONTAS, IMPOSTOS, DOACOES]').upper())
                    categoriaCorrigida = removerAcento(categoria)
            dataframe.iloc[indice][coluna] = categoriaCorrigida
            print('Categoria alterada com sucesso')
            print(dataframe.iloc[indice])

        if colunaCorrigida == 'CONTA':
            contas = ['CONTA CORRENTE', 'CONTA POUPANÇA', 'DINHEIRO VIVO', 'CARTAO DE CREDITO', 'INVESTIMENTOS', 'CARTEIRA DIGITAL', 'OUTROS']
            conta = str(input('Qual tipo de conta você deseja atribuir à esta transação: [CONTA CORRENTE, CONTA POUPANÇA, DINHEIRO VIVO, CARTAO DE CREDITO, INVESTIMENTOS, CARTEIRA DIGITAL, OUTROS]').upper())
            contaCorrigida = removerAcento(conta)
            if contaCorrigida not in contas:
                print('Caro usuário, por favor insira um tipo de conta válido! ')
                conta = str(input('Qual tipo de conta você deseja atribuir à esta transação: [CONTA CORRENTE, CONTA POUPANÇA, DINHEIRO VIVO, CARTAO DE CREDITO, INVESTIMENTOS, CARTEIRA DIGITAL, OUTROS]').upper())
                contaCorrigida = removerAcento(conta)
            dataframe.iloc[indice][coluna] = contaCorrigida
            print('Categoria alterada com sucesso')
            print(dataframe.iloc[indice])

        if colunaCorrigida == 'VALOR':
            while True:
                try:
                    valor = float(input('Qual valor você deseja atribuir à esta transação? '))
                    if valor == 0:
                        print('Caro usuário, valores neutros são inválidos! Por favor, insira um valor maior ou menor que zero')
                        valor = float(input('Qual valor você deseja atribuir à esta transação? '))
                    else:
                        dataframe.iloc[indice][coluna] = valor
                        print('Valor alterado com sucesso!')
                        print(dataframe.iloc[indice])
                except ValueError:
                    print('Caro usuário, insira um valor numérico!')

        if colunaCorrigida == 'FORMA DE PAGAMENTO':
            pagamentos = ['DINHEIRO', 'CARTAO DE DÉBITO', 'CARTÃO DE CDÉDITO', 'PIX', 'TRANSFERENCIA', 'TED', 'DOC', 'CHEQUE', 'PAYPAL', 'PICPAY', 'MERCADO PAGO', 'GOOGLE PAY', 'APPLE PAY', 'CRYPTO']
            pagamento = str(input('Insira a forma de pagamento da transação: [DINHEIRO, CARTAO DE DEBITO, CARTAO DE CRÉDITO, PIX, TRANSFERENCIA, TED, DOC, CHEQUE, PAYPAL, PICPAY, MERCADO PAGO, GOOGLE PAY, APPLE PAY, CRYPTO]').upper())
            pagamentoCorrigido = removerAcento(pagamento)
            if pagamentoCorrigido not in pagamentos:
                print('Caro usuário, insira uma forma de pagamento válida')
                pagamento = str(input('Insira a forma de pagamento da transação: [DINHEIRO, CARTAO DE DEBITO, CARTAO DE CRÉDITO, PIX, TRANSFERENCIA, TED, DOC, CHEQUE, PAYPAL, PICPAY, MERCADO PAGO, GOOGLE PAY, APPLE PAY, CRYPTO]').upper())
                pagamentoCorrigido = removerAcento(pagamento)
            dataframe.iloc[indice][coluna] = pagamentoCorrigido
            print('Forma de pagamento alterada com sucesso! ')
            print(dataframe.iloc[indice])
        if colunaCorrigida == 'TAG':
            tipoTransacao = tipoTransaction()
            categoriaTransacao = category(tipoTransacao)
            tag = tags(tipoTransacao, categoriaTransacao)
            dataframe.iloc[indice][colunaCorrigida] = tag
        if colunaCorrigida == 'CRIADO EM':
            print('Caro usuário, por motivos de segurança não podemos alterar o criado em')

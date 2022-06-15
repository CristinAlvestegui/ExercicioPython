def Exercicio01():
    A = 10
    B = 20
    msg = "Antes da troca: A= {}, B = {}".format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg + "\nDepois da troca: A= {} , B = {}".format(A,B)
    return msg

def Exercicio02(num1):
    return num1 - 1

def E3(base,altura):
    area = base * altura
    msg = 'A Area do Retângulo é: {}'.format(area)
    return msg

def E4(dia, mes, ano):
    dia = int(dia)
    mes = int(mes * 30)
    ano = int(ano * 365)
    idade = dia + (mes + ano)
    msg = 'Sua idade expressa em dias é: {}'.format(idade)
    return msg

def E5():
    return 'são eleitores, pula'

def E6(sal):
    total = sal((sal * 10,16)/100)
    msg = 'Junto com a reajuste desse ano que foi de: 10.16%\n' + 'Fico um total de: {}'.format(total)
    return msg

def E7():
    return 'é carro, pula'

def E8(nota1,nota2,nota3):
    total = nota1 + nota2 + nota3
    media = total / 3
    msg = 'Sua nota média é de: {}'.format(media)
    return msg

def E9(maca):
    if maca => 12:
        total = maca
        msg = 'Obrigada pela compra!!\n\n' + 'Você comprou: {}maças, com um valor total de {}R$, cada uma\n'.format(maca, total)
        return msg
    else:
        total = int(maca * 1,30)
        msg = 'Obrigada pela compra!!\n\n' + 'Você comprou: {}maças, com um valor total de {}R$, cada uma\n'.format(maca, total)
        return msg
    
def E10():
    return 'que preguiçaaaaaaaa'
def E11():
    return 'n fiz.....ainda'
def E12():
    return 'pro, estou com preguiça.....'
def E13(num1):
    if num1 < 10:
        num2 = 0
        for num2 in range(11):
            if num2 == 11:
                break
            else:
                multi = num1 * num2
                msg = '{} X {} = {}'.format(num1, num2, multi)
        return msg
    else:
        return 'Por favor informe um número entre 1 e 10'
    
    
    
    
    

def processar_resposta(cl):
    if cl == '1':
       po = float(input('Qual a tensão?: '))
       pi = float(input('Qual a corrente?: '))
       pt = po * pi
       print(f'A potencia é: {pt}P')
    elif cl == '2':
        pl = float(input('Qual a potencia?: '))
        pk = float(input('Qual a corrente?: '))
        pç = pl / pk
        print(f'A tensão é: {pç}V')
    elif cl == '3':
        pj = float(input('Qual a tensão?: '))
        ph = float(input('Qual a resistencia?: '))
        pi = pj / ph
        print(f'A corrente é: {pi}A')
    elif cl == '4':
        pg = float(input('Qual a tensão?: '))
        pf = float(input('Qual a corrente?: '))
        pc = pg / pf
        print(f'A Resistencia é: {pc}Ω')

def start():
    print('Calculadora de potencia, tensão, corrente e resistencia.')
    while True:
        cl = input('Qual conversão pretende fazer? Digite [1] - potencia, [2] - tensão,[3] - corrente ou [4] - resistencia: ')
        processar_resposta(cl)
if __name__ == '__main__':
    start()
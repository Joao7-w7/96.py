def área(larg, cump):
    a = larg * cump
    print(f'A área de um terreno {larg} X {cump} é de {a}m²')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l =  float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)

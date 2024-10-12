# Exigência de código 1 de 8
# \n faz quebra de linha
#print('|','___'*10,'|') faz separação 
print( "-"   *10,'bem-vindo a pizzaria do joão batista' ,'-'*10,)
print( "-" *24,'cardápio' ,'-'*24,)
print( '-'*58,)
print('-'*4,'|', 'Tamanho' ,'|' , 'Pizza Salgada(PS)', '|', 'Pizza Doce(PD)','|','-'*4)
print('-'*4,'|  ','P    ' ,'|    ' ,  'R$ 30.00     ' , '|  ', 'R$ 34,00'  , '    |','-'*4)
print('-'*4,'|  ', 'M    ','|    ' ,  'R$ 45.00     ' , '|  ','R$ 48,00' ,  '    |','-'*4)
print('-'*4,'|  ', 'G    ','|    ' ,  'R$ 60.00     ' , '|  ','R$ 66,00' ,  '    |','-'*4)
print( '-'*58,)

# Exigência de código 5 de 8
valor_total = 0

while True:  # Exigência de código 7 de 8 (uso de while)
    # Exigência de código 2 de 8
    sabor = input(" \n Escolha o sabor da pizza (PS/PD): ").upper()
    if sabor not in ['PS', 'PD']:
        print(" Sabor inválido. Tente novamente")
        continue  # Exigência de código 7 de 8 (uso de continue)
    
    # Exigência de código 3 de 8
    
    tamanho = input(" Escolha o tamanho da pizza (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print(" \n Tamanho inválido. Tente novamente")
        continue  # Exigência de código 7 de 8 (uso de continue)
    
    # Exigência de código 4 de 8
    if sabor == 'PS':
        if tamanho == 'P':
            preco = 30.00
        elif tamanho == 'M':
            preco = 45
        elif tamanho == 'G':
            preco = 60
    elif sabor == 'PD':
        if tamanho == 'P':
            preco = 34
        elif tamanho == 'M':
            preco = 48
        elif tamanho == 'G':
            preco = 66
        
            
  # Acumular valor total
    valor_total += preco

    # Exigência de código 6 de 8
    mais_alguma = input(" \n Deseja pedir mais alguma coisa? (S/N): ").upper()
    if mais_alguma == 'S':
        continue  # Exigência de código 7 de 8 (uso de break)

    if mais_alguma == 'S':
        break  # Exigência de código 7 de 8 (uso de break)

    print(f'      \n  Total a Pagar = R${valor_total}:')

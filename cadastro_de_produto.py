# Cadastro de Produtos@$

# Estrutura@$

produto = {'Descrição':'', 'Preço' : 0.0, 'Quantidade' : 0.0, 'Disponível': False}

# Apresentação@$

print('\n\t\t\t -- Cadastro Produto -- \n')

# Entrada@$

produto['Descrição'] = input("Insira a DESCRIÇÃO do Produto: ")
produto['Preço'] = float(input("Insira o PREÇO do Produto: "))
produto['Quantidade'] = int(input("Insira a QUANTIDADE de produtos disponiveis: "))
produto['Disponível'] = True

preçototal = produto['Preço'] * produto['Quantidade']

# Saída@$

print(f'Descrição: {produto["Descrição"]}')
print('Preço: R$ {:.2f}'.format(produto["Preço"]))
print(f'Quantidade: {produto["Quantidade"]}')
print(f'Preço Total: {preçototal}')
print("* Produto Disponível *") if produto['Disponível'] else print("* Produto Indisponível *")

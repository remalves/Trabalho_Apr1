
#-----------------------------------------------------Funções Clientes: -----------------------------------------------------------------------------------#]
# Cliente = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones] ]}
def listar_todos_clientes(dic_clientes):
     for cliente,dados in dic_clientes.items():
        print(f'CPF: {cliente}')
        print(f'Nome: {dados[0]}')
        print(f'Data de nascimento: {dados[1]}')
        print(f'Sexo: {dados[2]}')
        print(f'Salário: {dados[3]}')
        
        emails = ''
        for i in range(len(dados[4])):
            emails += dados[4][i]
            #para adicionar virgula entre os emails, mas não no último
            if i < len(dados[4])-1:
                emails+=', '
        print(f'E-mails: {emails}')
        
        telefones = ''
        for i in range(len(dados[5])):
            telefones += dados[5][i]
            #para adicionar virgula entre os telefone, mas não no último
            if i < len(dados[5])-1: 
                telefones+=', '    
        print(f'Telefones: {telefones}')
        print('-' * 40)
           
def listar_um_cliente(cpf,dic_clientes):
    if cpf not in dic_clientes:
        print('Cliente não cadastrado!')
    else:
        dados  = dic_clientes[cpf]
        print(f'Nome: {dados[0]} ')
        print(f'Data de Nascimento: {dados[1]} ')
        print(f'Sexo: {dados[2]} ')
        print(f'Salário: {dados[3]} ')

        emails = ''
        for i in range(len(dados[4])):
            emails+=dados[4][i]
            if i < len(dados[4])-1:
                emails+=', '
        print(f'Emails: {emails}')

        telefones = ''
        for t in range (len(dados[5])):
            telefones+=dados[5][t]
            if t < len(dados[5]) - 1:
                telefones+=', '
        print(f'Telefones: {telefones}')


def incluir_cliente(clientes_arq,cpf, dic_clientes):
    if cpf in dic_clientes:
        return False
    else:
        nome = input('Digite o nome do cliente: ').strip()
        data = input('Data de nascimento (dd/mm/aaaa): ').strip()
        sexo = input('Sexo (M, F): ').strip().upper()

        #tratar possiveis inserções incorretas como com virgula
        salario_valido = False
        while not salario_valido:
            entrada = input('Salário: ').strip().replace(',', '.')
            try:
                salario = float(entrada)
                salario_valido = True
            except ValueError:
                print('Erro! Digite o salário corretamente (ex: 1500.00 ou 1500,00).')
            
        emails = []
        qtd = int(input('Quantos e-mails deseja adicionar: '))
        i=0
        while i < qtd:
            email=input(f'Digite o {i+1}º email: ')
            emails.append(email)
            i+=1
            
        #incluindo telefones    
        telefones = []
        qtdade = int(input('Quantos telefones deseja adicionar: '))
        i=0
        while i < qtdade:
            telefone=input(f'Digite o {i+1}º telefone: ')
            telefones.append(telefone)
            i+=1
        dic_clientes[cpf] = [nome, data, sexo, salario, emails, telefones] #adiciona ao cliente, uma lista contendo todos os dados
        return True
    
def alterar_cliente(cpf, dic_clientes):
    if cpf not in dic_clientes:
        print('Cliente não cadastrado!')
    else:
        alterar = 0
        while alterar != 7:
            print('\n1 - Nome')
            print('2 - Data de nascimento')
            print('3 - Sexo')
            print('4 - Salário')
            print('5 - E-mails')
            print('6 - Telefones')
            print('7 - Finalizar alterações')

            entrada_valida = False  # flag para controlar se a entrada foi válida

            try:
                alterar = int(input('Digite a opção (1-7): '))
                if alterar < 1 or alterar > 7:
                    print('Opção fora do intervalo. Digite um número entre 1 e 7.')
                    entrada_valida = False
                else:
                    entrada_valida = True
            except ValueError:
                print('Opção inválida. Digite um número entre 1 e 7.')
                entrada_valida = False

            if entrada_valida:
                dados_cliente = dic_clientes[cpf]

                if alterar == 1:
                    dados_cliente[0] = input('Digite o novo nome: ').strip()
                elif alterar == 2:
                    dados_cliente[1] = input('Insira a nova data de nascimento (dd/mm/aaaa): ').strip()
                elif alterar == 3:
                    dados_cliente[2] = input('Informe o sexo (M, F): ').strip().upper()
                elif alterar == 4:
                    salario_valido = False  # Variável para controlar a validade da entrada
                    while not salario_valido:  # Enquanto a entrada não for válida, o loop vai continuar
                        try:
                            salario = float(input('Salário: ').strip())  # Tenta receber o salário como float
                            dados_cliente[3] = salario  # Se conseguir, salva o valor no cliente
                            salario_valido = True  # Marca como válido e sai do loop
                        except ValueError:  # Se não for possível converter para float (erro de entrada)
                            print('Erro! Digite o salário corretamente (ex: 1500.00 ou 1500,00).')  # Pede para tentar novamente

                elif alterar == 5:
                    print('Substituindo todos os e-mails do cliente...')
                    emails = []
                    qtd = int(input('Quantos e-mails deseja cadastrar: '))
                    for i in range(qtd):
                        email = input(f'Digite o {i+1}º e-mail: ')
                        emails.append(email)
                    dados_cliente[4] = emails

                elif alterar == 6:
                    print('Substituindo todos os telefones do cliente...')
                    telefones = []
                    qtd = int(input('Quantos telefones deseja adicionar: '))
                    for i in range(qtd): 
                        telefone = input(f'Digite o {i+1}º telefone: ')
                        telefones.append(telefone)
                    dados_cliente[5] = telefones

                elif alterar == 7:
                    print('Alterações concluídas com sucesso.')
                     
def excluir_cliente(cpf, clientes):
    if cpf not in clientes:
        print('Cliente não cadastrado!')
    else:
        del clientes[cpf]
        print('Cliente excluído com sucesso!')
# ------------------------------------------------------------------SUBMENU de Clientes ------------------------------------------------------------------------------#
def submenu_clientes(clientes_arq, dic_clientes):
    continuar = True
    while continuar:
        print("\n--- SUBMENU CLIENTES ---")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar ao menu principal")
        opcao = int(input("Escolha uma opção: "))
        print('\n')

        if opcao == 1:
           if len(dic_clientes) == 0:
               print('Não há clientes cadastrados!')
           else:
                listar_todos_clientes(dic_clientes)

        elif opcao == 2:
            print('Consultando um cliente...')
            if len(dic_clientes) == 0:
                print('Não há clientes cadastrados!')
            else:
                cpf = input('Digite o cpf do cliente: ').strip()
                listar_um_cliente(cpf,dic_clientes)
                print('\n')
                
        elif opcao == 3:
            print('Incluindo um cliente...')
            cpf = input('Digite o cpf do novo cliente: ').strip()
            res = incluir_cliente(clientes_arq,cpf,dic_clientes)
            print('\n')
            if res:
                print('Cliente incluido com sucesso!')
            else:
                print('Cliente já existe')

        elif opcao == 4:
            if len(dic_clientes) == 0:
                print('Não há clientes cadastrados!')
            else:
                print('Alterando Cliente ...')
                cpf = input('Digite o cpf do cliente: ').strip()
                print('\n')
                alterar_cliente(cpf, dic_clientes)
            
        elif opcao == 5:
            if len(dic_clientes) == 0:
                print('\nNão há clientes cadastrados!')
            else:
                print('\nExcluindo um cliente ...')
                cpf = input('\nDigite o cpf do cliente que deseja excluir: ').strip()
                excluir_cliente(cpf,dic_clientes)
            
        elif opcao == 6:
            print('\nVoltando ao menu inicial ...')
            return False
        else:
            print('\nOpção inválida. Digite um número de 1 - 6')

#******************************************************* PRODUTOS *************************************************************************#
def listar_todos_produtos(dic_produtos): 
    for codigo, produtos in dic_produtos.items():
        print(f'Código: {codigo}')
        print(f'Descrição: {produtos[0]}')
        print(f'Peso: {produtos[1]}')
        print(f'Preço: R${produtos[2]:.2f}')
        print(f'Desconto: {produtos[3]}%')
        print(f'Data de validade: {produtos[4]}')
        print('-' * 40)

#Produto = {'Código' : [Descrição, Peso, Preço, Desconto, Data de Validade] }  
def listar_um_produto(codigo,dic_produtos): 
    if codigo not in dic_produtos:
        print('Produto não cadastrado!')
    else:
        #pega as informações do produto que tem o código informado e guarda tudo na variável dados
        dados = dic_produtos[codigo]
        print(f'Código: {codigo}') #printa o codigo do produto
        print(f'Descrição: {dados[0]}') #printa a descrição 
        print(f'Peso: {dados[1]}') #printa o peso
        print(f'Preço: R${dados[2]:.2f}') #Printa o preco
        print(f'Desconto: {dados[3]}%') #Printa o desconto
        print(f'Data de validade: {dados[4]}')  #Printa a data de validade

def incluir_produto(codigo,produtos): 
    if codigo in produtos:
        return False
    else:
        descricao = input('Digite a descrição do produto: ').strip()  # strip() - > remove espaços em branco (e quebras de linha) do começo e do fim de uma string.
        peso = input('Digite o peso do produto: ').strip()
        preco = float(input('Digite o preço do produto: R$').strip())
        desconto = float(input('Digite o desconto (%): ').strip())
        validade = input('Digite a data de validade (dd/mm/aaaa): ').strip()
        produtos[codigo] = [descricao, peso, preco, desconto, validade]
        return True

def alterar_produto(codigo,produtos): 
    if codigo not in produtos:
        return False
    else:
        alterar = 1
        while alterar != 6:
            print('\nO que deseja alterar?')
            print('1- Descrição')
            print('2- Peso')
            print('3- Preço')
            print('4- Desconto')
            print('5- Data de validade')
            print('6- Finalizar alterações')
            
            try:
                alterar = int(input('Escolha uma opção: '))
                if alterar < 1 or alterar > 6:
                    print('Opção inválida! Digite um número entre 1 e 6.')
                else:
                    dados_produto = produtos[codigo]
                    if alterar == 1:
                        dados_produto[0] = input('Nova descrição: ').strip()
                    elif alterar == 2:
                        dados_produto[1] = input('Novo peso: ').strip()
                    elif alterar == 3:
                        dados_produto[2] = float(input('Novo preço: R$').strip())
                    elif alterar == 4:
                        dados_produto[3] = float(input('Novo desconto (%): ').strip())
                    elif alterar == 5:
                        dados_produto[4] = input('Nova data de validade (dd/mm/aaaa): ').strip()
                    elif alterar == 6:
                        print('Alterações finalizadas!')
            except:
                print('Opção inválida! Digite um número entre 1 e 6.')
        
        return True

def excluir_produto(codigo,produtos): 
    if codigo not in produtos:
        return False
    else:
        del produtos[codigo]
        return True

#--------------------------------------------------------Submenu de Produtos--------------------------------------------------------------
def submenu_produtos(produtos_arq, dic_produtos):
    continuar = True
    while continuar:
        print("\n--- SUBMENU PRODUTOS ---")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar ao menu principal")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            if len(dic_produtos) == 0:
                print('Não há produtos cadastrados no sistema!')
            else:
                listar_todos_produtos(dic_produtos)
     
        elif opcao == 2:
            if len(dic_produtos) == 0: 
                print('Não há produtos cadastrados no sistema!')
            else:
                print('Consultando um produto...')
                codigo = input('Digite o código do produto: ').strip()
                listar_um_produto(codigo,dic_produtos)

        elif opcao == 3:
            print('Incluindo um produto ...')
            codigo = input('Digite o código do novo produto: ').strip()
            res = incluir_produto(codigo,dic_produtos)
            if res:
                print('Produto incluido com sucesso!')
            else:
                print('Produto já existe')

        elif opcao == 4:
            if len(dic_produtos) ==0:
                print('Não há produtos cadastrados no sistema!')
            else:
                print('Alterando Produto ...')
                codigo = input('Digite o código do produto: ').strip()
                res = alterar_produto(codigo, dic_produtos)
                if res:
                    print('Produto alterado com sucesso!')
                else:
                    print('Erro ao alterar produto.')

        elif opcao == 5:
            if len(dic_produtos) == 0:
                print('\nNão há produtos cadastrados!')
            else:
                print('\nExcluindo produto ...')
                codigo = input('\nDigite o código do produto que deseja excluir: ').strip()
                res = excluir_produto(codigo,dic_produtos)
                if res:
                    print('\nProduto excluído com sucesso!')
                else:
                    print('\nProduto não existe!')

        elif opcao == 6:
            print('\nVoltando ao menu inicial ...')
            return False
        else:
            print('\nOpção inválida. Digite um número de 1 a 6')


#******************************************************* COMPRA/VENDA  *******************************************************
'''Compra/Venda = {'CPF Cliente, Código Produto, Data, Hora': preço}'''
def listar_todas_compras(cpf_cliente, compras):
    encontrou = False
    print(f'\nCompras do cliente {cpf_cliente}:\n')
    for chave, preco in compras.items():
        if chave[0] == cpf_cliente:
            print(f'- Código do produto: {chave[1]}')
            print(f'  Data: {chave[2]}')
            print(f'  Hora: {chave[3]}')
            print(f'  Valor: R${preco:.2f}')
            print('-' * 30)
            encontrou = True
    if not encontrou:
        print('Não há compras registradas para este cliente!')

def listar_uma_compra(chave, dic_compras):
    if chave in dic_compras:
            print(f'\nDetalhes da compra:')
            print(f'CPF Cliente: {chave[0]}')
            print(f'Código Produto: {chave[1]}')
            print(f'Data: {chave[2]}')
            print(f'Hora: {chave[3]}')
            print(f'Valor: R${dic_compras[chave]:.2f}')
    else:
        print('Compra não encontrada com os dados fornecidos!')

def incluir_compra(chave, dic_compras):
    if chave in dic_compras:
        print('\nCompra já cadastrada!')
    else:
            preco_valido = False
            while not preco_valido:
                try:
                    preco = float(input('\nDigite o preço do produto: '))
                    preco_valido = True
                except:
                    print('\nDigite um valor válido!')
                    preco_valido = False 

            desconto_valido = False
            while not desconto_valido:
                try:
                    desconto = float(input('\nDigite o desconto: '))
                    desconto_valido = True
                except:
                    print('\nDigite um valor válido!')
                    desconto_valido = False 

            valor_desconto = (preco * desconto) / 100
            valor_final = preco - valor_desconto
            dic_compras[chave] = valor_final
            print('\nCompra cadastrada com sucesso!')
    
def alterar_compra(chave, dic_compras):
    if chave not in dic_compras:
        print('\nCompra não cadastrada!')
    else:
        novo_preco_valido =  False
        while not novo_preco_valido:
            try:
                novo_preco = input('\nDigite o novo preco da compra: ')
                novo_preco_valido = True
            except ValueError:
                print('\nValor inválido!')
                novo_preco_valido = False
        dic_compras[chave] = novo_preco
            
def excluir_compra(chave, compras):
  if chave not in compras:
    print('\nCompra não cadastrada!')
  else:
    del compras[chave]
    print('\nCompra excluída com sucesso!')

#-----------------------------------------------------------------Submenu de Compra/Venda------------------------------------------------------
def submenu_compra_venda(compras_arq, dic_compras):
    continuar = True
    while continuar:
        print("\n--- SUBMENU COMPRA/VENDA ---")
        print("1. Listar todas as compras de um cliente")
        print("2. Listar uma compra específica")
        print("3. Incluir compra")
        print("4. Alterar compra")
        print("5. Excluir compra")
        print("6. Voltar ao menu principal")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            if len(dic_compras) == 0:
                print('Não há compras registradas!')
            else:
                print('Listando todas as compras de um cliente...')
                cpf = input('Digite o CPF do cliente: ').strip()
                listar_todas_compras(cpf, dic_compras)

        elif opcao == 2:
            if len(dic_compras) == 0:
                print('Não há compras registradas!')
            else:
                print('Consultando uma compra específica...')
                cpf = input('Digite o CPF do cliente: ').strip()
                codigo = input('Digite o código do produto: ').strip()
                data = input('Digite a data da compra (dd/mm/aaaa): ').strip()
                hora = input('Digite a hora da compra (hh:mm): ').strip()
                chave = (cpf,codigo,data,hora)
                listar_uma_compra(chave, dic_compras)

        elif opcao == 3:
            print('Registrando nova compra...')
            cpf = input('Digite o CPF do cliente: ').strip()
            codigo = input('Digite o código do produto: ').strip()
            data = input('Data (dd/mm/aaaa): ').strip()
            hora= input('Hora (hh:mm): ').strip()
            chave = (cpf,codigo,data, hora)
            incluir_compra(chave, dic_compras)
       

        elif opcao == 4:
            if len(dic_compras) ==0:
                print('\nNão há compras registradas!')
            else:
                print('\nAlterando compra...')

                cpf = input('Digite o CPF do cliente: ').strip()
                print('\nCompras registradas para este cpf: ')
                listar_todas_compras(cpf, dic_compras)

                print('Digite os demais dados para alterar a compra desejada: ')
                codigo = input('Digite o código do produto: ').strip()
                data = input('Digite a data da compra a alterar (dd/mm/aaaa): ').strip()
                hora = input('Digite a hora da compra a alterar (hh:mm): ').strip()
                chave = (cpf,codigo,data, hora)
                alterar_compra(chave, dic_compras)
            

        elif opcao == 5:
            print('\nExcluindo compra...')
            cpf = input('\nDigite o CPF do cliente: ').strip()
            print('\nCompras registradas para este cpf: ')
            listar_todas_compras(cpf,dic_compras)

            print('Digite os demais dados para excluir a compra desejada: ')
            codigo = input('Digite o código do produto: ').strip()
            data = input('Digite a data da compra a excluir (dd/mm/aaaa): ').strip()
            hora = input('Digite a hora da compra a excluir (hh:mm): ').strip()
            chave = (cpf,codigo,data,hora)
            excluir_compra(chave, dic_compras)
            
        elif opcao == 6:
            print('\nVoltando ao menu principal ...')
            continuar = False

        else:
            print('\nOpção inválida. Digite um número de 1 a 6')

#----------------------------------------------------------------------------------RELATÓRIOS ---------------------------------------------------------------------------------------------------------#
def relatorio_clientes_telefone(qtd,dic_clientes, clientes_telefones_arq):
    #Cliente = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones]}}
    if len(dic_clientes)==0:
        return False
    else:
        gravar_relatorio_clientes_telefone_em_arquivo(qtd,dic_clientes,clientes_telefones_arq)
        return True
        
def relatorio_produtos_vencidos(data_atual, produtos_arq, dic_produtos):
   if len(dic_produtos)==0:
        return False
   else:
       gravar_relatorio_produtos_vencidos_em_arquivo(data_atual,produtos_arq, dic_produtos)
       return True
        

def relatorio_vendas_periodo(data_inicial, data_final, dic_compras, dic_clientes, dic_produtos, vendas_periodos_arq):
       if gravar_relatorio_vendas_periodo_em_arquivo(data_inicial, data_final, dic_compras, dic_clientes, dic_produtos, vendas_periodos_arq):
           return True
       else:
           return False

def submenu_relatorios(clientes_arq, produtos_arq, compras_arq, clientes_telefones_arq, produtos_vencidos_arq, vendas_periodos_arq, dic_clientes, dic_produtos, dic_compras):
    opcao = 1
    while opcao != 0:
        print("\n=== RELATÓRIOS ===")
        print("1. Clientes com mais de X telefones")
        print("2. Produtos com validade vencida")
        print("3. Vendas entre duas datas")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            qtde_valida = False
            while not qtde_valida:
                try:
                    qtde = int(input("Digite a quantidade de telefones: "))
                    qtde_valida = True  # valor válido, sai do loop
                except ValueError:
                    print('Valor inválido, digite novamente: ')
                    
            res = relatorio_clientes_telefone(qtde,dic_clientes, clientes_telefones_arq)
            if res:
                print('Arquivo do relatório gerado com sucesso!')
            else:
                print('Erro ao gerar arquivo')
            
        elif opcao == "2":
            data_atual = input('Data atual (dd/mm/aaaa): ')
            res = relatorio_produtos_vencidos(data_atual, dic_produtos)
            if res:
                print('Arquivo do relatório gerado com sucesso!')
            else:
                print('Erro ao gerar arquivo')
                
        elif opcao == "3":
            print('Consultando vendas entre duas datas')
            data_ini = input('Digite a data incial: ')
            data_fim = input("Digite a data final: ")
            res = relatorio_vendas_periodo(data_ini, data_fim, dic_compras, vendas_periodos_arq)
            if res:
                print('Arquivo do relatório gerado com sucesso!')
            else:
                print('Erro ao gerar arquivo')        

        elif opcao == "0":
            print('Encerrando o programa ...')

        else:
            print("Opção inválida!")

#-------------------------------------------------------------------------------------------ARQUIVOS --------------------------------------------------------------------------#

def existe_arquivo(nome_arq):
    import os
    if os.path.exists(nome_arq):
        return True
    else:
        return False

#--------------------------------------- Clientes = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones]}} -----------#
def gravar_dados_clientes(dic_clientes, clientes_arq):
    arq = open(clientes_arq, 'w')
    for cpf in dic_clientes:
        linha  = ''
        linha+=cpf+';'
        linha+=dic_clientes[cpf][0] + ';' #adiciona o nome do cliente e ; 
        linha+=dic_clientes[cpf][1] + ';'  #adiciona a data de nascimento e ;
        linha+=dic_clientes[cpf][2]+ ';' #adiciona o sexo e ;
        linha+=str(dic_clientes[cpf][3]) + ';' #adiciona o salario como string e ;
        #adicionando os emails: 
        for email in dic_clientes[cpf][4]:
            linha+=email+'_'  # acrescenta o email + "_"
        linha += ';'  # separa do próximo campo  
        #adicionando os telefones: 
        for telefone in dic_clientes[cpf][5]:
            linha+=telefone+'_'
        linha+='\n' 
        arq.write(linha)
    arq.close()
 
def carregar_dados_clientes(clientes_arq):
    dic_clientes = {}
    if existe_arquivo(clientes_arq):
    #carrega os dados do arquivo para o dicionário criado
        arq_clientes = open(clientes_arq,'r')
        for linha in arq_clientes:
            #remove o \n da linha
            linha=linha.replace('\n','')
            #separa cada elemento da linha e coloca em uma lista
            linha = linha.split(';') 
            cpf_cliente = linha[0]
            dic_clientes[cpf_cliente]=[]
            dic_clientes[cpf_cliente].append(linha[1])
            dic_clientes[cpf_cliente].append(linha[2])
            dic_clientes[cpf_cliente].append(linha[3])
            dic_clientes[cpf_cliente].append(float(linha[4]))  # Salário (converter para float)

            emails=linha[5].split('_')# Separa os emails usando o underline como separador
            del emails[-1] # Remove o último item vazio (porque a linha termina com um underline)
            dic_clientes[cpf_cliente].append(emails) # Adiciona a lista de emails no dicionário

            telefones=linha[6].split('_')
            del telefones[-1] #remove o último elemento que é vazio
            dic_clientes[cpf_cliente].append(telefones)
        arq_clientes.close()  # Fecha o arquivo depois de ler tudo
    return dic_clientes  # Retorna o dicionário completo com todos os clientes carregados

#------------------------------------------------------------Produtos = {'Código' : [Descrição, Peso, Preço, Desconto, Data de Validade] } ----------------------------------------------------------------#
def gravar_dados_produtos(dic_produtos, produtos_arq):
    arq = open(produtos_arq, 'w')
    for codigo in dic_produtos:
        linha  = ''
        linha+=codigo +';'
        linha+=dic_produtos[codigo][0] + ';' #adiciona descrição e ; 
        linha+=dic_produtos[codigo][1] + ';'  #adiciona o peso e ;
        linha+= str(dic_produtos[codigo][2]) + ';' #adiciona o preço e ;
        linha+=str(dic_produtos[codigo][3]) + ';' #adiciona o desconto como string e ;
        linha+=(dic_produtos[codigo][4]) + '\n' 
        arq.write(linha)
    arq.close()

def carregar_dados_produtos(produtos_arq):
    dic_produtos = {}
    if existe_arquivo(produtos_arq):
        #carrega os dados do arquivo para o dicionário criado
            arq_produtos = open(produtos_arq,'r')
            for linha in arq_produtos:
                #remove o \n da linha
                linha=linha.replace('\n','')
                #separa cada elemento da linha e coloca em uma lista
                linha = linha.split(';') 
                codigo = linha[0]
                dic_produtos[codigo]=[]
                dic_produtos[codigo].append(linha[1])
                dic_produtos[codigo].append(linha[2])
                dic_produtos[codigo].append(linha[3])
                dic_produtos[codigo].append(linha[4])
            return dic_produtos

# ---------------------------------------------------------Compra/Venda = {'CPF Cliente, Código Produto, Data, Hora': preço}------------------------------------------------------#
def gravar_dados_compras(dic_compras, compras_arq, ):
    arq = open(compras_arq, 'w')
    for chave, preco in dic_compras.items():
        linha = ''
        linha += chave[0] + ';' #aceesa o cpf
        linha += chave[1] + ';' #aceesa o codigo
        linha += chave[2] + ';' #aceesa a data
        linha += chave[3] + ';' #aceesa a hora
        linha += str(preco) + '\n'
        arq.write(linha)
    arq.close()
    
def carregar_dados_compras(compras_arq):
    dic_compras = {}
    if existe_arquivo(compras_arq):
        arq_compras = open(compras_arq, 'r')
        for linha in arq_compras:
            linha = linha.replace('\n', '')
            partes = linha.split(';')  # [cpf, codigo, data, hora, preco]
            chave = (partes[0], partes[1], partes[2], partes[3])  # tupla
            dic_compras[chave] = float(partes[4])
        arq_compras.close()
    return dic_compras
#---------------------------------------------------------------- Relatórios ------------------------------------------------------------------------------------------#

def gravar_relatorio_clientes_telefone_em_arquivo(x, dic_clientes, clientes_telefones_arq):
    try:
        arq = open(clientes_telefones_arq, 'w')
        for cpf, dados in dic_clientes.items():
            telefones = dados[5]
            if len(telefones) > int(x):
                linha = ''
                linha += f'CPF: {cpf}\n'
                linha += f'Nome: {dados[0]}\n'
                linha += f'Data de Nascimento: {dados[1]}\n'
                linha += f'Sexo: {dados[2]}\n'
                linha += f'Salário: R${float(dados[3]):.2f}\n'
                emails = ''
                for i in range(len(dados[4])):
                    emails += dados[4][i]
                    if i < len(dados[4]) - 1:
                        emails += ', '
                linha += 'E-mails: ' + emails + '\n'

                telefones = ''
                for i in range(len(dados[5])):
                    telefones += dados[5][i]
                    if i < len(dados[5]) - 1:
                        telefones += ', '
                linha += 'Telefones: ' + telefones + '\n'
                linha += '-' * 30 + '\n'
                arq.write(linha)
        arq.close()
        return True
    except:
        return False

def carregar_relatorio_clientes_telefone(clientes_telefones_arq):
    if existe_arquivo(clientes_telefones_arq):
        arq = open(clientes_telefones_arq, 'r')
        print('\n--- RELATÓRIO: Clientes com mais de X telefones ---\n')
        for linha in arq:
            print(linha.strip())
        arq.close()
        return True
    else:
        return False
        
 #--------------------------------------------------------------------------------------------------------------             
def gravar_relatorio_produtos_vencidos_em_arquivo(data_atual, dic_produtos, produtos_vencidos_arq):
    arq = open(produtos_vencidos_arq, 'w')
    # Divide a data atual em dia, mês e ano (assumindo formato dd/mm/aaaa)
    partes_data = data_atual.split('/')
    dia_hoje = int(partes_data[0])
    mes_hoje = int(partes_data[1])
    ano_hoje = int(partes_data[2])
   # Percorre todos os produtos no dicionário
    for codigo, dados in dic_produtos.items():
        # A validade do produto está no índice 4 da lista "dados"
        # Também no formato dd/mm/aaaa, então divide a string para extrair dia, mês e ano
        partes = dados[4].split('/')
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        # Se o ano da validade é menor que o ano atual, já está vencido
        # Ou se é o mesmo ano, mas o mês é menor
        # Ou se é o mesmo ano e mês, mas o dia da validade é menor que o dia atual
        if (ano < ano_hoje or (ano == ano_hoje and mes < mes_hoje) or (ano == ano_hoje and mes == mes_hoje and dia < dia_hoje)):
            linha = ''
            linha += f'Código: {codigo}\n'
            linha += f'Descrição: {dados[0]}\n'
            linha += f'Peso: {dados[1]}\n'
            linha += f'Preço: R${float(dados[2]):.2f}\n'
            linha += f'Desconto: {dados[3]}%\n'
            linha += f'Validade: {dados[4]}\n'
            linha += '-' * 30 + '\n'
            arq.write(linha)
    arq.close()

def carregar_relatorio_produtos_vencidos(produtos_vencidos_arq):
    if existe_arquivo(produtos_vencidos_arq):
        arq = open(produtos_vencidos_arq, 'r')
        print('\n--- RELATÓRIO: Produtos com validade vencida ---\n')
        for linha in arq:
            print(linha.strip())
        arq.close()
        return True
    else:
        return False

 #--------------------------------------------------------------------------------------------------------------     
def gravar_relatorio_vendas_periodo_em_arquivo(data_ini, data_fim, dic_compras, dic_clientes, dic_produtos, vendas_periodos_arq):
    def formatar_data(data):  # para comparar corretamente as datas
        d, m, a = data.split('/')
        return a + m + d
    try:
        data_ini_f = formatar_data(data_ini)
        data_fim_f = formatar_data(data_fim)
        
        arq = open(vendas_periodos_arq, 'w')
        
        for chave, valor in dic_compras.items():
            cpf = chave[0]
            cod_prod = chave[1]
            data = chave[2]
            hora = chave[3]
            data_formatada = formatar_data(data)

            if data_ini_f <= data_formatada <= data_fim_f:
                nome_cliente = dic_clientes[cpf][0]
                descricao_produto = dic_produtos[cod_prod][0]

                linha = ''
                linha += f'CPF Cliente: {cpf}\n'
                linha += f'Nome Cliente: {nome_cliente}\n'
                linha += f'Código Produto: {cod_prod}\n'
                linha += f'Descrição Produto: {descricao_produto}\n'
                linha += f'Data da Venda: {data}\n'
                linha += f'Hora da Venda: {hora}\n'
                linha += f'Valor da Venda: R${valor:.2f}\n'
                linha += '-' * 30 + '\n'
                arq.write(linha)
        arq.close()
        return True
    
    except:
        return False 
    

def carregar_dados_vendas_periodos(vendas_periodos_arq):
    if existe_arquivo(vendas_periodos_arq):  
        arq = open(vendas_periodos_arq, 'r')
        print('\n--- RELATÓRIO: Vendas entre datas ---\n')
        for linha in arq:
            print(linha.strip())
        arq.close()
        return True 
    else:
        return False

#-----------------------------------------------------------------Menu principal---------------------------------------------------------------#

def menu_principal():
    #Criando os arquivos texto
    clientes_arq = "./clientes.txt"
    produtos_arq = "./produtos.txt"
    compras_arq = "./compras.txt"
    vendas_periodos_arq = "./vendas_periodos.txt"
    clientes_telefones_arq = "./client_telefones.txt"
    produtos_vencidos_arq = "./produtos_vencidos.txt"

    #Carregando os arquivos 
    Clientes = carregar_dados_clientes(clientes_arq)
    Compras = carregar_dados_compras(compras_arq) 
    Produtos = carregar_dados_produtos(produtos_arq)
    clientes_telefones = carregar_relatorio_clientes_telefone(clientes_telefones_arq)
    produtos_vencidos = carregar_relatorio_produtos_vencidos(produtos_vencidos_arq)
    vendas_periodos = carregar_dados_vendas_periodos(vendas_periodos_arq)

    opcao = 1
    while opcao != 5:
        print('\nMenu Principal:')
        print('1. Submenu de Clientes')
        print('2. Submenu de Produtos')
        print('3. Submenu de Compra/Venda')
        print('4. Submenu Relatórios')
        print('5. Sair')
        
        entrada_valida = False
        while not entrada_valida:
            try:
                opcao = int(input('Digite uma opção: '))
                if 1 <= opcao <= 5:
                    entrada_valida = True
                else:
                    print('Opção inválida. Digite entre 1 e 5.')
            except ValueError:
                print('Valor digitado inválido! Digite entre 1 - 5.')

        if opcao == 1:
            submenu_clientes(clientes_arq, Clientes)
        elif opcao == 2:
            submenu_produtos(produtos_arq, Produtos)
        elif opcao == 3:
            submenu_compra_venda(compras_arq, Compras)
        elif opcao == 4:
            submenu_relatorios(clientes_arq, produtos_arq, compras_arq, clientes_telefones_arq, produtos_vencidos_arq, vendas_periodos_arq,Clientes, Produtos, Compras)
        elif opcao == 5:
            # Gravar todos os dados antes de sair
            print("Gravando os dados em arquivos")
            gravar_dados_clientes(Clientes, clientes_arq)
            gravar_dados_produtos(Produtos,produtos_arq)
            gravar_dados_compras(Compras,compras_arq)
            print("\nTerminando a execução do programa.")
menu_principal()

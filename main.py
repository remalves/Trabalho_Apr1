
#-----------------------------------------------------------------------------Funções Clientes: -----------------------------------------------------------------------------------#]

# Cliente = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones] ]}
def listar_todos_clientes(dic_clientes):
    if len(dic_clientes)==0:
        print('Não há clientes cadastrados no sistema!')
    else:
            for cliente,dados in dic_clientes.items():
                print(f'CPF: {cliente}')
                print(f'Nome: {dados[0]}')
                print(f'Data de nascimento: {dados[1]}')
                print(f'Sexo: {dados[2]}')
                print(f'Salário: {dados[3]}')
                #imprimindo cada email da lista
                emails = ''
                for i in range(len(dados[4])):
                    emails += dados[4][i]
                #para adicionar virgula entre os emails, mas não no último
                    if i < len(dados[4])-1:
                        emails+=', '
                print(f'E-mails: {emails}')
                #imprimindo cada telefone da lista
                telefones = ''
                for i in range(len(dados[5])):
                    telefones += dados[5][i]
                #para adicionar virgula entre os telefone, mas não no último
                    if i < len(dados[5])-1: 
                        telefones+=', '    
                print(f'Telefones: {telefones}')
            #separador visual dos clientes com hifen 
            print('-' * 40)
           
#Cliente = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones]}}
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
  

#Cliente = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones]}}
def incluir_cliente(clientes_arq,cpf, clientes):
    if cpf in clientes:
        return False
    else:
        nome = input('Digite o nome do cliente').strip()
        aniversario = input('Data de nascimento (dd/mm/aaaa): ').strip()
        sexo = input('Sexo (M, F): ').strip().upper()
        salario = float(input('Salário: ').strip()) 
        #incluindo emails
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
        clientes[cpf] = [nome, aniversario, sexo, salario, emails, telefones]
        gravar_dados_clientes(clientes,clientes_arq)
        return True
    
def alterar_cliente(cpf, clientes):
    if len(clientes) == 0: #sem clientes cadastrados
        return False
    
    elif cpf not in clientes: #cliente não cadastrado
            return False
    else:
        alterar = 1
        while alterar != 7:
            print('1-Nome: ')
            print('2-Data de nascimento: ')
            print('3-Sexo: ')
            print('4-Salário: ')
            print('5-E-mails')
            print('6-Telefones')
            print('7-Finalizar alterações')
            alterar = int(input('Qual campo deseja alterar?'))

            #criando uma lista para acessar os dados do cliente em especifico
            dados_cliente = clientes[cpf]
            if alterar == 1:
             #acessando o nome
                dados_cliente[0] = input('Digite o novo nome: ').strip()
            elif alterar == 2:
                dados_cliente[1] = input('Insira a nova data de nascimento (dd/mm/aaaa): ').strip()
            elif alterar == 3:
                dados_cliente[2] = input('Informe o sexo (M, F): ').strip().upper()
            elif alterar == 4:
                dados_cliente[3] = float(input('Novo Salário: ').strip())
            elif alterar == 5:
                print('Alterando e-mails...')
                #pedir ajuda pra montar o codigo que altera um email especifico
                emails = []
                qtd = int(input('Quantos e-mails deseja adicionar: '))
                i=0
                while i < qtd:
                    email=input(f'Digite o {i+1}º email: ')
                    emails.append(email)
                    i+=1
                dados_cliente[4] = emails

            elif alterar == 6:
                telefones = []
                qtdade = int(input('Quantos telefones deseja adicionar: '))
                i=0
                while i < qtdade:
                    telefone=input(f'Digite o {i+1}º telefone: ')
                    telefones.append(telefone)
                    i+=1
                dados_cliente[5] = telefones
            elif alterar == 7:
                print('Fechando alterações...')
            else:
                print('Opção inválida.') 
                alterar = int(input('Qual campo deseja alterar? Digite um numero entre 1 - 7'))

def excluir_cliente(cpf, clientes):
    if len(clientes) == 0:
        return False
    else:
        if cpf not in clientes:
            return False
        else:
            del clientes[cpf]
            return True

# -------------------------------------------------------------------------------SUBMENU de Clientes ------------------------------------------------------------------------------#
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

        if opcao == 1:
           listar_todos_clientes(dic_clientes)

        elif opcao == 2:
            print('Consultando um cliente...')
            if len(dic_clientes) == 0:
                print('Não há clientes cadastrados!')
            else:
                cpf = input('Digite o cpf do cliente: ').strip()
                listar_um_cliente(cpf,dic_clientes)

        elif opcao == 3:
            print('Incluindo um cliente...')
            cpf = input('Digite o cpf do novo cliente: ').strip()
            res = incluir_cliente(clientes_arq,cpf,dic_clientes)
            if res:
                print('Cliente incluido com sucesso!')
            else:
                print('Cliente já existe')

        elif opcao == 4:
            print('Alterando Cliente ...')
            cpf = input('Digite o cpf do cliente: ').strip()
            res = alterar_cliente(cpf, dic_clientes)
            if res:
                print('Cliente alterado com sucesso!')
            else:
                print('Erro ao alterar cliente.')
        elif opcao == 5:
            print('Excluindo cliente ...')
            cpf = input('Digite o cpf do cliente que deseja excluir: ').strip()
            res = excluir_cliente(cpf,dic_clientes)
            if res:
                print('Cliente excluído com sucesso!')
            else:
                print('Cliente não existe')
        elif opcao == 6:
            print('Voltando ao menu inicial ...')
            return False
        else:
         print('Opção inválida. Digite um número de 1 - 6')

#------------------------------------------------------------ Seção Arquivos - Clientes -------------------------------------------------------------------------------#
#Cliente = {CPF: [Nome, Data de Nascimento, Sexo, Salário, [E-mails], [Telefones]}}
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

def existe_arquivo(clientes_arq):
    import os
    if os.path.exists(clientes_arq): #verifica se no diretorio atual existe um arquivo com o nome no disco
        return True
    else:
        return False
    
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
            emails=linha[4].split('_')
            del emails[-1] #remove o último elemento que é vazio
            dic_clientes[cpf_cliente].append(emails)
            telefones=linha[5].split('_')
            del telefones[-1] #remove o último elemento que é vazio
            dic_clientes[cpf_cliente].append(telefones)
    return dic_clientes

#-----------------------------------------------------------------Menu principal---------------------------------------------------------------#

def menu_principal():
    clientes_arq="./clientes.txt"
    #chama a função que carrega os dados do filme a partir do arquivo
    Clientes= carregar_dados_clientes(clientes_arq)
    Produtos = {}
    Compras = {}

    opcao = 1
    while opcao != 5:
        print('Menu Principal:')
        print('1.Submenu de Clientes')
        print('2.Submenu de Produtos')
        print('3.Submenu de Compra/Venda')
        print('4.Submenu Relatórios')
        print('5.Sair')    
        try: 
            opcao = int(input('Digite uma opção: '))
        except ValueError:
            print('Valor digitado inválido! Digite entre 1 - 5.')
            continue
        if opcao == 1:
            submenu_clientes(clientes_arq, Clientes)
        # elif opcao == 2:
            # submenu_produtos(Produtos)
        # elif opcao == 3:
            # Submenu_Compra_Venda(Compras)
        # elif opcao == 4:
            # registros()
        elif opcao == 5:
            print('Encerrando o programa ...')
        else:
            print('Opção inválida. Digite entre 1 e 5.')

menu_principal()






















''''
#Produtos
#Produtos = { 'Código': [Descrição, Peso, Preço, Desconto, Data de Validade])

def listar_todos_produtos(dic_produtos):
    if len(dic_produtos) == 0:
       print('Não há produtos cadastrados')
    else:
        for codigo,dados in dic_produtos.items():
            print(f'Código: {codigo}')
            print(f'Descrição: {dados[0]}')
            print(f'Peso: {dados[1]}')
            print(f'Preço: {dados[2]}')
            print(f'Desconto: {dados[3]}')
            print(f'Data de validade: {dados[4]}')
            

''' 
'''
def listar_um_produto(codigo, produtos):
def incluir_produto(codigo,produtos):
def alterar_produto(codigo, produtos):
def excluir_produto(codigo,produtos):
sub-menu de Produtos
def submenu_produtos(dic_produtos):
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
           listar_todos_produtos(dic_produtos)

        elif opcao == 2:
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
            print('Alterando Produto ...')
            codigo = input('Digite o código do produto: ').strip()
            res = alterar_produto(codigo, dic_produtos)
            if res:
                print('Produto alterado com sucesso!')
            else:
                print('Erro ao alterar produto.')
        elif opcao == 5:
            print('Excluindo produto ...')
            codigo = input('Digite o código do produto que deseja excluir: ').strip()
            res = excluir_produto(codigo,dic_produtos)
            if res:
                print('Produto excluído com sucesso!')
            else:
                print('Produto não existe')
        elif opcao == 6:
            print('Voltando ao menu inicial ...')
            return False
        else:
            print('Opção inválida. Digite um número de 1 - 6')'''

'''
#Compra/Venda
def listar_todas_compras(cpf_cliente,compras):
def listar_uma_compra(cpf_cliente, codigo_Produto, data, hora, compras):   
def incluir_compra(cpf_cliente, codigo_Produto,compras):
def alterar_compra(cpf_cliente, codigo_Produto, data, hora, compras):
def excluir_compra(cpf_cliente, codigo_Produto, data, hora, compras)
'''



    

          





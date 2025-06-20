# Trabalho APR1

**Tema 8: Controle de compras e vendas:**
Uma aplicação para uma loja de cosméticos precisa armazenar informações sobre os seus clientes, bem como sobre a compra/venda de produtos. Os dados a serem armazenados sobre cada cliente, produto e sobre a compra/venda de produtos por cliente são apresentados a seguir:
**Cliente** = (CPF, Nome, Data de Nascimento, Sexo, Salário, E-mails, Telefones)

**Produto** = (Código, Descrição, Peso, Preço, Desconto, Data de Validade)

**Compra/Venda** = (CPF Cliente, Código Produto, Data, Hora, Valor)

Atenção: os atributos grifados são chaves e você NÃO deve permitir a inclusão de mais
de um cadastro com os mesmos valores para os atributos chaves.

Utilizando os conhecimentos aprendidos nas aulas, desenvolva um programa em
Python que apresente o seguinte menu de opções para o usuário e implemente cada operação
usando função. Escolha a estrutura de dados mais apropriada para armazenar os dados de
cada entidade descrita anteriormente.

**Menu Principal:**

1. **Submenu de Clientes**
2. **Submenu de Produtos**
3. **Submenu de Compra/Venda**
4. **Submenu Relatórios**
5. **Sair**

Cada Submenu deverá oferecer as opções:

- Listar todos
- Listar um
- Incluir (sem repetição)
- Alterar e Excluir (após confirmação dos dados) um elemento do conjunto.

Observe que as informações que estão no plural significam que **deve ser possível incluir
vários itens do mesmo atributo, por exemplo, os atributos E-mails e Telefones, devem
permitir a inclusão de todos os e-mails e telefones daquele cliente.**

O Submenu Relatórios deverá ter uma opção para cada um dos relatórios solicitados abaixo
**Relatórios:**
a) Mostrar todos os dados de todos os clientes que possuem mais do que X telefones, onde X deve ser fornecido pelo usuário;

b) Mostrar todos os dados de todos os produtos que já tiveram sua data de validade vencida, considerando a data do sistema no momento da execução;

c) Mostrar o CPF e nome do cliente, código do produto, descrição e os demais dados das vendas que foram realizadas entre as datas X e Y, onde ambas as datas devem ser fornecidas pelo usuário.

**Obs:** Não utilize variáveis globais. Use parâmetros para fazer a transferência de valores entre as
funções. Dê nomes significativos para variáveis e funções.

***O programa deverá utilizar Arquivos para a persistência dos dados manipulados pela aplicação.***

- Em outras palavras, cada registro de Cliente, Produto e de cada Compra/Venda deverá ser
armazenado em um arquivo texto específico, que conterá apenas registros daquele mesmo
tipo de entidade.

**O submenu Relatórios também deverá usar arquivos textos para a persistência dos relatórios gerados.**

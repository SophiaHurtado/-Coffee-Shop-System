import re
import unidecode

padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

class Cafeteira():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []
        self.produtos = []
        self.pedidos = []

    def __str__(self):
        return f"""
        Nome: {self.nome}
        endereço: {self.endereco}
        cnpj {self.cnpj}
        clientes {self.clientes}
        produtos {self.produtos}
        """

    def cadastrar_cliente(self):
        while True:
            cliente_nome = input('Digite seu nome: ')
            try:
                cliente_nome = str(cliente_nome)
            except ValueError:
                print("Nome deve ser uma string.")
            if  cliente_nome == "":
                print("Nome não pode ser vazio.")
            elif not cliente_nome.isalpha():
                print("Nome deve conter apenas letras.")
            else:
                break
        while True:
            cliente_sobrenome = input('Digite seu sobrenome: ')
            try:
                cliente_sobrenome = str(cliente_sobrenome)
            except ValueError:
                print("Sobrenome deve ser uma string.")
            
            if  cliente_sobrenome == "":
                print("Sobrenome não pode ser vazio.")
            elif not cliente_sobrenome.isalpha():
                print("Sobrenome deve conter apenas letras.")
            else:
                break
        cliente_endereco = input('Digite seu endereço: ')
        while True:
            try:
                cliente_endereco = str(cliente_endereco)
            except ValueError:
                print("Endereço deve ser uma string.")
            
            if  cliente_endereco == "":
                print("Endereço não pode ser vazio.")
            else:
                break
        while True:
            cliente_email = input('Digite seu e-mail: ')
            if cliente_email == (""):
                print ("O e-mail não pode ser vazio.")
            elif re.match(padrao, cliente_email):
                print(f"O email {cliente_email} foi cadastrado com sucesso!")
                break
            else:
                print("O formato do e-mail não é válido. Digite novamente. ")   
        cliente_senha = input('Digite sua senha: ')

        cliente = Cliente(cliente_nome, cliente_sobrenome, cliente_email, cliente_endereco, cliente_senha)

        self.clientes.append(cliente)

        print(f'Cliente {cliente_nome} cadastrado com sucesso!')
        return cliente

    def cadastrar_produto (self):
        while True:
            nome_produto = input("Digite o produto: ")
            try:
                nome_produto = str(nome_produto)
            except ValueError:
                print("O produto deve ser uma string.")
            if nome_produto == "":
                print("O produto não pode ser vazio.")
            elif not nome_produto.isalpha():
                print("O nome do produto deve conter apenas letras.")
            else:
                self.produtos.append(nome_produto)
                break
        
        while True:
            tipo_produto = input("Digite o tipo do produto: ")
            try:
                tipo_produto = str(tipo_produto)
            except ValueError:
                print("O tipo do produto deve ser uma string.")
            if tipo_produto == "":
                print("O tipo de produto não pode ser vazio.")
            elif not tipo_produto.isalpha():
                print("O tipo do produto deve conter apenas letras.")
            else:
                break
        while True:
            tamanho_produto = input("Digite o tamanho do produto: ")
            try:
                tamanho_produto = int(tamanho_produto)
                if tamanho_produto <= 0:
                    print("O tamanho do produto deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("O tamanho do produto deve ser um número válido.")
        while True:
            preco_produto = input("Digite o preço do produto: ")
            try:
                preco_produto = float(preco_produto)
            except ValueError:
                print("O preço deve ser um número.")
            if preco_produto == "":
                print("O preço do produto não pode ser vazio.")
            else:
                break
        produto = Produto(nome_produto, tipo_produto, tamanho_produto, preco_produto)
        self.produtos.append(produto)

        print(f"O produto {nome_produto} foi cadastrado com sucesso! ")
        return produto
    
    def cadastrar_pedido(self):
        produto_pedido = input("Digite qual produto deseja adicionar ao seu pedido: ")
        if produto_pedido not in self.produtos: 
            print("O produto informado não está disponível.")
        else:
            self.pedidos.append(produto_pedido)
            print(f"Produto {self.pedidos[-1]} foi adicionado ao pedido.")
            return self.pedidos[-1]
    
class Cliente():
    def __init__(self, nome, sobrenome, email, endereco, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.endereco = endereco
        self.senha = senha

    def __str__(self):
        return f"""
            Nome: {self.nome}
            Sobrenome: {self.sobrenome}
            Email: {self.email}
            Endereço: {self.endereco}
            Senha: {self.senha}
            """
    

class Produto():
    def __init__(self, nome, tipo, tamanho, preco):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.preco = preco
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Tipo: {self.tipo}
        Tamanho: {self.tamanho}
        Preço: {self.preco}
        """

class Pedido():
    def __init__(self, pedido_):
        self.pedido_ = pedido_
    
    def __str__(self):
        return f"""
        Pedido: {self.pedido_}
        """


meuCafe = Cafeteira("Coffee Lovers", "Rua das Flores, 123", "12.345.678/0001-90")
print(meuCafe)

produto = meuCafe.cadastrar_produto()
print(produto)

cliente = meuCafe.cadastrar_cliente()
print(cliente)

meucafepedidos = meuCafe.cadastrar_pedido()
print(meucafepedidos)


from model import Categoria, Produtos, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from dao import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria Cadastrada.")
        else:
            print("Categoria já existente.")
    
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()

        cate = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cate) == 0:
            print("A categoria que deseja remover nao existe.")
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print("Categoria removida.")
            
            with open("categoria.txt", "w") as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines("\n")
    
    def alterarCategoria(self, categoriaPorAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cate = list(filter(lambda x: x.categoria == categoriaPorAlterar, x))

        if len(cate) > 0:
            cate1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cate1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaPorAlterar) else(x), x))
                print("Categoria alterada.")
                
            else:
                print("A categoria já existe.")
        else:
            print("A categoria não existe.")
        
        with open("categoria.txt", "w") as arq:
            for i in x:
                arq.writelines(i.categoria)
                aqr.writelines("\n")
    
    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print("Sem categoria.")
        else:
            for i in categorias:
                print(f"Categoria: {i.categoria}")

class ControllerEstoque:
    def cadastrarEstoque(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        z = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(z) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("Produto Cadastrado.")
            else:
                print("Produto já existe em estoque.")
        else:
            print("Categoria inexistente.")
        
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
                print("Produto removido.")
        else:
            print("O produto que deseja remover não existe.")
        
        with open("estoque.txt", "w") as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
        arq.writelines("\n")

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome == nomeAlterar) else(x), x))
                    print("Produto alterado.")
                else:
                    print("Produto já cadastrado.")
            else:
                print("O produo que deseja alterar não existe.")

            with open("estoque.txt", "w") as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines("\n")

        else:
            print("A categoria informada não existe.")

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            print("Produtos:")
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                f"Preço: {i.produto.preco}\n"
                f"Categoria: {i.produto.categoria}\n"
                f"Quantidade: {i.quantidade}")

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temporario =[]
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorDaCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            temporario.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open("estoque.txt", "w")
        arq.write("")

        for i in temporario:
            with open("estoque.txt", "a") as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + str(i[1]))
                arq.writelines("\n")

        if existe == False:
            print("O produto nao existe")
            return None
        elif not quantidade:
            print("A quantidade vendida nao contem em estoque")
            return None
        else:
            print("Produto vendido")
            return valorDaCompra

    def relatorioVenda(self):
        vendas = DaoVenda.ler()
        produtos = []

        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x["produto"] == nome, produtos))

            if len(tamanho) > 0:
                produtos = list(map(lambda x: {"produto": nome, "quantidade": int(x["quantidade"])+ int(quantidade)} if(x["produto"] == nome) else(x), produtos))
            else:
                produtos.append({"produto": nome, "quantidade":int(quantidade)})
            
        ordenado = sorted(produtos, key=lambda k: k["quantidade"])

        print("Os produtos mais vendidos são: ")
        for i in ordenado:
                print(f"Produto: {i["produto"]}\n" f"quantidade: {i["quantidade"]}\n")

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio,"%d/%m/%Y")
        dataTermino1 = datetime.strptime(dataTermino,"%d/%m/%Y")

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, "%d/%m/%Y") >= dataInicio1 and datetime.strptime(x.data, "%d/%m/%Y") <= dataTermino1, vendas ))

        contador = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"venda: {contador}")
            print(f"Nome: {i.itensVendido.nome}\n"
            f"Categoria:{i.itensVendido.categoria}\n"
            f"Data: {i.data}\n"
            f"Quantidade: {i.quantidadeVendida}\n"
            f"Cliente: {i.comprador}\n"
            f"Vendedor: {i.vendedor}")

            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            contador =+ 1
        print(f"Total vendido: {total}")


class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, telefone, categoria):
        if len(telefone) == 8:
            DaoFornecedor.salvar(Fornecedor(nome, telefone, categoria))
        else:
            print("Digite um numero de telefone valido.")
    
    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("Fornecedor inexistente")
            return None
        
        with open("fornecedores.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + str(i.categoria))
                aqr.writelines("\n")
            print("Fornecedor removido")

    def mostrarFornecedor(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print("Srm fornecedores.")
        else:
            print("Fornecedores:")
            for i in fornecedores:
                print(f"Categoria Fornecida: {i.categoria}\n"
                f"Nome: {i.nome}\n"
                f"Telefone: {i.telefone}")
    
class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, bi, email, endereco):
        x = DaoPessoa.ler()

        listaBi = list(filter(lambda x: x.bi == bi, x))
        if len(listaBi) > 0:
            print("BI já existente")
        else:
            if len(bi) == 13 and len(telefone) >= 9 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, bi, email, endereco))
                print('Cliente cadastrado com sucesso')
            else:
                print('Digite um BI ou telefone válido')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoBi, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoBi, novoEmail, novoEndereco) if x.nome == nomeAlterar else (x), x))
        else:
            print("O cliente que deseja alterar nao existe")
        
        with open("clientes.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.email + "|" + i.bi + "|" + i.endereco)
                arq.writelines("\n")
            print("Cliente alterado.")
            
    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("O cliente que deseja remover não existe.")
            return None
        
        with open("cliente.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.bi +"|" + i.email +"|" + i.endereco)
                arq.writelines("\n")
            print("Cliente removido")

    def mostrarCliente(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print("Sem clientes")
        
        for i in clientes:
            print(f"Nome: {i.nome}\n"
            f"Telefone: {i.telefone}\n"
            f"BI: {i.bi}\n"
            f"Email: {i.email}\n"
            f"Endereco: {i.endereco}")
    
class ControllerFuncionario:
    def cadastrarFuncionario(self, nome, telefone, bi, email, endereco):
        x = DaoFuncionario.ler()
        listaBi = list(filter(lambda x: x.bi == bi, x))
        if len(listaBi) > 0:
            print("BI ja existe.")
        else:
            if len(bi) == 13 and len(telefone) >= 9 and len(telefone) <= 12:
                DaoFuncionario.salvar(Funcionario(nome, telefone, bi, email, endereco))
                print("Funcionario cadastrado.")
            else:
                print("Digite numero de BI ou de telefone valido")
    
    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("O funcionario que deseja remover não existe.")
            return None
        
        with open("funcionarios.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.bi +"|" + i.email +"|" + i.endereco)
                arq.writelines("\n")
            print("Funcionario removido")

    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()
        if len(funcionario) == 0:
            print("Sem funcionarios")
        
        for i in funcionario:
            print(f"Nome: {i.nome}\n"
            f"Telefone: {i.telefone}\n"
            f"BI: {i.bi}\n"
            f"Email: {i.email}\n"
            f"Endereco: {i.endereco}")

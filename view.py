import controller
import os.path

def criarArquivos(*arquivos):
    for i in arquivos:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")

criarArquivos("categoria.txt", "clientes.txt", "estoque.txt", "fornecedores.txt", "funcionarios.txt", "venda.venda.txt")

if __name__ == "__main__":
    while True:
        menu = int(input("Digite 1 para acessar a categoria\n"
        "Digite 2 para acessar estoque\n"
        "Digite 3 para acessar fornecedor\n"
        "Digite 4 para acessar cliente\n"
        "Digite 5 para acessar funcionario\n"
        "Digite 6 para acessar vendas\n"
        "Digite 7 para ver produtos mais vendidos\n"
        "Digite 8 para saair\n"))

        if menu == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                "Digite 2 para remover uma categoria\n"
                "Digite 3 para alterar uma categoria\n"
                "Digite 4 para mostrar as categorias cadastradas\n"
                "Digite 5 para sair\n"))

                if decidir == 1:
                    novaCategoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastrarCategoria(novaCategoria)
                elif decidir == 2:
                    categoriaRemover = input("Digite a categoria que deseja remover\n")
                    cat.removerCategoria(categoriaRemover)
                elif decidir == 3:
                    categoriaPorAlterar = input("Digite a categoria que deseja alterar\n")
                    novaCategoria = input("Digite a nova categoria\n")
                    cat.alterarCategoria(categoriaPorAlterar, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        elif menu == 2:
            est = controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                "Digite 2 para remover um produto\n"
                "Digite 3 para alterar um produto\n"
                "Digite 4 para ver estoque\n"
                "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do produto\n")
                    preco = input("Digite o preco\n")
                    categoria = input("Digite a categoria\n")
                    quantidade = input("Digite a quantidade\n")
                    est.cadastrarEstoque(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    nome = input("Digite o produto que deseja remover")
                    est.removerProduto(nome)
                elif decidir == 3:
                    nomeAlterar = input("Digite o produto que deseja alterar\n")
                    novoNome = input("Digite o novo produto\n")
                    novoPreco = input("Digite o novo preco\n")
                    novaCategoria = input("Digite a nova categoria\n")
                    novaQuantidade = input("Digite a nova Quantidade\n")
                    est.alterarProduto(nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade)
                elif decidir ==4:
                    est.mostrarEstoque()
                else:
                    break
        
        elif menu == 3:
            cat = controller.ControllerFornecedor()
            while True:
                decidir = input("Digite 1 para cadastrar fornecedor\n"
                "Digite 2 para remover fornecedor\n"
                "Digite 3 para mostrar fornecedores\n"
                "Digite 4 para sair")

                if decidir == 1:
                    nome = input("Digite o nome do fornecedor\n")
                    telefone = input("Digite o telefone do fornecedor\n")
                    categoria = input("Digite a categoria que ele fornece")
                    cat.cadastrarFornecedor(nome, telefone, categoria)
                elif decidir == 2:
                    nome = input("Digite o nome do fornecedor que deseja remover")
                    cat.removerFornecedor(nome)
                elif decidir == 3:
                    cat.mostrarFornecedor()
                else:
                    break

        elif menu == 4:
            cat = controller.ControllerCliente()
            while True:
                decidir = input("Digite 1 para cadastrar cliente\n"
                "Digite 2 para alterar cliente\n"
                "Digite 3 para remover cliente\n"
                "Digite 4 para mostrar cliente\n"
                "Digite 5 para sair\n")

                if decidir == 1:
                    nome = input("Digite o nome do cliente")
                    telefone = input("Digite o telefone do cliente")
                    bi = input("Digite o BI do cliente")
                    email = input("Digite o email do cliente")
                    endereco = input("Digite o endereco do cliente")
                    cat.cadastrarCliente(nome, telefone, bi, email, endereco)
                elif decidir == 2:
                    nomeAlterar = input("Digite o nome do cliente que deseja alterar")
                    novoNome = input("Digite o nome do novo cliente")
                    novoTelefone = input("Digite o telefone do novo cliente")
                    novoBi = input("Digite o BI do novo cliente")
                    novoEmail = input("Digite o nome do novo cliente")
                    novoEndereco = input("Digite o endereco do novo cliente")
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoBi, novoEmail, novoEndereco)
                elif decidir == 3:
                    nome = input("Digite o nome do cliente que deseja remover")
                    cat.removerCliente(nome)
                elif decidir == 4:
                    cat.mostrarCliente()
                else:
                    break
        
        elif menu == 5:
            cat = controller.ControllerFuncionario()
            while True:
                decidir = input("Digite 1 para cadastrar funcionario\n"
                "Digite 2 para remover funcionario\n"
                "Digite 3 para mostrar funcionarios\n"
                "Digite 4 para sair")

                if decidir == 1:
                    nome = input("Digite o nome do funcionario\n")
                    telefone = input("Digite o telefone do funcionario\n")
                    bi = input("Digite o BI do funcionario\n")
                    email = input("Digite o email do funcionario\n")
                    endereco = input("Digite o endereco do funcionario\n")
                    cat.cadastrarFuncionario(nome, telefone, bi, email, endereco)
                elif decidir == 2:
                    nome = input("Digite o nome do funcionario que deseja remover")
                    cat.removerFuncionario(nome)
                elif decidir == 3:
                    cat.mostrarFuncionario()
                else:
                    break
                    
                



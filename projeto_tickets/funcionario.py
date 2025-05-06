from datetime import datetime
from db import conectar

def cadastrar_funcionario(nome, cpf):
    nome = nome.strip()
    cpf = str(cpf).strip()

    if nome == "" or cpf == "":
        print("Nome e CPF são obrigatórios.")
        return
    
    if not cpf.isdigit() or len(cpf) < 11:
        print('O CPF deve conter 11 números, sem pontos e hífens.')
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM  funcionarios WHERE cpf = %s", (cpf,))
    if cursor.fetchone():
        print('Funcionário já cadastrado com esse CPF.')
        return

    data_alteracao = datetime.now()
    cursor.execute("""
        INSERT INTO funcionarios (nome, cpf, situacao, data_alteracao)
        VALUES (%s, %s, 'A', %s)
    """, (nome, cpf, data_alteracao))
    conexao.commit()
    print('Funcionário cadastrado com sucesso!')

    cursor.close()
    conexao.close()

def editar_funcionario(id_funcionario, novo_nome=None, nova_situacao=None):
    if not id_funcionario:
        print("ID do funcionário obrigatório.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT situacao FROM funcionarios WHERE id = %s", (id_funcionario,))
    resultado = cursor.fetchone()
    if not resultado:
        print("Funcionário não encontrado.")
        return

    atual_situacao = resultado[0]

    if nova_situacao == 'I' and atual_situacao == 'A':
        pass
    elif nova_situacao not in [None, 'A', 'I']:
        print("Situação inválida. Use: 'A' ou 'I'.")
        return

    campos = []
    valores = []

    if novo_nome:
        campos.append("nome = %s")
        valores.append(novo_nome)

    if nova_situacao:
        campos.append("situacao = %s")
        valores.append(nova_situacao)

    if not campos:
        print("Nenhuma alteração fornecida.")
        return

    campos.append("data_alteracao = %s")
    valores.append(datetime.now())

    valores.append(id_funcionario)

    query = f"UPDATE funcionarios SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(query, valores)
    conexao.commit()

    print("Funcionário atualizado com sucesso.")

    cursor.close()
    conexao.close()
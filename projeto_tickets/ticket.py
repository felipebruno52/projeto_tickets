from datetime import datetime
from db import conectar

def cadastrar_ticket(id_funcionario, quantidade):
    if quantidade <= 0:
        print('Quantidade inválida, deve ser maior que 0.')
        return
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT situacao FROM funcionarios WHERE id = %s
        """, (id_funcionario,))
    resultado = cursor.fetchone()

    if not resultado:
        print('Funcionário não encontrado.')
        return
    
    if resultado[0] != 'A':
        print('Funcionário está inativo.')
        return
    
    data_entrega = datetime.now()
    cursor.execute("""
    INSERT INTO tickets_entregues (id_funcionario, quantidade, data_entrega, situacao)
    VALUES (%s, %s, CURDATE(), 'A')
    """, (id_funcionario, quantidade))


    conexao.commit()
    print('Ticket cadastrado com sucesso.')
    cursor.close()
    conexao.close()

def editar_ticket(id_ticket, nova_quantidade=None, nova_situacao=None):
    if not id_ticket:
        print('ID do ticket é obrigatório.')
        return
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tickets_entregues WHERE id = %s", (id_ticket,))
    resultado = cursor.fetchone()

    if not resultado:
        print('Ticket não encontrado')
        return
    
    campos = []
    valores = []

    if nova_quantidade is not None:
        if nova_quantidade <= 0:
            print('Quantidade inválida.')
            return
        campos.append("quantidade = %s")
        valores.append(nova_quantidade)
    
    if nova_situacao:
        if nova_situacao not in ['A', 'I']:
            print("Situação inválida. Use: 'A' ou 'I'.")
            return
        campos.append("situacao = %s")
        valores.append(nova_situacao)
    
    if not campos:
        print('Nenhuma alteração fornecida.')
        return
    
    valores.append(id_ticket)
    query = f"UPDATE tickets_entregues SET {', '.join(campos)} WHERE id = %s"

    cursor.execute(query, valores)
    conexao.commit()
    print('Ticket atualizado.')
    
    cursor.close()
    conexao.close()

def emitir_relatorio_funcionario(id_funcionario, data_inicio, data_fim):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, cpf FROM funcionarios WHERE id = %s
    """, (id_funcionario,))
    funcionario = cursor.fetchone()

    if not funcionario:
        print("Funcionário não encontrado.")
        return

    print(f"\n📄 Relatório de Tickets – Funcionário: {funcionario[0]} (CPF: {funcionario[1]})")
    print(f"📆 Período: {data_inicio} a {data_fim}\n")

    cursor.execute("""
        SELECT id, data_entrega, quantidade, situacao
        FROM tickets_entregues
        WHERE id_funcionario = %s AND data_entrega BETWEEN %s AND %s
        ORDER BY data_entrega
    """, (id_funcionario, data_inicio, data_fim))

    tickets = cursor.fetchall()

    if not tickets:
        print("Nenhum ticket encontrado no período.")
    else:
        total_tickets = 0
        total_unidades = 0

        print("ID Ticket | Data Entrega | Quantidade | Situação")
        print("-----------------------------------------------")

        for ticket in tickets:
            print(f"{ticket[0]:<9} | {ticket[1].strftime('%d/%m/%Y')}   | {ticket[2]:<9} | {'Ativo' if ticket[3] == 'A' else 'Inativo'}")
            total_tickets += 1
            total_unidades += ticket[2]

        print("\nTotal de tickets entregues no período:", total_tickets)
        print("Total de unidades:", total_unidades)

    cursor.close()
    conexao.close()

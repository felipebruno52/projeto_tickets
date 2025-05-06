from db import conectar

def gerar_relatorio(data_inicio, data_fim):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT f.nome, SUM(t.quantidade) AS total_tickets
        FROM tickets_entregues t
        JOIN funcionarios f ON f.id = t.id_funcionario
        WHERE t.data_entrega BETWEEN %s AND %s
        GROUP BY f.id, f.nome
    """
    cursor.execute(query, (data_inicio, data_fim))
    resultados = cursor.fetchall()

    total_geral = 0
    print("\n📊 RELATÓRIO DE TICKETS")
    print(f"De {data_inicio} até {data_fim}")
    print("-" * 40)

    for linha in resultados:
        print(f"Funcionário: {linha['nome']} - Total de Tickets: {linha['total_tickets']}")
        total_geral += linha['total_tickets']

    print("-" * 40)
    print(f"🎯 Total Geral de Tickets: {total_geral}\n")

    cursor.close()
    conexao.close()
    
    return resultados
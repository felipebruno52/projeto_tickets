from funcionario import cadastrar_funcionario, editar_funcionario
from ticket import cadastrar_ticket, editar_ticket
from relatorio import gerar_relatorio

import csv
import json
import pandas as pd  # pip install pandas
from openpyxl.workbook import Workbook # pip install openpyxl

def exportar_relatorio(report):
    """
    Pergunta o formato e exporta o relatório.
    """
    if not report:
        print("⚠️  Não há dados no relatório para exportar.")
        return

    print("\nComo deseja exportar o relatório?")
    print("1. Excel")
    print("2. CSV")
    print("3. JSON")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        df = pd.DataFrame(report)
        df.to_excel('relatorio.xlsx', index=False)
        print("✅ Relatório exportado para relatorio.xlsx")

    elif escolha == '2':
        with open('relatorio.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=report[0].keys())
            writer.writeheader()
            writer.writerows(report)
        print("✅ Relatório exportado para relatorio.csv")

    elif escolha == '3':
        with open('relatorio.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)
        print("✅ Relatório exportado para relatorio.json")

    else:
        print("❌ Opção inválida — nenhum arquivo foi gerado.")


def menu():
    while True:
        print("\n==== MENU ====")
        print("1. Cadastrar funcionário")
        print("2. Editar funcionário")
        print("3. Cadastrar ticket")
        print("4. Editar ticket")
        print("5. Gerar relatório")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cadastrar_funcionario(nome, cpf)

        elif opcao == '2':
            id_func = int(input("ID do funcionário: "))
            nome = input("Novo nome (ou deixe vazio): ")
            situacao = input("Nova situação (A/I ou deixe vazio): ")
            editar_funcionario(id_func,
                               nome if nome else None,
                               situacao if situacao else None)

        elif opcao == '3':
            id_func = int(input("ID do funcionário: "))
            qtd = int(input("Quantidade de tickets: "))
            cadastrar_ticket(id_func, qtd)

        elif opcao == '4':
            id_ticket = int(input("ID do ticket: "))
            qtd = input("Nova quantidade (ou deixe vazio): ")
            sit = input("Nova situação (A/I ou deixe vazio): ")
            editar_ticket(id_ticket,
                          int(qtd) if qtd else None,
                          sit if sit else None)

        elif opcao == '5':
            data_inicio = input("Data início (YYYY-MM-DD): ")
            data_fim    = input("Data fim    (YYYY-MM-DD): ")
            report = gerar_relatorio(data_inicio, data_fim)
            exportar_relatorio(report)

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
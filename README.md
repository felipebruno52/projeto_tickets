# Sistema de Tickets
Este repositório contém um sistema simples para gerenciar e gerar relatórios de tickets. Ele inclui:

- Conexão com o banco de dados MySQL (**db.py**)
- Cadastro e edição de funcionários (**funcionario.py**)
- Cadastro e edição de tickets (**ticket.py**)
- Geração de relatórios e exportação em Excel, CSV ou JSON (**relatorio.py e menu.py**)


# Pré-requisitos

- MySQL Server (local ou remoto)
- Bibliotecas Python necessárias:

  ```bash
  pip install mysql-connector-python pandas
  pip install openpyxl

# Configuração do Banco de Dados

**1. Acesse seu console MySQL e execute:**

```sql
CREATE DATABASE sistema_tickets;
USE sistema_tickets;

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    situacao CHAR(1) NOT NULL CHECK (situacao IN ('A', 'I')),
    data_alteracao DATETIME NOT NULL
);

CREATE TABLE tickets_entregues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_funcionario INT NOT NULL,
    quantidade INT NOT NULL,
    situacao CHAR(1) NOT NULL CHECK (situacao IN ('A', 'I')),
    data_entrega DATETIME NOT NULL,
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
);
```
**2. Atualize o arquivo db.py com as credenciais do seu servidor MySQL:**

```sql
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_tickets"
    )
```

# Estrutura dos Módulos
- **db.py**: Implementa a função `conectar()` para criar a conexão com o banco de dados.
- **funcionario.py:**
    - `cadastrar_funcionario(nome, cpf)`
    - `editar_funcionario(id, novo_nome=None, nova_situacao=None)`
    - `emitir_relatorio_funcionario(...)` (OPCIONAL)
- **relatorio.py**:
  - `gerar_relatorio(data_inicio, data_fim)` retorna uma lista de dicionários com os totais por funcionário
- **menu.py:** Interface de comando com as seguintes opções:
  
    1. Cadastrar funcionário
    2. Editar funcionário
    3. Cadastrar ticket
    4. Editar ticket
    5. Gerar relatório (sendo possível exportar)
    6. Sair


# Uso
**1.** Navegue até a pasta do projeto
```bash
cd caminho/para/projeto
```

**2.** Execute no terminal:
```bash
python main.py
```

**3.** No menu, escolha a opção `5` para gerar o relatório.
  - Informe a data de início e fim no formato: `YYYY-MM-DD`
  - Após visualizar, escolha como exportar:
      - `1` = Excel (.xlsx)
      - `2` = CSV (.csv)
      - `3` = JSON (.json)


## Notas sobre o projeto

> **Atenção:** Este é um projeto pessoal e está em fase inicial.

### Sugestões para melhoria:

- **Melhoria de interface:** A ideia é criar uma interface, para que o usuário consiga interagir com o sistema de forma mais simples e prática, sem precisar usar o console. O objetivo é deixar tudo mais fácil.
- **Novas funcionalidades:** Podemos incluir opções como "Excluir funcionário", "Visualizar histórico de tickets" ou "Gerenciar relatórios por setor"
- **Suporte para Multiplos formatos:** Atualmente, os relatórios só podem ser exportados em: .XLSX, .CSV e .JSON. Novos formatos, como PDF, poderão ser implementados.
- **Feedback:** Conto muito com o feedback de vocês para que eu possa melhorar! 






  

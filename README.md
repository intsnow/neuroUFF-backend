# NeuroUFF - Backend

**Versão:** 1.0.0 (Stable)
**Arquitetura:** MVC (Model-View-Controller)

> 📌 **Histórico de Refatoração:**
> Para detalhes sobre a evolução de versões do projeto (de script monolítico para arquitetura modular), consulte o [CHANGELOG.md](./CHANGELOG.md).

---

## 📋 Visão Geral

Backend desenvolvido em Python para gerenciamento de dados acadêmicos. O projeto marca a transição de scripts de automação isolados para uma aplicação estruturada com princípios de **Engenharia de Software**.

O foco desta versão v1.0.0 foi a **refatoração arquitetural**: o código foi desacoplado em camadas lógicas (MVC), garantindo que as regras de negócio (`neurouff/sistema.py`) independam da interface de usuário ou do mecanismo de persistência.

## 🛠️ Tecnologias e Padrões

A implementação prioriza a biblioteca padrão do Python para demonstrar domínio dos fundamentos da linguagem antes da adoção de frameworks externos.

* **Linguagem:** Python 3.10+ (Com o uso extensivo de `Type Hints` e `Dataclasses`).
* **Persistência:** SQLite3 (Nativo).
* **Design Pattern:** MVC.

## 🏗️ Decisões de Arquitetura e Implementação

Abaixo estão as principais decisões técnicas tomadas para garantir segurança e manutenibilidade:

### 1. Segurança e Integridade de Dados
* **Prepared Statements:** Todas as consultas SQL utilizam *placeholders* (`?`) em vez de formatação de strings (`f-strings`), mitigando possíveis vulnerabilidades de **SQL Injection**.
* **Validação de Entrada:** Implementação de um *Factory Method* (`from_dict`) no Model, que filtra, sanatiza e valida os dados brutos antes da instanciação do objeto.

### 2. Gerenciamento de Recursos
* **Context Managers:** A conexão com o banco de dados é gerenciada via protocolo `with`, garantindo o fechamento atômico da conexão após cada transação, prevenindo *Memory Leaks* e erros de *Database Locked*.

### 3. Legibilidade e Manutenção
* **Row Factory Customizada:** O driver do SQLite foi configurado para retornar objetos do tipo dicionário (`sqlite3.Row`), substituindo o acesso por índices/posição propenso a erros (ex: `row[2]`) pelo acesso nominal (ex: `row['email']`), aumentando a clareza do código.

## 📂 Estrutura do Repositório

O código fonte foi organizado no pacote `neurouff` para isolar o namespace da aplicação.

```text
neurouff-backend/
├── neurouff/             # Core Package
│   ├── database.py       # Data Access Object (DAO) e Conexão
│   ├── sistema.py        # Controller/Service (Regras de Negócio)
│   ├── user.py           # Model (Schema e Serialização)
│   └── ui_view.py        # View (Interface CLI)
├── run.py                # Ponto de Entrada da aplicação
├── neuro_uff.db          # Arquivo de banco de dados (Auto-gerado)
└── CHANGELOG.md          # Registro de alterações e versões

```

## 🚀 Como Rodar

1. **Clone o repositório:**

```bash
git clone https://github.com/intsnow/neurouff-backend.git
cd neurouff-backend

```

2. **Execute o projeto:**
Necessário Python 3.10 ou superior.

```bash
python run.py

```

*Ao rodar, o sistema cria o banco de dados `neuro_uff.db` automaticamente.*

---

*Projeto de estudo focado em boas práticas de desenvolvimento backend.*

```

```

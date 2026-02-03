# Changelog: NeuroUFF Backend

Histórico de evolução, refatoração e decisões de arquitetura do projeto.

---

## [v1.0.0] - Versão Estável (Modular & Typed)
**Data:** 03/02/2026
**Status:** Código modularizado em pacote, com persistência segura e pronto para a API Flask.

### 🏗️ Infraestrutura & Organização

* **Python Packaging:** Reestruturei os arquivos soltos para dentro de uma pasta `neurouff`.
    > **Motivo:** Diferentemente das versões anteriores, em vista do crescimento desordenado do projeto, agora consigo fazer importações absolutas e mantenho o diretório raiz limpo para o servidor Web.

* **Modularização Real (MVC):** Desacoplamento total das camadas.
    * A classe `Sistema` não conhece mais a `UI_View`. Ela apenas processa dados e retorna objetos, provando que a lógica de negócio independe da interface (seja Terminal ou Web).

### 💾 Banco de Dados (Database.py)

* **Segurança (SQL Injection):** Substituição total das concatenações de strings inseguras por **Prepared Statements** (placeholders `?`).
* **Gestão de Recursos (Context Managers):** Refatorei os métodos de acesso para usar estritamente `with self.start_conn()`.
    * **Antes:** Conexões manuais no `__init__` que podiam causar Memory Leaks ou Database Locks.
    * **Agora:** O Python abre e fecha a conexão atomicamente a cada transação, garantindo estabilidade.
* **Mapeamento de Resultados:** Configurado-se o `row_factory` do SQLite, com o acesso às colunas pelo nome (`row['email']`) em vez de índices numéricos, erros triviais de contagem serão evitados.

### 🧠 Modelagem de Dados (User.py)

* **Uso de Dataclasses:** Migração da classe `User` para `@dataclass`. Ganho de tipagem estática, reduzindo a verbosidade do código.
* **Sanitização (`from_dict`):** Criei um Factory Method que filtra os dados de entrada: Se o dicionário tiver campos inválidos, o método os descarta antes de criar o objeto.
* **Serialização (`to_dict`):** Substituição total do uso de `vars()` por um método integrado diretamente ao `User.py`, dedicado a preparar o objeto para o banco (e.g.: remoção do ID `None` para ativar o auto-incremento).

### 🖥️ Interface (UI_View.py)

* **Código Limpo:** Substituí loops baseados em índice (`range`) por iteração direta (`.items()`), tornando a leitura e manutenção da View muito mais simples e direta.

---

## [v0.5.0] - Refatoração MVC (Model-View-Controller)
**Status:** Separação lógica, mas com gerenciamento de recursos manual.

### Arquitetura
* **Desacoplamento Inicial:** Quebra do script único (`main.py`) em módulos de responsabilidade única (`ui_view`, `sistema`, `database`).
* **Integridade de Dados:** Adicionei a constraint `UNIQUE` no campo email. Agora, tenho uma dupla verificação: no código Python e na estrutura física do Banco de Dados.

---

## [v0.1.0] - Legado (Proof of Concept)
**Status:** Funcional, mas monolítico e inseguro.

### Características Antigas
* **Conexão Persistente:** O banco mantinha a conexão aberta indefinidamente (Risco alto de travamento).
* **Acoplamento Forte:** As regras de negócio continham `print()`, impedindo o reuso do código.
* **Tratamento de Erros:** Usava exceções genéricas que mascaravam os erros reais do SQL.
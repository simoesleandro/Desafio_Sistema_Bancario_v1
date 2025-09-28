# 🏦 Sistema Bancário com POO em Python

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Conclu%C3%ADdo-brightgreen.svg)

## 🎯 Contexto do Projeto

Este projeto foi desenvolvido como resposta ao **Desafio de Código "Modelando um Sistema Bancário em Python"** do bootcamp **Suzano - Python Developer #2**. O principal objetivo é aplicar na prática os conceitos de Programação Orientada a Objetos (POO) para construir um sistema funcional e bem estruturado.

## 💡 Conceitos de POO Aplicados

Para a construção deste sistema, foram aplicados os seguintes pilares e conceitos de POO:

-   **Abstração:** Criação de classes como `Conta`, `Cliente` e `Transacao` que representam entidades do mundo real de forma simplificada.
-   **Encapsulamento:** Proteção dos atributos das classes (como `_saldo` e `_agencia`), expondo o acesso a eles apenas através de métodos públicos (`sacar()`, `depositar()`, etc.).
-   **Herança:** Utilização de uma classe base (`Cliente`) para criar classes mais específicas (`PessoaFisica`), aproveitando e estendendo seu comportamento.
-   **Composição:** A classe `Conta` é "composta por" um objeto da classe `Historico`, demonstrando uma relação "tem-um" forte entre elas.

## ✨ Funcionalidades

-   👤 **Gestão de Clientes:** Cadastro de clientes do tipo Pessoa Física.
-   💳 **Criação de Contas:** Abertura de contas correntes vinculadas a um cliente.
-   💰 **Operações Financeiras:**
    -   **Depósitos:** Com validação para aceitar apenas valores positivos.
    -   **Saques:** Com verificação de saldo e controle de limite de saques diários.
-   📜 **Histórico de Transações:** Registro detalhado de todas as operações realizadas.

## 🏗️ Estrutura do Projeto

O projeto foi modelado utilizando os seguintes componentes principais:

| Classe          | Herança         | Responsabilidade                                            |
| --------------- | --------------- | ----------------------------------------------------------- |
| `Cliente`       | -               | Gerencia os dados do usuário e suas contas.                 |
| `PessoaFisica`  | `Cliente`       | Especializa `Cliente` com atributos como CPF e data de nascimento. |
| `Conta`         | -               | Classe base que define a estrutura de uma conta bancária.   |
| `ContaCorrente` | `Conta`         | Implementa regras específicas, como limite de saques.       |
| `Historico`     | -               | Armazena e gerencia a lista de transações de uma conta.     |
| `Transacao`     | (Abstrata)      | Interface para as operações de depósito e saque.            |
| `Deposito`      | `Transacao`     | Representa a operação de depósito.                          |
| `Saque`         | `Transacao`     | Representa a operação de saque.                             |

## 🚀 Começando

Siga as instruções abaixo para executar o projeto em seu ambiente local.

### Pré-requisitos

-   Python 3.7 ou superior.

### Instalação

1.  Clone o repositório:
    ```sh
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  Navegue até o diretório do projeto:
    ```sh
    cd seu-repositorio
    ```

### 👨‍💻 Exemplo de Uso

```python
# Crie um cliente
cliente_maria = PessoaFisica(nome="Maria da Silva", data_nascimento="01/01/1990", cpf="123.456.789-00", endereco="Rua A, 123")

# Crie uma conta para o cliente
conta_maria = ContaCorrente.nova_conta(cliente=cliente_maria, numero=1001)

# Realize operações
conta_maria.depositar(1000)
conta_maria.sacar(200)

# Exiba o extrato
print("================ EXTRATO ================")
for transacao in conta_maria.historico.transacoes:
    print(f"{transacao['tipo']}:\t R$ {transacao['valor']:.2f}")

print(f"\nSaldo atual:\t R$ {conta_maria.saldo:.2f}")
print("=======================================")
📝 Licença
Este projeto está sob a licença MIT.

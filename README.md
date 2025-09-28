# 🏦 Sistema Bancário em Python com POO

<p align="left">
  <a href="https://www.python.org" target="_blank">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  </a>
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status do Projeto"/>
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-blue?style=for-the-badge" alt="Licença MIT"/>
</p>

## 🎯 Sobre o Projeto

Este projeto é a minha implementação do desafio "Modelando um Sistema Bancário em Python" proposto no bootcamp **Suzano - Python Developer \#2**. O objetivo foi criar, a partir do zero, um sistema bancário funcional utilizando os princípios da **Programação Orientada a Objetos (POO)**.

Foi uma jornada incrível de aprendizado, onde pude solidificar conceitos essenciais e transformar teoria em código funcional. Mais do que apenas um sistema, este projeto representa um passo importante na minha evolução como desenvolvedor.

## ✨ Funcionalidades Principais

O sistema oferece uma experiência de terminal interativa com as seguintes operações:

  * **👤 Gestão de Clientes:** Cadastrar novos usuários (Pessoas Físicas).
  * **💳 Criação de Contas:** Abrir contas correntes vinculadas a um cliente.
  * **💰 Transações Seguras:**
      * **Depositar:** Adicionar valores à conta (apenas valores positivos).
      * **Sacar:** Retirar dinheiro, com validação de saldo, limite de R$ 500 por saque e máximo de 3 saques diários.
  * **📜 Extrato Detalhado:** Visualizar o histórico completo de transações, incluindo data e hora.
  * \*\* robustez:\*\* Tratamento de entradas inválidas para garantir a estabilidade do programa.

## 💡 Conceitos de POO Aplicados

A estrutura do projeto foi pensada para ser modular e escalável, aplicando os pilares da POO:

  * **Abstração:** Modelagem de entidades do mundo real (`Conta`, `Cliente`) em classes.
  * **Encapsulamento:** Proteção dos dados, como o saldo, garantindo que o acesso seja feito de forma controlada.
  * **Herança:** Criação de classes mais específicas a partir de uma base (`ContaCorrente` herda de `Conta`).
  * **Composição:** Construção de classes complexas a partir de outras mais simples (`Conta` "tem um" `Historico`).

## 🏗️ Estrutura das Classes

A organização das classes foi um ponto central no desenvolvimento. A tabela abaixo ilustra a responsabilidade de cada uma:

| Classe         | Herança    | Responsabilidade Principal                                      |
| :------------- | :--------- | :-------------------------------------------------------------- |
| `Cliente`      | -          | Gerencia os dados do usuário e sua lista de contas.             |
| `PessoaFisica` | `Cliente`  | Especializa `Cliente` com atributos como CPF e data de nascimento. |
| `Conta`        | -          | Classe base que define a estrutura de uma conta bancária.       |
| `ContaCorrente`| `Conta`    | Implementa regras de negócio específicas, como limites de saque. |
| `Historico`    | -          | Armazena e gerencia a lista de transações de uma conta.         |
| `Transacao`    | (Abstrata) | Define a interface para as operações de depósito e saque.       |
| `Deposito`     | `Transacao`| Representa a operação de depósito, registrando o valor.         |
| `Saque`        | `Transacao`| Representa a operação de saque, validando limites e saldo.      |

## 🚀 Como Executar o Projeto

Para testar o sistema em sua máquina, siga os passos abaixo.

### Pré-requisitos

  * **Python 3.7** ou superior.

### Passos

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/simoesleandro/Desafio_Sistema_Bancario_v1.git
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd Desafio_Sistema_Bancario_v1
    ```

3.  **Execute o script principal:**

    ```bash
    python Desafio_v1.py
    ```

Pronto\! Agora é só seguir as instruções do menu interativo no terminal.

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para explorar, modificar e usar como referência para seus estudos\!

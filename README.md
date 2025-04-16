# Teste Selenium Prova

Este repositório contém os scripts e a documentação relacionados ao processo de automação de testes utilizando **Selenium** em **Python** e **Node.js**, além de testes de desempenho feitos com **JMeter**.

## Descrição 

O objetivo deste trabalho foi criar automações para testes de login em páginas de um site específico utilizando o Selenium, e realizar testes de desempenho com o JMeter para avaliar o comportamento e a carga do sistema.

### Tecnologias Utilizadas: 

- **Python** com Selenium  
- **Node.js** com Selenium WebDriver 
- **JMeter** para testes de desempenho 

---

## Scripts

### 1. **Automação com Selenium - Python** 
O script em Python realiza o login na página e valida o redirecionamento após o login.

- **Funcionalidade**: Acesse a página de login, insira o nome de usuário e senha de forma simulada (digitando lentamente), e valida se houve o redirecionamento correto após o login.
- **Tecnologia**: Python, Selenium

**Arquivo**: [main.py](./main.py)

### 2. **Automação com Selenium - Node.js** 
O script em Node.js realiza a mesma automação do script em Python, mas utilizando Selenium WebDriver no ambiente JavaScript.

- **Funcionalidade**: Acesse a página de login, insira o nome de usuário e senha de forma simulada (digitando lentamente), e valida se houve o redirecionamento correto após o login.
- **Tecnologia**: Node.js, Selenium WebDriver

**Arquivo**: [node.js](./node.js)

---

## Testes de Desempenho com JMeter 

Os testes de desempenho foram realizados utilizando o **JMeter**. Através dele, foi possível realizar testes de carga nas páginas de login do site.

- **Funcionalidade**: Verificar a performance da página de login em dois cenários diferentes de tráfego de usuários.
- **Tecnologia**: JMeter

**Arquivo de Configuração**: [jmeter_test.jmx](./jmeter_test.jmx)

---

## Vídeos

Aqui estão os vídeos que demonstram o funcionamento dos testes:

1. **Teste de Automação com Python e Node.js**:  

https://github.com/user-attachments/assets/689b1357-b448-4192-b9f1-bd8673361bc5


2. **Teste de Desempenho com JMeter**: 
   
https://github.com/user-attachments/assets/58ab5162-9ecf-41eb-8315-d32972140c49


---

## Como Executar ⚙️
 
### 1. **Instalar Dependências**

#### **Python**

Para executar o script Python, certifique-se de ter o Python e as dependências instaladas:

```bash
pip install selenium webdriver-manager

```
### 2. **Dependências para Node.js** (Selenium WebDriver)

Se você ainda não tem o **Node.js** instalado, baixe o [Node.js aqui](https://nodejs.org/).

Depois, para instalar as dependências necessárias no Node.js, crie um arquivo `package.json` caso não tenha, e então instale o **selenium-webdriver**:

```bash
npm init -y
npm install selenium-webdriver

```

## Dupla da Prova 

A atividade foi realizada pela dupla:

- **Murillo Daigder** 
- **Murilo Cavazzana** 

---

**Murillo Daigder**  
<img src="https://github.com/user-attachments/assets/37b2b376-ddad-4928-a435-3543671ee590" width="100" alt="Murillo Daigder"/>

**Murilo Cavazzana**  
<img src="https://github.com/user-attachments/assets/45b22182-717b-42ea-9676-a36c9551455f" width="100" alt="Murilo Cavazzana"/>




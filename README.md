# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github)

![Energia](https://img.shields.io/badge/Energia-Consumo%20El%C3%A9trico-yellow)

![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-green)

## 📌 Sobre o projeto

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em Python que permite estimar o consumo mensal de energia elétrica de um aparelho.

O sistema solicita o nome do aparelho, sua potência em watts e o tempo médio de utilização diária. Com essas informações, calcula o consumo estimado em **kWh por mês**, apresenta uma estimativa de custo e classifica o nível de consumo.

Além disso, o sistema apresenta uma **dica de economia de energia** de acordo com o consumo calculado. 💡

## 🎯 Objetivo

O objetivo do projeto é facilitar a compreensão do consumo de energia elétrica dos aparelhos, ajudar o usuário a ter uma estimativa do valor gasto mensalmente e incentivar o uso consciente da energia.

## 🛠️ Tecnologias utilizadas

* 🐍 Python

* 💻 Visual Studio Code

* 🐙 Git e GitHub

## 🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000
```

Onde:

* **potência** = potência do aparelho em watts (W)

* **horasDia** = quantidade média de horas de uso por dia

* **30** = quantidade estimada de dias no mês

* **1000** = conversão de watts para quilowatts

O custo estimado é calculado utilizando o valor fixo de **R$ 0,75 por kWh**.

```text
custoMensal = consumoMensal × 0,75
```

## 📊 Classificação do consumo

O programa também classifica o consumo mensal do aparelho em três níveis:

* 🟢 **Baixo** = até 30 kWh/mês

* 🟡 **Moderado** = acima de 30 até 100 kWh/mês

* 🔴 **Alto** = acima de 100 kWh/mês

Essa classificação é realizada por meio de estruturas de decisão `if`, `elif` e `else`.

## 💡 Dicas de economia

Após classificar o consumo, o programa apresenta uma dica de acordo com o resultado:

* 🟢 **Baixo:** o sistema incentiva o usuário a continuar utilizando o aparelho de forma consciente.

* 🟡 **Moderado:** o sistema recomenda reduzir algumas horas de uso para economizar energia.

* 🔴 **Alto:** o sistema alerta sobre o consumo elevado e recomenda reduzir o tempo de utilização.

## 🧩 Funções utilizadas

O programa foi organizado utilizando funções para deixar o código mais estruturado e facilitar sua compreensão.

### `calcular_consumo()`

Responsável por calcular o consumo mensal de energia elétrica.

```python
def calcular_consumo(potencia, horas_dia):
    return (potencia * horas_dia * 30) / 1000
```

### `classificar_consumo()`

Responsável por analisar o consumo calculado e informar se ele é **baixo, moderado ou alto**.

```python
def classificar_consumo(consumo):
    if consumo <= 30:
        return "🟢 Baixo"
    elif consumo <= 100:
        return "🟡 Moderado"
    else:
        return "🔴 Alto"
```

### `mostrar_dica()`

Responsável por apresentar uma dica de economia de energia de acordo com o consumo do aparelho.

```python
def mostrar_dica(consumo):
    if consumo <= 30:
        return "💡 O consumo está baixo. Continue usando o aparelho de forma consciente!"
    elif consumo <= 100:
        return "💡 Dica: tente reduzir algumas horas de uso para economizar energia."
    else:
        return "⚠️ O consumo está alto. Reduzir o tempo de utilização pode gerar uma boa economia."
```

## ▶️ Como executar

### 1. Instale o Python

Certifique-se de que o Python está instalado no computador.

### 2. Abra o projeto no VS Code

Abra a pasta:

```text
projetos/consumo-energia
```

### 3. Execute o programa

No terminal do VS Code, utilize:

```bash
python app.py
```

Em alguns computadores, pode ser necessário utilizar:

```bash
python3 app.py
```

### 4. Informe os dados

O programa solicitará:

1. Nome do aparelho;

2. Potência em watts;

3. Tempo médio de uso diário.

Após inserir os dados, o sistema apresentará o consumo mensal estimado, o custo aproximado, a classificação do consumo e uma dica de economia.

## 💡 Exemplo

```text
======================================
   CALCULADORA DE CONSUMO ELÉTRICO
======================================

Digite o nome do aparelho: Geladeira

Digite a potência do aparelho em watts (W): 100

Digite o tempo médio de uso diário em horas: 15

======================================
          RESULTADO
======================================

Aparelho: Geladeira
Potência: 100 W
Uso diário: 15.0 horas
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75
Classificação: 🟡 Moderado

💡 Dica: tente reduzir algumas horas de uso para economizar energia.

======================================
```

## 📂 Estrutura do projeto

```text
consumo-energia/

├── app.py

└── README.md
```

## 👨‍💻 Autor

Autor Rodrigo D. - Projeto desenvolvido como atividade de Técnico em Desenvolvimento de Sistemas pela Etec.

---

⚡ **Pequenas atitudes podem ajudar a entender e reduzir o consumo de energia!**

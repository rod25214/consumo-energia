# ⚡ Calculadora Inteligente de Consumo Elétrico

VALOR_KWH = 0.75


def calcular_consumo(potencia, horas_dia):
    return (potencia * horas_dia * 30) / 1000


def classificar_consumo(consumo):
    if consumo <= 30:
        return "🟢 Baixo"
    elif consumo <= 100:
        return "🟡 Moderado"
    else:
        return "🔴 Alto"


def mostrar_dica(consumo):
    if consumo <= 30:
        return "💡 O consumo está baixo. Continue usando o aparelho de forma consciente!"
    elif consumo <= 100:
        return "💡 Dica: tente reduzir algumas horas de uso para economizar energia."
    else:
        return "⚠️ O consumo está alto. Reduzir o tempo de utilização pode gerar uma boa economia."


# Entrada de dados
print("=" * 50)
print("⚡ CALCULADORA INTELIGENTE DE CONSUMO ELÉTRICO")
print("=" * 50)

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculos
consumo = calcular_consumo(potencia, horas_dia)
custo = consumo * VALOR_KWH
classificacao = classificar_consumo(consumo)
dica = mostrar_dica(consumo)

# Resultado com dicas e com a classificação 
print("\n" + "=" * 50)
print("📊 RESULTADO")
print("=" * 50)

print(f"Aparelho: {aparelho}")
print(f"Potência: {potencia:.0f} W")
print(f"Uso diário: {horas_dia:.1f} horas")
print(f"Consumo estimado: {consumo:.2f} kWh/mês")
print(f"💰 Custo estimado: R$ {custo:.2f}")
print(f"Classificação: {classificacao}")
print(f"\n{dica}")

print("=" * 50)

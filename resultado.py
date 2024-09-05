import json

# 2) Função para verificar se um número pertence à sequência de Fibonacci
def fibonacci(n):
    # Inicializando a sequência com os dois primeiros números (0 e 1)
    fib_sequence = [0, 1]
    
    # Continuar gerando a sequência até o último valor ser maior ou igual ao número fornecido
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Verificar se o número informado está na sequência gerada
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


# 3) Cálculos de faturamento diário de uma distribuidora
def faturamento_diario(faturamento_mensal_json):
    # Carregar o JSON
    faturamento_mensal = json.loads(faturamento_mensal_json)
    faturamentos = faturamento_mensal["dias"]

    # Remover dias com faturamento 0
    faturamentos_validos = [f for f in faturamentos if f > 0]

    # Menor e maior valor de faturamento
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    # Cálculo da média mensal
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

    # Dias com faturamento acima da média
    dias_acima_da_media = len([f for f in faturamentos_validos if f > media_mensal])

    # Resultados
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }


# 4) Percentual de representação de faturamento por estado
def percentual_faturamento_por_estado(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())

    # Calculando o percentual de representação de cada estado
    percentuais = {}
    for estado, valor in faturamento_estados.items():
        percentuais[estado] = (valor / total_faturamento) * 100
    
    return percentuais


# 5) Função para inverter uma string sem usar funções prontas
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida


# Executando e testando as funções

# 2) Teste da função de Fibonacci
numero_fibonacci = 21
print(fibonacci(numero_fibonacci))  # Exemplo de número pertencente à sequência

# 3) Teste da função de faturamento diário
faturamento_mensal_json = '''
{
    "dias": [0, 1500, 2200, 0, 1850, 1750, 0, 2100, 2000, 1800, 1700, 0, 0, 0, 2300, 2600, 2400, 0, 0, 1800, 1900, 0, 0, 0, 2200, 2000, 0, 1900, 2300, 2100, 2600]
}
'''
resultado_faturamento = faturamento_diario(faturamento_mensal_json)
print(f"Menor faturamento: R${resultado_faturamento['menor_faturamento']}")
print(f"Maior faturamento: R${resultado_faturamento['maior_faturamento']}")
print(f"Dias com faturamento acima da média: {resultado_faturamento['dias_acima_da_media']}")

# 4) Teste da função de percentual por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
percentuais = percentual_faturamento_por_estado(faturamento_estados)
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# 5) Teste da função de inversão de string
string_para_inverter = "Exemplo"
print(f"String invertida: {inverter_string(string_para_inverter)}")

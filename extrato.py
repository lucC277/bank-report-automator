# ============================================================
#  extrato.py — Lê um CSV de transações e imprime formatado
# ============================================================

# "import" traz uma biblioteca pronta para usar
# "csv" já vem com o Python — não precisa instalar nada
import csv

# ── PASSO 1: ABRIR O ARQUIVO CSV ─────────────────────────────
#
# open("nome_do_arquivo", "r") abre o arquivo para leitura
# encoding="utf-8" garante que acentos (ã, é, ç) aparecem certo
# "with" garante que o arquivo é fechado automaticamente no final

with open("transacoes.csv", "r", encoding="utf-8") as arquivo:

    # csv.DictReader lê cada linha como um dicionário
    # Ex: {"data": "2026-03-01", "descricao": "Salário", "valor": "3500.00"}
    # Assim você acessa pelo nome da coluna, não pelo número
    leitor = csv.DictReader(arquivo)

    # ── PASSO 2: GUARDAR OS DADOS EM UMA LISTA ───────────────
    #
    # Criamos uma lista vazia e vamos preenchendo com cada linha
    transacoes = []

    # "for linha in leitor" percorre cada linha do CSV
    for linha in leitor:

        # linha["valor"] vem como texto "89.90"
        # float(...) converte para número 89.90
        # Sem isso não conseguimos fazer cálculos
        linha["valor"] = float(linha["valor"])

        # .append() adiciona a linha na nossa lista
        transacoes.append(linha)


# ── PASSO 3: IMPRIMIR O CABEÇALHO DO EXTRATO ────────────────

print("=" * 62)
print(f"{'EXTRATO DE TRANSAÇÕES — MARÇO 2026':^62}")
print("=" * 62)
print(f"{'DATA':<12} {'DESCRIÇÃO':<22} {'CATEGORIA':<14} {'VALOR':>10}")
print("-" * 62)


# ── PASSO 4: IMPRIMIR CADA TRANSAÇÃO ────────────────────────
#
# Percorremos a lista de transações com for
# Para cada transação, formatamos e imprimimos uma linha

for t in transacoes:

    # Pegamos cada campo pelo nome da coluna
    data      = t["data"]
    descricao = t["descricao"]
    categoria = t["categoria"]
    valor     = t["valor"]
    tipo      = t["tipo"]

    # Se for saída, mostra com sinal negativo e cor diferente
    # Se for entrada, mostra com sinal positivo
    if tipo == "saida":
        valor_fmt = f"-R$ {valor:>7.2f}"
    else:
        valor_fmt = f"+R$ {valor:>7.2f}"

    # f-string com alinhamento:
    # :<12 = alinha à esquerda em 12 caracteres
    # :>10 = alinha à direita em 10 caracteres
    print(f"{data:<12} {descricao:<22} {categoria:<14} {valor_fmt:>10}")


# ── PASSO 5: CALCULAR E IMPRIMIR O RESUMO ───────────────────

print("=" * 62)

# Usamos for + if para separar entradas de saídas
# (for loop + if/else )
total_entradas = 0
total_saidas   = 0

for t in transacoes:
    if t["tipo"] == "entrada":
        total_entradas += t["valor"]   # += é o mesmo que = total + valor
    else:
        total_saidas += t["valor"]

saldo_final = total_entradas - total_saidas

print(f"{'Total de entradas:':<30} +R$ {total_entradas:>8.2f}")
print(f"{'Total de saídas:':<30} -R$ {total_saidas:>8.2f}")
print("-" * 62)
print(f"{'SALDO DO MÊS:':<30}  R$ {saldo_final:>8.2f}")
print("=" * 62)


# ── PASSO 6: RESUMO POR CATEGORIA ───────────────────────────
#
# Dicionário para acumular gastos por categoria
# {chave: valor} — ex: {"Alimentação": 689.30, "Transporte": 340.40}

print(f"\n{'GASTOS POR CATEGORIA':^62}")
print("-" * 62)

por_categoria = {}   # dicionário vazio

for t in transacoes:
    if t["tipo"] == "saida":    # só conta as saídas
        cat = t["categoria"]
        val = t["valor"]

        # Se a categoria ainda não existe no dicionário, cria com 0
        # Se já existe, só soma
        if cat not in por_categoria:
            por_categoria[cat] = 0
        por_categoria[cat] += val

# Ordena do maior para o menor gasto
# sorted() com key e reverse=True ordena de forma decrescente
categorias_ordenadas = sorted(por_categoria.items(), key=lambda x: x[1], reverse=True)

for categoria, total in categorias_ordenadas:
    # Barra visual proporcional ao gasto (cada █ = R$ 50)
    barra = "█" * int(total / 50)
    print(f"{categoria:<14} R$ {total:>8.2f}  {barra}")

print("=" * 62)
print(f"\n✅ {len(transacoes)} transações processadas com sucesso.")

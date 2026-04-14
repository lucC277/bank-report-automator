# 🏦 Bank Report Automator

> Automação Python que lê transações financeiras de um arquivo CSV
> e gera relatórios formatados com análise por categoria.

## 📋 Features

- ✅ Lê arquivo CSV com transações financeiras
- ✅ Imprime extrato formatado em tabela no terminal
- ✅ Calcula saldo (entradas - saídas)
- ✅ Agrupa despesas por categoria
- ✅ **Gera Excel profissional com 4 abas:**
  - `Extrato Completo` — todas as transações
  - `Saídas` — apenas despesas
  - `Entradas` — apenas receitas
  - `Por Categoria` — análise com total, quantidade e ticket médio
  - `⚠️ Alertas` — transações acima de R$ 300 (limiar configurável)

## 🛠️ Technologies

- Python 3.12+
- **pandas** — processamento e análise de dados
- **openpyxl** — geração de arquivos Excel
- csv (built-in)

## ▶️ How to run

### Instalação de dependências

```bash
pip install pandas openpyxl
```

### Executar o relatório principal

```bash
python relatorios_pandas.py
```

**Resultado:** Cria arquivo `relatorio_completo.xlsx` com 4 abas prontas para usar.

### Executar versão simples (terminal)

```bash
python extrato.py
```

## 📊 Sample output

### Terminal (extrato.py)
```
==============================================================
          EXTRATO DE TRANSAÇÕES — MARÇO 2026
==============================================================
DATA         DESCRIÇÃO          CATEGORIA      VALOR
--------------------------------------------------------------
2026-03-01   Salário março      Receita    +R$ 3500.00
2026-03-02   Mercado Extra      Alimentação -R$  187.50
2026-03-05   Netflix            Lazer       -R$   45.90
==============================================================
RESUMO POR CATEGORIA:
Alimentação                          ███████████ R$   187.50
Lazer                                   █████ R$    45.90
==============================================================
SALDO DO MÊS:                   R$  3265.60
==============================================================
```

### Excel gerado (relatorios_pandas.py)
```
📊 Gerando relatório financeiro com pandas...
========================================
  Total entradas: R$  3500.00
  Total saídas:   R$   233.40
  Saldo do mês:   R$ 3266.60
========================================
✅ relatorio_completo.xlsx gerado com sucesso!
```

## 📋 Arquivo CSV esperado

O arquivo `transacoes.csv` deve ter este formato:

```csv
data,descricao,categoria,tipo,valor
2026-03-01,Salário março,Receita,entrada,3500.00
2026-03-02,Mercado Extra,Alimentação,saida,187.50
2026-03-05,Netflix,Lazer,saida,45.90
```

**Colunas obrigatórias:**
- `data` — data da transação (formato: YYYY-MM-DD)
- `descricao` — descrição da transação
- `categoria` — categoria (Alimentação, Transporte, etc)
- `tipo` — "entrada" ou "saida"
- `valor` — valor em reais (numérico)

## 👤 Author

**Lucas Ricardo** — [LinkedIn](https://linkedin.com/in/-lucas-ti)

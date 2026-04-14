# 🏦 Bank Report Automator

> Automação Python que lê transações financeiras de um arquivo CSV 
> e gera relatórios formatados com análise por categoria.

## 📚 Projeto em Desenvolvimento

Este repositório segue um plano de **2 meses focado em RPA e automação**, com entregas semanais progredindo em complexidade e funcionalidade.

---

## 📂 Estrutura do Projeto

```
bank-report-automator/
├── extrato.py              # Semana 1: Script básico com CSV nativo
├── relatorios_pandas.py    # Semana 2: Automação com Pandas + Excel
├── transacoes.csv          # Dados de exemplo (transações fictícias)
└── README.md               # Este arquivo
```

---

## 🚀 Semana 1: Script Básico (`extrato.py`)

**Objetivo:** Ler dados de um CSV e exibir relatório formatado no terminal.

### Features
- ✅ Lê arquivo CSV com transações
- ✅ Imprime extrato formatado em tabela
- ✅ Calcula saldo (entradas - saídas)
- ✅ Agrupa despesas por categoria
- ✅ Mostra o total de cada categoria com barra visual

### Tecnologias
- Python 3.12+
- Biblioteca `csv` (built-in)

### Como usar

```bash
python extrato.py
```

### Output esperado
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

---

## 📊 Semana 2: Relatório Avançado com Excel (`relatorios_pandas.py`)

**Objetivo:** Automatizar geração de relatórios multi-aba em Excel com análise profissional.

### Features
- ✅ Lê CSV com Pandas (1 linha de código vs 7 da semana 1)
- ✅ Filtra e agrupa dados por categoria
- ✅ Gera **Excel com 4 abas:**
  - `Extrato Completo` — todas as transações
  - `Saídas` — apenas despesas
  - `Entradas` — apenas receitas  
  - `Por Categoria` — análise com total, quantidade e ticket médio
  - `⚠️ Alertas` — transações acima de R$ 300 (limiar configurável)

### Tecnologias
- Python 3.12+
- **pandas** — processamento e análise de dados
- **openpyxl** — geração de arquivos Excel
- Integração com bibliotecas padrão

### Instalação de dependências

```bash
pip install pandas openpyxl
```

### Como usar

```bash
python relatorios_pandas.py
```

**Resultado:** Cria arquivo `relatorio_completo.xlsx` com 4 abas prontas para usar.

### Exemplo de saída no terminal
```
📊 Gerando relatório financeiro com pandas...
========================================
  Total entradas: R$  3500.00
  Total saídas:   R$   233.40
  Saldo do mês:   R$ 3266.60
========================================
✅ relatorio_completo.xlsx gerado com sucesso!
```

### Configuração
Edite no arquivo `relatorios_pandas.py`:

```python
ARQUIVO_CSV   = "transacoes.csv"      # Arquivo de entrada
ARQUIVO_EXCEL = "relatorio_completo"  # Nome do Excel gerado
LIMITE_ALERTA = 300.00                # Valor limite para alertas
```

---

## 📈 Comparação: Semana 1 vs Semana 2

| Aspecto | Semana 1 | Semana 2 |
|---------|----------|----------|
| **Tecnologia** | CSV nativo | Pandas + openpyxl |
| **Linhas de código** | ~50 | ~70 |
| **Saída** | Terminal | 4 abas Excel |
| **Filtros** | Manuais (for loop) | Automáticos (.groupby()) |
| **Tempo de execução** | Segundos | Milissegundos |
| **Profissionalismo** | ⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🔧 Requisitos

- Python 3.11+
- pandas
- openpyxl

Instale tudo com:
```bash
pip install -r requirements.txt  # (se tiver)
# ou
pip install pandas openpyxl
```

---

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

---

## 🎯 Próximos passos (Semana 3 em diante)

- S3: Web scraping e APIs (Bacen, cotações de moedas)
- S4: Projeto integrado com Git + README profissional
- S5+: SQL, agendamento automático, email

---

## 👤 Author

**Lucas Ricardo** — [LinkedIn](https://linkedin.com/in/-lucas-ti)

---

## 📝 Licença

Este projeto é de código aberto para fins educacionais e de portfólio.

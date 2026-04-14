# ============================================================
#  relatorio_pandas.py
#  Lê transacoes.csv e gera relatorio_completo.xlsx com 4 abas
# ============================================================

# ── 1. IMPORTS ───────────────────────────────────────────────
import pandas as pd

# ── 2. CONFIGURAÇÕES ─────────────────────────────────────────
ARQUIVO_CSV   = "transacoes.csv"
ARQUIVO_EXCEL = "relatorio_completo.xlsx"
LIMITE_ALERTA = 300.00

# ── 3. FUNÇÕES ───────────────────────────────────────────────
def carregar_dados(caminho):
    """Lê o CSV e retorna DataFrame."""
    df = pd.read_csv(caminho)
    return df

def calcular_resumo(df):
    """Calcula e imprime o resumo financeiro."""
    entradas = df[df["tipo"]=="entrada"]["valor"].sum()
    saidas   = df[df["tipo"]=="saida"]["valor"].sum()
    saldo    = entradas - saidas

    print("=" * 40)
    print(f"  Total entradas: R$ {entradas:>8.2f}")
    print(f"  Total saídas:   R$ {saidas:>8.2f}")
    print(f"  Saldo do mês:   R$ {saldo:>8.2f}")
    print("=" * 40)

def gerar_excel(df, caminho):
    """Gera Excel com 4 abas."""
    saidas   = df[df["tipo"]=="saida"]
    entradas = df[df["tipo"]=="entrada"]
    alertas  = df[df["valor"] > LIMITE_ALERTA]
    por_cat  = (
        saidas.groupby("categoria")["valor"]
        .agg(total="sum", transacoes="count", media="mean")
        .round(2).reset_index()
        .sort_values("total", ascending=False)
    )

    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Extrato Completo", index=False)
        saidas.to_excel(writer, sheet_name="Saídas", index=False)
        entradas.to_excel(writer, sheet_name="Entradas", index=False)
        por_cat.to_excel(writer, sheet_name="Por Categoria", index=False)
        if len(alertas) > 0:
            alertas.to_excel(writer, sheet_name="⚠️ Alertas", index=False)

    print(f"✅ {caminho} gerado com sucesso!")

# ── 4. EXECUÇÃO PRINCIPAL ─────────────────────────────────────
if __name__ == "__main__":
    print("📊 Gerando relatório financeiro com pandas...")
    df = carregar_dados(ARQUIVO_CSV)
    calcular_resumo(df)
    gerar_excel(df, ARQUIVO_EXCEL)
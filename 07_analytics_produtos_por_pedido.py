import csv
import os
from collections import defaultdict
from openpyxl import Workbook

# Diretório e arquivos
diretorio = r"C:\Users\wande\OneDrive\Documentos\_01_projeto_databricks_azure\archive"

arquivo_csv = os.path.join(
    diretorio,
    "sales_transaction_v_4a_tratado_data.csv"
)

arquivo_excel = os.path.join(
    diretorio,
    "total_produtos_por_pedido.xlsx"
)

# Dicionário: TransactionNo -> total de produtos
produtos_por_pedido = defaultdict(int)

# ===== Leitura do CSV =====
with open(arquivo_csv, mode="r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")

    cabecalho = next(leitor)

    # Validação das colunas necessárias
    if "TransactionNo" not in cabecalho or "ProductName" not in cabecalho:
        raise Exception("Colunas 'TransactionNo' ou 'ProductName' não encontradas.")

    idx_pedido = cabecalho.index("TransactionNo")
    idx_produto = cabecalho.index("ProductName")

    # Dados a partir da linha 2
    for linha in leitor:
        if not linha or len(linha) <= max(idx_pedido, idx_produto):
            continue

        pedido = linha[idx_pedido].strip()
        produto = linha[idx_produto].strip()

        if pedido and produto:
            produtos_por_pedido[pedido] += 1

# ===== Criação do Excel =====
wb = Workbook()
ws = wb.active
ws.title = "Produtos_por_Pedido"

# Cabeçalho
ws.append(["TransactionNo", "Total_Produtos"])

# Dados ordenados por número do pedido
for pedido in sorted(produtos_por_pedido):
    ws.append([pedido, produtos_por_pedido[pedido]])

# Salvar arquivo
wb.save(arquivo_excel)

print("Arquivo Excel gerado com sucesso:")
print(arquivo_excel)

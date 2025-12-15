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
    "total_lucro_por_segmento.xlsx"
)

# ===== Mapeamento País -> Segmento =====
pais_para_segmento = {
    "Australia": "Oceania",
    "Austria": "Europa",
    "Bahrain": "Oriente Médio",
    "Belgium": "Europa",
    "Brazil": "América Latina",
    "Canada": "América do Norte",
    "Channel Islands": "Europa",
    "Cyprus": "Europa",
    "Czech Republic": "Europa",
    "Denmark": "Europa",
    "EIRE (Irlanda)": "Europa",
    "European Community": "Europa",
    "Finland": "Europa",
    "France": "Europa",
    "Germany": "Europa",
    "Greece": "Europa",
    "Hong Kong": "Ásia",
    "Iceland": "Europa",
    "Israel": "Oriente Médio",
    "Italy": "Europa",
    "Japan": "Ásia",
    "Lebanon": "Oriente Médio",
    "Lithuania": "Europa",
    "Malta": "Europa",
    "Netherlands": "Europa",
    "Norway": "Europa",
    "Poland": "Europa",
    "Portugal": "Europa",
    "RSA (South Africa)": "África",
    "Saudi Arabia": "Oriente Médio",
    "Singapore": "Ásia",
    "Spain": "Europa",
    "Sweden": "Europa",
    "Switzerland": "Europa",
    "United Arab Emirates": "Oriente Médio",
    "United Kingdom": "Europa",
    "Unspecified": "Não Identificado",
    "USA": "América do Norte"
}

# ===== Acumuladores =====
# Segmento -> quantidade de vendas
qtd_vendas_por_segmento = defaultdict(int)

# Segmento -> valor total
valor_por_segmento = defaultdict(float)

# ===== Leitura do CSV =====
with open(arquivo_csv, mode="r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")
    cabecalho = next(leitor)

    if "Country" not in cabecalho or "Price" not in cabecalho:
        raise Exception("Colunas 'Country' ou 'Price' não encontradas.")

    idx_country = cabecalho.index("Country")
    idx_price = cabecalho.index("Price")

    for linha in leitor:
        if not linha or len(linha) <= max(idx_country, idx_price):
            continue

        pais = linha[idx_country].strip()
        price_raw = linha[idx_price].strip()

        # Conversão do Price (formato brasileiro)
        try:
            valor = float(price_raw.replace(".", "").replace(",", "."))
        except ValueError:
            continue

        segmento = pais_para_segmento.get(pais, "Não Identificado")

        qtd_vendas_por_segmento[segmento] += 1
        valor_por_segmento[segmento] += valor

# ===== Criação do Excel =====
wb = Workbook()
ws = wb.active
ws.title = "Lucro_por_Segmento"

# Cabeçalho
ws.append(["Segmento", "Total de Vendas", "Valor Total"])

# Dados
for segmento in sorted(qtd_vendas_por_segmento):
    ws.append([
        segmento,
        qtd_vendas_por_segmento[segmento],
        round(valor_por_segmento[segmento], 2)
    ])

# Salvar Excel
wb.save(arquivo_excel)

print("Arquivo Excel gerado com sucesso:")
print(arquivo_excel)

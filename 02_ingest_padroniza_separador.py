import csv
import os

# Caminhos dos arquivos
diretorio = r"C:\Users\wande\OneDrive\Documentos\_01_projeto_databricks_azure\archive"
arquivo_origem = os.path.join(diretorio, "Sales_Transaction_v_4a.csv")
arquivo_destino = os.path.join(
    diretorio,
    "sales_transaction_v_4a_separador_tratado.csv"
)

def tratar_separador_csv(arquivo_entrada, arquivo_saida):
# Lê um arquivo CSV separado por vírgula (,), e grava um novo arquivo CSV separado por ponto e vírgula (;),
# mantendo todos os registros e colunas intactos.

    with open(arquivo_entrada, mode="r", encoding="utf-8", newline="") as csv_in:
        leitor = csv.reader(csv_in, delimiter=",")

        with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as csv_out:
            escritor = csv.writer(csv_out, delimiter=";")

            for linha in leitor:
                escritor.writerow(linha)

    print("Arquivo tratado com sucesso!")
    print(f"Arquivo gerado em: {arquivo_saida}")

if __name__ == "__main__":
    tratar_separador_csv(arquivo_origem, arquivo_destino)

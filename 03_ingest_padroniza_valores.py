import csv
import os

# Diretório e arquivos
diretorio = r"C:\Users\wande\OneDrive\Documentos\_01_projeto_databricks_azure\archive"
arquivo_origem = os.path.join(
    diretorio,
    "sales_transaction_v_4a_separador_tratado.csv"
)
arquivo_destino = os.path.join(
    diretorio,
    "sales_transaction_v_4a_com_virgula.csv"
)

def converter_price_para_padrao_br(arquivo_entrada, arquivo_saida):
    """
    Converte o separador decimal do campo Price
    de ponto (.) para vírgula (,),
    mantendo o delimitador de campo (;)
    """

    with open(arquivo_entrada, mode="r", encoding="utf-8", newline="") as csv_in:
        leitor = csv.DictReader(csv_in, delimiter=";")
        campos = leitor.fieldnames

        with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as csv_out:
            escritor = csv.DictWriter(csv_out, fieldnames=campos, delimiter=";")
            escritor.writeheader()

            for linha in leitor:
                valor_price = linha.get("Price")

                if valor_price:
                    # Substitui apenas o separador decimal
                    linha["Price"] = valor_price.replace(".", ",")

                escritor.writerow(linha)

    print("Conversão concluída com sucesso.")
    print(f"Arquivo gerado: {arquivo_saida}")

if __name__ == "__main__":
    converter_price_para_padrao_br(arquivo_origem, arquivo_destino)

"""
Exemplo oficial (case) — Pipeline de eventos de pedidos (simulado)
Objetivo: Demonstrar ingestão (Bronze), tratamento (Silver) e métrica (Gold)
usando PySpark, alinhado à arquitetura Databricks + Lakehouse.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, regexp_replace


def main():
    spark = (
        SparkSession.builder
        .appName("real_time_orders_example")
        .getOrCreate()
    )

    # -----------------------------
    # 1) BRONZE — Simulação de eventos (como se viessem do streaming)
    # -----------------------------
    events = [
        ("C123456", "2023-10-01", "P1001", "Gift Box", 10.0, -1, "12345", "United Kingdom"),
        ("123457",  "2023-10-01", "P1002", "Toy Car",  15.0,  2, "12346", "France"),
        ("123458",  "2023-10-01", "P1003", "Lamp",     25.0,  1, "12347", "Germany"),
    ]

    columns = [
        "TransactionNo", "Date", "ProductNo", "ProductName",
        "Price", "Quantity", "CustomerNo", "Country"
    ]

    df_bronze = spark.createDataFrame(events, columns)

    print("\n=== BRONZE (raw events) ===")
    df_bronze.show(truncate=False)

    # -----------------------------
    # 2) SILVER — Tratamento / regras de negócio
    #    - separa cancelamento do TransactionNo
    #    - padroniza TransactionNo
    #    - calcula TotalValue (métrica base)
    # -----------------------------
    df_silver = (
        df_bronze
        .withColumn(
            "TransactionNo_Cancel",
            when(col("TransactionNo").startswith("C"), "C").otherwise("N")
        )
        .withColumn(
            "TransactionNo_clean",
            regexp_replace(col("TransactionNo"), "^C", "")
        )
        .withColumn(
            "TotalValue",
            col("Price") * col("Quantity")
        )
    )

    print("\n=== SILVER (treated) ===")
    df_silver.show(truncate=False)

    # -----------------------------
    # 3) GOLD — Agregação para consumo (ex.: Receita por país)
    # -----------------------------
    df_gold = (
        df_silver
        .groupBy("Country")
        .sum("TotalValue")
        .withColumnRenamed("sum(TotalValue)", "Revenue")
    )

    print("\n=== GOLD (analytics) ===")
    df_gold.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()

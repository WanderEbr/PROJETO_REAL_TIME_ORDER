Case – Solução de Dados em Tempo Real para Varejo Online
1. Contexto do Projeto

Este repositório faz parte de um case técnico cujo objetivo é propor e exemplificar uma solução de dados em tempo real para uma empresa de varejo online com atuação global.
A solução foi desenhada considerando a separação de responsabilidades entre a squad de produtos (sistema transacional) e a equipe de dados (plataforma analítica), utilizando uma arquitetura orientada a eventos e processamento em streaming.

O foco principal é demonstrar raciocínio arquitetural, boas práticas de engenharia de dados e capacidade de transformar dados transacionais em informações analíticas de valor para o negócio.

2. Objetivo do Código

O código presente neste repositório tem como objetivo servir como exemplo técnico para engenheiros de software e engenheiros de dados, demonstrando:

Ingestão de eventos de pedidos (simulada)

Tratamento de dados com regras de negócio

Organização em camadas Bronze, Silver e Gold

Geração de métricas analíticas para apoio à tomada de decisão

O exemplo foi propositalmente mantido simples, legível e explicável, priorizando clareza arquitetural em vez de complexidade operacional.

3. Arquitetura de Referência

O código está alinhado com a seguinte arquitetura lógica:

Sistema Transacional (fora deste repositório)
Emite eventos de negócio de forma assíncrona (ex.: pedido criado, pedido cancelado).

Plataforma de Dados (Databricks / Azure)

Ingestão de eventos em tempo real

Processamento distribuído com PySpark

Organização dos dados em camadas:

Bronze: dados brutos, sem tratamento

Silver: dados tratados com regras de negócio

Gold: dados agregados prontos para consumo analítico

Consumo Analítico
KPIs de vendas, como receita, volume e cancelamentos, utilizados por BI e Analytics.

4. Descrição do Arquivo de Código

Arquivo:
09_real_time_orders_example.py

O que o código demonstra:

Camada Bronze
Simulação da chegada de eventos de pedidos, representando dados vindos do sistema transacional em tempo real.

Camada Silver
Aplicação de regras de negócio, incluindo:

Separação do indicador de cancelamento do campo TransactionNo

Padronização do número da transação

Cálculo do valor total do pedido

Camada Gold
Agregação dos dados para geração de métricas analíticas, como receita por país, prontas para consumo por ferramentas de BI.

5. Tecnologias Utilizadas

Python / PySpark
Linguagem escolhida por ser amplamente utilizada em plataformas de dados modernas e nativamente suportada pelo Databricks.

Apache Spark (via Databricks)
Utilizado para processamento distribuído e compatível com cenários de batch e streaming.

Arquitetura Lakehouse (conceitual)
Aplicada por meio da separação Bronze, Silver e Gold, garantindo rastreabilidade, qualidade e governança dos dados.

6. Execução do Código

O código pode ser executado de duas formas:

1. Databricks

Importar o arquivo como notebook ou job

Executar diretamente no ambiente Databricks

2. Ambiente local (com Spark configurado)

spark-submit 09_real_time_orders_example.py

7. Observações Importantes

A ingestão de eventos é simulada para fins didáticos.
Em um cenário real, essa etapa seria substituída por leitura de um sistema de mensageria (ex.: Event Hub, Kafka).

O foco do exemplo é arquitetural e conceitual, não operacional.

O código não altera dados de origem, respeitando o princípio de preservação da fonte original.

8. Conclusão

Este repositório complementa a documentação e os diagramas do case, demonstrando na prática como uma solução de dados em tempo real pode ser implementada de forma escalável, desacoplada e orientada ao negócio, atendendo às necessidades de análise e tomada de decisão da área de vendas.
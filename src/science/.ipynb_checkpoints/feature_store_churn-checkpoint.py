from pyspark.sql import DataFrame
from pyspark.sql import functions as F

class FeatureStoreChurn:
    def __init__(self):
        pass

    def rename_columns(self, columns_dic: dict, df: DataFrame) -> DataFrame:
        """Renomeia as colunas de um DataFrame baseado no dicionário fornecido."""
        for old_column, new_column in columns_dic.items():
            df = df.withColumnRenamed(old_column, new_column)
        return df

    def join_dfs(self, df_01: DataFrame, df_02: DataFrame, join_condition: str, join_type: str) -> DataFrame:
        """Realiza um join entre dois DataFrames com base nas condições e tipo especificados."""
        return df_01.join(df_02, on=join_condition, how=join_type)

    def df_to_parquet(self, df: DataFrame, file_path: str) -> None:
        """Converte um DataFrame em Pandas e salva como arquivo Parquet."""
        df_p = df.toPandas()
        df_p.to_parquet(file_path, index=False)
        print("DF Salvo!")
        
    def read_parquet_file(file_path):
        """Realiza a leitura de um arquivo Parquet."""
        df = spark.read.parquet(file_path)
        return df

    def feat_tempo_ultima_transacao(self, df_transaction: DataFrame) -> DataFrame:
        """Calcula o tempo desde a última transação para cada cliente."""
        columns_dic = {
            "ID Transação": "NB_ID_TRANSACAO",
            "ID Cliente": "NB_ID_CLIENTE",
            "Data": "DT_DATA",
            "Valor": "NB_VALOR",
            "Categoria": "TX_CATEGORIA"
        }
        df_transaction_01 = self.rename_columns(columns_dic, df_transaction)
        
        max_data_value = df_transaction_01.agg(F.max("DT_DATA")).collect()[0][0]
        
        df_new = (df_transaction_01.groupBy("NB_ID_CLIENTE")
                  .agg(
                      F.datediff(F.lit(max_data_value), F.max(F.col("DT_DATA"))).alias("NB_TEMPO_ULTIMA_TRANSACAO")
                  )
                  .orderBy(F.col("NB_ID_CLIENTE"))
                 )
        
        return df_new


    def feat_freq_compras(self, df_transaction: DataFrame, df_base: DataFrame) -> DataFrame:
        """Calcula a quantidade de compras que o cliente fez dividida pelo número de meses desde sua inscrição."""
        columns_dic = {"ID": "NB_ID_CLIENTE"
                       , "Idade": "NB_IDADE"
                       , "Gênero": "TX_GENERO"
                       , "Dias desde a Inscrição": "NB_DIAS_INSCRITO"
                       , "Usou Suporte": "NB_SUPORTE"
                       , "Plano": "TX_PLANO"
                       , "Churn": "FL_CHURN"}
        df_base_01 = self.rename_columns(columns_dic, df_base)
        
        columns_dic = {"ID Transação": "NB_ID_TRANSACAO"
                       , "ID Cliente": "NB_ID_CLIENTE"
                       , "Data": "DT_DATA"
                       , "Valor": "NB_VALOR"
                       , "Categoria": "TX_CATEGORIA"}
        df_transaction_01 = self.rename_columns(columns_dic, df_transaction)
        
        df_max_compras_01 = (
            df_base_01
            .join(
                df_transaction_01.groupBy("NB_ID_CLIENTE")
                .agg(F.count("*").alias("NB_TOTAL_COMPRAS")),
                on="NB_ID_CLIENTE",
                how="left"
            )
            .withColumn(
                "DT_PRIMEIRO_DIA",
                F.date_sub(F.current_timestamp(), F.col("NB_DIAS_INSCRITO"))
            )
            .withColumn(
                "NB_MESES_INSCRITO",
                F.months_between(F.current_timestamp(), F.col("DT_PRIMEIRO_DIA")).cast("int")
            )
            .withColumn(
                "NB_FREQ_COMPRAS",
                    F.round(F.col("NB_TOTAL_COMPRAS") / F.col("NB_MESES_INSCRITO"), 2)
                )
            ).select("NB_ID_CLIENTE", "NB_FREQ_COMPRAS")
        
        return df_max_compras_01
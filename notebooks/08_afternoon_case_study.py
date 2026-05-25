# Databricks notebook source
# MAGIC %md
# MAGIC # 08 - Après-midi 2: mini-cas métier
# MAGIC
# MAGIC Objectif: répondre à une question métier avec un workflow complet, encore guidé.
# MAGIC
# MAGIC Question:
# MAGIC
# MAGIC > Quels segments semblent associés aux charges médicales les plus élevées?
# MAGIC
# MAGIC Ce notebook est un peu plus autonome que le précédent. Les étapes restent balisées.

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import avg, count

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

spark_df.createOrReplaceTempView("insurance")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 1 - Préparer une variable de segment
# MAGIC
# MAGIC Concept: une variable numérique peut être transformée en classes pour faciliter l'analyse.
# MAGIC
# MAGIC Ici, on transforme `age` en trois tranches.

# COMMAND ----------

df_with_segments = df.assign(
    age_segment=pd.cut(
        df["age"],
        bins=[0, 30, 50, 100],
        labels=["<30", "30-50", ">50"]
    )
)

df_with_segments[["age", "age_segment", "smoker", "charges"]].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Affichez le nombre de lignes par `age_segment`.

# COMMAND ----------

df_with_segments["age_segment"].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df_with_segments["age_segment"].value_counts()
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: quand vous créez un segment, vérifiez toujours sa répartition.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 2 - Analyse 1: charges par statut fumeur

# COMMAND ----------

analysis_smoker = (
    df_with_segments
    .groupby("smoker")["charges"]
    .mean()
    .sort_values(ascending=False)
)

analysis_smoker

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Écrivez une phrase courte dans une cellule Markdown:
# MAGIC
# MAGIC > Les charges moyennes sont plus élevées pour ...

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Exemple de phrase</summary>
# MAGIC
# MAGIC > Les charges moyennes sont plus élevées pour les fumeurs que pour les non-fumeurs dans ce dataset.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: commencez par une analyse simple avant de croiser plusieurs dimensions.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 3 - Analyse 2: charges par tranche d'âge

# COMMAND ----------

analysis_age = (
    df_with_segments
    .groupby("age_segment", observed=True)["charges"]
    .mean()
    .sort_values(ascending=False)
)

analysis_age

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Ajoutez le nombre de lignes par tranche d'âge pour vérifier la taille des segments.

# COMMAND ----------

age_segment_summary = (
    df_with_segments
    .groupby("age_segment", observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

age_segment_summary

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC age_segment_summary = (
# MAGIC     df_with_segments
# MAGIC     .groupby("age_segment", observed=True)
# MAGIC     .agg(
# MAGIC         row_count=("charges", "size"),
# MAGIC         avg_charges=("charges", "mean")
# MAGIC     )
# MAGIC     .sort_values("avg_charges", ascending=False)
# MAGIC )
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: une moyenne sans nombre de lignes peut être trompeuse.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 4 - Analyse 3: croiser deux segments
# MAGIC
# MAGIC Question: que se passe-t-il si on croise `smoker` et `age_segment`?

# COMMAND ----------

segment_summary = (
    df_with_segments
    .groupby(["smoker", "age_segment"], observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

segment_summary

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez `age_segment` par `region` dans l'analyse croisée.

# COMMAND ----------

region_smoker_summary = (
    df_with_segments
    .groupby(["smoker", "region"], observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

region_smoker_summary

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC region_smoker_summary = (
# MAGIC     df_with_segments
# MAGIC     .groupby(["smoker", "region"], observed=True)
# MAGIC     .agg(
# MAGIC         row_count=("charges", "size"),
# MAGIC         avg_charges=("charges", "mean")
# MAGIC     )
# MAGIC     .sort_values("avg_charges", ascending=False)
# MAGIC )
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: plus on croise de dimensions, plus il faut surveiller `row_count`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 5 - Refaire l'analyse croisée en SQL
# MAGIC
# MAGIC On crée d'abord une version Spark avec la colonne `age_segment`.

# COMMAND ----------

spark_df_with_segments = spark.createDataFrame(df_with_segments)
spark_df_with_segments.createOrReplaceTempView("insurance_segments")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        age_segment,
# MAGIC        COUNT(*) AS row_count,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance_segments
# MAGIC GROUP BY smoker, age_segment
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Modifiez la requête pour croiser `smoker` et `region`.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        region,
# MAGIC        COUNT(*) AS row_count,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance_segments
# MAGIC GROUP BY smoker, region
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```sql
# MAGIC SELECT smoker,
# MAGIC        region,
# MAGIC        COUNT(*) AS row_count,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance_segments
# MAGIC GROUP BY smoker, region
# MAGIC ORDER BY avg_charges DESC
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: SQL est très utile pour relire une analyse de segmentation de manière transparente.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 6 - Conclusion métier
# MAGIC
# MAGIC Rédigez une conclusion en 3 phrases:
# MAGIC
# MAGIC 1. Le segment avec les charges moyennes les plus élevées est ...
# MAGIC 2. Le résultat est basé sur ...
# MAGIC 3. Limite: cette analyse est descriptive et ne prouve pas ...

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Exemple de conclusion</summary>
# MAGIC
# MAGIC Le segment avec les charges moyennes les plus élevées est généralement lié au statut fumeur, en particulier lorsqu'il est croisé avec une tranche d'âge élevée. Le résultat est basé sur une moyenne de `charges` par segment et doit être relu avec le nombre de lignes par groupe. Cette analyse est descriptive: elle montre une association dans le dataset, mais ne prouve pas une causalité.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: une conclusion d'analyse doit toujours mentionner la mesure, le segment et la limite.


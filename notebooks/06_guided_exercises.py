# Databricks notebook source
# MAGIC %md
# MAGIC # 06 - Exercices guidés
# MAGIC
# MAGIC Objectif: réutiliser les concepts de la semaine sans partir d'une page blanche.
# MAGIC
# MAGIC Pattern de chaque exercice:
# MAGIC
# MAGIC 1. Concept.
# MAGIC 2. Code de départ.
# MAGIC 3. À vous.
# MAGIC 4. Correction masquée.
# MAGIC 5. Bonne pratique.

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import avg

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")
spark_df = spark.read.csv("/FileStore/tables/insurance.csv", header=True, inferSchema=True)
spark_df.createOrReplaceTempView("insurance")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 1 - Explorer
# MAGIC
# MAGIC Concept: avant une analyse, on contrôle la table.

# COMMAND ----------

df.head()

# COMMAND ----------

len(df)

# COMMAND ----------

df.columns

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Notez:
# MAGIC
# MAGIC - le nombre de lignes,
# MAGIC - la colonne cible,
# MAGIC - deux colonnes de segmentation.

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC - Nombre de lignes attendu: 420.
# MAGIC - Colonne cible: `charges`.
# MAGIC - Exemples de segmentation: `smoker`, `region`, `sex`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: une exploration doit produire une vérification concrète, pas seulement afficher une table.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 2 - Filtrer avec pandas

# COMMAND ----------

df[df["age"] > 50].head()

# COMMAND ----------

df[df["smoker"] == "yes"].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Modifiez le code pour afficher les personnes avec `bmi > 30`.

# COMMAND ----------

df[df["bmi"] > 30].head()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df[df["bmi"] > 30].head()
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: lisez un filtre comme une phrase métier.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 3 - Agréger avec pandas

# COMMAND ----------

df.groupby("region")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Calculez la moyenne de `charges` par `smoker`, puis par `sex`.

# COMMAND ----------

df.groupby("smoker")["charges"].mean()

# COMMAND ----------

df.groupby("sex")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df.groupby("smoker")["charges"].mean()
# MAGIC df.groupby("sex")["charges"].mean()
# MAGIC ```
# MAGIC
# MAGIC Interprétez toujours le segment le plus élevé.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: une moyenne par groupe doit être triée ou comparée explicitement.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 4 - Traduire en Spark

# COMMAND ----------

display(spark_df.select("age", "charges"))

# COMMAND ----------

display(spark_df.filter(spark_df.bmi > 30))

# COMMAND ----------

display(spark_df.groupBy("smoker").agg(avg("charges").alias("avg_charges")))

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez `smoker` par `region` dans le groupBy Spark.

# COMMAND ----------

display(spark_df.groupBy("region").agg(avg("charges").alias("avg_charges")))

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC display(spark_df.groupBy("region").agg(avg("charges").alias("avg_charges")))
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: en Spark, nommez toujours les résultats agrégés avec `alias`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 5 - SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY smoker
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez `smoker` par `region`.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT region,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```sql
# MAGIC SELECT region,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: `ORDER BY ... DESC` facilite la lecture du segment le plus élevé.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mini challenge final
# MAGIC
# MAGIC Question métier: quel segment génère les coûts médicaux les plus élevés?
# MAGIC
# MAGIC Choisissez pandas, Spark ou SQL.

# COMMAND ----------

analysis = (
    df
    .assign(age_segment=pd.cut(df["age"], bins=[0, 30, 50, 100], labels=["<30", "30-50", ">50"]))
    .groupby(["smoker", "age_segment"], observed=True)["charges"]
    .mean()
    .sort_values(ascending=False)
)

analysis

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Rédigez une phrase:
# MAGIC
# MAGIC > Le segment le plus coûteux est ... car ...

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Exemple de phrase:
# MAGIC
# MAGIC > Dans ce dataset, les fumeurs de plus de 50 ans présentent les charges moyennes les plus élevées. Ce résultat doit être interprété comme un signal descriptif, pas comme une conclusion causale.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: distinguez toujours observation descriptive et conclusion causale.


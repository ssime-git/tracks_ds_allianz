# Databricks notebook source
# MAGIC %md
# MAGIC # 06 - Exercices guidés
# MAGIC
# MAGIC Principe: pas de page blanche. Modifiez le code existant, puis exécutez.

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import avg, count

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")
spark_df = spark.read.csv("/FileStore/tables/insurance.csv", header=True, inferSchema=True)
spark_df.createOrReplaceTempView("insurance")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 1 - Exploration
# MAGIC
# MAGIC Tâches:
# MAGIC
# MAGIC - afficher les 5 premières lignes,
# MAGIC - compter les lignes,
# MAGIC - afficher les colonnes,
# MAGIC - afficher les statistiques.

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
# MAGIC ## Exercice 2 - Filtrage
# MAGIC
# MAGIC Modifiez les seuils ou les modalités dans les cellules ci-dessous.

# COMMAND ----------

df[df["age"] > 50].head()

# COMMAND ----------

df[df["smoker"] == "yes"].head()

# COMMAND ----------

df[df["bmi"] > 30].head()

# COMMAND ----------

df[(df["sex"] == "female") & (df["smoker"] == "yes")].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 3 - GroupBy pandas
# MAGIC
# MAGIC Complétez ou modifiez la colonne de regroupement.

# COMMAND ----------

df.groupby("region")["charges"].mean()

# COMMAND ----------

df.groupby("smoker")["charges"].mean()

# COMMAND ----------

df.groupby("sex")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 4 - Traduction Spark

# COMMAND ----------

display(spark_df.select("age", "charges"))

# COMMAND ----------

display(spark_df.filter(spark_df.bmi > 30))

# COMMAND ----------

display(spark_df.groupBy("smoker").agg(avg("charges").alias("avg_charges")))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercice 5 - SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS row_count
# MAGIC FROM insurance

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY smoker
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT region,
# MAGIC        sex,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC WHERE age > 50
# MAGIC GROUP BY region, sex
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mini challenge final
# MAGIC
# MAGIC Question métier: quel segment de population génère les coûts médicaux les plus élevés?
# MAGIC
# MAGIC Piste guidée:
# MAGIC
# MAGIC 1. Choisissez des segments: `smoker`, `region`, `sex`, ou une tranche d'âge.
# MAGIC 2. Calculez la moyenne de `charges`.
# MAGIC 3. Triez du plus élevé au plus faible.
# MAGIC 4. Rédigez une phrase d'interprétation.

# COMMAND ----------

analysis = (
    df
    .assign(age_segment=pd.cut(df["age"], bins=[0, 30, 50, 100], labels=["<30", "30-50", ">50"]))
    .groupby(["smoker", "age_segment"], observed=True)["charges"]
    .mean()
    .sort_values(ascending=False)
)

analysis


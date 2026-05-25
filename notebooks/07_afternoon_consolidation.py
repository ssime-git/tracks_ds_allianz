# Databricks notebook source
# MAGIC %md
# MAGIC # 07 - Après-midi 1: consolidation guidée
# MAGIC
# MAGIC Objectif: refaire les gestes clés de la matinée avec un peu moins d'aide, mais sans page blanche.
# MAGIC
# MAGIC Progression:
# MAGIC
# MAGIC 1. Contrôler la table.
# MAGIC 2. Filtrer un segment.
# MAGIC 3. Agréger avec pandas.
# MAGIC 4. Refaire une analyse en Spark.
# MAGIC 5. Refaire une analyse en SQL.
# MAGIC 6. Écrire une phrase métier.

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
# MAGIC ## Étape 1 - Contrôler avant d'analyser
# MAGIC
# MAGIC Concept: une analyse fiable commence par vérifier que la table est bien chargée.
# MAGIC
# MAGIC Commandes utiles:
# MAGIC
# MAGIC ```python
# MAGIC df.head()
# MAGIC df.shape
# MAGIC df.columns
# MAGIC df.describe()
# MAGIC ```

# COMMAND ----------

df.head()

# COMMAND ----------

df.shape

# COMMAND ----------

df.columns

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Répondez mentalement avant d'ouvrir la correction:
# MAGIC
# MAGIC 1. Quelle est la colonne cible?
# MAGIC 2. Quelle colonne indique le statut fumeur?
# MAGIC 3. Quelle colonne indique le coût médical?

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC 1. Colonne cible pour l'analyse: `charges`.
# MAGIC 2. Statut fumeur: `smoker`.
# MAGIC 3. Coût médical: `charges`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: nommer la colonne cible avant de filtrer évite de manipuler la mauvaise variable.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 2 - Filtrer un segment simple
# MAGIC
# MAGIC Question: à quoi ressemblent les observations des fumeurs?

# COMMAND ----------

smokers = df[df["smoker"] == "yes"]

smokers.head()

# COMMAND ----------

len(smokers)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Créez une table `older_than_50` qui garde les personnes de plus de 50 ans.

# COMMAND ----------

older_than_50 = df[df["age"] > 50]

older_than_50.head()

# COMMAND ----------

len(older_than_50)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC older_than_50 = df[df["age"] > 50]
# MAGIC older_than_50.head()
# MAGIC len(older_than_50)
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: stocker un filtre dans une variable (`older_than_50`) rend la suite plus lisible.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 3 - Filtrer un segment combiné
# MAGIC
# MAGIC Question: quelles lignes correspondent aux fumeurs de plus de 50 ans?
# MAGIC
# MAGIC En pandas, chaque condition est mise entre parenthèses.

# COMMAND ----------

older_smokers = df[(df["age"] > 50) & (df["smoker"] == "yes")]

older_smokers.head()

# COMMAND ----------

len(older_smokers)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Créez une table `high_bmi_smokers`:
# MAGIC
# MAGIC - `bmi > 30`
# MAGIC - `smoker == "yes"`

# COMMAND ----------

high_bmi_smokers = df[(df["bmi"] > 30) & (df["smoker"] == "yes")]

high_bmi_smokers.head()

# COMMAND ----------

len(high_bmi_smokers)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC high_bmi_smokers = df[(df["bmi"] > 30) & (df["smoker"] == "yes")]
# MAGIC high_bmi_smokers.head()
# MAGIC len(high_bmi_smokers)
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: pour combiner des conditions pandas, utilisez `&` et mettez chaque condition entre parenthèses.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 4 - Agréger avec pandas
# MAGIC
# MAGIC Question: les charges moyennes changent-elles selon le statut fumeur?

# COMMAND ----------

df.groupby("smoker")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Calculez la moyenne de `charges` par `region`.

# COMMAND ----------

df.groupby("region")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df.groupby("region")["charges"].mean()
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: après une moyenne par groupe, cherchez le groupe le plus élevé et le plus faible.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 5 - Trier le résultat
# MAGIC
# MAGIC Une table triée est plus facile à lire.

# COMMAND ----------

avg_by_region = (
    df
    .groupby("region")["charges"]
    .mean()
    .sort_values(ascending=False)
)

avg_by_region

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Créez `avg_by_smoker` trié du plus élevé au plus faible.

# COMMAND ----------

avg_by_smoker = (
    df
    .groupby("smoker")["charges"]
    .mean()
    .sort_values(ascending=False)
)

avg_by_smoker

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC avg_by_smoker = (
# MAGIC     df
# MAGIC     .groupby("smoker")["charges"]
# MAGIC     .mean()
# MAGIC     .sort_values(ascending=False)
# MAGIC )
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: trier un résultat agrégé évite de tirer une conclusion trop vite.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 6 - Refaire en Spark
# MAGIC
# MAGIC Même question: moyenne des charges par statut fumeur.

# COMMAND ----------

display(
    spark_df
    .groupBy("smoker")
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez `smoker` par `region`.

# COMMAND ----------

display(
    spark_df
    .groupBy("region")
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC display(
# MAGIC     spark_df
# MAGIC     .groupBy("region")
# MAGIC     .agg(
# MAGIC         count("*").alias("row_count"),
# MAGIC         avg("charges").alias("avg_charges")
# MAGIC     )
# MAGIC )
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: ajouter `row_count` aide à vérifier qu'un segment n'est pas trop petit.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 7 - Refaire en SQL
# MAGIC
# MAGIC Même question, syntaxe SQL.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        COUNT(*) AS row_count,
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
# MAGIC        COUNT(*) AS row_count,
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
# MAGIC        COUNT(*) AS row_count,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: comparer pandas, Spark et SQL aide à séparer la logique métier de la syntaxe.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 8 - Phrase métier
# MAGIC
# MAGIC Complétez:
# MAGIC
# MAGIC > Dans ce dataset, le segment avec la moyenne de charges la plus élevée est ... La différence observée est descriptive et ne prouve pas une causalité.

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Exemple de formulation</summary>
# MAGIC
# MAGIC > Dans ce dataset, les fumeurs ont des charges moyennes plus élevées que les non-fumeurs. C'est une observation descriptive sur ce fichier; elle ne suffit pas à prouver une causalité.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: terminer une analyse par une phrase métier courte et prudente.


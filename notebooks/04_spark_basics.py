# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - Spark Basics
# MAGIC
# MAGIC Objectif: refaire les gestes pandas avec l'API Spark disponible dans Databricks.
# MAGIC
# MAGIC Pattern:
# MAGIC
# MAGIC 1. Concept.
# MAGIC 2. Commande.
# MAGIC 3. Pratique guidée.
# MAGIC 4. Correction masquée.
# MAGIC 5. Bonne pratique.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 1 - Spark dans Databricks
# MAGIC
# MAGIC Dans Databricks, `spark` est déjà disponible. Il permet de créer des Spark DataFrames.
# MAGIC
# MAGIC Aujourd'hui, on retient seulement:
# MAGIC
# MAGIC - Spark manipule aussi des tables,
# MAGIC - on utilise `display(...)` pour afficher les résultats,
# MAGIC - on retrouve les gestes `select`, `filter`, `groupBy`.

# COMMAND ----------

spark

# COMMAND ----------

# MAGIC %md
# MAGIC **Bonne pratique**: ne cherchez pas à comprendre l'architecture Spark aujourd'hui. Concentrez-vous sur les gestes analytiques.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 2 - Lire le CSV avec Spark
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC spark_df = spark.read.csv(
# MAGIC     "/FileStore/tables/insurance.csv",
# MAGIC     header=True,
# MAGIC     inferSchema=True
# MAGIC )
# MAGIC ```
# MAGIC
# MAGIC Différence importante: le chemin Spark ne commence pas par `/dbfs`.

# COMMAND ----------

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

display(spark_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Exécutez `spark_df.printSchema()` pour afficher les colonnes et les types.

# COMMAND ----------

spark_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC spark_df.printSchema()
# MAGIC ```
# MAGIC
# MAGIC On doit retrouver `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: après un chargement Spark, vérifiez toujours le schéma.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 3 - Sélectionner des colonnes
# MAGIC
# MAGIC pandas:
# MAGIC
# MAGIC ```python
# MAGIC df[["age", "charges"]]
# MAGIC ```
# MAGIC
# MAGIC Spark:
# MAGIC
# MAGIC ```python
# MAGIC spark_df.select("age", "charges")
# MAGIC ```

# COMMAND ----------

display(spark_df.select("age", "charges"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Sélectionnez `smoker` et `charges`.

# COMMAND ----------

display(spark_df.select("smoker", "charges"))

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC display(spark_df.select("smoker", "charges"))
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: utilisez `display(...)` dans Databricks pour inspecter visuellement les DataFrames Spark.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 4 - Filtrer
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC spark_df.filter(spark_df.age > 50)
# MAGIC ```

# COMMAND ----------

display(spark_df.filter(spark_df.age > 50))

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Filtrez les lignes avec `bmi > 30`.

# COMMAND ----------

display(spark_df.filter(spark_df.bmi > 30))

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC display(spark_df.filter(spark_df.bmi > 30))
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: lisez le filtre comme une phrase: "je garde les lignes où BMI est supérieur à 30".

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 5 - Agréger
# MAGIC
# MAGIC Spark utilise des fonctions d'agrégation comme `avg`.
# MAGIC
# MAGIC Il faut d'abord importer la fonction:
# MAGIC
# MAGIC ```python
# MAGIC from pyspark.sql.functions import avg
# MAGIC ```

# COMMAND ----------

from pyspark.sql.functions import avg

display(
    spark_df
    .groupBy("region")
    .agg(avg("charges").alias("avg_charges"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Calculez la moyenne de `charges` par `smoker`.

# COMMAND ----------

display(
    spark_df
    .groupBy("smoker")
    .agg(avg("charges").alias("avg_charges"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC display(
# MAGIC     spark_df
# MAGIC     .groupBy("smoker")
# MAGIC     .agg(avg("charges").alias("avg_charges"))
# MAGIC )
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: nommez les colonnes agrégées avec `.alias(...)` pour obtenir une table lisible.


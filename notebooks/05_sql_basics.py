# Databricks notebook source
# MAGIC %md
# MAGIC # 05 - SQL Basics dans Databricks
# MAGIC
# MAGIC Objectif: utiliser SQL dans un notebook Databricks à partir d'un Spark DataFrame.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 1 - Créer une vue temporaire
# MAGIC
# MAGIC SQL ne peut pas interroger directement la variable Python `spark_df`.
# MAGIC
# MAGIC On crée donc une vue temporaire:
# MAGIC
# MAGIC ```python
# MAGIC spark_df.createOrReplaceTempView("insurance")
# MAGIC ```
# MAGIC
# MAGIC Ensuite, les cellules `%sql` peuvent interroger `insurance`.

# COMMAND ----------

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

spark_df.createOrReplaceTempView("insurance")

# COMMAND ----------

# MAGIC %md
# MAGIC **Bonne pratique**: donnez à la vue SQL un nom simple et métier.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 2 - Prévisualiser
# MAGIC
# MAGIC Commande SQL:
# MAGIC
# MAGIC ```sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC LIMIT 10
# MAGIC ```

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Modifiez `LIMIT 10` en `LIMIT 5`.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC LIMIT 5

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC LIMIT 5
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: utilisez toujours `LIMIT` pour prévisualiser une table.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 3 - Compter
# MAGIC
# MAGIC ```sql
# MAGIC SELECT COUNT(*) AS row_count
# MAGIC FROM insurance
# MAGIC ```

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS row_count
# MAGIC FROM insurance

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Exécutez la requête et vérifiez que le volume correspond au fichier attendu.

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Le dataset synthétique contient 420 lignes.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: compter les lignes est un premier contrôle de chargement.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 4 - Agréger avec GROUP BY
# MAGIC
# MAGIC Très proche de `PROC SQL`.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT region,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez `region` par `smoker`.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY smoker
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```sql
# MAGIC SELECT smoker,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY smoker
# MAGIC ORDER BY avg_charges DESC
# MAGIC ```
# MAGIC
# MAGIC Interprétez: quel statut fumeur a les charges moyennes les plus élevées?
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: ajoutez `ORDER BY` pour lire les segments du plus élevé au plus faible.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 5 - Filtrer avec WHERE

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC WHERE smoker = 'yes'
# MAGIC LIMIT 20

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Filtrez les lignes avec `age > 50`.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC WHERE age > 50
# MAGIC LIMIT 20

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC WHERE age > 50
# MAGIC LIMIT 20
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: dans SQL, les textes sont entre apostrophes: `'yes'`.


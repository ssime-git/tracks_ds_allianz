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
# MAGIC 5. À retenir.

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
# MAGIC **À retenir**: ne cherchez pas à comprendre l'architecture Spark aujourd'hui. Concentrez-vous sur les gestes analytiques.

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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><pre><code class="language-python">spark_df.printSchema()</code></pre>
<p>On doit retrouver <code>age</code>, <code>sex</code>, <code>bmi</code>, <code>children</code>, <code>smoker</code>, <code>region</code>, <code>charges</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: après un chargement Spark, vérifiez toujours le schéma.
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

display(spark_df.select(..., ...))

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><pre><code class="language-python">display(spark_df.select(&quot;smoker&quot;, &quot;charges&quot;))</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: utilisez `display(...)` dans Databricks pour inspecter visuellement les DataFrames Spark.
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

display(spark_df.filter(spark_df.bmi > ...))

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><pre><code class="language-python">display(spark_df.filter(spark_df.bmi &gt; 30))</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: lisez le filtre comme une phrase: "je garde les lignes où BMI est supérieur à 30".
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
    .groupBy(...)
    .agg(avg("charges").alias("avg_charges"))
)

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><pre><code class="language-python">display(
spark_df
.groupBy(&quot;smoker&quot;)
.agg(avg(&quot;charges&quot;).alias(&quot;avg_charges&quot;))
)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: nommez les colonnes agrégées avec `.alias(...)` pour obtenir une table lisible.

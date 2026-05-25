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
# MAGIC **À retenir**: donnez à la vue SQL un nom simple et métier.

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
# MAGIC LIMIT <à remplacer>

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
<div><pre><code class="language-sql">SELECT *
FROM insurance
LIMIT 5</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: utilisez toujours `LIMIT` pour prévisualiser une table.
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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><p>Le dataset synthétique contient 420 lignes.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: compter les lignes est un premier contrôle de chargement.
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
# MAGIC GROUP BY <à remplacer>
# MAGIC ORDER BY avg_charges DESC

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
<div><pre><code class="language-sql">SELECT smoker,
AVG(charges) AS avg_charges
FROM insurance
GROUP BY smoker
ORDER BY avg_charges DESC</code></pre>
<p>Interprétez: quel statut fumeur a les charges moyennes les plus élevées?</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: ajoutez `ORDER BY` pour lire les segments du plus élevé au plus faible.
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
# MAGIC WHERE <condition à remplacer>
# MAGIC LIMIT 20

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
<div><pre><code class="language-sql">SELECT *
FROM insurance
WHERE age &gt; 50
LIMIT 20</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: dans SQL, les textes sont entre apostrophes: `'yes'`.

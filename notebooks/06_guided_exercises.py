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
# MAGIC 5. À retenir.

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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><p>- Nombre de lignes attendu: 420.</p>
<p>- Colonne cible: <code>charges</code>.</p>
<p>- Exemples de segmentation: <code>smoker</code>, <code>region</code>, <code>sex</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: une exploration doit produire une vérification concrète, pas seulement afficher une table.
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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><pre><code class="language-python">df[df[&quot;bmi&quot;] &gt; 30].head()</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: lisez un filtre comme une phrase métier.
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

df.groupby(...)["charges"].mean()

# COMMAND ----------

df.groupby(...)["charges"].mean()

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
<div><pre><code class="language-python">df.groupby(&quot;smoker&quot;)[&quot;charges&quot;].mean()
df.groupby(&quot;sex&quot;)[&quot;charges&quot;].mean()</code></pre>
<p>Interprétez toujours le segment le plus élevé.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: une moyenne par groupe doit être triée ou comparée explicitement.
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

display(spark_df.groupBy(...).agg(avg("charges").alias("avg_charges")))

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
<div><pre><code class="language-python">display(spark_df.groupBy(&quot;region&quot;).agg(avg(&quot;charges&quot;).alias(&quot;avg_charges&quot;)))</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: en Spark, nommez toujours les résultats agrégés avec `alias`.
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
<div><pre><code class="language-sql">SELECT region,
AVG(charges) AS avg_charges
FROM insurance
GROUP BY region
ORDER BY avg_charges DESC</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: `ORDER BY ... DESC` facilite la lecture du segment le plus élevé.
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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><p>Exemple de phrase:</p>
<p>> Dans ce dataset, les fumeurs de plus de 50 ans présentent les charges moyennes les plus élevées. Ce résultat doit être interprété comme un signal descriptif, pas comme une conclusion causale.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: distinguez toujours observation descriptive et conclusion causale.

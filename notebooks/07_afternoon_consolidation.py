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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><p>1. Colonne cible pour l'analyse: <code>charges</code>.</p>
<p>2. Statut fumeur: <code>smoker</code>.</p>
<p>3. Coût médical: <code>charges</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: nommer la colonne cible avant de filtrer évite de manipuler la mauvaise variable.
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

older_than_50 = df[df["age"] > ...]

older_than_50.head()

# COMMAND ----------

len(older_than_50)

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
<div><pre><code class="language-python">older_than_50 = df[df[&quot;age&quot;] &gt; 50]
older_than_50.head()
len(older_than_50)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: stocker un filtre dans une variable (`older_than_50`) rend la suite plus lisible.
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

high_bmi_smokers = df[(df["bmi"] > ...) & (df["smoker"] == ...)]

high_bmi_smokers.head()

# COMMAND ----------

len(high_bmi_smokers)

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
<div><pre><code class="language-python">high_bmi_smokers = df[(df[&quot;bmi&quot;] &gt; 30) &amp; (df[&quot;smoker&quot;] == &quot;yes&quot;)]
high_bmi_smokers.head()
len(high_bmi_smokers)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: pour combiner des conditions pandas, utilisez `&` et mettez chaque condition entre parenthèses.
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
<div><pre><code class="language-python">df.groupby(&quot;region&quot;)[&quot;charges&quot;].mean()</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: après une moyenne par groupe, cherchez le groupe le plus élevé et le plus faible.
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
    .groupby(...)["charges"]
    .mean()
    .sort_values(ascending=False)
)

avg_by_smoker

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
<div><pre><code class="language-python">avg_by_smoker = (
df
.groupby(&quot;smoker&quot;)[&quot;charges&quot;]
.mean()
.sort_values(ascending=False)
)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: trier un résultat agrégé évite de tirer une conclusion trop vite.
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
    .groupBy(...)
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
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
.groupBy(&quot;region&quot;)
.agg(
count(&quot;*&quot;).alias(&quot;row_count&quot;),
avg(&quot;charges&quot;).alias(&quot;avg_charges&quot;)
)
)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: ajouter `row_count` aide à vérifier qu'un segment n'est pas trop petit.
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
COUNT(*) AS row_count,
AVG(charges) AS avg_charges
FROM insurance
GROUP BY region
ORDER BY avg_charges DESC</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: comparer pandas, Spark et SQL aide à séparer la logique métier de la syntaxe.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Étape 8 - Phrase métier
# MAGIC
# MAGIC Complétez:
# MAGIC
# MAGIC > Dans ce dataset, le segment avec la moyenne de charges la plus élevée est ... La différence observée est descriptive et ne prouve pas une causalité.

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
<div><p>> Dans ce dataset, les fumeurs ont des charges moyennes plus élevées que les non-fumeurs. C'est une observation descriptive sur ce fichier; elle ne suffit pas à prouver une causalité.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: terminer une analyse par une phrase métier courte et prudente.

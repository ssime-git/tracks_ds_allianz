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

df_with_segments[...].value_counts()

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
<div><pre><code class="language-python">df_with_segments[&quot;age_segment&quot;].value_counts()</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: quand vous créez un segment, vérifiez toujours sa répartition.
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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><p>> Les charges moyennes sont plus élevées pour les fumeurs que pour les non-fumeurs dans ce dataset.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: commencez par une analyse simple avant de croiser plusieurs dimensions.
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
    .groupby(..., observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

age_segment_summary

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
<div><pre><code class="language-python">age_segment_summary = (
df_with_segments
.groupby(&quot;age_segment&quot;, observed=True)
.agg(
row_count=(&quot;charges&quot;, &quot;size&quot;),
avg_charges=(&quot;charges&quot;, &quot;mean&quot;)
)
.sort_values(&quot;avg_charges&quot;, ascending=False)
)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: une moyenne sans nombre de lignes peut être trompeuse.
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
    .groupby(["smoker", ...], observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

region_smoker_summary

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
<div><pre><code class="language-python">region_smoker_summary = (
df_with_segments
.groupby([&quot;smoker&quot;, &quot;region&quot;], observed=True)
.agg(
row_count=(&quot;charges&quot;, &quot;size&quot;),
avg_charges=(&quot;charges&quot;, &quot;mean&quot;)
)
.sort_values(&quot;avg_charges&quot;, ascending=False)
)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: plus on croise de dimensions, plus il faut surveiller `row_count`.
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
# MAGIC GROUP BY smoker, <à remplacer>
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
region,
COUNT(*) AS row_count,
AVG(charges) AS avg_charges
FROM insurance_segments
GROUP BY smoker, region
ORDER BY avg_charges DESC</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: SQL est très utile pour relire une analyse de segmentation de manière transparente.
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

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Afficher la correction</summary>
<div><p>Le segment avec les charges moyennes les plus élevées est généralement lié au statut fumeur, en particulier lorsqu'il est croisé avec une tranche d'âge élevée. Le résultat est basé sur une moyenne de <code>charges</code> par segment et doit être relu avec le nombre de lignes par groupe. Cette analyse est descriptive: elle montre une association dans le dataset, mais ne prouve pas une causalité.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: une conclusion d'analyse doit toujours mentionner la mesure, le segment et la limite.

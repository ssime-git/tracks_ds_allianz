# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - pandas Basics
# MAGIC
# MAGIC Pattern répété:
# MAGIC
# MAGIC 1. Concept.
# MAGIC 2. Explication de la commande.
# MAGIC 3. Pratique guidée.
# MAGIC 4. Correction masquée.
# MAGIC 5. À retenir.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 1 - Importer pandas
# MAGIC
# MAGIC `pandas` est un package Python pour manipuler des tables.
# MAGIC
# MAGIC La convention standard est:
# MAGIC
# MAGIC ```python
# MAGIC import pandas as pd
# MAGIC ```
# MAGIC
# MAGIC Lire: "je rends pandas disponible sous le nom court `pd`".

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: gardez la convention `pd`. Elle est comprise par la majorité des analystes Python.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 2 - Charger une table CSV
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")
# MAGIC ```
# MAGIC
# MAGIC Lecture:
# MAGIC
# MAGIC - `pd.read_csv(...)` lit un fichier CSV,
# MAGIC - le chemin commence par `/dbfs` car pandas lit via le système de fichiers Databricks,
# MAGIC - le résultat est stocké dans `df`.

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Exécutez une commande pour vérifier le type de l'objet `df`.

# COMMAND ----------

type(...)

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
<div><p>Le type attendu est:</p>
<pre><code class="language-text">pandas.core.frame.DataFrame</code></pre>
<p>C'est la table pandas.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: après un chargement, vérifiez toujours que la table existe avant de continuer.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 3 - Contrôler la table
# MAGIC
# MAGIC Trois commandes de contrôle:
# MAGIC
# MAGIC | Commande | Question |
# MAGIC |---|---|
# MAGIC | `df.head()` | À quoi ressemblent les premières lignes? |
# MAGIC | `df.info()` | Quelles colonnes et quels types? |
# MAGIC | `df.describe()` | Quels ordres de grandeur numériques? |

# COMMAND ----------

df.head()

# COMMAND ----------

df.info()

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Complétez avec une commande pour afficher la liste des colonnes de `df`.

# COMMAND ----------

...

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
<div><pre><code class="language-python">df.columns</code></pre>
<p>Colonnes attendues: <code>age</code>, <code>sex</code>, <code>bmi</code>, <code>children</code>, <code>smoker</code>, <code>region</code>, <code>charges</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: ne filtrez jamais avant d'avoir regardé les colonnes et les types.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 4 - Sélectionner des colonnes
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC df[["age", "charges"]]
# MAGIC ```
# MAGIC
# MAGIC Les doubles crochets signifient: "je veux plusieurs colonnes".

# COMMAND ----------

df[["age", "charges"]].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Sélectionnez les colonnes `smoker` et `charges`, puis affichez les premières lignes.

# COMMAND ----------

df[[..., ...]].head()

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
<div><pre><code class="language-python">df[[&quot;smoker&quot;, &quot;charges&quot;]].head()</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: sélectionnez uniquement les colonnes utiles quand vous préparez une analyse.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 5 - Filtrer des lignes
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC df[df["smoker"] == "yes"]
# MAGIC ```
# MAGIC
# MAGIC Lecture:
# MAGIC
# MAGIC - `df["smoker"] == "yes"` pose une question vrai/faux à chaque ligne,
# MAGIC - `df[...]` garde les lignes où la réponse est vraie.

# COMMAND ----------

df[df["smoker"] == "yes"].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Créez un filtre pour garder les personnes avec `bmi > 30`.

# COMMAND ----------

df[df[...] > ...].head()

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
# MAGIC **À retenir**: utilisez `==` pour comparer, pas `=`. Un seul `=` sert à affecter une valeur.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 6 - Trier
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC df.sort_values("charges", ascending=False)
# MAGIC ```
# MAGIC
# MAGIC Lire: trier la table par `charges`, du plus grand au plus petit.

# COMMAND ----------

df.sort_values("charges", ascending=False).head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Triez par `bmi`, du plus grand au plus petit.

# COMMAND ----------

df.sort_values(..., ascending=...).head()

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
<div><pre><code class="language-python">df.sort_values(&quot;bmi&quot;, ascending=False).head()</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: après un tri, lisez les premières lignes et vérifiez que l'ordre est celui attendu.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 7 - Agréger avec groupby
# MAGIC
# MAGIC Équivalent mental de `PROC MEANS` avec une variable de classe.
# MAGIC
# MAGIC ```python
# MAGIC df.groupby("region")["charges"].mean()
# MAGIC ```
# MAGIC
# MAGIC Lecture:
# MAGIC
# MAGIC - grouper par `region`,
# MAGIC - prendre la colonne `charges`,
# MAGIC - calculer la moyenne.

# COMMAND ----------

df.groupby("region")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Calculez la moyenne de `charges` par `smoker`.

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
<div><pre><code class="language-python">df.groupby(&quot;smoker&quot;)[&quot;charges&quot;].mean()</code></pre>
<p>Interprétez le résultat: les charges moyennes sont-elles plus élevées chez les fumeurs?</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: une agrégation doit toujours finir par une phrase métier.

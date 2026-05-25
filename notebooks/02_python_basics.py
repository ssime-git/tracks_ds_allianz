# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Python Basics pour analystes SAS
# MAGIC
# MAGIC Pattern de travail dans ce notebook:
# MAGIC
# MAGIC 1. **Concept**: ce que l'on veut comprendre.
# MAGIC 2. **Commande**: lecture lente de la syntaxe.
# MAGIC 3. **À vous**: modification guidée, jamais page blanche.
# MAGIC 4. **Correction masquée**: ouvrez seulement après avoir essayé.
# MAGIC 5. **À retenir**: règle à retenir.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 1 - Python, modules et packages
# MAGIC
# MAGIC Python est le langage. Un **module** est un fichier de code réutilisable. Un **package** regroupe plusieurs modules.
# MAGIC
# MAGIC Dans Databricks, beaucoup d'outils sont déjà disponibles dans l'environnement d'exécution:
# MAGIC
# MAGIC - `pandas` pour les tables en mémoire,
# MAGIC - `pyspark` pour les DataFrames Spark,
# MAGIC - des modules Python standards comme `math`.
# MAGIC
# MAGIC La commande `import` rend un module ou package disponible dans le notebook.

# COMMAND ----------

import math

math.sqrt(16)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Utilisez la même commande pour calculer la racine carrée de `25`.

# COMMAND ----------

math.sqrt(...)

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
<div><pre><code class="language-python">math.sqrt(25)</code></pre>
<p>Résultat attendu: <code>5.0</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: quand vous voyez `import`, demandez-vous toujours: quel outil rend-on disponible?
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 2 - Variables
# MAGIC
# MAGIC Une variable donne un nom à une valeur. Pour un analyste, c'est utile pour stocker un seuil, une modalité ou un montant.
# MAGIC
# MAGIC Lecture de la commande:
# MAGIC
# MAGIC ```python
# MAGIC age = 45
# MAGIC ```
# MAGIC
# MAGIC Lire: "je stocke la valeur 45 dans le nom age".

# COMMAND ----------

age = 45
region = "southwest"
premium = 1200.50

print(age)
print(region)
print(premium)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Complétez la cellule pour:
# MAGIC
# MAGIC 1. créer `age` avec la valeur `52`,
# MAGIC 2. créer `region` avec la valeur `"northeast"`,
# MAGIC 3. garder `premium` à `1200.50`,
# MAGIC 4. afficher les trois valeurs.

# COMMAND ----------

age = ...
region = ...
premium = ...

# Afficher les trois variables

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
<div><pre><code class="language-python">age = 52
region = &quot;northeast&quot;
premium = 1200.50

print(age)
print(region)
print(premium)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: utilisez des noms simples et métier: `age`, `region`, `premium`, plutôt que `x`, `var1`, `tmp`.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 3 - Types de données
# MAGIC
# MAGIC Python distingue plusieurs types. Les quatre premiers à reconnaître:
# MAGIC
# MAGIC | Type | Exemple | Usage |
# MAGIC |---|---|---|
# MAGIC | `int` | `45` | entier |
# MAGIC | `float` | `27.5` | nombre décimal |
# MAGIC | `str` | `"southwest"` | texte |
# MAGIC | `bool` | `True` | vrai/faux |

# COMMAND ----------

age = 45
bmi = 27.5
region = "southwest"
is_smoker = True

print(type(age))
print(type(bmi))
print(type(region))
print(type(is_smoker))

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Complétez avec les valeurs suivantes, puis observez les types:
# MAGIC
# MAGIC - `age = 54`
# MAGIC - `bmi = 31.2`
# MAGIC - `region = "southeast"`
# MAGIC - `is_smoker = False`

# COMMAND ----------

age = ...
bmi = ...
region = ...
is_smoker = ...

print(type(age))
print(type(bmi))
print(type(region))
print(type(is_smoker))

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
<div><p>Les valeurs peuvent changer sans changer le type:</p>
<p>- <code>54</code> reste un <code>int</code>,</p>
<p>- <code>31.2</code> reste un <code>float</code>,</p>
<p>- <code>"southeast"</code> reste un <code>str</code>,</p>
<p>- <code>False</code> reste un <code>bool</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: avant de filtrer ou calculer, vérifiez si vous manipulez un nombre ou du texte.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 4 - Conditions
# MAGIC
# MAGIC Une condition répond à une question vrai/faux.
# MAGIC
# MAGIC SAS:
# MAGIC
# MAGIC ```sas
# MAGIC if age > 50 then segment = "senior";
# MAGIC ```
# MAGIC
# MAGIC Python:
# MAGIC
# MAGIC ```python
# MAGIC if age > 50:
# MAGIC     segment = "senior"
# MAGIC ```
# MAGIC
# MAGIC Le `:` ouvre le bloc. L'indentation indique ce qui appartient au bloc.

# COMMAND ----------

age = 54

if age > 50:
    segment = "senior"
else:
    segment = "non senior"

segment

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Complétez avec `age = 35`. Avant d'exécuter, prédisez le résultat.

# COMMAND ----------

age = ...

if age > 50:
    segment = "senior"
else:
    segment = "non senior"

segment

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
<div><p>Avec <code>age = 35</code>, la condition <code>age > 50</code> est fausse. Le résultat est:</p>
<pre><code class="language-python">&quot;non senior&quot;</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: lisez toujours une condition avant de l'exécuter: variable, opérateur, seuil.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 5 - Fonction
# MAGIC
# MAGIC Une fonction donne un nom à une règle réutilisable.
# MAGIC
# MAGIC Ici, la règle convertit un coût mensuel en coût annuel.

# COMMAND ----------

def annual_cost(monthly_cost):
    return monthly_cost * 12

annual_cost(120)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Appelez la fonction deux fois:
# MAGIC
# MAGIC 1. avec `250`,
# MAGIC 2. avec `80`.

# COMMAND ----------

annual_cost(...)

# COMMAND ----------

annual_cost(...)

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
<div><pre><code class="language-python">annual_cost(250)  # 3000
annual_cost(80)   # 960</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: une fonction doit avoir un nom qui décrit la règle métier.

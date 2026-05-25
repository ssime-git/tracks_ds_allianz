# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Introduction à Azure Databricks
# MAGIC
# MAGIC Objectif: ouvrir un notebook, exécuter des cellules et comprendre où sont le code, la donnée et le résultat.
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
# MAGIC ## Concept 1 - Notebook
# MAGIC
# MAGIC Un notebook mélange:
# MAGIC
# MAGIC - du texte explicatif,
# MAGIC - du code,
# MAGIC - des résultats.
# MAGIC
# MAGIC Équivalence SAS:
# MAGIC
# MAGIC | SAS | Databricks |
# MAGIC |---|---|
# MAGIC | Programme SAS | Notebook |
# MAGIC | Bloc de code | Cellule |
# MAGIC | Log / output | Résultat sous la cellule |

# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: exécutez cellule par cellule au début. Évitez `Run all` tant que vous apprenez.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 2 - Première cellule Python
# MAGIC
# MAGIC Commande d'affichage:
# MAGIC
# MAGIC pour afficher en python, on utilise la commande `print()` en lui passant en argument ce que l'on veut afficher. Par exemple pour afficher le texte "Hello Databricks", on écrit:
# MAGIC
# MAGIC ```python
# MAGIC print("Hello Databricks")
# MAGIC ```
# MAGIC
# MAGIC Exécutez cette cellule pour afficher le texte entre guillemets.

# COMMAND ----------

print("Hello Databricks")

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez le texte par votre prénom ou par le nom de votre équipe.

# COMMAND ----------

print("Hello Allianz")

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
<div><p>Exemple:</p>
<pre><code class="language-python">print(&quot;Hello Allianz&quot;)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: après exécution, regardez toujours où apparaît le résultat.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 3 - Variables
# MAGIC
# MAGIC Une variable donne un nom à une valeur. Le code ci-dessous permet de créer deux variables: `age` et `region` en leur assignant des valeurs avec l'opérateur `=`.

# MAGIC
# MAGIC Exécutez cette cellule pour créer les variables et les afficher. (Sans exécution, rien ne se passe et vos modifications ne seront pas pris en compte.)

# COMMAND ----------

age = 45
region = "North"

print(age)
print(region)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Complétez la cellule ci-dessous pour:
# MAGIC
# MAGIC 1. mettre `age` à `52`,
# MAGIC 2. mettre `region` à `"South"`,
# MAGIC 3. afficher les deux valeurs avec `print()`.

# COMMAND ----------

age = ...
region = ...

# Afficher les deux variables

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
<div><pre><code>age = 52
region = "South"

print(age)
print(region)</code></pre>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: si le résultat ne change pas, vérifiez que vous avez exécuté la bonne cellule.
# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 4 - Calcul simple
# MAGIC
# MAGIC En Python, on peut faire des calculs directement avec les variables.
# MAGIC
# MAGIC Par exemple:
# MAGIC
# MAGIC ```python
# MAGIC premium = 1000
# MAGIC premium_with_tax = premium * 1.2
# MAGIC ```
# MAGIC
# MAGIC Ici, `premium_with_tax` reçoit le résultat du calcul.

# COMMAND ----------

premium = 1000
premium_with_tax = premium * 1.2

premium_with_tax

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Complétez la cellule ci-dessous pour:
# MAGIC
# MAGIC 1. créer une variable `premium` avec la valeur `1500`,
# MAGIC 2. créer une variable `premium_with_tax`,
# MAGIC 3. afficher le résultat.

# COMMAND ----------

premium = ...
premium_with_tax = ...

premium_with_tax

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
<div><pre><code>premium = 1500
premium_with_tax = premium * 1.2

premium_with_tax</code></pre>
<p>Résultat attendu: <code>1800</code>.</p>
</div>
</details>
""")
# COMMAND ----------

# MAGIC %md
# MAGIC **À retenir**: gardez une cellule courte quand vous découvrez une nouvelle commande.

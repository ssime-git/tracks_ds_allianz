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
# MAGIC 5. **Bonne pratique**: règle à retenir.

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
# MAGIC Remplacez `16` par `25`, puis exécutez la cellule.

# COMMAND ----------

math.sqrt(25)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC math.sqrt(25)
# MAGIC ```
# MAGIC
# MAGIC Résultat attendu: `5.0`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: quand vous voyez `import`, demandez-vous toujours: quel outil rend-on disponible?

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
# MAGIC 1. Remplacez `age` par `52`.
# MAGIC 2. Remplacez `region` par `"northeast"`.
# MAGIC 3. Ré-exécutez la cellule.

# COMMAND ----------

age = 52
region = "northeast"
premium = 1200.50

print(age)
print(region)
print(premium)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC age = 52
# MAGIC region = "northeast"
# MAGIC premium = 1200.50
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: utilisez des noms simples et métier: `age`, `region`, `premium`, plutôt que `x`, `var1`, `tmp`.

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
# MAGIC Modifiez les valeurs, puis observez si les types changent.

# COMMAND ----------

age = 54
bmi = 31.2
region = "southeast"
is_smoker = False

print(type(age))
print(type(bmi))
print(type(region))
print(type(is_smoker))

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Les valeurs peuvent changer sans changer le type:
# MAGIC
# MAGIC - `54` reste un `int`,
# MAGIC - `31.2` reste un `float`,
# MAGIC - `"southeast"` reste un `str`,
# MAGIC - `False` reste un `bool`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: avant de filtrer ou calculer, vérifiez si vous manipulez un nombre ou du texte.

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
# MAGIC Remplacez `age = 54` par `age = 35`. Avant d'exécuter, prédisez le résultat.

# COMMAND ----------

age = 35

if age > 50:
    segment = "senior"
else:
    segment = "non senior"

segment

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Avec `age = 35`, la condition `age > 50` est fausse. Le résultat est:
# MAGIC
# MAGIC ```python
# MAGIC "non senior"
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: lisez toujours une condition avant de l'exécuter: variable, opérateur, seuil.

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
# MAGIC 1. Remplacez `120` par `250`.
# MAGIC 2. Créez un deuxième appel avec `annual_cost(80)`.

# COMMAND ----------

annual_cost(250)

# COMMAND ----------

annual_cost(80)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC annual_cost(250)  # 3000
# MAGIC annual_cost(80)   # 960
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: une fonction doit avoir un nom qui décrit la règle métier.


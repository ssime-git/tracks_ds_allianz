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
# MAGIC 5. Bonne pratique.

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
# MAGIC **Bonne pratique**: exécutez cellule par cellule au début. Évitez `Run all` tant que vous apprenez.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 2 - Première cellule Python
# MAGIC
# MAGIC Commande:
# MAGIC
# MAGIC ```python
# MAGIC print("Hello Databricks")
# MAGIC ```
# MAGIC
# MAGIC Lire: afficher le texte entre guillemets.

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

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Exemple:
# MAGIC
# MAGIC ```python
# MAGIC print("Hello Allianz")
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: après exécution, regardez toujours où apparaît le résultat.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 3 - Variables
# MAGIC
# MAGIC Une variable donne un nom à une valeur.

# COMMAND ----------

age = 45
region = "North"

print(age)
print(region)

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Changez `age` et `region`, puis ré-exécutez la cellule.

# COMMAND ----------

age = 52
region = "South"

print(age)
print(region)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Toute valeur est acceptable si le résultat affiché correspond à votre modification.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: si le résultat ne change pas, vérifiez que vous avez exécuté la bonne cellule.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concept 4 - Calcul simple

# COMMAND ----------

premium = 1000
premium_with_tax = premium * 1.2

premium_with_tax

# COMMAND ----------

# MAGIC %md
# MAGIC ### À vous
# MAGIC
# MAGIC Remplacez `premium = 1000` par `premium = 1500`.

# COMMAND ----------

premium = 1500
premium_with_tax = premium * 1.2

premium_with_tax

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Avec `premium = 1500`, le résultat attendu est `1800`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: gardez une cellule courte quand vous découvrez une nouvelle commande.


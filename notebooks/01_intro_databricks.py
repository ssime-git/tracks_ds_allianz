# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Introduction à Azure Databricks
# MAGIC
# MAGIC Objectif: apprendre à ouvrir un notebook, exécuter des cellules et comprendre le rôle du cluster.
# MAGIC
# MAGIC Équivalence SAS:
# MAGIC
# MAGIC | SAS | Databricks |
# MAGIC |---|---|
# MAGIC | Programme SAS | Notebook |
# MAGIC | Exécuter un bloc de code | Exécuter une cellule |
# MAGIC | Log SAS | Résultat de cellule |
# MAGIC | Bibliothèque SAS | Espace de stockage / catalogue |

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Première cellule Python
# MAGIC
# MAGIC Cliquez dans la cellule, puis utilisez **Run cell**.

# COMMAND ----------

print("Hello Databricks")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Variables
# MAGIC
# MAGIC Une variable est un nom donné à une valeur. En SAS, on manipule souvent des colonnes ou des macro-variables. En Python, on commence par des variables simples.

# COMMAND ----------

age = 45
region = "North"

print(age)
print(region)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Calcul simple
# MAGIC
# MAGIC Le signe `=` stocke une valeur. Le signe `*` multiplie.

# COMMAND ----------

premium = 1000
premium_with_tax = premium * 1.2

premium_with_tax

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Listes
# MAGIC
# MAGIC Une liste contient plusieurs valeurs. Elle est pratique pour représenter un ensemble de modalités.

# COMMAND ----------

regions = ["North", "South", "East", "West"]

regions

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Fonction simple
# MAGIC
# MAGIC Une fonction permet de réutiliser une règle de calcul.

# COMMAND ----------

def annual_cost(monthly_cost):
    return monthly_cost * 12

annual_cost(120)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mini-exercice guidé
# MAGIC
# MAGIC 1. Remplacez `120` par `250`.
# MAGIC 2. Ré-exécutez la cellule.
# MAGIC 3. Vérifiez que le résultat correspond à un coût annuel.


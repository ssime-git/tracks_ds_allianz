# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - pandas Basics
# MAGIC
# MAGIC Objectif: manipuler une table avec pandas.
# MAGIC
# MAGIC Équivalence SAS:
# MAGIC
# MAGIC | SAS | pandas |
# MAGIC |---|---|
# MAGIC | SAS dataset | DataFrame |
# MAGIC | PROC PRINT | `head()` |
# MAGIC | PROC CONTENTS | `info()` |
# MAGIC | PROC MEANS | `describe()` / `groupby()` |

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Charger le CSV

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Premières lignes

# COMMAND ----------

df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Structure et statistiques

# COMMAND ----------

df.info()

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Sélectionner des colonnes

# COMMAND ----------

df[["age", "charges"]].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Filtrer des lignes
# MAGIC
# MAGIC Exemple: uniquement les fumeurs.

# COMMAND ----------

df[df["smoker"] == "yes"].head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Trier les valeurs

# COMMAND ----------

df.sort_values("charges", ascending=False).head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Agréger avec groupby
# MAGIC
# MAGIC Très proche de l'esprit `PROC MEANS` avec une variable de classe.

# COMMAND ----------

df.groupby("region")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mini workflow métier
# MAGIC
# MAGIC Question: les charges moyennes sont-elles plus élevées chez les fumeurs?

# COMMAND ----------

df.groupby("smoker")["charges"].mean()


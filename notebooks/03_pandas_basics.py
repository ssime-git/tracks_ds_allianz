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
# MAGIC 5. Bonne pratique.

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
# MAGIC **Bonne pratique**: gardez la convention `pd`. Elle est comprise par la majorité des analystes Python.

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
# MAGIC Exécutez la cellule ci-dessous pour vérifier le type de l'objet `df`.

# COMMAND ----------

type(df)

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC Le type attendu est:
# MAGIC
# MAGIC ```text
# MAGIC pandas.core.frame.DataFrame
# MAGIC ```
# MAGIC
# MAGIC C'est la table pandas.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: après un chargement, vérifiez toujours que la table existe avant de continuer.

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
# MAGIC Complétez avec une commande pour afficher la liste des colonnes.

# COMMAND ----------

df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df.columns
# MAGIC ```
# MAGIC
# MAGIC Colonnes attendues: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`.
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: ne filtrez jamais avant d'avoir regardé les colonnes et les types.

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
# MAGIC Sélectionnez les colonnes `smoker` et `charges`.

# COMMAND ----------

df[["smoker", "charges"]].head()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df[["smoker", "charges"]].head()
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: sélectionnez uniquement les colonnes utiles quand vous préparez une analyse.

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

df[df["bmi"] > 30].head()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df[df["bmi"] > 30].head()
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: utilisez `==` pour comparer, pas `=`. Un seul `=` sert à affecter une valeur.

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

df.sort_values("bmi", ascending=False).head()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df.sort_values("bmi", ascending=False).head()
# MAGIC ```
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: après un tri, lisez les premières lignes et vérifiez que l'ordre est celui attendu.

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

df.groupby("smoker")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC <details>
# MAGIC <summary>Correction masquée</summary>
# MAGIC
# MAGIC ```python
# MAGIC df.groupby("smoker")["charges"].mean()
# MAGIC ```
# MAGIC
# MAGIC Interprétez le résultat: les charges moyennes sont-elles plus élevées chez les fumeurs?
# MAGIC </details>
# MAGIC
# MAGIC **Bonne pratique**: une agrégation doit toujours finir par une phrase métier.


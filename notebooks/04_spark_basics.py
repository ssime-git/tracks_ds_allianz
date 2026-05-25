# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - Spark Basics
# MAGIC
# MAGIC Objectif: découvrir les DataFrames Spark sans entrer dans les détails distribués.
# MAGIC
# MAGIC Message clé: Spark manipule aussi des tables, mais il est fait pour des volumes plus grands.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Lire le CSV avec Spark

# COMMAND ----------

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Afficher la table

# COMMAND ----------

display(spark_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Sélectionner des colonnes

# COMMAND ----------

display(spark_df.select("age", "charges"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Filtrer des lignes

# COMMAND ----------

display(spark_df.filter(spark_df.age > 50))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. GroupBy

# COMMAND ----------

from pyspark.sql.functions import avg

display(
    spark_df
    .groupBy("region")
    .agg(avg("charges").alias("avg_charges"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lecture SAS
# MAGIC
# MAGIC Cette cellule correspond à l'esprit suivant:
# MAGIC
# MAGIC ```sas
# MAGIC proc means data=insurance mean;
# MAGIC   class region;
# MAGIC   var charges;
# MAGIC run;
# MAGIC ```


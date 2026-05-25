# Databricks notebook source
# MAGIC %md
# MAGIC # 05 - SQL Basics dans Databricks
# MAGIC
# MAGIC Objectif: réutiliser SQL dans un notebook Databricks.

# COMMAND ----------

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

spark_df.createOrReplaceTempView("insurance")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Prévisualiser

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Compter les lignes

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS row_count
# MAGIC FROM insurance

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Agréger

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT region,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Filtrer

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC WHERE smoker = 'yes'
# MAGIC LIMIT 20


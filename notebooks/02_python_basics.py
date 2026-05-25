# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Python Basics pour analystes SAS
# MAGIC
# MAGIC Objectif: lire et modifier du Python simple, sans théorie avancée.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Types de données

# COMMAND ----------

age = 45                 # entier
bmi = 27.5               # nombre décimal
region = "southwest"     # texte
is_smoker = True         # booléen: vrai ou faux

print(age)
print(bmi)
print(region)
print(is_smoker)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Lire une condition
# MAGIC
# MAGIC En SAS, on peut écrire `if age > 50 then ...`.
# MAGIC En Python, la logique est très proche.

# COMMAND ----------

age = 54

if age > 50:
    print("Segment: senior")
else:
    print("Segment: non senior")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Indentation
# MAGIC
# MAGIC L'indentation indique quelles lignes appartiennent au `if`.
# MAGIC Les lignes indentées sont exécutées seulement si la condition est vraie.

# COMMAND ----------

smoker = "yes"

if smoker == "yes":
    print("Smoker segment")
    print("Higher risk group")

print("This line is always executed")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Listes et boucle simple
# MAGIC
# MAGIC Cette boucle lit chaque région une par une.

# COMMAND ----------

regions = ["northeast", "northwest", "southeast", "southwest"]

for region in regions:
    print(region)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Fonction métier
# MAGIC
# MAGIC Une fonction isole une règle de calcul, comme une petite règle réutilisable.

# COMMAND ----------

def add_tax(amount):
    return amount * 1.2

add_tax(1000)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mini-exercice guidé
# MAGIC
# MAGIC Complétez la fonction pour appliquer une réduction de 10%.

# COMMAND ----------

def apply_discount(amount):
    return amount * 0.90

apply_discount(1000)


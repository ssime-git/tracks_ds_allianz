# Data Scientist Track - Week 1

Supports de formation pour la semaine 1: **Python Fundamentals in Azure Databricks**.

Public cible:

- utilisateurs SAS,
- niveau débutant en Python,
- niveau débutant en Databricks,
- profil analyste métier / data analyst.

## Livrables

- `slides/week1_python_fundamentals_databricks.pptx`: deck visuel Liora pour une session live de 4h, avec QCM, slides sombres, schémas, bonnes pratiques et appels notebooks.
- `notebooks/01_intro_databricks.py`: découverte de Databricks et des notebooks.
- `notebooks/02_python_basics.py`: bases Python guidées.
- `notebooks/03_pandas_basics.py`: manipulation tabulaire avec pandas.
- `notebooks/04_spark_basics.py`: découverte des DataFrames Spark.
- `notebooks/05_sql_basics.py`: SQL dans Databricks.
- `notebooks/06_guided_exercises.py`: exercices autonomes guidés.
- `data/insurance.csv`: dataset synthétique compatible avec le schéma Kaggle Medical Cost.
- `docs/databricks_setup.md`: instructions d’import dans le workspace.
- `docs/week1_run_of_show.md`: timing détaillé pour tenir les 4h.
- `tools/generate_assets.py`: régénère le dataset.
- `tools/generate_liora_week1_deck.py`: régénère le deck Week 1 avec la charte visuelle Liora.

## Dataset

Le dataset recommandé est Kaggle - Medical Cost Personal Dataset:
<https://www.kaggle.com/datasets/mirichoi0218/insurance>

Pour éviter une dépendance aux identifiants Kaggle pendant la formation, ce repo inclut un dataset synthétique `data/insurance.csv` avec les mêmes colonnes:

- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`
- `charges`

Le fichier peut être remplacé par le CSV Kaggle officiel avant l’import Databricks.

## Import Databricks

1. Créer ou utiliser un cluster single-node.
2. Activer l’auto-termination à 30 minutes.
3. Importer les notebooks dans `/Shared/training`.
4. Charger `data/insurance.csv` dans `/FileStore/tables/insurance.csv`.
5. Exécuter les notebooks dans l’ordre.

## Pattern pédagogique des notebooks

Chaque notebook suit le même rythme:

1. Concept.
2. Explication de la commande.
3. Pratique guidée.
4. Correction masquée.
5. Bonne pratique à retenir.

Voir `docs/databricks_setup.md` pour le détail.

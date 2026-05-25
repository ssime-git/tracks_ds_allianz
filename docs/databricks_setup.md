# Databricks Setup - Week 1

## Cluster recommandé

- Workspace partagé Allianz.
- Cluster single-node.
- Petite taille de VM.
- Auto-termination: 30 minutes.
- Usage pédagogique uniquement.

## Arborescence cible

```text
/Shared/training
├── 01_Intro_Databricks
├── 02_Python_Basics
├── 03_Pandas_Basics
├── 04_Spark_Basics
├── 05_SQL_Basics
└── insurance.csv
```

## Import des notebooks

Importer les fichiers `.py` du dossier `notebooks/` comme notebooks Databricks.

Ordre recommandé:

1. `01_intro_databricks.py`
2. `02_python_basics.py`
3. `03_pandas_basics.py`
4. `04_spark_basics.py`
5. `05_sql_basics.py`
6. `06_guided_exercises.py`

## Upload du CSV

Charger `data/insurance.csv` dans Databricks à l’emplacement:

```text
/FileStore/tables/insurance.csv
```

Dans pandas, le chemin utilisé est:

```python
/dbfs/FileStore/tables/insurance.csv
```

Dans Spark, le chemin utilisé est:

```python
/FileStore/tables/insurance.csv
```

## Points d’attention pour l’animation

- Lire le code ligne par ligne.
- Montrer chaque exécution de cellule.
- Rappeler les équivalences SAS à chaque étape.
- Ne pas expliquer Spark en profondeur.
- Garder les exercices guidés: les apprenants modifient du code existant.


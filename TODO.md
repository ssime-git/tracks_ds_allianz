# TODO - Week 1 Python Fundamentals in Azure Databricks

## Done

- [x] Read the Data Scientist Track PDF and scoped Week 1.
- [x] Created repository structure for slides, notebooks, exercises, data, docs, and tools.
- [x] Created Databricks-ready notebooks for live session and self-paced work.
- [x] Created a visual 4h PowerPoint deck for Week 1 using the Liora visual grammar.
- [x] Added a synthetic training CSV with the same schema as the Kaggle Medical Cost dataset.
- [x] Added setup and import instructions for Databricks.
- [x] Initialized the local Git repository.

## Pending before delivery in Databricks

- [ ] Re-authenticate GitHub CLI: `gh auth login -h github.com`.
- [ ] Create the remote GitHub repository with `gh repo create`.
- [ ] Push the repository once GitHub authentication is fixed.
- [ ] Import notebooks into `/Shared/training` in the Allianz Databricks workspace.
- [ ] Upload `data/insurance.csv` to `/FileStore/tables/insurance.csv`.
- [ ] Run every notebook once on the shared single-node cluster.
- [ ] Optionally replace the synthetic CSV with the Kaggle Medical Cost Personal Dataset.

## Recommended Databricks workspace layout

```text
/Shared/training
├── 01_Intro_Databricks
├── 02_Python_Basics
├── 03_Pandas_Basics
├── 04_Spark_Basics
├── 05_SQL_Basics
└── insurance.csv
```

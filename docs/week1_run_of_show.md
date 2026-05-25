# Week 1 - Run of Show 4h

Objectif: tenir une session live de 4h sans accélérer artificiellement les slides.

## Timing global

| Séquence | Durée | Format |
|---|---:|---|
| Cadrage + mapping SAS | 20 min | discussion guidée |
| Databricks | 40 min | démo + exercice court |
| Python basics | 45 min | lecture de code + binômes |
| Pause | 10 min | pause |
| pandas | 60 min | démo + exercices progressifs |
| Spark | 30 min | traduction pandas vers Spark |
| SQL | 25 min | requêtes guidées |
| Challenge + synthèse | 10 min | restitution courte |
| **Total** | **240 min** | **4h** |

## Après-midi self-paced encadrée

Après la session live de 4h, utiliser deux notebooks progressifs:

| Notebook | Durée indicative | Objectif |
|---|---:|---|
| `07_afternoon_consolidation.py` | 1h30-1h45 | consolider pandas, Spark et SQL sur les mêmes questions |
| `08_afternoon_case_study.py` | 1h30-1h45 | traiter un mini-cas métier avec segmentation et conclusion |

Le notebook 07 reste très guidé. Le notebook 08 augmente légèrement la complexité: création d'une variable `age_segment`, analyses croisées, vérification du nombre de lignes par segment, conclusion métier.

## Règle d'animation

Ne pas présenter les slides comme un cours magistral continu. Les slides "Activité guidée" doivent être réellement jouées:

- lire la consigne,
- laisser 3 à 8 minutes de travail,
- corriger à l'écran,
- demander une phrase d'interprétation.

Les slides sombres servent de rupture de rythme:

- changement de section,
- QCM,
- consigne "allez dans le notebook",
- message méthodologique important.

Quand une slide indique **Allez dans le notebook**, arrêter le deck et faire exécuter le notebook correspondant.

## Points de contrôle

À la fin de la session, chaque apprenant doit avoir:

- ouvert un notebook Databricks,
- attaché un cluster,
- exécuté une cellule Python,
- modifié une variable,
- chargé `insurance.csv`,
- utilisé `head`, `info`, `describe`,
- filtré une table pandas,
- fait un `groupby`,
- traduit une opération en Spark,
- exécuté une requête SQL,
- formulé une conclusion métier courte.

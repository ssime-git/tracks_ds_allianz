#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  createSlideContext,
  ensureArtifactToolWorkspace,
  importArtifactTool,
  saveBlobToFile,
} from "/Users/seb/.codex/plugins/cache/openai-primary-runtime/presentations/26.521.10419/skills/presentations/scripts/artifact_tool_utils.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SKILL_DIR = "/Users/seb/.codex/plugins/cache/openai-primary-runtime/presentations/26.521.10419/skills/presentations";
const WORKSPACE = path.join(ROOT, "outputs", "manual-week1-v3", "presentations", "week1-v3");
const PREVIEW_DIR = path.join(WORKSPACE, "preview");
const OUT = path.join(ROOT, "slides", "week1_python_fundamentals_databricks_v3.pptx");
const NOTES = path.join(ROOT, "slides", "week1_python_fundamentals_databricks_v3_notes.md");

const C = {
  navy: "#1A1A33",
  orange: "#FF6745",
  lime: "#DDFF45",
  cyan: "#00E5EE",
  violet: "#7657FF",
  purple: "#C445FF",
  cream: "#E8E7E1",
  cream2: "#F2F1ED",
  white: "#FFFFFF",
  black: "#000000",
  muted: "#6F6D82",
  softNavy: "#282846",
  pink: "#FFE1DC",
  green: "#C5EFCE",
};

const W = 1280;
const H = 720;

function add(slide, ctx, o) {
  return ctx.addShape(slide, o);
}

function text(slide, ctx, textValue, x, y, w, h, opts = {}) {
  return ctx.addText(slide, {
    text: textValue,
    left: x,
    top: y,
    width: w,
    height: h,
    fontSize: opts.size ?? 24,
    color: opts.color ?? C.navy,
    bold: opts.bold ?? false,
    typeface: opts.face ?? (opts.title ? "Arial" : "Arial"),
    align: opts.align ?? "left",
    valign: opts.valign ?? "top",
    fill: opts.fill ?? "#00000000",
    insets: opts.insets ?? { left: 0, right: 0, top: 0, bottom: 0 },
  });
}

function bg(slide, ctx, color = C.cream) {
  add(slide, ctx, { left: 0, top: 0, width: W, height: H, fill: color });
}

function footer(slide, ctx, n, label, dark = false) {
  text(slide, ctx, label.toUpperCase(), 56, 688, 320, 16, { size: 9, color: dark ? "#B8B4C8" : C.muted, bold: true });
  text(slide, ctx, String(n).padStart(2, "0"), 1190, 688, 36, 16, { size: 9, color: dark ? "#B8B4C8" : C.muted, bold: true, align: "right" });
}

function title(slide, ctx, crumb, headline, sub = "", n = 1, dark = false) {
  text(slide, ctx, crumb.toUpperCase(), 56, 48, 320, 16, { size: 9, color: dark ? C.orange : C.muted, bold: true });
  text(slide, ctx, headline, 56, 84, 900, 72, { size: 34, color: dark ? C.white : C.navy, bold: true });
  if (sub) text(slide, ctx, sub, 58, 148, 880, 38, { size: 17, color: dark ? "#CDC9D8" : C.muted });
  add(slide, ctx, { left: 56, top: 196, width: 1120, height: 2, fill: dark ? "#3A3A58" : "#CCC8BC" });
  footer(slide, ctx, n, crumb, dark);
}

function pill(slide, ctx, label, x, y, color = C.orange, txt = C.white) {
  add(slide, ctx, { left: x, top: y, width: 138, height: 30, geometry: "roundRect", fill: color });
  text(slide, ctx, label, x + 12, y + 8, 114, 12, { size: 9, color: txt, bold: true, align: "center" });
}

function code(slide, ctx, value, x, y, w, h) {
  add(slide, ctx, { left: x, top: y, width: w, height: h, fill: "#111118" });
  text(slide, ctx, value, x + 24, y + 26, w - 48, h - 48, { size: 19, color: C.white, face: "Menlo" });
}

function card(slide, ctx, x, y, w, h, eyebrow, head, body, accent = C.orange) {
  add(slide, ctx, { left: x, top: y, width: w, height: h, fill: C.cream2, line: { fill: "#D6D2C7", width: 1 } });
  add(slide, ctx, { left: x, top: y, width: 6, height: h, fill: accent });
  text(slide, ctx, eyebrow.toUpperCase(), x + 22, y + 20, w - 40, 14, { size: 8, color: accent, bold: true });
  text(slide, ctx, head, x + 22, y + 46, w - 40, 30, { size: 18, color: C.navy, bold: true });
  text(slide, ctx, body, x + 22, y + 88, w - 40, h - 100, { size: 13, color: C.muted });
}

function arrow(slide, ctx, x1, y1, x2, y2, color = C.navy) {
  const width = Math.max(2, x2 - x1);
  add(slide, ctx, { left: x1, top: y1 - 1, width, height: 2, fill: color });
  add(slide, ctx, { left: x2 - 8, top: y2 - 6, width: 12, height: 12, geometry: "triangle", fill: color });
}

function newSlide(presentation, ctx, color = C.cream) {
  const slide = presentation.slides.add();
  bg(slide, ctx, color);
  return slide;
}

function cover(p, ctx, n) {
  const s = newSlide(p, ctx, C.navy);
  text(s, ctx, "FORMATION · DATA SCIENTIST TRACK", 70, 64, 520, 18, { size: 12, color: C.orange, bold: true });
  text(s, ctx, "Python\nFundamentals\nin Azure Databricks", 68, 145, 860, 245, { size: 66, color: C.cream, bold: true });
  pill(s, ctx, "WEEK 01 / 06", 72, 510);
  text(s, ctx, "SAS → Python · pandas · Spark · SQL", 238, 514, 520, 22, { size: 19, color: "#D6D1E3" });
  add(s, ctx, { left: 875, top: -70, width: 310, height: 310, geometry: "ellipse", fill: C.orange });
  add(s, ctx, { left: 1010, top: 250, width: 170, height: 170, geometry: "ellipse", fill: C.lime });
  add(s, ctx, { left: 900, top: 470, width: 240, height: 24, fill: C.cyan });
  footer(s, ctx, n, "Liora · Allianz", true);
}

function ecosystemMap(p, ctx, n) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "02 · Écosystème", "Python: ce qui s’emboîte.", "Langage, modules, packages, environnement Databricks.", n);
  const layers = [
    ["Notebook", "cellules · texte · résultats", C.navy, C.white, 80, 250, 1040, 84],
    ["Python", "variables · conditions · fonctions", C.orange, C.white, 125, 335, 950, 74],
    ["Modules", "math · pathlib · fonctions réutilisables", C.violet, C.white, 170, 410, 860, 64],
    ["Packages", "pandas · numpy · pyspark", C.lime, C.navy, 215, 475, 770, 54],
    ["Runtime Databricks", "versions installées · cluster · librairies", C.cream2, C.navy, 260, 530, 680, 44],
  ];
  for (const [head, body, fill, col, x, y, w, h] of layers) {
    add(s, ctx, { left: x, top: y, width: w, height: h, geometry: "roundRect", fill });
    text(s, ctx, head, x + 24, y + 20, 260, 28, { size: 22, color: col, bold: true });
    text(s, ctx, body, x + 330, y + 24, w - 360, 24, { size: 16, color: col });
  }
}

function notebookPattern(p, ctx, n) {
  const s = newSlide(p, ctx, C.navy);
  title(s, ctx, "Méthode", "Chaque notebook suit le même rituel.", "Répéter le rituel rend les débutants autonomes.", n, true);
  const steps = [
    ["1", "Concept", "ce que l’on apprend"],
    ["2", "Commande", "lecture de la syntaxe"],
    ["3", "Pratique", "modifier du code existant"],
    ["4", "Correction", "ouvrir après essai"],
    ["5", "Bonne pratique", "ce qu’on retient"],
  ];
  let x = 70;
  for (const [num, head, body] of steps) {
    add(s, ctx, { left: x, top: 290, width: 190, height: 190, geometry: "ellipse", fill: num === "3" ? C.orange : C.softNavy });
    text(s, ctx, num, x + 70, 325, 50, 40, { size: 36, color: num === "3" ? C.white : C.orange, bold: true, align: "center" });
    text(s, ctx, head, x + 20, 385, 150, 26, { size: 19, color: C.white, bold: true, align: "center" });
    text(s, ctx, body, x + 24, 426, 140, 34, { size: 12, color: "#CCC8D8", align: "center" });
    x += 230;
  }
}

function workflowMap(p, ctx, n) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "03 · Méthode DataFrame", "La méthode analytique reste stable.", "Les outils changent, le raisonnement doit rester lisible.", n);
  const steps = ["Charger", "Contrôler", "Explorer", "Filtrer", "Agréger", "Interpréter"];
  let x = 70;
  for (let i = 0; i < steps.length; i++) {
    const active = i === 1 || i === 5;
    add(s, ctx, { left: x, top: 310, width: 150, height: 78, geometry: "roundRect", fill: active ? C.orange : C.cream2, line: { fill: active ? C.orange : "#D6D2C7", width: 1 } });
    text(s, ctx, steps[i], x + 15, 337, 120, 22, { size: 18, color: active ? C.white : C.navy, bold: true, align: "center" });
    if (i < steps.length - 1) arrow(s, ctx, x + 158, 349, x + 205, 349, C.navy);
    x += 195;
  }
  text(s, ctx, "Tip formateur: demander une phrase métier après chaque résultat.", 138, 500, 900, 36, { size: 22, color: C.navy, bold: true, align: "center" });
}

function qcm(p, ctx, n, question, choices, answer) {
  const s = newSlide(p, ctx, C.navy);
  title(s, ctx, "QCM live", question, "Vote à main levée ou dans le chat.", n, true);
  let y = 250;
  for (const [letter, choice] of choices) {
    add(s, ctx, { left: 120, top: y, width: 930, height: 58, fill: C.cream2 });
    text(s, ctx, letter, 145, y + 17, 32, 18, { size: 16, color: C.orange, bold: true });
    text(s, ctx, choice, 195, y + 17, 790, 18, { size: 16, color: C.navy, bold: true });
    y += 76;
  }
  text(s, ctx, `Réponse: ${answer}`, 120, 610, 900, 20, { size: 13, color: C.orange, bold: true });
}

function section(p, ctx, n, label, titleValue, subtitle) {
  const s = newSlide(p, ctx, C.orange);
  text(s, ctx, label, 78, 105, 140, 54, { size: 56, color: C.navy, bold: true });
  text(s, ctx, titleValue, 300, 175, 780, 82, { size: 54, color: C.navy, bold: true });
  text(s, ctx, subtitle, 304, 292, 760, 34, { size: 22, color: C.navy });
  footer(s, ctx, n, `section ${label}`, false);
}

function twoWorlds(p, ctx, n) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "SAS → Databricks", "Deux mondes, mêmes gestes.", "On garde la logique analytique, on change l’environnement.", n);
  card(s, ctx, 110, 270, 430, 230, "SAS", "Programme + tables", "DATA step, PROC SQL, bibliothèques, log d’exécution.", C.orange);
  card(s, ctx, 720, 270, 430, 230, "Databricks", "Notebook + DataFrames", "Cellules Python/SQL, cluster, FileStore, display.", C.violet);
  arrow(s, ctx, 560, 385, 700, 385, C.navy);
  text(s, ctx, "Message formateur: rassurer avant d’introduire la syntaxe.", 230, 560, 820, 24, { size: 20, color: C.navy, bold: true, align: "center" });
}

function checklist(p, ctx, n, heading, items) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "Checklist", heading, "À cocher avant de passer à l’étape suivante.", n);
  let y = 250;
  for (const item of items) {
    add(s, ctx, { left: 145, top: y, width: 28, height: 28, fill: C.cream2, line: { fill: C.navy, width: 2 } });
    text(s, ctx, item, 205, y + 2, 820, 22, { size: 20, color: C.navy, bold: true });
    y += 64;
  }
}

function conceptLens(p, ctx, n, heading, lenses) {
  const s = newSlide(p, ctx, C.navy);
  title(s, ctx, "Méthode", heading, "La bonne question avant la bonne commande.", n, true);
  let x = 90;
  for (const [head, body, color] of lenses) {
    add(s, ctx, { left: x, top: 275, width: 250, height: 250, geometry: "ellipse", fill: color });
    text(s, ctx, head, x + 35, 335, 180, 30, { size: 25, color: color === C.lime || color === C.cyan ? C.navy : C.white, bold: true, align: "center" });
    text(s, ctx, body, x + 42, 395, 166, 52, { size: 14, color: color === C.lime || color === C.cyan ? C.navy : C.white, align: "center" });
    x += 300;
  }
}

function notebookCTA(p, ctx, n, notebook, task) {
  const s = newSlide(p, ctx, C.navy);
  text(s, ctx, "STOP SLIDES", 78, 74, 240, 20, { size: 13, color: C.orange, bold: true });
  text(s, ctx, "Allez dans le notebook.", 75, 155, 850, 70, { size: 52, color: C.white, bold: true });
  text(s, ctx, notebook, 80, 250, 850, 38, { size: 30, color: C.lime, bold: true });
  add(s, ctx, { left: 80, top: 400, width: 880, height: 88, fill: C.orange });
  text(s, ctx, task, 112, 432, 810, 28, { size: 22, color: C.white, bold: true });
  footer(s, ctx, n, "notebook", true);
}

function diagramDatabricks(p, ctx, n) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "01 · Databricks", "Où sont le code, la donnée et le calcul ?", "Les débutants doivent d'abord se repérer.", n);
  const items = [
    ["Workspace", "notebooks\n/Shared/training", 90, 300, C.orange],
    ["Cluster", "exécute le code", 405, 300, C.violet],
    ["FileStore", "insurance.csv", 720, 300, C.lime],
    ["Résultat", "table · texte · graphique", 1010, 300, C.cyan],
  ];
  for (const [h, b, x, y, col] of items) {
    add(s, ctx, { left: x, top: y, width: 190, height: 130, geometry: "roundRect", fill: col });
    text(s, ctx, h, x + 18, y + 28, 154, 24, { size: 21, color: h === "FileStore" || h === "Résultat" ? C.navy : C.white, bold: true, align: "center" });
    text(s, ctx, b, x + 18, y + 68, 154, 38, { size: 14, color: h === "FileStore" || h === "Résultat" ? C.navy : C.white, align: "center" });
  }
  arrow(s, ctx, 285, 365, 390, 365);
  arrow(s, ctx, 600, 365, 705, 365);
  arrow(s, ctx, 915, 365, 1000, 365);
}

function codeAnnotated(p, ctx, n, crumb, heading, codeValue, notes) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, crumb, heading, "Lecture ligne par ligne.", n);
  code(s, ctx, codeValue, 72, 250, 650, 300);
  let y = 260;
  for (const [label, body, col] of notes) {
    add(s, ctx, { left: 780, top: y, width: 340, height: 64, fill: col });
    text(s, ctx, label, 800, y + 12, 300, 16, { size: 12, color: col === C.lime || col === C.green ? C.navy : C.white, bold: true });
    text(s, ctx, body, 800, y + 34, 300, 16, { size: 12, color: col === C.lime || col === C.green ? C.navy : C.white });
    y += 78;
  }
}

function practiceSlide(p, ctx, n, titleValue, steps, output) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "Activité guidée", titleValue, "Les apprenants modifient du code déjà présent.", n);
  let y = 250;
  let i = 1;
  for (const step of steps) {
    add(s, ctx, { left: 105, top: y, width: 52, height: 52, geometry: "ellipse", fill: i === 1 ? C.orange : C.navy });
    text(s, ctx, String(i).padStart(2, "0"), 116, y + 17, 30, 14, { size: 14, color: C.white, bold: true, align: "center" });
    text(s, ctx, step, 190, y + 14, 840, 26, { size: 20, color: C.navy, bold: i === 1 });
    y += 75;
    i++;
  }
  add(s, ctx, { left: 190, top: 590, width: 760, height: 44, fill: C.green });
  text(s, ctx, `Sortie attendue · ${output}`, 212, 605, 720, 14, { size: 13, color: C.navy, bold: true });
}

function bestPractice(p, ctx, n, titleValue, tips) {
  const s = newSlide(p, ctx, C.navy);
  title(s, ctx, "Bonnes pratiques", titleValue, "À répéter pendant toute la journée.", n, true);
  let y = 250;
  for (const [head, body] of tips) {
    add(s, ctx, { left: 110, top: y, width: 880, height: 58, fill: C.softNavy });
    add(s, ctx, { left: 110, top: y, width: 8, height: 58, fill: C.orange });
    text(s, ctx, head, 138, y + 12, 260, 16, { size: 15, color: C.white, bold: true });
    text(s, ctx, body, 420, y + 13, 520, 16, { size: 14, color: "#D6D1E3" });
    y += 74;
  }
}

function miniCase(p, ctx, n) {
  const s = newSlide(p, ctx, C.cream);
  title(s, ctx, "Après-midi", "Mini-cas: quel segment coûte le plus ?", "Un cas guidé, puis une conclusion métier.", n);
  const steps = [
    ["1", "Créer un segment", "age_segment"],
    ["2", "Comparer", "smoker · region · sex"],
    ["3", "Croiser", "smoker × age_segment"],
    ["4", "Contrôler", "row_count"],
    ["5", "Conclure", "phrase prudente"],
  ];
  let x = 85;
  for (const [num, h, b] of steps) {
    add(s, ctx, { left: x, top: 275, width: 185, height: 230, fill: num === "5" ? C.navy : C.cream2, line: { fill: "#D6D2C7", width: 1 } });
    text(s, ctx, num, x + 22, 300, 40, 30, { size: 26, color: num === "5" ? C.orange : C.orange, bold: true });
    text(s, ctx, h, x + 22, 350, 138, 24, { size: 20, color: num === "5" ? C.white : C.navy, bold: true });
    text(s, ctx, b, x + 22, 410, 138, 40, { size: 15, color: num === "5" ? "#D6D1E3" : C.muted });
    x += 210;
  }
}

function finalSlide(p, ctx, n) {
  const s = newSlide(p, ctx, C.navy);
  text(s, ctx, "FIN · WEEK 01", 72, 72, 260, 18, { size: 12, color: C.orange, bold: true });
  text(s, ctx, "Vous savez exécuter\nune analyse guidée\ndans Databricks.", 72, 165, 900, 210, { size: 56, color: C.white, bold: true });
  text(s, ctx, "La suite: écrire du Python plus structuré sans perdre la méthode.", 76, 500, 780, 28, { size: 22, color: "#D6D1E3" });
  footer(s, ctx, n, "synthèse", true);
}

async function main() {
  await fs.mkdir(path.join(ROOT, ".codex_presentations"), { recursive: true });
  await fs.copyFile(
    path.join(SKILL_DIR, "scripts", "artifact_tool_utils.mjs"),
    path.join(ROOT, ".codex_presentations", "artifact_tool_utils.mjs"),
  );
  await ensureArtifactToolWorkspace(WORKSPACE);
  const artifact = await importArtifactTool(WORKSPACE);
  const { Presentation, PresentationFile } = artifact;
  const presentation = Presentation.create({ slideSize: { width: W, height: H } });
  const ctx = createSlideContext(artifact, {
    slideSize: { width: W, height: H },
    workspaceDir: WORKSPACE,
    titleFont: "Arial",
    bodyFont: "Arial",
    monoFont: "Menlo",
  });

  let n = 1;
  cover(presentation, ctx, n++);
  notebookPattern(presentation, ctx, n++);
  twoWorlds(presentation, ctx, n++);
  ecosystemMap(presentation, ctx, n++);
  section(presentation, ctx, n++, "01", "Databricks", "Se repérer avant de coder.");
  diagramDatabricks(presentation, ctx, n++);
  checklist(presentation, ctx, n++, "Avant d’exécuter une cellule", ["Le bon notebook est ouvert", "Le cluster est attaché", "Le fichier est au bon endroit", "Je sais quel résultat attendre"]);
  notebookCTA(presentation, ctx, n++, "01_intro_databricks.py", "Exécuter Hello Databricks, puis modifier une variable.");
  qcm(presentation, ctx, n++, "Un notebook Databricks sert d’abord à…", [["A", "Stocker uniquement un CSV"], ["B", "Mélanger texte, code et résultats"], ["C", "Remplacer le cluster"], ["D", "Installer Python"]], "B");
  section(presentation, ctx, n++, "02", "Python utile", "Lire, modifier, vérifier.");
  codeAnnotated(presentation, ctx, n++, "Python", "Lire une variable.", 'age = 45\nregion = "southwest"\npremium = 1200.50', [["Nom", "age, region, premium", C.orange], ["Valeur", "45, texte, montant", C.violet], ["Réflexe", "modifier puis exécuter", C.lime]]);
  codeAnnotated(presentation, ctx, n++, "Python", "Comprendre import.", 'import pandas as pd\nfrom pyspark.sql.functions import avg', [["Package", "pandas devient pd", C.orange], ["Fonction", "avg est importée seule", C.violet], ["Conseil", "ne pas mémoriser: reconnaître", C.lime]]);
  conceptLens(presentation, ctx, n++, "Lire une ligne de code en trois passes.", [["Quoi ?", "quel objet est manipulé", C.orange], ["Comment ?", "quelle commande est appelée", C.violet], ["Résultat ?", "qu’est-ce qui doit sortir", C.lime]]);
  practiceSlide(presentation, ctx, n++, "Variables et types", ["Changer age, bmi, smoker", "Exécuter type(...)", "Dire le type à voix haute"], "3 types identifiés");
  notebookCTA(presentation, ctx, n++, "02_python_basics.py", "Faire les blocs modules, variables, conditions.");
  qcm(presentation, ctx, n++, "Que fait `import pandas as pd` ?", [["A", "Lit automatiquement le CSV"], ["B", "Rend pandas disponible sous le nom pd"], ["C", "Crée une table Spark"], ["D", "Lance un cluster"]], "B");
  section(presentation, ctx, n++, "03", "pandas", "Contrôler, filtrer, agréger.");
  workflowMap(presentation, ctx, n++);
  checklist(presentation, ctx, n++, "Avant d’analyser une table", ["Afficher les premières lignes", "Lister les colonnes", "Vérifier les types", "Identifier la colonne cible"]);
  codeAnnotated(presentation, ctx, n++, "pandas", "Charger et contrôler.", 'df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")\ndf.head()\ndf.info()\ndf.describe()', [["Chemin", "/dbfs pour pandas", C.orange], ["Contrôle", "avant d’analyser", C.violet], ["Tip", "ne jamais filtrer trop tôt", C.lime]]);
  practiceSlide(presentation, ctx, n++, "Contrôler la table", ["Afficher head()", "Compter les lignes", "Identifier charges"], "table comprise avant filtre");
  codeAnnotated(presentation, ctx, n++, "pandas", "Filtrer sans page blanche.", 'df[df["smoker"] == "yes"]\ndf[df["bmi"] > 30]', [["Condition", "vrai/faux par ligne", C.orange], ["==", "compare", C.violet], ["=", "affecte une valeur", C.lime]]);
  qcm(presentation, ctx, n++, "Pourquoi utilise-t-on `==` dans un filtre pandas ?", [["A", "Pour affecter une valeur"], ["B", "Pour comparer deux valeurs"], ["C", "Pour trier"], ["D", "Pour importer pandas"]], "B");
  codeAnnotated(presentation, ctx, n++, "pandas", "Agréger pour répondre.", 'df.groupby("smoker")["charges"].mean()\n.sort_values(ascending=False)', [["Group", "segment métier", C.orange], ["Measure", "charges", C.violet], ["Output", "phrase métier", C.lime]]);
  conceptLens(presentation, ctx, n++, "Lire une agrégation.", [["Segment", "par qui regroupe-t-on ?", C.orange], ["Mesure", "que calcule-t-on ?", C.violet], ["Décision", "que peut-on dire ?", C.cyan]]);
  notebookCTA(presentation, ctx, n++, "03_pandas_basics.py", "Charger, contrôler, filtrer, agréger.");
  bestPractice(presentation, ctx, n++, "pandas: les réflexes débutants", [["Contrôler", "head, info, describe avant filtre"], ["Nommer", "variables métier, pas tmp"], ["Trier", "mettre le segment le plus important en haut"], ["Interpréter", "une sortie doit devenir une phrase"]]);
  qcm(presentation, ctx, n++, "Quelle sortie est la plus utile pour décider ?", [["A", "Une table non triée"], ["B", "Une moyenne par segment triée"], ["C", "Le code seul"], ["D", "Une cellule vide"]], "B");
  section(presentation, ctx, n++, "04", "Spark", "Reconnaître la syntaxe Databricks.");
  codeAnnotated(presentation, ctx, n++, "Spark", "Même geste, API Spark.", 'spark_df.select("age", "charges")\nspark_df.filter(spark_df.age > 50)\nspark_df.groupBy("region").agg(avg("charges"))', [["Objectif", "reconnaître les verbes", C.orange], ["Databricks", "display(...) pour voir", C.violet], ["Limite", "pas d’internals aujourd’hui", C.lime]]);
  notebookCTA(presentation, ctx, n++, "04_spark_basics.py", "Refaire select, filter, groupBy avec display.");
  section(presentation, ctx, n++, "05", "SQL", "Retrouver un repère familier.");
  codeAnnotated(presentation, ctx, n++, "SQL", "PROC SQL reste un repère.", 'SELECT smoker,\n       AVG(charges) AS avg_charges\nFROM insurance\nGROUP BY smoker\nORDER BY avg_charges DESC', [["SELECT", "colonnes et mesures", C.orange], ["GROUP BY", "segment", C.violet], ["ORDER BY", "lecture rapide", C.lime]]);
  notebookCTA(presentation, ctx, n++, "05_sql_basics.py", "Créer la vue puis exécuter les requêtes SQL.");
  section(presentation, ctx, n++, "06", "Après-midi", "Consolider puis analyser.");
  miniCase(presentation, ctx, n++);
  notebookCTA(presentation, ctx, n++, "07 puis 08", "Consolider, puis traiter le mini-cas métier.");
  checklist(presentation, ctx, n++, "Avant de conclure", ["Le segment est nommé", "La mesure est claire", "Le nombre de lignes est vérifié", "La limite est mentionnée"]);
  bestPractice(presentation, ctx, n++, "Conseils à répéter toute la journée", [["Avant le code", "quel est le résultat attendu ?"], ["Après le code", "le résultat a-t-il du sens ?"], ["Avant conclusion", "combien de lignes par segment ?"], ["Toujours", "descriptif n’est pas causal"]]);
  finalSlide(presentation, ctx, n++);

  await fs.mkdir(PREVIEW_DIR, { recursive: true });
  for (let i = 0; i < presentation.slides.count; i++) {
    const slide = presentation.slides.getItem(i);
    const preview = await presentation.export({ slide, format: "png", scale: 1 });
    await saveBlobToFile(preview, path.join(PREVIEW_DIR, `slide-${String(i + 1).padStart(2, "0")}.png`));
  }
  await fs.mkdir(path.dirname(OUT), { recursive: true });
  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(OUT);
  await fs.writeFile(NOTES, "# V3 notes\n\nDesign-first deck generated with artifact-tool Presentations workflow.\n", "utf8");
  console.log(OUT);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

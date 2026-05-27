# Databricks notebook source
# MAGIC %md
# MAGIC # 02 — Python Basics for SAS Analysts
# MAGIC
# MAGIC **Goal:** read and write simple Python — variables, lists, data types, conditions, functions.
# MAGIC These are the building blocks that appear in every analysis.
# MAGIC
# MAGIC > **Pattern for every concept:**
# MAGIC >> 1. What it is and why it matters.
# MAGIC >> 2. Read the syntax — slowly.
# MAGIC >> 3. Practice: modify, predict, then run.
# MAGIC >> 4. Open the solution only after you have tried.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Modules and `import`
# MAGIC
# MAGIC > Python is a language. A **module** is a file of reusable code. A **package** bundles several modules.
# MAGIC >
# MAGIC > In Databricks, the most useful packages are already installed on the cluster:
# MAGIC >> * `pandas` — tables in memory.
# MAGIC >> * `pyspark` — Spark DataFrames.
# MAGIC >> * `math`, `datetime` — standard Python utilities.
# MAGIC >
# MAGIC > The `import` statement makes a module available in the notebook.
# MAGIC > It is the equivalent of a SAS `LIBNAME` — you declare what you need before you use it.
# MAGIC >
# MAGIC > ```python
# MAGIC > import math           # load the entire math module
# MAGIC > import pandas as pd   # load pandas, call it "pd" for short
# MAGIC > ```
# MAGIC >
# MAGIC > The `as` keyword creates an **alias** — a shorter name you type instead of the full module name.
# MAGIC > `pd` is the universal convention for pandas. You will see it in every notebook and tutorial.

# COMMAND ----------

import math

math.sqrt(16)   # → 4.0

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Use the same function to compute the square root of `81`.
# MAGIC >
# MAGIC > **(b)** Compute `math.floor(7.9)` — predict the result before running.
# MAGIC > Then compute `math.ceil(7.1)`. What does each function do?

# COMMAND ----------

# (a)
math.sqrt(...)

# COMMAND ----------

# (b)
print(math.floor(7.9))
print(math.ceil(7.1))

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
math.sqrt(81)    # → 9.0

# (b)
math.floor(7.9)  # → 7  (rounds DOWN to nearest integer)
math.ceil(7.1)   # → 8  (rounds UP to nearest integer)</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** when you see `import`, ask yourself — which tool am I making available?

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Variables
# MAGIC
# MAGIC > A variable gives a name to a value. In SAS you store values in macro variables (`%let`) or
# MAGIC > dataset columns. In Python, any name can hold any value.
# MAGIC >
# MAGIC > ```python
# MAGIC > age = 45              # stores the integer 45 in the name "age"
# MAGIC > region = "southwest"  # stores the text "southwest"
# MAGIC > premium = 1200.50     # stores a decimal number
# MAGIC > ```
# MAGIC >
# MAGIC > Rules for naming variables:
# MAGIC >> * Start with a letter or underscore — never a digit.
# MAGIC >> * Only letters, digits, and underscores — no spaces or hyphens.
# MAGIC >> * Case-sensitive: `Age` and `age` are two different variables.
# MAGIC >> * Use descriptive names: `annual_premium` rather than `x` or `tmp`.

# COMMAND ----------

age = 45
region = "southwest"
premium = 1200.50

print(age)
print(region)
print(premium)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Update `age` to `52`, `region` to `"northeast"`, `premium` to `980.0`. Print all three.
# MAGIC >
# MAGIC > **(b)** Create a variable `annual_premium` equal to `premium * 12`. Print it.
# MAGIC >
# MAGIC > **(c)** Without running: what happens if you print `annual_premium` before the cell that defines it?

# COMMAND ----------

# (a)
age = ...
region = ...
premium = ...

print(age)
print(region)
print(premium)

# COMMAND ----------

# (b)
annual_premium = ...
print(annual_premium)

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
age = 52
region = "northeast"
premium = 980.0
print(age, region, premium)

# (b)
annual_premium = premium * 12
print(annual_premium)  # → 11760.0</code></pre>
<p>(c) You would get a <code>NameError</code> — Python does not know a variable until the cell defining it has been executed.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** use names that describe the business meaning — `annual_premium`, `smoker_flag`, `avg_charges`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Lists
# MAGIC
# MAGIC > A list groups several values under one name.
# MAGIC > This is useful when you have a fixed set of categories — regions, product types, segment labels.
# MAGIC >
# MAGIC > ```python
# MAGIC > regions = ["northeast", "northwest", "southeast", "southwest"]
# MAGIC > ```
# MAGIC >
# MAGIC > Key operations:
# MAGIC >
# MAGIC > | What you want | Syntax | Result |
# MAGIC > |---------------|--------|--------|
# MAGIC > | Number of elements | `len(regions)` | `4` |
# MAGIC > | First element | `regions[0]` | `"northeast"` |
# MAGIC > | Last element | `regions[-1]` | `"southwest"` |
# MAGIC > | Add an element | `regions.append("central")` | list grows by 1 |
# MAGIC >
# MAGIC > **Important:** indexing starts at **0**, not 1.
# MAGIC > The first element is `[0]`, the second is `[1]`, the last is `[-1]`.

# COMMAND ----------

regions = ["northeast", "northwest", "southeast", "southwest"]

print(len(regions))   # → 4
print(regions[0])     # → "northeast"
print(regions[-1])    # → "southwest"

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Print the **second** element of `regions`.
# MAGIC >
# MAGIC > **(b)** Add `"central"` to the list using `.append()`. Print the list and its new length.
# MAGIC >
# MAGIC > **(c)** Create a list `smoker_values` containing `"yes"` and `"no"`. Print the first element.

# COMMAND ----------

# (a)
print(regions[...])

# COMMAND ----------

# (b)
regions.append(...)
print(regions)
print(len(regions))

# COMMAND ----------

# (c)
smoker_values = [...]
print(smoker_values[0])

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a) — second element is at index 1
print(regions[1])   # → "northwest"

# (b)
regions.append("central")
print(regions)        # → [..., "central"]
print(len(regions))   # → 5

# (c)
smoker_values = ["yes", "no"]
print(smoker_values[0])  # → "yes"</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** indexing starts at 0. The element at position `n` is accessed with `[n-1]`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Data Types
# MAGIC
# MAGIC > Python tracks the **type** of every value. Four types you will see in every analysis:
# MAGIC >
# MAGIC > | Type | Example | When you see it |
# MAGIC > |------|---------|-----------------|
# MAGIC > | `int` | `45` | age, number of children |
# MAGIC > | `float` | `27.5` | BMI, charges, premium |
# MAGIC > | `str` | `"southwest"` | region, smoker status, sex |
# MAGIC > | `bool` | `True` / `False` | filter conditions, flags |
# MAGIC >
# MAGIC > Use `type()` to check the type of any value.
# MAGIC > This matters when filtering: you cannot compare a number to a string.

# COMMAND ----------

age = 45
bmi = 27.5
region = "southwest"
is_smoker = True

print(type(age))        # → <class 'int'>
print(type(bmi))        # → <class 'float'>
print(type(region))     # → <class 'str'>
print(type(is_smoker))  # → <class 'bool'>

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Without running: what type is `charges = 4500.0`? What about `children = 2`?
# MAGIC >
# MAGIC > **(b)** Create the four variables with the values below, then print their types:
# MAGIC >> * `age = 54`, `bmi = 31.2`, `region = "southeast"`, `is_smoker = False`
# MAGIC >
# MAGIC > **(c)** Run `age + region`. Read the error message carefully — what type conflict does it describe?

# COMMAND ----------

# (a) — predict, then check
charges = 4500.0
children = 2
print(type(charges))
print(type(children))

# COMMAND ----------

# (b)
age = ...
bmi = ...
region = ...
is_smoker = ...

print(type(age))
print(type(bmi))
print(type(region))
print(type(is_smoker))

# COMMAND ----------

# (c) — expected error, read the message
age + region

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a): charges → float | children → int

# (b)
age = 54        # int
bmi = 31.2      # float
region = "southeast"  # str
is_smoker = False     # bool

# (c) TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Python refuses to add a number and a string.</code></pre>
<p>Before filtering or calculating, verify you are working with the right type. A column that looks like a number may be stored as text.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** before filtering a DataFrame column, check its type with `df.info()`. A column that looks numeric may be stored as `str`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Conditions
# MAGIC
# MAGIC > A condition answers a true/false question and lets the code take different paths.
# MAGIC >
# MAGIC > SAS:
# MAGIC > ```sas
# MAGIC > if age > 50 then segment = 'senior';
# MAGIC > else segment = 'non-senior';
# MAGIC > ```
# MAGIC >
# MAGIC > Python:
# MAGIC > ```python
# MAGIC > if age > 50:
# MAGIC >     segment = "senior"
# MAGIC > else:
# MAGIC >     segment = "non-senior"
# MAGIC > ```
# MAGIC >
# MAGIC > Two differences from SAS:
# MAGIC >> 1. The condition line ends with a **colon** `:`.
# MAGIC >> 2. The code block is **indented** with 4 spaces. Python uses indentation instead of `then`/`end`.

# COMMAND ----------

age = 54

if age > 50:
    segment = "senior"
else:
    segment = "non-senior"

segment

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Before running: what is `segment` when `age = 35`? Predict, then change the value and verify.
# MAGIC >
# MAGIC > **(b)** Add a middle branch with `elif`: if `age > 30` (but not > 50), set `segment = "mid"`.
# MAGIC > Test with `age = 40`.
# MAGIC >
# MAGIC > **(c)** Write a condition that sets `bmi_flag = "high"` if `bmi > 30`, else `"normal"`.
# MAGIC > Test with `bmi = 27.5` and with `bmi = 35.0`.

# COMMAND ----------

# (a) Predict then verify
age = ...

if age > 50:
    segment = "senior"
else:
    segment = "non-senior"

segment

# COMMAND ----------

# (b) Add elif branch
age = 40

if age > 50:
    segment = "senior"
elif age > ...:
    segment = ...
else:
    segment = "non-senior"

segment

# COMMAND ----------

# (c) BMI flag
bmi = 27.5

if bmi > ...:
    bmi_flag = ...
else:
    bmi_flag = ...

bmi_flag

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a) age = 35 → "non-senior"

# (b)
age = 40
if age > 50:
    segment = "senior"
elif age > 30:
    segment = "mid"
else:
    segment = "non-senior"
# → "mid"

# (c)
bmi = 27.5
if bmi > 30:
    bmi_flag = "high"
else:
    bmi_flag = "normal"
# bmi = 27.5 → "normal" | bmi = 35.0 → "high"</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** read a condition as a sentence — "if age is greater than 50, then...". Indentation is mandatory — Python will raise an `IndentationError` if it is missing.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Functions
# MAGIC
# MAGIC > A function is a **named, reusable rule**.
# MAGIC > Instead of rewriting the same calculation each time, you define it once and call it by name.
# MAGIC >
# MAGIC > ```python
# MAGIC > def annual_cost(monthly_cost):
# MAGIC >     return monthly_cost * 12
# MAGIC > ```
# MAGIC >
# MAGIC > - `def` — keyword that starts the definition.
# MAGIC > - `annual_cost` — the name you choose (use a verb or action phrase).
# MAGIC > - `monthly_cost` — the **parameter**: the input value the function receives.
# MAGIC > - `return` — sends the result back to the caller.
# MAGIC >
# MAGIC > Call the function by writing its name with the input in parentheses:
# MAGIC > ```python
# MAGIC > annual_cost(120)   # → 1440
# MAGIC > ```

# COMMAND ----------

def annual_cost(monthly_cost):
    return monthly_cost * 12

annual_cost(120)   # → 1440

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Call `annual_cost` with `250` and then with `80`. What are the two results?
# MAGIC >
# MAGIC > **(b)** Write a function `apply_tax(amount, rate)` that returns `amount * (1 + rate)`.
# MAGIC > Call it with `amount=1000, rate=0.2`. Expected: `1200.0`.
# MAGIC >
# MAGIC > **(c)** Write a function `classify_bmi(bmi)` that returns `"high"` if `bmi > 30`, else `"normal"`.
# MAGIC > Test with `bmi=27` and `bmi=35`.

# COMMAND ----------

# (a)
annual_cost(...)

# COMMAND ----------

annual_cost(...)

# COMMAND ----------

# (b)
def apply_tax(amount, rate):
    return ...

apply_tax(amount=1000, rate=0.2)

# COMMAND ----------

# (c)
def classify_bmi(bmi):
    if bmi > ...:
        return ...
    else:
        return ...

print(classify_bmi(27))
print(classify_bmi(35))

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
annual_cost(250)  # → 3000
annual_cost(80)   # → 960

# (b)
def apply_tax(amount, rate):
    return amount * (1 + rate)
apply_tax(amount=1000, rate=0.2)  # → 1200.0

# (c)
def classify_bmi(bmi):
    if bmi > 30:
        return "high"
    else:
        return "normal"
classify_bmi(27)  # → "normal"
classify_bmi(35)  # → "high"</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** name a function after what it *does* — `classify_bmi`, `apply_tax`, `compute_ratio`.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this notebook you learned the six Python building blocks used in every analysis:
# MAGIC >
# MAGIC > | Concept | Syntax | SAS equivalent |
# MAGIC > |---------|--------|----------------|
# MAGIC > | Load a module | `import pandas as pd` | `LIBNAME` / proc statement |
# MAGIC > | Store a value | `age = 45` | `%let age = 45;` |
# MAGIC > | Group values | `regions = ["a", "b", "c"]` | array / macro list |
# MAGIC > | Check type | `type(age)` | `vartype()` |
# MAGIC > | Branch logic | `if x > 50: ... else: ...` | `if x > 50 then ...; else ...;` |
# MAGIC > | Reusable rule | `def f(x): return x * 12` | SAS macro |
# MAGIC >
# MAGIC > **The key difference from SAS:** indentation replaces `then`/`end`/`run`.
# MAGIC > Python uses whitespace as structure — 4 spaces inside every `if`, `def`, or loop.

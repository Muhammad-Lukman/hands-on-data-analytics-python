# Data Analytics in Python

**Short Course | University of Agriculture Faisalabad**   
Instructor: Muhammad Lukman


![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8+-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13+-4C72B0)
![SciPy](https://img.shields.io/badge/SciPy-1.12+-8CAAE6?logo=scipy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


## About the Course

This is a 3-month, 24-session short course designed for undergraduates/graduates with no prior data science background. It covers the complete data analytics pipeline in Python - from Python fundamentals through to hypothesis testing and data-driven decision making - using real datasets throughout.

**Target audience:** Undergraduates/Graduates  
**Duration:** 8 weeks · 3 sessions/week (Friday, Saturday, Sunday) · 1–2 hrs/session  
**Total marks:** 400 (300 module assessments + 100 final exam)

---

## Course Structure

| Module | Topic | Week | Classes | Dataset |
|--------|-------|------|---------|---------|
| M1 | Python Foundations | 1–2 | C1–C6 | — |
| M2 | NumPy | 3 | C7–C9 | — |
| M3 | Pandas | 4–5 | C10–C15 | Titanic · Patients · Sales · Students · COVID |
| M4 | Data Visualisation | 6 | C16–C18 | Sales · Heart Disease · COVID |
| M5 | Statistics & EDA | 7 | C19–C21 | Heart Disease |
| M6 | Hypothesis & Decisions | 8 | C22–C24 | A/B Test · Telco Churn · Clinical Trial |

### Class-by-class breakdown

| # | Class | Key concepts |
|---|-------|-------------|
| C1 | Introduction & Setup | Variables, data types, operators, f-strings, I/O |
| C2 | Strings & Regex | String methods, slicing, `re` module |
| C3 | Lists, Tuples & Comprehensions | Sequences, list comprehensions, nested comprehensions |
| C4 | Dictionaries & Sets | Key-value lookup, dict comprehensions, set operations |
| C5 | Control Flow & Loops | `if/elif/else`, `for`, `while`, `enumerate`, `zip`, `break`, `continue` |
| C6 | Functions, Lambdas & Modules | `def`, `*args`, `**kwargs`, scope, `lambda`, `map`, `filter`, `collections` |
| C7 | NumPy Fundamentals | Arrays, dtypes, indexing, slicing, views vs copies, boolean masking |
| C8 | Operations & Broadcasting | Element-wise ops, broadcasting rules, ufuncs, axis aggregation, reshape |
| C9 | NumPy for Analytics | `np.where`, `argsort`, `unique`, `random`, percentile, `corrcoef` |
| C10 | Introduction to Pandas | Series, DataFrame, `read_csv`, `info`, `describe`, column access, sorting |
| C11 | Indexing & Filtering | `.loc`, `.iloc`, boolean filters, `.isin`, `.between`, `.query`, `get_dummies` |
| C12 | Data Cleaning | Null audit, `dropna`, `fillna`, duplicates, `to_numeric`, `.str` methods |
| C13 | GroupBy & Aggregation | Split-Apply-Combine, `.agg`, `pivot_table`, `.transform` |
| C14 | Merging & Reshaping | `pd.merge` (inner/left/outer), `indicator=True`, `concat`, `melt`, `pivot` |
| C15 | Apply, Map & Time Series | `.apply`, `.map`, `.dt` accessor, `resample`, `rolling`, `pct_change` |
| C16 | Matplotlib Fundamentals | Figure/Axes OO API, line, bar, histogram, scatter, subplots, `savefig` |
| C17 | Seaborn Statistical Plots | `histplot`, `kdeplot`, `boxplot`, `violinplot`, heatmap, `pairplot` |
| C18 | Advanced Viz & Storytelling | `GridSpec`, `annotate`, Plotly Express, narrative framework |
| C19 | Descriptive Statistics | Mean/median/mode, variance, IQR, skewness, kurtosis |
| C20 | Distributions & Outlier Detection | Empirical rule, z-scores, IQR fence, Winsorization, log-transform |
| C21 | Full EDA Workflow | Profile ---> Univariate ---> Bivariate ---> Correlation ---> Findings |
| C22 | Hypothesis Testing | H₀/H₁, t-test, chi-square, p-value, Cohen's d, Type I/II errors |
| C23 | Data-Informed Decisions | KPIs, churn drivers, Simpson's Paradox, survivorship bias, decision memo |
| C24 | Final Capstone + Exam | End-to-end pipeline on an unseen dataset under exam conditions |

---

## Datasets

All datasets are in the `datasets/` folder. Real public datasets are used wherever available.

| File | Rows | Source | Used in |
|------|------|--------|---------|
| `titanic.csv` | 891 | [Kaggle / Seaborn](https://github.com/datasciencedojo/datasets) | C10, C11 |
| `patients.csv` | 16 | Synthetic (intentionally dirty) | C12 |
| `sales.csv` | 600 | Synthetic (Pakistan e-commerce) | C13, C16, C18 |
| `students_demographics.csv` | 20 | Synthetic | C14 |
| `students_grades.csv` | 100 | Synthetic | C14 |
| `students_attendance.csv` | 17 | Synthetic (3 missing) | C14 |
| `heart_disease.csv` | 303 | [Cleveland Heart Disease / UCI](https://github.com/sharmaroshan/Heart-UCI-Dataset) | C17, C19–C21 |
| `covid_cases.csv` | 3225 | [Our World in Data](https://github.com/owid/covid-19-data) | C15, C18 |
| `ab_test.csv` | 2400 | Synthetic (A/B click-through test) | C22 |
| `churn.csv` | 7043 | [IBM Telco Churn](https://github.com/IBM/telco-customer-churn-on-icp4d) | C23 |
| `clinical_trial.csv` | 450 | Synthetic (Phase II trial) | C24 |

---

## How to Use

### 1. Clone the repo

```bash
git clone https://github.com/Muhammad-Lukman/hands-on-data-analytics-python.git
cd hands-on-data-analytics-python
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy plotly jupyter
```

Or with conda:

```bash
conda install pandas numpy matplotlib seaborn scipy plotly jupyter
```

### 3. Folder structure the notebooks expect

```
data-analytics-python/
├── datasets/        <--- CSV files live here
└── notebooks/       <--- open and run .ipynb files from here
```

Each notebook sets `DATA_DIR = "../datasets"` at the top. If you open a notebook from a different working directory, update that one variable.

### 4. Run

```bash
cd notebooks
jupyter notebook
```

---

## Assessment Structure

| Component | Format | Marks |
|-----------|--------|-------|
| Module Assessment × 6 | 20 MCQ + 30 Practical | 50 × 6 = **300** |
| Final Exam | 40 MCQ + 60 Practical (capstone) | **100** |
| **Total** | | **400** |

### Certificate Tiers

| Grade | Percentage | Tier |
|-------|-----------|------|
| A+ | ≥ 85% | Distinction |
| A  | ≥ 75% | Merit |
| B  | ≥ 65% | Credit |
| C  | ≥ 50% | Completion |
| F  | < 50% | No certificate |

Assessment papers and question banks are not included in this repository to maintain academic integrity.

---

## Prerequisites

Students are expected to have:
- Basic computer literacy
- No prior Python or data science experience required

By the end of the course, students can:
- Write Python programs for data processing
- Load, clean, filter, group, and reshape tabular data with Pandas
- Build publication-quality charts with Matplotlib and Seaborn
- Profile any dataset using descriptive statistics and EDA
- Run hypothesis tests and translate results into a business decision

---

## Dependencies

```
python>=3.10
pandas>=2.0
numpy>=1.26
matplotlib>=3.8
seaborn>=0.13
scipy>=1.12
plotly>=5.18
jupyter>=1.0
```

---

## License

This course material is released under the [MIT License](LICENSE).  
You are free to use, adapt, and redistribute with attribution.

---

## Instructor

**Muhammad Luqman**  
BSc (Hons) Microbiology 
Department of Microbiology  
University of Agriculture Faisalabad  
GitHub: [Muhammad-Lukman](https://github.com/Muhammad-Lukman)

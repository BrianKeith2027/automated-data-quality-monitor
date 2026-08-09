# 📊 Automated Data Quality Monitor

An automated data quality monitoring framework that profiles datasets, detects anomalies, validates schema compliance, and generates comprehensive quality reports. Built for data engineers and ML practitioners who need reliable data pipeline health checks.

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue) ![Pandas](https://img.shields.io/badge/Pandas-Data-green) ![Scipy](https://img.shields.io/badge/SciPy-Stats-orange) ![License MIT](https://img.shields.io/badge/License-MIT-yellow)

---

> ### 📍 Project Status — In Active Development
>
> **Committed so far:** `config/quality_rules.yaml`, `tests/test_quality_monitor.py`
>
> **Still to be implemented:** `Data-Quality-Monitor.ipynb`
>
> The architecture, setup, and usage sections below describe the target design for this project. Components listed as still to be implemented are tracked in the Roadmap at the end of this README — some setup or usage commands will not run until those land.

## 📋 Overview

Poor data quality is one of the leading causes of ML model failures and incorrect business decisions. This project provides a comprehensive, automated framework to continuously monitor and validate data quality across your pipelines.

The monitor performs automated profiling, statistical anomaly detection, schema validation, and generates actionable quality reports with visualizations.

## 🔧 Key Features

- **Automated Data Profiling** — Statistical summaries, distributions, and pattern detection for every column
- **Anomaly Detection** — Z-score and IQR-based outlier detection with configurable thresholds
- **Schema Validation** — Enforce expected column types, nullable constraints, and value ranges
- **Null Analysis** — Track missing data patterns, null correlations, and imputation recommendations
- **Duplicate Detection** — Identify exact and fuzzy duplicate records across configurable key columns
- **Distribution Drift** — Compare current data distributions against baseline using KS tests
- **Data Quality Scoring** — Composite quality score (0-100) across completeness, accuracy, consistency, and timeliness
- **Visual Reports** — Matplotlib/Seaborn dashboards for quality metrics visualization
- **Alerting Framework** — Configurable thresholds with warning and critical alert levels
- **Pipeline Integration** — Designed to plug into ETL/ELT workflows as a validation step

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Data Sources                        │
│  (CSV, Parquet, Database, API)                       │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              Data Quality Monitor                    │
│                                                      │
│  ┌──────────┐ ┌──────────┐ ┌───────────────┐       │
│  │ Profiler │ │ Validator│ │Anomaly Detector│       │
│  └──────────┘ └──────────┘ └───────────────┘       │
│  ┌──────────┐ ┌──────────┐ ┌───────────────┐       │
│  │ Scorer   │ │ Reporter │ │   Alerter      │       │
│  └──────────┘ └──────────┘ └───────────────┘       │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              Quality Reports & Alerts                │
│  (HTML Reports, Quality Scores, Alert Notifications) │
└─────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/BrianKeith2027/automated-data-quality-monitor.git
cd automated-data-quality-monitor

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Data-Quality-Monitor.ipynb
```

## 📊 Quality Dimensions

The framework evaluates data quality across four key dimensions:

1. **Completeness** — Measures the percentage of non-null values across all columns
2. **Accuracy** — Validates data types, value ranges, and format compliance
3. **Consistency** — Checks for duplicates, contradictions, and referential integrity
4. **Timeliness** — Monitors data freshness and date field validity

## 🛠️ Tech Stack

- **Python 3.8+** — Core language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **SciPy** — Statistical testing (KS test, Z-scores)
- **Matplotlib / Seaborn** — Visualization
- **PyYAML** — Configuration management
- **JSON Schema** — Schema validation

## 📁 Project Structure

```
automated-data-quality-monitor/
├── Data-Quality-Monitor.ipynb    # Main notebook with full pipeline
├── config/
│   └── quality_rules.yaml        # Quality rules configuration
├── tests/
│   └── test_quality_monitor.py   # Unit tests
├── requirements.txt              # Dependencies
├── .gitignore
├── LICENSE
└── README.md
```

## 📈 Sample Output

The monitor generates a composite quality score and detailed breakdown:

```
📊 DATA QUALITY REPORT
═══════════════════════════════════
Overall Quality Score: 87.3 / 100
═══════════════════════════════════
  Completeness:  92.5%  ✅
  Accuracy:      85.0%  ⚠️
  Consistency:   88.7%  ✅
  Timeliness:    83.0%  ⚠️

⚠️ 2 warnings detected
  - Column 'email': 7.5% null values exceed 5% threshold
  - Column 'amount': 3 outliers detected (Z-score > 3)
```

## 👤 Author

**Brian Stratton** — Senior Data Engineer | AI/ML Engineer | Doctoral Researcher
- [GitHub](https://github.com/BrianKeith2027)
- [LinkedIn](https://www.linkedin.com/in/briankstratton/)

## 🗺️ Roadmap

**Built**

- [x] `config/quality_rules.yaml`
- [x] `tests/test_quality_monitor.py`

**Planned**

- [ ] `Data-Quality-Monitor.ipynb`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# automated-data-quality-monitor
Python-based automated data quality monitoring framework with anomaly detection, profiling dashboards, and alerting for data pipeline health checks

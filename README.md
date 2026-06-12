# ARES Framework – Security Domain Classification Engine

ARES (Adaptive Risk-based Evaluation for Security) is a quantitative framework designed to **prioritize and classify security domains** based on risk, effectiveness, and interdependencies.

This repository provides a **Python implementation** of the ARES model, enabling users to input their own parameters and obtain a **ranked classification of security domains**.

***

## 🚀 Key Features

* Risk-based weighting of security objectives
* Multi-factor evaluation of security domains
* Interdependency modeling between domains
* Quantitative scoring and ranking
* Fully customizable inputs
* Lightweight and reusable Python implementation

***

## 🧠 Framework Overview

ARES operates in four main steps:

1. **Risk Weighting**
2. **Topic Effectiveness Calculation**
3. **Interdependency Adjustment**
4. **Final Scoring & Classification**

***

## ⚙️ Mathematical Model

### 1. Risk Weighting

For each objective $$o$$:

R\_o = λ × ι × ε × assurance × localization

Normalized weight:

w\_o = R\_o / Σ R

***

### 2. Base Effectiveness

ηₒₜ = β · rₒₜ + (1 - β) · vₜ · uₒₜ

Where:

* rₒₜ = relevance
* uₒₜ = utility
* vₜ = vulnerability pressure
* β = balance parameter

***

### 3. Interdependency Adjustment

η' = (I + αD) · η

Where:

* D = interdependency matrix
* α = dependency scaling factor

***

### 4. Final Score

Score(t) = Σ wₒ · η'ₒₜ

***

## 🏗️ Architecture

```
                +----------------------+
                |   User Inputs        |
                |----------------------|
                | Risk Parameters      |
                | Relevance (r)        |
                | Utility (u)          |
                | Vulnerability (v)    |
                | Dependencies (D)     |
                +----------+-----------+
                           |
                           v
        +--------------------------+
        |  Risk Weight Computation |
        +--------------------------+
                           |
                           v
        +--------------------------+
        |  Base Effectiveness (η)  |
        +--------------------------+
                           |
                           v
        +------------------------------+
        | Interdependency Adjustment   |
        | (η' = (I + αD)η)             |
        +------------------------------+
                           |
                           v
        +--------------------------+
        |   Global Scoring         |
        +--------------------------+
                           |
                           v
        +--------------------------+
        | Ranking & Classification |
        +--------------------------+
```

***

## 📊 Example Output

```
1. Critical Infrastructure Security   → 0.830
2. Security Operations                → 0.748
3. Identity & Access Management      → 0.747
4. Supply Chain Security             → 0.711
...
```

***

## 🧩 Project Structure

```
ares-framework/
│
├── ares_framework.py     # Core engine
├── example.py            # Example usage
├── README.md
└── data/                 # (optional) input datasets
```

***

## ▶️ Usage

### 1. Install dependencies

```bash
pip install numpy
```

### 2. Run the framework

```bash
python ares_framework.py
```

### 3. Customize inputs

Modify:

* `risk_params`
* `r` (relevance)
* `u` (utility)
* `v` (vulnerability)
* `D` (interdependency matrix)

***

## 🧪 Example Code

```python
from ares_framework import *

weights = compute_risk_weights(risk_params)
eta = compute_base_eta(topics, objectives, r, u, v, beta)
eta_prime = compute_adjusted_eta(topics, objectives, eta, D, alpha)

scores = compute_scores(topics, objectives, eta_prime, weights)
ranking = rank_topics(scores)

print(ranking)
```

***

## 📈 Use Cases

* Security strategy prioritization
* Cyber maturity assessments
* Investment decision support
* Risk-based governance
* Regulatory alignment (NIS2, DORA, ISO 27001)

***

## 🔮 Future Improvements

* Web interface (Streamlit)
* API (FastAPI)
* Sensitivity analysis
* Visualization dashboards
* Multi-organization comparison

***

## 👤 Author

Hadi CHAMAS  
Information Security Officer

***

## 📄 License

XXX
:::

***

# Robustness-and-Stability-Analysis-of-Risk-Prioritization-Security-Assessment-Model





# 🌊 Water Potability Prediction Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://water-potability-app-nntpzmgryzvn7bmba26hs.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

An interactive, user-friendly Machine Learning web application designed to evaluate water safety and predict whether water is **Potable (Safe for Drinking)** or **Not Potable (Unsafe)** based on key physical and chemical parameters.

---

## 🌐 Live Demo & Web App

You can access and test the live application directly in your browser:
👉 **[Launch Water Potability Predictor App](https://water-potability-live-99rryqdkhzy6zyv3v4gcxk.streamlit.app/)**

---

## 📋 Table of Contents

- [Overview](#-overview-non-technical-summary)
- [Dataset & Parameters](#-dataset--parameters-overview)
- [Machine Learning Architecture](#-machine-learning-architecture--performance)
- [Valid Testing Profiles](#-valid-testing-profiles-sample-inputs)
- [Project Architecture](#-project-architecture--file-structure)
- [Installation & Local Deployment](#-installation--local-deployment)
- [Streamlit Cloud Deployment](#-cloud-deployment-guide)
- [Tech Stack](#-tech-stack)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## 🧐 Overview (Non-Technical Summary)

Safe drinking water is essential for human health and environmental sustainability. However, evaluating water quality in real time requires evaluating complex, multi-variable chemical parameters.

This application automates and simplifies water quality evaluation:

1. **User Input:** Non-technical users input standard water quality indicators (such as pH level, hardness, sulfate, and turbidity) using intuitive sliders and numeric fields.
2. **AI Analysis:** A pre-trained machine learning classification model analyzes the complex non-linear relationships across all metrics simultaneously.
3. **Instant Results:** The app delivers an immediate visual classification (**Potable / Safe** vs **Not Potable / Unsafe**) with responsive indicators.

---

## 📊 Dataset & Parameters Overview

The machine learning model is trained on standard environmental water potability records. Below are the 9 parameters evaluated by the system:

| Feature Name        | Description                                 | World Health Organization (WHO) / Standard Units |
| :------------------ | :------------------------------------------ | :----------------------------------------------- |
| **pH**              | Evaluates the acid-base balance of water    | `6.5 - 8.5` (Standard safe range)                |
| **Hardness**        | Concentration of mineral deposits (Ca & Mg) | `mg/L`                                           |
| **Solids (TDS)**    | Total Dissolved Solids in water             | `ppm` (parts per million)                        |
| **Chloramines**     | Primary disinfectant amount                 | `ppm`                                            |
| **Sulfate**         | Dissolved sulfate mineral concentration     | `mg/L`                                           |
| **Conductivity**    | Electrical conductivity of the water sample | `μS/cm`                                          |
| **Organic Carbon**  | Total Organic Carbon (TOC) levels           | `ppm`                                            |
| **Trihalomethanes** | Concentration of THM chemical byproducts    | `μg/L`                                           |
| **Turbidity**       | Cloudiness and clarity of the water sample  | `NTU`                                            |

---

## ⚙️ Machine Learning Architecture & Performance

### Algorithm Selection

- **Model Type:** **Random Forest Classifier**
- **Rationale:** The Water Potability dataset features complex, highly non-linear decision boundaries and variable interactions. Ensemble decision trees (Random Forest) effectively handle these relationships compared to standard linear classification algorithms.
- **Model Persistence:** Serialized using `joblib` for optimized, zero-latency inference inside the Streamlit web framework.

### Performance & Metrics

- **Accuracy:** `~68% - 72%` _(Evaluated on cross-validation test split)_
- **Class Balancing:** Data preprocessing included threshold checks to handle target variable imbalances.

---

## 🧪 Valid Testing Profiles (Sample Inputs)

Because water quality prediction involves non-linear boundary intersections, arbitrary random inputs frequently result in a `Not Potable` classification. To verify a positive **`Potable (Safe for Drinking)`** prediction in the web app, use the following calibrated test profile:

| Parameter           | Recommended Input Value |
| :------------------ | :---------------------- |
| **pH**              | `9.45`                  |
| **Hardness**        | `145.80`                |
| **Solids (TDS)**    | `13168.60`              |
| **Chloramines**     | `9.44`                  |
| **Sulfate**         | `310.58`                |
| **Conductivity**    | `592.66`                |
| **Organic Carbon**  | `8.60`                  |
| **Trihalomethanes** | `77.58`                 |
| **Turbidity**       | `3.87`                  |

_Entering these exact parameters into the application will trigger a **Potable / Safe for Drinking** output._

---

## 📁 Project Architecture & File Structure

This repository follows a clean, single-root deployment layout optimized for zero-path-error execution on cloud hosts:

```text
water-potability-live/
│
├── main.py                     # Streamlit web application frontend and inference engine
├── water_potability_model.pkl  # Serialized Random Forest machine learning model
├── requirements.txt            # Explicit dependency declarations for cloud build
└── README.md                   # Full technical and project documentation
```

---

## 🚀 Installation & Local Deployment

To run this application locally on your machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/umarraja61933/water-potability-live.git
cd water-potability-live
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Application

```bash
streamlit run main.py
```

_The app will automatically start at `http://localhost:8501`._

---

## ☁️ Streamlit Cloud Deployment Settings

If deploying your own copy to Streamlit Community Cloud:

1. Connect your GitHub account to [share.streamlit.io](https://share.streamlit.io/).
2. Select repository: `water-potability-live`.
3. Set **Branch**: `main` (or `master`).
4. Set **Main file path**: `main.py`.
5. Click **Deploy!**.

---

## 🛠️ Tech Stack

- **Python 3.10+** - Core Programming Language
- **Streamlit** - Interactive Web Application UI
- **Scikit-Learn** - Machine Learning Modeling & Feature Scaling
- **Pandas & NumPy** - Data Cleaning, Structuring, & Tensor Operations
- **Joblib** - Fast Model Serialization & Deserialization
- **Seaborn & Matplotlib** - Data Visualization & EDA

---

## 👩‍💻 Author & Acknowledgments

Developed as an end-to-end Machine Learning pipeline demonstration covering exploratory data analysis (EDA), model training, algorithm selection, hyperparameter tuning, web app creation, and cloud hosting.

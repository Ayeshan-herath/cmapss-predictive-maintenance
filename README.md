# AeroRUL - Predictive Maintenance System

An end-to-end Machine Learning project for predicting
the Remaining Useful Life (RUL) of aircraft engines
using NASA C-MAPSS sensor data.

## Project Objective

Develop an intelligent predictive maintenance system
that analyzes engine sensor measurements and estimates
the remaining operating cycles before engine failure.

## Dataset

NASA C-MAPSS Turbofan Engine Degradation Dataset.

Initial dataset: FD001

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- XGBoost
- TensorFlow / Keras
- Matplotlib and Seaborn
- Streamlit

## Planned Features

- Engine sensor data analysis
- Remaining Useful Life prediction
- XGBoost regression model
- LSTM deep learning model
- Model performance comparison
- Engine health visualization
- Maintenance risk estimation
- Interactive Streamlit dashboard

## Development Progress

Current stage: Project setup

## Project Status

In Development


## Development Setup

### Requirements
- Python 3.11 or 3.12
- Git
- VS Code (recommended)

### Installation

1. Clone the repository.

2. Create a virtual environment:

   python -m venv .venv

3. Activate the environment on Windows PowerShell:

   .\.venv\Scripts\Activate.ps1

4. Install dependencies:

   python -m pip install -r requirements.txt

### Dataset

Download the NASA C-MAPSS dataset and place
CMAPSSData.zip inside data/raw/.

The dataset is not tracked by Git.

### Current Development Status

Milestone 2: Python environment configuration.

## Development Progress

- [x] Milestone 1: GitHub repository setup
- [x] Milestone 2: Python environment setup
- [x] Milestone 3: NASA FD001 data loading and understanding
- [ ] Milestone 4: Exploratory Data Analysis
- [ ] Milestone 5: RUL target engineering
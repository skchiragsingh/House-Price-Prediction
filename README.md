# House Price Prediction

A Machine Learning project that predicts house prices using regression models.

## Project Overview

This project uses the California Housing dataset to predict house prices based on different housing-related features.

The project includes data exploration, visualization, preprocessing, model training, evaluation, and house price prediction.

## Dataset

The project uses the California Housing dataset available through Scikit-learn.

The dataset contains 20,640 records and the following features:

- MedInc
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

The target variable is:

- Price

## Machine Learning Models

Two regression models were implemented and compared:

1. Linear Regression
2. Random Forest Regressor

## Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

| Model | MAE | MSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.5332 | 0.5559 | 0.5758 |
| Random Forest | 0.3275 | 0.2554 | 0.8051 |

Random Forest achieved the best performance with an R² score of approximately 0.81.

## Project Workflow

```text
Dataset
   ↓
Data Exploration
   ↓
Data Visualization
   ↓
Correlation Analysis
   ↓
Train-Test Split
   ↓
Linear Regression
   ↓
Random Forest Regression
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
House Price Prediction

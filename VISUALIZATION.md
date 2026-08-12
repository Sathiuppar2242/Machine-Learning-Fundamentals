# Iris Dataset Visualization

## Overview

Data visualization was used to understand the relationships between the different measurements of Iris flowers.

The project uses Matplotlib and Seaborn for visualization.

## 1. Pairplot

A pairplot was created to visualize relationships between all four numerical features.

The features include:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The `species` column was used to distinguish the three Iris classes.

The pairplot helps identify patterns and differences between Setosa, Versicolor, and Virginica flowers.

## 2. Correlation Heatmap

A correlation heatmap was created to understand the relationships between numerical features.

Correlation values range from:

- `-1` → Strong negative relationship
- `0` → No linear relationship
- `+1` → Strong positive relationship

The heatmap provides a quick visual representation of feature relationships.

## 3. Confusion Matrix

A confusion matrix was created after training the KNN model.

It compares:

- Actual classes
- Predicted classes

This helps identify which Iris species were classified correctly and which were misclassified.

## Visualization Libraries

The following libraries were used:

```python
import matplotlib.pyplot as plt
import seaborn as sns
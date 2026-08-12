# K-Nearest Neighbors Model Training

## Overview

The Iris Flower Classification project uses the **K-Nearest Neighbors (KNN)** algorithm to classify Iris flowers.

KNN is a supervised Machine Learning algorithm commonly used for classification problems.

## How KNN Works

KNN classifies a new data point by finding the nearest data points in the training dataset.

The algorithm:

1. Receives a new data point.
2. Calculates its distance from training samples.
3. Finds the nearest neighbors.
4. Checks the classes of those neighbors.
5. Assigns the most common class to the new data point.

## Model Configuration

The project uses:

```python
KNeighborsClassifier(n_neighbors=5)

This means the model considers the 5 nearest neighbors when making a prediction.

Training Process

The model was trained using the scaled training dataset:

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train_scaled, y_train)
Feature Scaling

Before training, StandardScaler was used to standardize the features.

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

Feature scaling is particularly useful for KNN because KNN relies on distances between data points.

Training and Testing Data

The Iris dataset was divided into:

Dataset	Samples
Training	120
Testing	30

The split was performed using:

train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
Model Prediction

After training, the model was used to predict the classes of the test samples:

y_pred = model.predict(X_test_scaled)
Conclusion

The KNN algorithm successfully learned patterns from the Iris training data and classified the test samples.

The trained model achieved an accuracy of 93.33% on the test dataset.
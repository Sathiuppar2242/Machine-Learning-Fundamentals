# ============================================================
# Machine Learning Fundamentals
# Project: Iris Flower Classification
# ============================================================

# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# -----------------------------
# 2. Load Iris Dataset
# -----------------------------
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

df["species"] = df["target"].map({
    0: "setosa",
    1: "versicolor",
    2: "virginica"
})

print("=" * 60)
print("IRIS FLOWER CLASSIFICATION")
print("=" * 60)


# -----------------------------
# 3. Explore Dataset
# -----------------------------
print("\nFirst five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
df.info()

print("\nClass distribution:")
print(df["species"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical summary:")
print(df.describe())


# -----------------------------
# 4. Data Visualization
# -----------------------------

# Pairplot
print("\nGenerating pairplot...")

sns.pairplot(
    df,
    hue="species",
    diag_kind="hist"
)

plt.suptitle(
    "Iris Flower Feature Relationships",
    y=1.02
)

plt.show()


# -----------------------------
# 5. Correlation Heatmap
# -----------------------------
print("\nGenerating correlation heatmap...")

correlation = df[iris.feature_names].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()


# -----------------------------
# 6. Prepare Features and Target
# -----------------------------
X = df[iris.feature_names]
y = df["target"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# -----------------------------
# 7. Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# -----------------------------
# 8. Feature Scaling
# -----------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")


# -----------------------------
# 9. Train Machine Learning Model
# -----------------------------
model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train_scaled, y_train)

print("\nKNN model training completed.")


# -----------------------------
# 10. Make Predictions
# -----------------------------
y_pred = model.predict(X_test_scaled)

print("\nPredictions:")
print(y_pred)


# -----------------------------
# 11. Evaluate Model
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# -----------------------------
# 12. Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Iris Classification")

plt.tight_layout()
plt.show()


# -----------------------------
# 13. Test With New Flower
# -----------------------------
new_flower = np.array([
    [5.1, 3.5, 1.4, 0.2]
])

new_flower_scaled = scaler.transform(new_flower)

prediction = model.predict(new_flower_scaled)

predicted_species = iris.target_names[prediction[0]]

print("\n" + "=" * 60)
print("NEW FLOWER PREDICTION")
print("=" * 60)

print("\nInput measurements:")
print(new_flower)

print("\nPredicted species:", predicted_species)


# -----------------------------
# 14. Prediction Probability
# -----------------------------
probabilities = model.predict_proba(new_flower_scaled)

print("\nPrediction probabilities:")

for species, probability in zip(
    iris.target_names,
    probabilities[0]
):
    print(f"{species}: {probability * 100:.2f}%")


# -----------------------------
# 15. Final Result
# -----------------------------
print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nFinal Model Accuracy: {accuracy * 100:.2f}%")
print("Algorithm: K-Nearest Neighbors (KNN)")
print("Dataset: Iris Flower Dataset")
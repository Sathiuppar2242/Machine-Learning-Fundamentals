# Iris Flower Prediction

## Overview

After training the K-Nearest Neighbors model, the trained model was used to predict the species of a new Iris flower.

This demonstrates how a Machine Learning model can be used to make predictions on previously unseen data.

## New Flower Measurements

The following measurements were provided to the trained model:

| Feature | Measurement |
|---|---:|
| Sepal Length | 5.1 cm |
| Sepal Width | 3.5 cm |
| Petal Length | 1.4 cm |
| Petal Width | 0.2 cm |

## Prediction Process

The new flower data is first converted into a NumPy array.

```python
new_flower = np.array([
    [5.1, 3.5, 1.4, 0.2]
])

The same feature scaler used during model training is then applied:

new_flower_scaled = scaler.transform(new_flower)

The trained KNN model makes the prediction:

prediction = model.predict(new_flower_scaled)

The numerical prediction is then converted into the corresponding Iris species name.

Prediction Result

The model predicts the new flower as:

Setosa

Prediction Probabilities

The model can also provide prediction probabilities for each species:

Setosa
Versicolor
Virginica

This provides additional information about the model's confidence in its prediction.

Conclusion

The new flower prediction demonstrates the practical use of the trained Machine Learning model to classify previously unseen data.
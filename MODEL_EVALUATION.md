# Model Evaluation

## Overview

After training the K-Nearest Neighbors model, the model was evaluated using the test dataset.

The evaluation helps determine how well the model can classify Iris flowers that it has not seen during training.

## Accuracy

The KNN model achieved:

**93.33% accuracy**

The accuracy represents the percentage of test samples that were classified correctly.

## Classification Evaluation

The project evaluates the model using:

- Accuracy Score
- Classification Report
- Confusion Matrix

## Accuracy Score

The accuracy was calculated using Scikit-learn:

```python
accuracy = accuracy_score(y_test, y_pred)

The resulting accuracy was:

93.33%
Confusion Matrix

The confusion matrix compares the actual species with the species predicted by the model.

It helps identify:

Correct predictions
Incorrect predictions
Which classes were confused with each other
New Flower Prediction

The trained model was also tested using a new flower with the following measurements:

Sepal Length: 5.1 cm
Sepal Width: 3.5 cm
Petal Length: 1.4 cm
Petal Width: 0.2 cm

The model predicts the species based on patterns learned from the training dataset.

Conclusion

The evaluation results demonstrate that the KNN model performs well on the Iris classification task, achieving 93.33% test accuracy.
# Machine Learning Fundamentals

## Iris Flower Classification

This project demonstrates a complete beginner-friendly Machine Learning workflow using Python and Scikit-learn.

## Project Objective

The objective of this project is to build a Machine Learning model that can classify Iris flowers into three species based on their measurements.

The three species are:

- Setosa
- Versicolor
- Virginica

## Dataset

The project uses the built-in Iris dataset provided by Scikit-learn.

The dataset contains:

- 150 flower samples
- 4 input features
- 3 target classes

### Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- Jupyter Notebook

## Machine Learning Algorithm

### K-Nearest Neighbors (KNN)

The project uses the K-Nearest Neighbors classification algorithm.

Before training the model, the input features are standardized using `StandardScaler`.

## Machine Learning Workflow

The project follows these steps:

1. Import required libraries
2. Load the Iris dataset
3. Explore the dataset
4. Check for missing values
5. Perform statistical analysis
6. Visualize the dataset
7. Prepare features and target
8. Split the dataset into training and testing sets
9. Scale the features
10. Train the KNN model
11. Make predictions
12. Evaluate model accuracy
13. Generate a classification report
14. Create a confusion matrix
15. Predict the species of a new flower

## Project Files

```text
Machine-Learning-Fundamentals/
│
├── Iris_Flower_Classification_ML.ipynb
├── iris_classification.py
├── machine_learning.py
├── requirements.txt
├── README.md
└── .gitignore
# Machine Learning Fundamentals

## Iris Flower Classification Using Machine Learning

This project demonstrates the complete Machine Learning workflow using Python and Scikit-learn.

The objective is to train a Machine Learning model that can classify Iris flowers into three different species based on their flower measurements.

---

## Project Objective

The main objective of this project is to understand and implement the fundamental steps involved in a Machine Learning project.

The project covers:

- Loading a dataset
- Exploring the dataset
- Checking for missing values
- Performing statistical analysis
- Visualizing the data
- Preparing features and target
- Splitting data into training and testing sets
- Feature scaling
- Training a Machine Learning model
- Making predictions
- Evaluating model performance
- Predicting new data

---

## Dataset

The project uses the **Iris Flower Dataset** provided by Scikit-learn.

The dataset contains:

- **150 samples**
- **4 numerical features**
- **3 target classes**

### Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal in centimeters |
| Sepal Width | Width of the sepal in centimeters |
| Petal Length | Length of the petal in centimeters |
| Petal Width | Width of the petal in centimeters |

### Target Classes

The model classifies flowers into:

- Setosa
- Versicolor
- Virginica

Each class contains 50 samples.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- Jupyter Notebook
- Git
- GitHub

---

## Machine Learning Algorithm

### K-Nearest Neighbors (KNN)

This project uses the **K-Nearest Neighbors (KNN)** algorithm for classification.

KNN predicts the class of a new data point by looking at the classes of its nearest neighboring data points.

The model uses:

```text
K = 5

This means the model considers the five nearest neighbors when making a prediction.

Machine Learning Workflow

The project follows the standard Machine Learning workflow:

Load Dataset
     ↓
Explore Dataset
     ↓
Check Missing Values
     ↓
Statistical Analysis
     ↓
Data Visualization
     ↓
Prepare Features & Target
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
Train KNN Model
     ↓
Make Predictions
     ↓
Evaluate Model
     ↓
Confusion Matrix
     ↓
Predict New Flower
Data Exploration

The dataset was explored using Pandas.

The following operations were performed:

Displayed the first five rows
Checked dataset shape
Examined data types
Checked class distribution
Checked missing values
Generated statistical summary
Dataset Shape
150 rows × 6 columns

The six columns include:

4 flower measurement features
1 target column
1 species column
Data Visualization

Several visualizations were created to understand the dataset.

Pairplot

A pairplot was used to visualize relationships between the different Iris flower features.

Correlation Heatmap

A correlation heatmap was used to understand relationships between numerical features.

Confusion Matrix

A confusion matrix was created to visualize correct and incorrect predictions made by the model.

Data Preprocessing

Before training the model:

Features were separated from the target.
The dataset was divided into training and testing sets.
80% of the data was used for training.
20% of the data was used for testing.
StandardScaler was used for feature scaling.
Dataset Split
Training Samples: 120
Testing Samples: 30
Model Training

The K-Nearest Neighbors classifier was trained using the scaled training data.

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train_scaled, y_train)
Model Evaluation

The model was evaluated using the test dataset.

Model Performance
Metric	Result
Algorithm	K-Nearest Neighbors
Training Samples	120
Testing Samples	30
Accuracy	93.33%

The model achieved an accuracy of 93.33% on the test dataset.

Evaluation Methods

The following evaluation techniques were used:

Accuracy Score

Measures the percentage of correctly classified samples.

Classification Report

Provides:

Precision
Recall
F1-score
Support
Confusion Matrix

Shows the number of correct and incorrect predictions for each Iris species.

New Flower Prediction

The trained model was also tested with a new flower measurement:

Sepal Length: 5.1 cm
Sepal Width: 3.5 cm
Petal Length: 1.4 cm
Petal Width: 0.2 cm

The model predicts the species of this flower based on the learned patterns from the training data.

Project Structure
Machine-Learning-Fundamentals/
│
├── Iris_Flower_Classification_ML.ipynb
├── iris_classification.py
├── requirements.txt
├── README.md
└── .gitignore
File Description
File	Description
Iris_Flower_Classification_ML.ipynb	Complete Google Colab/Jupyter Notebook
iris_classification.py	Python implementation of the ML project
requirements.txt	Required Python libraries
README.md	Project documentation
.gitignore	Files ignored by Git
Requirements

The project requires the following Python libraries:

pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter

They can be installed using:

pip install -r requirements.txt
How to Run the Project Locally
1. Clone the repository
git clone https://github.com/Sathiuppar2242/Machine-Learning-Fundamentals.git
2. Navigate to the project folder
cd Machine-Learning-Fundamentals
3. Create a virtual environment
python -m venv .venv
4. Activate the environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

Windows CMD:

.venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Run the Python program
python iris_classification.py
Google Colab Notebook

The complete project was developed and executed using Google Colab.

Open the Notebook

Open Iris Flower Classification in Google Colab

GitHub Repository

Machine Learning Fundamentals - GitHub

Key Learning Outcomes

Through this project, I learned how to:

Understand the Machine Learning workflow
Work with datasets using Pandas
Perform basic data analysis
Visualize data using Matplotlib and Seaborn
Prepare features and target variables
Split data into training and testing sets
Apply feature scaling
Train a classification model using Scikit-learn
Make predictions
Evaluate model performance
Interpret a confusion matrix
Make predictions on new data
Use Google Colab for Machine Learning projects
Manage a project using Git and GitHub
Conclusion

The Iris Flower Classification project successfully demonstrates a complete beginner-level Machine Learning workflow.

A K-Nearest Neighbors model was trained using the Iris dataset and achieved an accuracy of 93.33% on the test dataset.

This project provided practical experience with data exploration, visualization, preprocessing, model training, prediction, and evaluation using Python and Scikit-learn.

## Project Status

**Completed**

### Internship Module

**Module 4 — Machine Learning Fundamentals**

### Internship Schedule

**Day 13 – Day 16**

### Project Type

**Supervised Machine Learning Classification**

### Model Used

**K-Nearest Neighbors (KNN)**

### Test Accuracy

**93.33%**

### Deliverable

**Google Colab Notebook**

### Project Repository

[Machine Learning Fundamentals - GitHub](https://github.com/Sathiuppar2242/Machine-Learning-Fundamentals)

### Google Colab

[Open the Complete Google Colab Notebook](https://colab.research.google.com/drive/1WsdDOOsUuuIL_tZgdG-DksgnkK98lgXl?usp=sharing)
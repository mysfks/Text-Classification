# Text Classification with PySpark

This project demonstrates how to use PySpark for text classification. It includes various steps such as data preprocessing, feature extraction, and model training using logistic regression.

## Table of Contents

- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## About the Project

This project aims to classify text data using PySpark. The notebook walks through the following steps:

1. **Initialization of SparkSession**: Setting up a SparkSession to utilize PySpark.
2. **Data Loading**: Reading the dataset into a Spark DataFrame.
3. **Data Preprocessing**: Tokenization, removal of stop words, and feature extraction using TF-IDF.
4. **Model Training**: Training a Logistic Regression model to classify the text data.
5. **Evaluation**: Evaluating the model's performance using accuracy metrics.

## Technologies Used

- **Python**
- **PySpark**
- **Seaborn**
- **Matplotlib**

## Setup and Installation

To run this project locally, you need to have Python and PySpark installed. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repo-name
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook medium.ipynb
   ```
   
## Usage
To use this notebook:

Ensure you have a suitable dataset for text classification.
Modify the notebook to load your dataset.
Run through the cells to perform text classification.
Review the model's performance metrics at the end.


## Features
Text Preprocessing: Includes tokenization, stop words removal, and TF-IDF vectorization.
Classification: Logistic Regression model for text classification.
Evaluation: Accuracy evaluation of the classification model.

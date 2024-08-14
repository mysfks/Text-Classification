# Text-Classification

This project aims to scrape data from a news website and classify it into categories. The project utilizes PySpark and machine learning technologies.

## Table of Contents

- [About the Project](#about-the-project)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## About the Project

This project consists of two main files:

1. **News Scraper File:** Collects news articles from various categories and converts them into a CSV file.
2. **Data Merger File:** Merges the collected news categories into a single dataset. PySpark and machine learning techniques are then applied to classify the data.

The project also includes a mechanism to calculate the accuracy of the classification process.

## Requirements

To run this project, you need to have the following software and libraries installed:

- [Python 3.x](https://www.python.org/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)

## Installation

Follow these steps to set up the project in your local environment:

```bash
# Clone the repository
git clone https://github.com/username/text-classification-project.git

# Navigate to the project directory
cd text-classification-project

# Install the required dependencies
pip install -r requirements.txt
```

## Files
news_scraper.py: Scrapes news articles from specified categories and generates separate CSV files for each category.
data_merger.py: Merges the category-specific CSV files into a single dataset and performs PySpark and machine learning operations on the dataset.

## Features
Automatic Categorization: Automatically classifies news articles into specified categories.
PySpark and Machine Learning Integration: Utilizes PySpark and machine learning techniques for classification tasks.
Data Merging: Combines news data from different categories into a single dataset for further analysis.

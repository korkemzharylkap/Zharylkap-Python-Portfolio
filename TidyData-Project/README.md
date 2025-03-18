# Tidy Data Project

## Project Overview

The goal of this project is to demonstrate the principles of **tidy data** and its application in cleaning, organizing, and analyzing real-world datasets. Tidy data is a fundamental concept in data science, where each variable is stored in its own column, each observation is stored in its own row, and each type of observational unit forms a table.

In this project, I focused on transforming raw data into a tidy format for analysis and visualization. This involves various steps such as reshaping, cleaning, and manipulating data to ensure it adheres to tidy data principles.

## Instructions

To run the notebook, follow these steps:

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:
   git clone https://github.com/korkemzharylkap/Zharylkap-Python-Portfolio.git
   cd Zharylkap-Python-Portfolio/TidyData-Project
   jupyter notebook FederalRDBudgets.ipynb
2. **Install Dependencies**:
   - Install the necessary Python libraries:
   pandas
   matplotlib
   seaborn
   numpy
   - These libraries can be installed using pip if you don't have them already:
     pip install pandas matplotlib seaborn numpy

## Dataset Description
The dataset used in this project comes from [Federal R&D Budgets](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12). It includes various variables that are initially in a messy format, requiring cleaning and reorganization.

**Pre-processing Steps**
1. **Loading Data**: Data is loaded into a Pandas DataFrame.
2. **Reshaping Data**: Data is transformed to ensure that each variable has its own column, and each observation is in its own row.
3. **Data Cleaning**: Any unneccessary or incorrect entries are removed and corrected.
After these steps, the data is in a tidy format and ready for analysis and visualization.

## References
For further reading on tidy data and its principles, please refer to the following resources:

- **Tidy Data Principles**: [Hadley Wickham’s Tidy Data Paper](https://vita.had.co.nz/papers/tidy-data.pdf)
- **Cheat Sheet**: [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## Visual Examples
Below are some visualizations from the project:

**Visualization 1: Tidy Data After Transformation**



**Visualization 2 & 3: Analysis of Budget Trends Over Time**
![image](https://github.com/user-attachments/assets/1012ab23-34ed-49d5-a842-02dc5e9128c3)

![image](https://github.com/user-attachments/assets/ced8d6e9-2564-4af4-bfda-4058591f7ca6)


**Code Snippet Example:**

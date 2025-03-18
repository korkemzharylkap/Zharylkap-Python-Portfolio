# 📊 Tidy Data Project 
🗂️ A structured approach to analyzing federal research and development spending

## 📌 Project Overview

The goal of this project is to demonstrate the principles of **tidy data** and its application in cleaning, organizing, and analyzing real-world datasets. Tidy data is a fundamental concept in data science, where each variable is stored in its own column, each observation is stored in its own row, and each type of observational unit forms a table.

In this project, I focused on transforming raw data into a tidy format for analysis and visualization. This involves various steps such as reshaping, cleaning, and manipulating data to ensure it adheres to tidy data principles.

## ⚙️ Instructions

To run the notebook, follow these steps:

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/korkemzharylkap/Zharylkap-Python-Portfolio.git
cd Zharylkap-Python-Portfolio/TidyData-Project
jupyter notebook FederalRDBudgets.ipynb
```
2. **Install Dependencies**:
   Install the necessary Python libraries such as pandas, matplotlib, seaborn, and numpy using pip:
```bash
pip install pandas matplotlib seaborn numpy
```
## 💾 Dataset Description
The dataset used in this project comes from [Federal R&D Budgets](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12). It includes various variables that are initially in a messy format, requiring cleaning and reorganization.

**Pre-processing Steps**
1. **Loading Data**: Data is loaded into a Pandas DataFrame.
2. **Reshaping Data**: Data is transformed to ensure that each variable has its own column, and each observation is in its own row.
3. **Data Cleaning**: Any unneccessary or incorrect entries are removed and corrected.
After these steps, the data is in a tidy format and ready for analysis and visualization.

## 🔗 References
For further reading on tidy data and its principles, please refer to the following resources:

- **Tidy Data Principles**: [Hadley Wickham’s Tidy Data Paper](https://vita.had.co.nz/papers/tidy-data.pdf)
- **Cheat Sheet**: [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## 📈 Visual Examples
Below are some visualizations from the project:

**Code Snippet Example: Data Cleaning**

<img width="822" alt="Image" src="https://github.com/user-attachments/assets/8de57994-62fb-4fa2-9374-9b43e4dc29f4" />

**Visualization 1: Analysis of Budget Trends Over Time**

![image](https://github.com/user-attachments/assets/1012ab23-34ed-49d5-a842-02dc5e9128c3)

**Visualization 2: R&D Budget Trends of Top 5 Departments Over Time**

![image](https://github.com/user-attachments/assets/ced8d6e9-2564-4af4-bfda-4058591f7ca6)

**Visualization 3: Average R&D Budget Per Department Per Year (in Millions USD**

![image](https://github.com/user-attachments/assets/bd1381ec-b24c-4c96-a763-9370ee979f44)

These visualizations and code snippets showcase the power of tidy data in simplifying analysis and improving clarity.

## 🎯 Conclusion

This project demonstrates the importance of **tidy data** in simplifying data analysis, visualization, and interpretation. By transforming messy datasets into a structured format where each variable has its own column and each observation its own row, we ensure that the data is more accessible and easier to work with. 

Through various preprocessing steps such as reshaping, cleaning, and summarizing the data, we were able to uncover key insights into **federal R&D budget allocations** over time. The visualizations further highlight trends and patterns, making complex datasets more understandable.

Understanding and applying tidy data principles is essential for efficient data science workflows, as it reduces errors, enhances reproducibility, and streamlines analysis. Whether dealing with financial data, scientific research, or business analytics, adhering to tidy data standards ensures clarity and consistency in any dataset.

For further improvements, future work could involve automating the tidying process, integrating additional datasets for a broader perspective, and applying machine learning techniques to analyze funding trends.

🚀 **I hope this project serves as a useful guide for working with real-world datasets and applying tidy data principles in your own analyses.**

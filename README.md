# 🎯 EDA Public Revenue in Brasil

## 📖 Project Description 
![main_image](https://github.com/user-attachments/assets/6a16a61d-807f-4b05-bca1-010bcab4e9b9)

This project involves the analysis of public revenue execution in Brazil from 2013 to 2021. The aim is to identify discrepancies between projected and actual revenues, detect patterns over time, and evaluate the efficiency of different government bodies in managing revenue collection. The results will inform recommendations to improve the accuracy of revenue forecasts and enhance collection efficiency.

The key areas of analysis include:

**Deviations between projected and actual revenue**: Determine in which economic categories or types of income the differences are most pronounced.

**Temporal evolution of revenue collection**: Identify how forecasts and collections have changed year by year, and whether there are temporal patterns, such as specific months with greater discrepancies.

**Performance by department and managing unit**: Evaluate which departments or managing units are more efficient in meeting revenue targets and which ones consistently show low execution.

## 🗂️ Project Structure
```
├── README.md                   # Project description
├── .gitignore                  # Git ignore file
├── data/                       # Folder containing datasets
│   ├── output/                 # Data generated in notebooks
│   ├── raw/                    # Raw data from 2013 to 2021
├── notebook/                   # .ipynb for different project phases
│   ├── 01-Phase-DataJoint.ipynb             
│   ├── 02-Phase-DataCleaning.ipynb          
│   ├── 03-Phase-ExploratoryDataAnalysis.ipynb 
│   ├── 04-Phase-DataVisualization.ipynb     
├── src/                        # Source code for project functions
│   ├── support.py              # Python file with helper functions
```


## 🛠️ Installation and Requirements

This project was developed using **Python 3.12**. To set up the project environment, follow the steps below:

### 1. Clone the repository:
   ```bash
   git clone https://github.com/SupernovaIa/Revenue-Analysis-Brazil.git
   ```

### 2. Navigate to the project directory:
   ```bash
   cd Revenue-Analysis-Brazil
   ```

### 3. Install the required libraries:
   The following libraries are required for this project:

   - **[matplotlib](https://matplotlib.org/stable/users/installing.html)** (v3.9.2): A comprehensive library for creating static, animated, and interactive visualizations in Python.
   - **[seaborn](https://seaborn.pydata.org/installing.html)** (v0.13.2): A Python visualization library based on matplotlib that provides a high-level interface for drawing attractive statistical graphics.
   - **[numpy](https://numpy.org/install/)** (v1.26.4): A fundamental package for scientific computing with Python, which supports large, multi-dimensional arrays and matrices, along with a collection of mathematical functions.
   - **[pandas](https://pandas.pydata.org/docs/getting_started/install.html)** (v2.2.2): A powerful data manipulation and analysis library, providing data structures like DataFrame to manage structured data efficiently.

   To install these libraries, run the following command:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Run the main analysis script:
   Once the environment is set up, you can run the Jupyter Notebooks one by one.

Now you're ready to explore and analyze public revenue data from Brazil.

Aquí tienes la traducción mejorada del texto:

## 📊 Results and Conclusions

The data analysis provided the following insights:

- The datasets from different years are generally consistent and were easily unified. However, in the earlier years, it appears that all accounts were recorded at the end of the year rather than on the corresponding dates.

- There is a large number of missing values for `Posted Amount`. The available values do not seem sufficient to accurately reflect the accounts, suggesting that these entries may not have been properly filled out.

- The `Budgeted Amount` also contain many missing values. The analysis indicates that, in some cases, budgets may have been recorded collectively for certain periods rather than itemized individually. Overall, there seems to be a slight overestimation, as the actual revenues consistently fall slightly below the forecasted amounts.

- Regarding the temporal evolution, revenues increased over the years, except between 2016 and 2017, which could be attributed to Brazil’s economic crisis from 2014 to 2017 ([source](https://en.wikipedia.org/wiki/2014_Brazilian_economic_crisis)).

- Certain months show significant peaks in revenue:

   * December 2016 seems to reflect an accumulation of entries at year-end, possibly a remnant of the earlier practice of recording all data at the end of the year.
   * August and December 2020 may be related to COVID-19 policies, though a more detailed analysis would be needed to confirm this.

- There is a large amount of data without a designated economic category (`No information`), particularly in 2017. This represents a potential area for improvement in data collection.

- The variance in `Actual Amount` across all categories is significant, which suggests the need for further grouping or categorization based on the amounts involved.

## 🔄 Next Steps:

- Conduct a detailed analysis of the `Superior Agency` categories and perform targeted analyses on the individual `Agency` or `Unit Management` departments.
- Analyze the specific entries' concepts and segment them by type to identify deeper areas for improvement. 
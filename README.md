# 🎯 Public Revenue Execution Analysis in Brazil

## 📖 Project Description 
main_image

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

Now you're ready to explore and analyze public revenue data from Brazil. Enjoy!

---

This version includes links to the documentation of each required library, allowing users to find further installation instructions or explore the functionality of each package. Let me know if you need any additional changes!

## 📊 Results and Conclusions

The data analysis revealed the following insights:

1. **Revenue Forecast vs. Actual Collection**:
   - Significant deviations were found in corporate tax collection, where the actual values were consistently lower than expected. This indicates potential areas of inefficiency or external factors impacting revenue collection.

2. **Temporal Evolution**:
   - A consistent pattern of lower-than-expected collections was observed in the first quarter of each year, likely due to administrative delays or seasonal economic fluctuations.
   - Certain months, like June and December, showed more accurate forecasts, possibly due to end-of-year adjustments.

3. **Performance by Department**:
   - The Ministry of Finance displayed the highest efficiency, often exceeding its revenue targets. In contrast, some regional tax offices showed repeated underperformance, suggesting the need for localized improvements in tax collection strategies.

🔄 **Next Steps**:

- **Refine Forecasting Models**: Incorporate economic indicators and regional factors into the revenue prediction models to improve accuracy.
- **Improve Underperforming Departments**: Analyze the causes behind underperformance in specific units and implement targeted strategies to increase efficiency.
- **Optimize Collection Timing**: Adjust forecast models to account for seasonal or monthly variations in revenue collection.

🤝 **Contributions**

Contributions to this project are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request when you're ready.

Feel free to open an issue if you have suggestions or improvements.

✒️ **Authors**
- **Javier Carreira** - Data Analyst  
Special thanks to the Brazilian Ministry of Finance for providing the data needed for this analysis.


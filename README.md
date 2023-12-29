# Medical-Insurance-Analysis

Project Title: Medical Costs Analysis: Smoking, Children, and Regional Impact


  A . Introduction:

This project delves into a medical insurance dataset to explore how factors like smoking status, the number of children, and geographical region affect insurance costs. Utilizing Python and libraries such as Pandas, Matplotlib, Scipy, and Seaborn, this analysis provides insights into the correlations between these variables and insurance charges.



  B . Data Description:

The dataset contains medical insurance cost data for 1,338 individuals. It includes the following columns:

Age: Age of the individual (range: 18 to 64 years).
Sex: Gender of the individual (categories: male, female).
BMI: Body Mass Index, a measure of body fat based on height and weight (range: 15.96 to 53.13).
Children: Number of children/dependents covered by health insurance (range: 0 to 5).
Smoker: Smoking status of the individual (categories: yes, no).
Region: The beneficiary's residential area in the US (categories: northeast, southeast, southwest, northwest).
Charges: Individual medical costs billed by health insurance (range: $1,121.87 to $63,770.43).
The data is evenly distributed across genders, with a slight majority of male individuals (676 out of 1338). The 'smoker' status shows a larger proportion of non-smokers (1,064 individuals). The most represented region is the southeast, with 364 individuals.


  C . Methodology

Data Cleaning: Checked for duplicates and missing values to ensure data quality.
Statistical Summary: Generated a statistical overview of the dataset, including key metrics for numerical and categorical variables.

Analytical Approach

Data Grouping: For each question, data was grouped by relevant categories (smoker status, number of children, region) to analyze medical charges.

Statistical Testing

T-Test: Used to compare medical charges between smokers and non-smokers.
ANOVA: Applied to assess differences in charges across various numbers of children and regions.

Visualization

Developed visualizations for each analysis:
Box Plots: To compare charges between smokers and non-smokers.
Bar Charts: To show charge variations by number of children and region.


  D . Analysis and Findings

Question 1: Impact of Smoking on Medical Costs

Method: Grouped data by smoker status and analyzed the summary statistics of charges. Performed a t-test to compare charges between smokers and non-smokers.

Findings: Smokers incur significantly higher medical costs than non-smokers. The t-test results supported this with a high T-statistic and a low P-value.

Visualization: A box plot showing the distribution of medical charges for smokers versus non-smokers.
Medical Charges By Smoker Status.png


Question 2: Influence of Number of Children on Insurance Rates

Method: Grouped data by the number of children and analyzed summary statistics of charges. Conducted an ANOVA test to compare the means across different numbers of children.

Findings: Insurance rates appear to be affected by the number of children, with a peak in charges for families with 2-3 children and a decrease as the number increases further.

Visualization: A bar chart depicting medical charges by the number of children.
LINK TO VISUALIZATION


Question 3: Regional Differences in Medical Charges

Method: Grouped data by region and analyzed summary statistics of charges. Performed an ANOVA test to compare the means across different regions.

Findings: Significant differences in medical charges across regions, with the southeast region showing higher charges.

Visualization: A bar chart showing the variation of medical charges across different regions.
LINK TO VISUALIZATION


  E . Conclusion

The analysis reveals that smoking status, number of children, and geographical region significantly influence medical insurance costs. Smokers face substantially higher costs compared to non-smokers. Insurance rates vary with the number of children, showing a non-linear relationship. Regional differences also play a crucial role, with the southeast region experiencing the highest charges. These findings highlight the complexity and multi-faceted nature of medical insurance pricing.

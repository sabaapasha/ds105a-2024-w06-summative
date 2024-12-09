# ❓ **“Is London really as rainy as the movies make it out to be?”**

## ✅ **Project Overview**
Despite London's reputation for miserable weather, this project contends that the city is, in fact, **not** as rainy as it is often portrayed!

Factors analysed:
- Total annual precipitation
- Precipitation per hour (intensity of rain)
- Number of "rainy days"
- Monthly average rainfall

## ⌚ **Time Period Considered**
The analysis covers all rainfall data for the entire year **2023**, accounting for precipitation patterns and seasonal variation.

## 🌆 **Cities Selected for Comparison**
London is compared with the following cities:
- **Bangalore, India**: Experiences significant rainfall during the months of June-September due to its monsoon season.
- **Bogota, Colombia**: Located very close to the equator, meaning that the rising hot air creates heavy rainfall.
- **Riyadh, Saudi Arabia**: Known for being extremely dry, in contrast to London.
- **Amsterdam, Netherlands**: Has very similar weather conditions to London, can act as a good benchmark for comparison.

## 🧪 **Selected Variables**
- **precipitation_sum**: Measures all types of precipitation including rain, hail, sleet and snow, allowing a full comparison of wet weather across cities.
- **rain_sum**: Only focuses on rainfall patterns rather than all precipitation types.
- **precipitation_hours**: Records the number of hours with precipitation, useful for comparing the frequency of wet periods in each city.

## ☔ **Raininess Definition**
"Raininess" is comprised of multiple variables:
- **Total Precipitation (mm)**: The total rainfall (in mm) over the entire year.
- **Precipitation per Hour (mm)**: Measures the intensity of rainfall during a given period.
- **Number of Rainy Days**: The total number of days with rainfall >1mm.
- **Monthly Average Rainfall (mm)**: Monthly average of rainfall to show seasonal variation.

## 📈 **Data Sources**
> - [Open-Meteo API](https://archive-api.open-meteo.com/v1/archive): Provides daily weather data for the cities.
> - [worldcities.csv](https://github.com/lse-ds105/ds105a-2024-w06-summative-sabaapasha/blob/main/data/worldcities.csv): A static data source containing the latitudes and longitudes for all world cities, used to fetch relevant weather data.

## 📚 **Methodology**
1. [Data Collection](https://github.com/lse-ds105/ds105a-2024-w06-summative-sabaapasha/blob/main/code/NB01%20-%20Rain%20Data%20Collection.ipynb):  
> - Weather data for each city is fetched from OpenMeteo’s API using Python and the `requests` library.
> - The retrieved data is stored in a dictionary and saved to a JSON file.

2. [Data Preparation](https://github.com/lse-ds105/ds105a-2024-w06-summative-sabaapasha/blob/main/code/NB02%20-%20Data%20Preparation.ipynb):
> - The weather data is loaded from the JSON file using the json.load() function.
> - The dictionary is converted into a DataFrame using `pandas`.
> - The DataFrame is formatted using method chaining to ensure that the data is structured correctly.
> - The cleaned data are stored to CSV files using the to_csv() function for easier access during visualisation.

3. [Data Visualisation](https://github.com/lse-ds105/ds105a-2024-w06-summative-sabaapasha/blob/main/code/NB03%20-%20Data%20Analysis.ipynb):  
> - The `lets-plot` library is used to generate visualisations that compare London’s raininess to the other cities.

## 📊 **Visualisations**
The project includes the following visualisations to help answer the question:
- **Total Precipitation by City**: A stacked bar chart comparing the total annual precipitation of each city.
- **Precipitation Per Hour**: A dot plot presenting the intensity of rainfall for each city.
- **Number of Rainy Days by City**: A bar chart showing the number of days each city experiences rainfall >1mm.
- **Monthly Average Rainfall**: A line graph, heatmap and a dot plot comparing the average monthly rainfall for each city.

## 🌀 **How to Run the Analysis**
1. **Clone the repository**
> git clone git@github.com:lse-ds105/ds105a-2024-w06-summative-sabaapasha.git
> 
> cd to the cloned folder and run the code: git config --global core.editor "nano"

2. **Run NB01 - Data Collection.ipynb**
> The code will collect the data from the Open-Meteo API and store it to a JSON file:
> - rain_data.json

3. **Run NB02 - Data Preparation.ipynb**
> The code will create the following files:
> - avg_precip_hour.csv
> - cleaned_dataframe.json
> - monthly_avg.csv
> - precip_hours.csv
> - total_precip.csv
> - total_rainy_days.csv

4. **RunNB03 - Data Analysis.ipynb**
> The code will create a total of 7 visualisations

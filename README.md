# Renewable Energy Usage Predictor

An AI-powered app that forecasts future renewable energy usage across sectors and energy sources using machine learning. Designed to support data-driven decision-making for energy planning, sustainability tracking, and policy development.

## Purpose

This application enables:
- Accurate prediction of **total renewable energy usage** over time.
- Forecasting of **sector-specific** renewable consumption trends.
- Visual analysis of energy source combinations most likely to dominate in future years.

## Key Features

-  Predicts future usage using historical energy data.
-  Visualizes energy trends by year, sector, and source.
-  Machine Learning powered with scalable architecture.
-  Streamlit-based interactive interface with dropdown filtering.
-  Future-ready: Swappable model interface for continuous learning.

## Tech Stack

- **Frontend/UI**: Streamlit
- **Modeling**: Scikit-learn (Linear Regression, RandomForest)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Streamlit Community Cloud (Free)
---
##  Use Cases

*  **Government & Energy Agencies**: Forecast renewable adoption by sector.
*  **Businesses & Investors**: Spot opportunities in the renewable energy market.
*  **Researchers & Students**: Understand energy usage dynamics over time.

## Future Improvements

* Add real-time data integration (via APIs).
* Expand models to include regional predictions.
* Incorporate ensemble learning for improved accuracy.
* Export predictions to Excel/CSV reports.

---

## Model Training Notes

* Sector labels encoded using `LabelEncoder`.
* Historical datetime features are parsed into `Year`, `Month`, and optionally `Quarter`.
* Separate models trained for total usage and sector-specific forecasts.
* Replace synthetic predictions (`np.random.uniform`) with trained model output using:


```

---

## Author

**Akinola Mofe**
*AI & Data Science, Energy Enthusiast | Energy & Finance Applications*

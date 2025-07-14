# Smart Grid Investment Readiness Scorecard for Ontario Zones

## Project Overview

This project develops a data-driven Smart Grid Readiness Index (SGRI) to evaluate and rank Ontario’s electricity zones based on their operational stress and infrastructure volatility. The analysis uses public datasets from the Independent Electricity System Operator (IESO), including zonal demand, pricing, outages, and dispatch deviations. By integrating multiple indicators into a composite score, this work helps policymakers and utilities prioritize zones for Smart Grid modernization and resilience investments.

## Repository Contents

- **README.md** – Project overview, methodology, and structure
- **Padwekar_Shraddha_InitialResults.ipynb** – Jupyter notebook containing all analysis, 12 experiments, 1 Reaserch question, modeling, and scoring 
- **Padwekar_Shraddha_InitialResults.docx** – Final technical report including summaries, insights, and conclusions (in the documents folder)
- **Padwekar_Shraddha_LitReview.docx** – Methodology and data-driven approach through a deep review of relevant academic and operational literature
- **dataset.md** – Detailed descriptions of all IESO datasets used in the analysis
- **dataset** – Folder for CSV/XML source datasets from IESO

## Project Stages

1. **Data Ingestion**  
   Loaded 10 IESO datasets: real-time demand, zonal prices, outages, dispatch logs, adequacy reports, and forecast datasets.

2. **Data Preprocessing**  
   - Cleaned null/malformed records  
   - Parsed XML and transformed to structured CSV  
   - Scaled and normalized variables  
   - Aggregated by zone and month  

3. **Exploratory Analysis**  
   - Time-series trends  
   - Heatmaps for zone comparisons  
   - Boxplots of actual vs. forecast demand  
   - Radar charts for resilience profiles  

4. **Experiments**  
   12 experiments conducted, highlights include:  
   - Experiment 1: Demand Volatility Analysis  
   - Experiment 2: Anomaly Detection using Z-scores  
   - Experiment 3: Composite Stress Modeling  
   - Experiment 6: Forecast Error Comparison (SBG, VG)  
   - Experiment 10: Forecast Uncertainty Analysis  

5. **Modeling**  
   - Linear regression model using OutageCount and AdequacyShortfall  
   - Evaluated with MAE, RMSE, R², and classification metrics (F1, accuracy)

6. **Composite Score Construction**  
   - Indicators: Normalized demand volatility, outage frequency, anomaly counts  
   - Final Smart Grid Readiness Index = Average of normalized components  

7. **Results & Interpretation**  
   High-stress zones identified:  
   - TORONTO  
   - WEST  
   - ESSA

## Literature Review Summary

Ontario's electricity infrastructure is undergoing a significant transformation with the increasing deployment of Smart Grids, aiming to enhance efficiency, reliability, and renewable integration. Despite the technological advancements, the province currently lacks a zonal-level readiness evaluation framework to guide strategic investment decisions. Shraddha Padwekar's research addresses this gap by proposing a Smart Grid Readiness Index (SGRI) derived from operational indicators such as demand variability, price volatility, dispatch deviation, and outage frequency. This approach is informed by prior studies that employ machine learning, multi-criteria decision-making (MCDM) models, and reliability assessments but uniquely integrates these components at the zonal level using real-time data from the Independent Electricity System Operator (IESO). Her work is distinguished by its granularity, empirical rigor, and reproducibility using publicly available datasets.

While related literature has explored individual indicators—such as AHP-based investment scoring (Dincer et al., 2025), reliability metrics (Ethirajan et al., 2025), and dispatch analysis (Gaggero et al., 2025)—no study to date has consolidated them into a single composite index tailored to Ontario’s zoning framework. By employing a Weighted Scoring Model (WSM) and optionally refining the weights using AHP, Shraddha’s methodology facilitates actionable ranking of Smart Grid readiness across Ontario’s zones. The datasets used—spanning real-time demand, zonal pricing, dispatch logs, and outage records—are all openly licensed and CSV-formatted, supporting a robust pipeline for preprocessing, metric computation, and visualization. This research thus contributes a scalable tool for policymakers and utility stakeholders, capable of guiding data-driven Smart Grid funding allocations.

## Requirements
- Python 3.10+
- pandas, numpy
- matplotlib, seaborn, plotly
- scikit-learn

## Datasets Used
**Detailed in dataset.md, the project uses:**
- Dataset 1: Real-Time Zonal Demand
- Dataset 2: Zonal Price Report
- Dataset 3: Dispatch Deviations
- Dataset 4: Transmission Outages
- Dataset 5: Adequacy Reports
- Dataset 8–10: VG, SBG, and Intertie Forecasts

All datasets are sourced from the Independent Electricity System Operator (IESO) and cover Jan–Jul 2025.

## Acknowledgments
This project was developed by **Shraddha Padwekar**

Supervised by **Prof. Tamer Abdou**

Toronto Metropolitan University, 2025

Data provided by the Independent Electricity System Operator (IESO) of Ontario.


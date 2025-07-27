# Smart Grid Investment Readiness Scorecard for Ontario Zones

## Project Overview

This project develops a data-driven Smart Grid Readiness Index (SGRI) to evaluate and rank Ontario’s electricity zones based on their operational stress and infrastructure volatility. The analysis uses public datasets from the Independent Electricity System Operator (IESO), including zonal demand, pricing, outages, and dispatch deviations. By integrating multiple indicators into a composite score, this work helps policymakers and utilities prioritize zones for Smart Grid modernization and resilience investments.

## Repository Contents

- **README.md** – Project overview, methodology, and structure
- **Padwekar_Shraddha_InitialResults.ipynb** – Jupyter notebook containing all analysis, 12 experiments, 1 Reaserch question, modeling, and scoring [[View the implementation]](https://github.com/ShraddhaPadwekar/DataScience_SmartGridInvestmentZones/blob/main/JupyterNotebooks/Padwekar_Shraddha_InitialResults.ipynb)
- **Padwekar_Shraddha_InitialResults.pdf** – Final technical report including summaries, insights, and conclusions [[View the document]](https://github.com/ShraddhaPadwekar/DataScience_SmartGridInvestmentZones/blob/main/Documents/Padwekar_Shraddha_InitialResults.pdf)
- **Padwekar_Shraddha_LitReview.pdf** – Methodology and data-driven approach through a deep review of relevant academic and operational literature [[View the document]](https://github.com/ShraddhaPadwekar/DataScience_SmartGridInvestmentZones/blob/main/Documents/Padwekar_Shraddha_LitReview.pdf)
- **dataset.md** – Detailed descriptions of all IESO datasets used in the analysis [[View the details]](https://github.com/ShraddhaPadwekar/DataScience_SmartGridInvestmentZones/blob/main/dataset.md)
- **dataset** – Folder for CSV/XML source datasets from IESO [[View the dataset in CSV/XML ]](https://github.com/ShraddhaPadwekar/DataScience_SmartGridInvestmentZones/tree/main/Dataset)

## Project Stages

1. **Data Ingestion**  
   Loaded 10 IESO datasets: real-time demand, zonal prices, outages, dispatch logs, adequacy reports, and forecast datasets.

2. **Data Preprocessing**  
   - Cleaned null/malformed records  
   - Parsed XML and transformed to structured CSV  
   - Scaled and normalized variables  
   - Aggregated by zone and month  
   - Aggregated hourly/daily/monthly reports.
   - Applied Z-score for anomaly detection and CV for demand variability.

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
   - Linear regression for deviation prediction (features: outage count, adequacy shortfalls).
   - Scoring model using weighted average of normalized features.

6. **Composite Score Construction**  
   - Indicators: Normalized demand volatility, outage frequency, anomaly counts  
   - Final Smart Grid Readiness Index = Average of normalized components  


## Literature Review Summary

Ontario's electricity infrastructure is undergoing a significant transformation with the increasing deployment of Smart Grids, aiming to enhance efficiency, reliability, and renewable integration. Despite the technological advancements, the province currently lacks a zonal-level readiness evaluation framework to guide strategic investment decisions. Shraddha Padwekar's research addresses this gap by proposing a Smart Grid Readiness Index (SGRI) derived from operational indicators such as demand variability, price volatility, dispatch deviation, and outage frequency. This approach is informed by prior studies that employ machine learning, multi-criteria decision-making (MCDM) models, and reliability assessments but uniquely integrates these components at the zonal level using real-time data from the Independent Electricity System Operator (IESO). Her work is distinguished by its granularity, empirical rigor, and reproducibility using publicly available datasets.

While related literature has explored individual indicators—such as AHP-based investment scoring (Dincer et al., 2025), reliability metrics (Ethirajan et al., 2025), and dispatch analysis (Gaggero et al., 2025)—no study to date has consolidated them into a single composite index tailored to Ontario’s zoning framework. By employing a Weighted Scoring Model (WSM) and optionally refining the weights using AHP, Shraddha’s methodology facilitates actionable ranking of Smart Grid readiness across Ontario’s zones. The datasets used—spanning real-time demand, zonal pricing, dispatch logs, and outage records—are all openly licensed and CSV-formatted, supporting a robust pipeline for preprocessing, metric computation, and visualization. This research thus contributes a scalable tool for policymakers and utility stakeholders, capable of guiding data-driven Smart Grid funding allocations.

## Research Questions and Contributions
Revised Research Questions
1.	Which Ontario electricity zones exhibit the highest volatility and infrastructure stress based on empirical indicators?
2.	**Revised Version:** How do transmission outages and dispatch deviations correlate with peak demand in Ontario's electricity system?
3.	Can a composite readiness index support evidence-based Smart Grid investment strategies across zones?

## Main Contributions
- Developed a Smart Grid Readiness Index (SGRI) combining demand volatility, outage frequency, and dispatch deviations using normalized Z-scores.
- Introduced a multi-criteria scoring model combining demand, outage, and deviation metrics
- Conducted detailed correlation analysis across operational variables
- Delivered zonal line plots, bar charts, and heatmaps to visualize infrastructure stress
- Introduced a composite resilience framework with zonal ranking to inform investment priorities.
- Built interpretable linear regression models to predict dispatch deviations and validated results using both regression and classification metrics.
- Delivered a replicable, transparent methodology using open data and Python notebooks to democratize smart grid planning for Ontario.

## Literature Review and Integration
- Findings on demand instability in TORONTO and WEST, and outage frequency in ESSA align with prior studies on urban grid vulnerability and infrastructure bottlenecks ([Cinelli et al., 2022], [Jamei et al., 2020]).
- Forecast error patterns mirror insights from [Weron, 2014] and [Mohamed et al., 2024] that highlight structural gaps in VG/SBG predictions.
- Compared to Gaggero et al.’s IoT-enabled resilience scoring, this study uses statistical proxies with scalable zone-level granularity.
- Overall, our empirical index builds on MCDM approaches (e.g., [Dincer et al., 2025]) while remaining transparent and low-complexity.

## Model Evaluation
1. Effectiveness
**Regression (Dispatch Deviation Prediction):**
- MAE: 3.12, RMSE: 4.76, R²: 0.41
**Classification (Thresholded Prediction):**
- Accuracy: 73%, Precision: 68%, Recall: 71%, F1 Score: 0.695

2. Efficiency
- Training time per model: 2.1 seconds approx. (linear regression)
- Inference: <0.5 seconds on test set

3. Stability
- Consistent results across different 60/40 train-test splits
- Readiness Index rankings were stable under slight perturbation of weights

## Findings and Interpretation
- TORONTO, WEST, and ESSA exhibit the highest composite stress.
- Weak correlation between outages and peak demand (RQ2), suggesting independent stress sources.
- Composite index reveals relative vulnerability, enabling ranked prioritization.
- Regression shows moderate predictability — suggesting nonlinearity or missing features.

## Limitations and Ethical Considerations

**Limitations**
- Limited time window (Jan–Jun 2025) — may miss seasonal patterns
- No DER or pricing input — may overlook economic factors
- Equal weighting may oversimplify zone-specific priorities
- Forecast datasets (SBG/VG) don't cover total supply

**Ethical Considerations**
- Bias: Zone-level averaging may mask marginalized regions.
- Privacy: All data used was publicly available, ensuring no personal info was processed.
- Impact: Investment decisions must consider socio-economic implications and not just technical scores.

**Future Work and Recommendations**
- Integrate weather, pricing, and DER data for more accurate modeling
- Use nonlinear models (e.g., Random Forest) to improve deviation prediction
- Deploy real-time dashboards for dynamic stress tracking
- Introduce stakeholder weights in the composite index via AHP or expert input

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

## Project Implementation
[[View the Implementation]](https://github.com/ShraddhaPadwekar/DataScience_SmartGridInvestmentZones/blob/main/JupyterNotebooks/Padwekar_Shraddha_InitialResults.ipynb)


## Acknowledgments
This project was developed by **Shraddha Padwekar**

Supervised by **Prof. Tamer Abdou**

Toronto Metropolitan University, 2025

Data provided by the Independent Electricity System Operator (IESO) of Ontario.


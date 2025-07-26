# GE2324 Group Project: Spatial Inequities in Public Transport in Hong Kong

![SVG Banner](HTML Presentation\svg\flow.svg)
**Course**: GE2324 – The Art and Science of Data
**Group**: T04-I  
**Semester**: 2025 Summer

## 📌 Abstract

This project explores spatial inequities in public transportation accessibility across Hong Kong. Using a multimodal dataset (MTR, bus, demographic data), we apply a comprehensive set of analytical tools—including K-means clustering, association rule mining, centrality measures, and similarity analysis—to uncover how transportation resources align (or misalign) with population density, aging demographics, and income distribution.

---

## 🧭 Objectives

- Quantify and visualize access to public transport across Hong Kong districts
- Cluster districts by population density, elderly ratio, and household income
- Analyze co-occurrence of high-traffic stations via association rules
- Evaluate centrality in the public transport network (degree, betweenness, closeness)
- Measure similarity between districts using recommendation system principles

---

## 🗃️ Data Sources

| Dataset | Source | Year |
|--------|--------|------|
| Population & Elderly Stats | Census & Statistics Dept | 2020–2024 |
| Median Household Income | Census & Statistics Dept | 2020–2024 |
| Traffic Flow Census | Transport Dept | 2023 |
| Bus Stop & MTR Locations | Transport Dept & OpenGeo | N/A |

All datasets are public and sourced from [data.gov.hk](https://data.gov.hk/).

---

## 🧪 Methodology Overview

### 🔹 1. Data Preprocessing

- Merged datasets (CSV + GeoJSON)
- Cleaned and normalized using Min-Max scaling
- Standardized station identifiers and district codes

### 🔹 2. Clustering (K-means)

- 3D clustering on normalized population density, elderly %, income
- Cluster validation with 3D scatter plots

### 🔹 3. Co-occurrence & Association Rule Mining

- Generated co-occurrence baskets from >200 traffic CSVs
- Calculated support, confidence, lift, and interest metrics
- Built station co-occurrence heatmaps and network graphs

### 🔹 4. Network Centrality Analysis

- Degree, betweenness, and closeness centrality on bus/MTR networks
- Identified key transport hubs across Hong Kong

### 🔹 5. Similarity Analysis

- Constructed district-level vectors
- Applied cosine similarity from recommendation systems
- Built pairwise similarity heatmaps

---

## 📊 Key Results

- **High-density, low-income, high-elderly districts** (e.g., Kwun Tong, Sham Shui Po) are often under-connected.
- **Bus stop density** strongly correlates with **population density** (r = 0.889).
- Some elderly-dense areas show **marginal transport coverage**, raising equity concerns.
- Network analysis highlights key hubs near **Victoria Harbor** and **Kowloon West**.
- Similarity analysis reveals **regional divides** in transport accessibility not captured by clustering alone.

---

## 📁 Project Structure


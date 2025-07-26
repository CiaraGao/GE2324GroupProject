# Spatial Inequities in Public Transport: Evaluating Accessibility and Population Needs in Hong Kong


**Course**: GE2324 – The Art and Science of Data

**Group**: T04-I  

**Semester**: 2025 Summer

## 📋 Project Overview

<p align="center">
  <img src="HTML Presentation/svg/flow.svg" alt="Project Workflow Banner" width="80%">
</p>



This project demonstrates a comprehensive application of knowledge and methodologies learned in course **GE2324**, utilizing Hong Kong's public transport system as a case study. We systematically apply key course concepts including data preprocessing, clustering analysis, network centrality measures, correlation analysis, and recommendation systems to investigate spatial patterns in Hong Kong's transport network.

## 📁 Repository Structure

```
├── Code/
│   ├── transport net/                   # transport network modeling
│   ├── association and frequency.ipynb  # frequent items analysis
│   └── clustering code.py               # Clustering and Correlation
├── Dataset/
│   └── Dataset Links.txt        # Dataset saved on Google Drive
├── HTML Presentation/           # used for presentation
├── README.md
├── Report.pdf                   # Final Project Report
└── Slides                       # Screenshot of the HTML presentation slides

```

### 🎯 Objectives

- Apply theoretical concepts from GE2324 to real-world transportation data
- Analyze spatial inequities in Hong Kong's public transport accessibility
- Investigate relationships between demographic characteristics and transport provision
- Demonstrate integration of multiple analytical methodologies

## 👥 Team Members (Group T04-I)

| Member | Responsibility | Contribution |
|--------|---------------|--------------|
| **Qimiao Gao** | Association and Frequent Items Analysis; HTML and LaTeX Integration | 20% |
| **Yongxi Qi** | Clustering Analysis; Correlation Analysis; Data Preprocessing | 20% |
| **Zerun Zhang** | Clustering Analysis; Correlation Analysis; Reference Management | 20% |
| **Zichong Deng** | Bus Network Modeling; Mapping; Similarity Analysis | 20% |
| **Yiqing Yang** | MTR Network Modeling | 20% |

## 📊 Data Sources

We compiled multimodal transport and demographic datasets from official Hong Kong government portals:

| Dataset | Source | Year/Period |
|---------|--------|-------------|
| Median Household Income | HK Gov Data Portal | 2020–2024 |
| Elderly Population (%) | HK Gov Data Portal | 2020–2024 |
| Traffic Flow Census | HK Gov Data Portal | 2023 |
| Population Density | HK Gov Data Portal | 2022 |
| Bus Stop Locations | HK Transport Routes | N/A |
| MTR Station and Routes | Google Places API | N/A |

## 🔬 Methodology

### Core Analytical Techniques

1. **Data Preprocessing and Normalization**
   - Min-Max scaling for feature standardization
   - Multi-source data integration and cleaning

2. **K-Means Clustering Analysis**
   - District grouping based on population density, elderly percentage, and median income
   - 3-cluster solution identifying distinct residential patterns

3. **Association Rule Mining**
   - Co-occurrence frequency analysis of high-traffic stations
   - Support-confidence framework implementation
   - Lift and interest measures calculation

4. **Network Centrality Analysis**
   - Degree, betweeness, and closeness centrality computation
   - Transport hub identification and connectivity analysis

5. **Correlation Analysis**
   - Pearson, Spearman, and Kendall correlation measures
   - Relationship assessment between transport provision and demographics

6. **Similarity Analysis**
   - Cosine similarity for district comparison
   - Recommendation system techniques application

### Key Formulas

**Population Density:**
```
Population Density_i = Total Population_i / Area_i
```

**K-Means Clustering Objective:**
```
argmin_C Σ(k=1 to K) Σ(x_i ∈ C_k) ||x_i - μ_k||²
```

**Co-occurrence Frequency:**
```
Freq_ij = c_ij / |B|
```

## 🔍 Key Findings

### District Clustering Results

- **Cluster 0**: High population density, high elderly percentages, lower incomes
- **Cluster 1**: Low population density, moderate elderly percentages, moderate incomes  
- **Cluster 2**: Medium population density, varying elderly percentages, highest incomes

### Correlation Insights

- Strong positive correlation between bus stop density and population density (r=0.889***)
- Marginal significance in bus coverage for aging areas (ρ=0.509*)
- Weak correlation between MTR stations and demographic indicators

### Network Analysis

- Uneven distribution of transport facilities across regions
- Higher centrality measures in western Hong Kong Island and western Kowloon
- Key transport hubs identified near Victoria Harbor tunnels


## 📚 Course Integration

This project serves as a comprehensive synthesis of **GE2324** course materials, demonstrating:

- Practical application of theoretical concepts
- Integration of multiple analytical methodologies
- Real-world dataset handling and preprocessing
- Statistical analysis and interpretation
- Network analysis and graph theory applications

## 📈 Visualizations

The project generates various visualizations including:

- **Co-occurrence Network Map**: Station relationships and high-frequency connections
- **Centrality Analysis**: Degree, betweenness, and closeness visualizations
- **Clustering Plots**: 3D scatter plots showing district groupings
- **Correlation Matrices**: Heatmaps showing variable relationships
- **Similarity Heatmaps**: District comparison visualizations

## ⚠️ Limitations

- Analysis relies on district-level aggregate data, potentially obscuring within-district variations
- Static accessibility measures don't account for real-time factors
- Limited to formal public transport modes (MTR and buses)
- No causal relationships established between transport accessibility and socioeconomic outcomes

## 🔮 Future Extensions

Potential areas for extending this analytical framework:

- Advanced clustering techniques (hierarchical clustering, DBSCAN)
- Sequential pattern mining for temporal associations
- Community detection algorithms for network analysis
- Multi-dimensional similarity measures and dimensionality reduction
- Regression analysis and hypothesis testing integration
  

## 🙏 Acknowledgments

- Hong Kong Government's data.gov.hk portal for providing access to datasets
- Course GE2324 instructors and teaching assistants
- Peer reviewers during presentation for valuable feedback

## 📄 License

This project is part of academic coursework for GE2324. Please cite appropriately if using any components of this analysis.

## 📞 Contact

qimiaogao2-c@my.cityu.edu.hk

For questions or collaboration opportunities, please contact the team members or open an issue in this repository.

---

*This project demonstrates the practical application of data analysis techniques learned in GE2324 to understand transportation equity in Hong Kong.* 


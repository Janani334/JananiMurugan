# AeroHome Manufacturing – Performance & Operations Dashboard

## 1. Project Overview

AeroHome Manufacturing Performance & Operations Dashboard is a Power BI project developed to analyze manufacturing performance, production efficiency, quality, downtime, machine performance, and procurement expenditure.

The project follows an end-to-end data analytics approach, starting from understanding the business problem and preparing the data to developing an interactive Power BI dashboard and generating actionable business insights.

---

## 2. Business Problem

AeroHome Manufacturing operates across multiple plants, products, machines, operators, suppliers, and production activities.

The organization needs better visibility into production performance and operational issues such as:

- Production targets not being achieved
- Production shortfalls across plants
- Differences in quality performance
- High downtime and its major reasons
- Machines with high downtime relative to production
- Overall procurement expenditure

The objective is to transform operational data into meaningful insights that can help management monitor performance and identify areas requiring further investigation.

---

## 3. Business Objectives

- Monitor planned versus actual production
- Measure production achievement and shortfall
- Compare performance across plants
- Analyze defect rates
- Identify major downtime reasons
- Analyze machine downtime against production output
- Monitor procurement expenditure
- Support data-driven operational decisions

---

## 4. Data Understanding & Profiling

The dataset contains multiple fact and dimension tables covering different manufacturing processes.

### Fact Tables

- `fact_production`
- `fact_quality`
- `fact_downtime`
- `fact_purchase_orders`

### Dimension Tables

- `dim_plants`
- `dim_products`
- `dim_machines`
- `dim_materials`
- `dim_suppliers`
- `dim_operators`
- `bridge_bill_of_materials`
- `DateTable`

Data profiling was performed to understand:

- Table structures
- Column names and data types
- Key business attributes
- Relationships between tables
- Production, quality, downtime and procurement fields
- Data required for KPI and dashboard development

---

## 5. Data Cleaning & Preparation

The data was prepared using Power Query and Power BI.

Key activities included:

- Reviewing and validating the dataset
- Checking data types
- Identifying and handling data quality issues
- Validating important fields
- Preparing data for analysis
- Creating relationships between tables
- Creating a dedicated Date table
- Creating Year, Month and Month Number fields
- Sorting months chronologically

The fact tables were kept separate according to their respective business processes to support accurate analysis.

---

## 6. Data Modeling

A fact-and-dimension data model was developed in Power BI.

The model connects operational data through dimensions such as:

- Plant
- Product
- Machine
- Material
- Supplier
- Operator
- Date

This model enables interactive filtering and analysis while maintaining appropriate fact-table granularity.

---

## 7. Data Analysis

The analysis focused on five major areas:

### Production Analysis
Planned production was compared with actual production to measure achievement and identify production shortfalls across plants and months.

### Quality Analysis
Defect rates were analyzed across plants to identify differences in quality performance.

### Downtime Analysis
Downtime was analyzed by reason to identify the major contributors to production downtime.

### Machine Analysis
Machine downtime was compared with production output to identify machines that may require further investigation.

### Procurement Analysis
Procurement expenditure was calculated to provide management with an overview of purchasing exposure.

---

## 8. Key Performance Indicators

| KPI | Value |
|---|---:|
| Production Achievement | 96.26% |
| Production Shortfall | 41K Units |
| Defect Rate | 1.69% |
| Total Downtime | 122K Minutes |
| Procurement Spend | ₹1,161.84M |

---

## 9. Dashboard

![AeroHome Manufacturing Performance & Operations Dashboard](AeroHome_Dashboard.png)

### Dashboard Visuals

**Planned vs Produced Units**  
Compares planned and actual production across months.

**Production Shortfall by Plant**  
Highlights plant-level contributions to production shortfall.

**Defect Rate by Plant**  
Compares defect-rate contribution across plants.

**Downtime by Reason**  
Identifies the major reasons contributing to production downtime.

**Machine Downtime vs Production**  
Compares machine downtime with production output to identify machines requiring further investigation.

### Filters

- Plant Name
- Product Name
- Month Name

---

## 10. Key Insights

- Overall production achievement is **96.26%**, with approximately **41K units of production shortfall**.
- The overall defect rate is **1.69%**, with differences in quality performance across plants.
- Total recorded downtime is approximately **122K minutes**.
- **Material Shortage (18.44%)** is the largest displayed downtime category, followed by Preventive Maintenance (17.92%) and Machine Breakdown (17.06%).
- Machine-level analysis highlights machines with relatively high downtime and lower production output for further investigation.
- Total procurement expenditure is approximately **₹1,161.84M**.

---

## 11. Recommendations

- Investigate recurring production shortfalls at plant level.
- Prioritize major downtime categories such as material shortage and machine breakdown.
- Review preventive maintenance and recurring machine downtime.
- Monitor plants with relatively higher defect rates.
- Investigate machines with high downtime and comparatively lower production.
- Monitor procurement expenditure and supplier-related risks.

---

## 12. Tools & Technologies

- **Microsoft Power BI**
- **Power Query**
- **DAX**
- **Microsoft Excel**

### Skills Demonstrated

Data Cleaning • Data Profiling • Data Transformation • Data Modeling • DAX • KPI Development • Data Visualization • Dashboard Development • Business Intelligence • Manufacturing Analytics • Operational Analysis • Insight Generation

---

## 13. Project Workflow

**Business Problem → Data Understanding → Data Profiling → Data Cleaning → Data Modeling → Data Analysis → DAX Measures → Dashboard Development → Insights → Recommendations**

---

## 14. Conclusion

The AeroHome Manufacturing Performance & Operations Dashboard demonstrates an end-to-end approach to solving a manufacturing analytics problem using Power BI.

The project transforms operational data into meaningful KPIs and interactive visualizations covering production, quality, downtime, machine performance, and procurement.

The dashboard enables management to identify production gaps, monitor quality and downtime, investigate machine performance, and prioritize areas for operational improvement.

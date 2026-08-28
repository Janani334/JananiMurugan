# Hospital Analytics Database – SQL Data Analysis

## 1. Project Overview

Hospital Analytics Database is a healthcare data analysis project developed using MySQL. It organizes hospital, department, doctor, patient, appointment, admission, treatment, billing, payment, laboratory, pharmacy, and employee data into a relational database.

The project demonstrates how SQL can be used to manage healthcare data, identify data-quality issues, perform analysis, and generate useful insights for operational decision-making.


## 2. Business Understanding

The healthcare organization manages multiple hospitals, departments, doctors, patients, and medical services. A structured database is required to maintain these records and understand operational performance.

The analysis focuses on hospital capacity, doctor availability, specialization, consultation fees, appointments, departments, and other healthcare activities.


## 3. Problem Statements

The project aims to understand hospital resources and operational activities through SQL analysis. The main focus is to compare hospitals, doctors, specializations, departments, consultation fees, and appointment activity.

The analysis also helps identify patterns that can support workforce planning, resource allocation, and operational decision-making.


## 4. Database Structure

The database consists of multiple related tables representing different areas of hospital operations. The main tables used for analysis are:

| Main Table | Purpose |
|---|---|
| Hospitals | Hospital details, location, type, and bed capacity |
| Departments | Department information and hospital relationships |
| Doctors | Doctor details, specialization, experience, and consultation fees |
| Patients | Patient demographic and contact information |
| Appointments | Patient appointment details |
| Admissions | Patient admission and discharge information |
| Treatments | Treatment details |
| Billing | Patient billing information |
| Payments | Payment information related to billing |
| Laboratory | Laboratory test information |
| Pharmacy | Medicine-related information |
| Employees | Hospital employee information |


## 5. Database Schema

The database follows a relational structure where healthcare entities are connected through primary and foreign keys. These relationships allow information from different tables to be combined for analysis while maintaining data consistency.

![Hospital Database Schema](Screenshots/database_schema.png)


## 6. Data Profiling

Data profiling was performed before analysis to understand the quality and consistency of the database. SQL queries were used to check missing values, duplicate records, inconsistent categorical values, extra spaces, invalid email formats, and missing relationship fields.

The profiling results helped identify records that required correction before performing the final analysis.

![Data Profiling](Screenshots/Data_Profiling.png)


## 7. Data Cleaning

The identified data-quality issues were reviewed and corrected using SQL queries. The cleaning process included trimming unwanted spaces, standardizing gender values, correcting email formats, and handling inconsistent or missing values.

The cleaned data was validated before analysis to ensure that the database remained consistent and the relationships between tables were maintained.

![Data Cleaning](Screenshots/Data_Cleaning.png)


## 8. Database Keys & Constraints

Primary keys were used to uniquely identify records in each table, while foreign keys were used to establish relationships between related tables. This relational structure connects entities such as hospitals, departments, doctors, patients, appointments, admissions, and billing.

Constraints such as PRIMARY KEY, FOREIGN KEY, NOT NULL, and UNIQUE were used to maintain data integrity and prevent invalid or duplicate records where required.


## 9. Data Analysis

SQL analysis was performed to understand hospital capacity, doctor distribution, specialization, consultation fees, appointments, and department coverage. Related tables were combined using joins to provide a broader view of healthcare operations.

The analysis included filtering, grouping, aggregation, comparisons, top-N analysis, and ranking to answer the defined business questions.


## 10. SQL Functions & Techniques

| Function / Technique | Purpose |
|---|---|
| COUNT() | Count hospitals, doctors, departments, and appointments |
| SUM() | Calculate total values such as bed capacity |
| AVG() | Calculate average consultation fees |
| MIN() / MAX() | Identify minimum and maximum values |
| WHERE | Filter records based on conditions |
| GROUP BY | Create grouped summaries |
| HAVING | Filter aggregated results |
| ORDER BY | Sort analysis results |
| LIMIT | Retrieve selected top records |
| INNER JOIN | Combine matching records from related tables |
| LEFT JOIN | Include records from the left table even without a match |
| RANK() | Rank records based on selected values |
| ROW_NUMBER() | Assign sequential numbers to records |
| LAG() / LEAD() | Compare values with previous or following records |


## 11. Hospital Analysis

Hospital analysis was performed to understand differences in bed capacity, doctor availability, department coverage, hospital type, and location. This provides a basis for comparing hospital resources and operational capacity.

![Hospital Analysis](Screenshots/Hospital_Analysis.png)


## 12. Doctor & Specialization Analysis

Doctor and specialization analysis was used to examine doctor availability, specialization, experience, consultation fees, hospital assignment, and appointment activity. The results help identify variations in medical workforce distribution and consultation pricing.

![Doctor Analysis](Screenshots/Doctor_Analysis.png)


## 13. Appointment & Department Analysis

Appointment analysis was used to understand doctor-level patient activity and identify differences in appointment volumes. Department analysis was performed to compare departmental availability across hospitals and understand healthcare service coverage.


## 14. Ranking Analysis

Advanced SQL window functions were used to rank doctors based on consultation fees and compare doctors within their respective specializations. This analysis demonstrates the use of SQL ranking techniques for detailed business-oriented comparisons.

![Ranking Analysis](Screenshots/Ranking_Analysis.png)


## 15. Key Performance Indicators

The analysis provides operational indicators that can be used to understand the size and resources of the healthcare organization.

| KPI | Purpose |
|---|---|
| Total Hospitals | Measures the hospital network size |
| Total Doctors | Measures available medical workforce |
| Total Departments | Measures departmental coverage |
| Total Bed Capacity | Measures hospital capacity |
| Average Consultation Fee | Measures average consultation pricing |
| Doctors by Specialization | Shows specialty-wise availability |
| Doctors by Hospital | Compares workforce distribution |
| Appointments by Doctor | Indicates doctor-level activity |


## 16. Key Insights

The analysis highlights differences in hospital capacity, doctor distribution, specialization availability, consultation fees, appointment activity, and department coverage.

The results provide a better understanding of resource distribution across hospitals and help identify areas that may require further operational attention.


## 17. Recommendations

The analysis can support better workforce allocation by identifying hospitals and specializations with different levels of doctor availability and appointment activity.

Hospital capacity and department analysis can assist with resource planning, while consultation-fee and appointment analysis can support workload and pricing comparisons.

Regular data profiling and cleaning should also be continued to maintain accurate, consistent, and reliable healthcare records.


## 18. Project Workflow

The project followed a structured workflow from database design and data insertion through profiling, cleaning, validation, SQL analysis, advanced queries, insights, and recommendations.

Database Design → Data Insertion → Data Profiling → Data Cleaning → Data Validation → SQL Analysis → Advanced SQL Queries → Insights → Recommendations


## 19. Project Outcome

The project transformed healthcare data into a structured relational database and used SQL analysis to generate meaningful operational information. It demonstrates practical experience in database design, data quality management, relational relationships, SQL querying, joins, aggregations, and analytical functions.


## 20. Conclusion

The Hospital Analytics Database project demonstrates the practical application of MySQL for healthcare data management and analysis.

By combining relational database concepts, data cleaning, SQL analysis, and business interpretation, the project converts healthcare data into useful information that can support operational planning and data-driven decision-making.
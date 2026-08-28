\# HealthPlus Care – Healthcare Database Analysis



\## 1. Project Overview



HealthPlus Care is a relational healthcare database developed using MySQL to manage and analyze healthcare operations. The database integrates information related to clinics, specialists, members, consultations, telemedicine, healthcare packages, prescriptions, laboratory tests, claims, billing, payments, and feedback.



The project focuses on database design, data profiling, data cleaning, and SQL-based analysis to generate meaningful healthcare and business insights.





\## 2. Business Understanding



The project aims to understand healthcare operations such as member management, specialist performance, consultations, billing, payments, laboratory services, healthcare packages, and feedback. SQL analysis was used to identify patterns and answer business-related questions that can support better operational decision-making.





\## 3. Problem Statements



The analysis focuses on understanding member and specialist activity, consultation trends, clinic performance, billing and payment patterns, laboratory costs, healthcare package usage, and feedback. It also examines relationships between different healthcare entities to support data-driven decision-making.





\## 4. Tools \& Technologies



MySQL was used to create and manage the relational healthcare database, while MySQL Workbench was used to write, execute, and validate SQL queries. SQL was used for database creation, data profiling, data cleaning, analysis, and generating business insights.





\## 5. Database Structure



The HealthPlus Care database consists of 17 relational tables.



| Table | Description |

|---|---|

| Clinics | Stores clinic information, location, and contact details |

| Specialists | Stores specialist details, specialization, experience, and consultation fees |

| Members | Stores member demographic and membership information |

| Corporates | Stores corporate organization information |

| Corporate\_Members | Connects corporate organizations with members |

| Consultations | Stores consultation details and status |

| Telemedicine\_Sessions | Stores telemedicine session information |

| Chronic\_Care\_Programs | Stores chronic care program details |

| Health\_Packages | Stores healthcare package details and pricing |

| Package\_Subscriptions | Stores member package subscriptions |

| Prescriptions | Stores prescription information |

| Lab\_Tests | Stores laboratory test information and costs |

| Claims | Stores insurance claim information |

| Staff | Stores hospital/clinic staff information |

| Billing | Stores billing information |

| Payments | Stores payment transaction information |

| Feedback | Stores member feedback and ratings |





\## 6. Database Relationships



The database uses primary keys and foreign keys to connect related healthcare entities and maintain data consistency.



| Relationship | Purpose |

|---|---|

| Specialists → Clinics | Connects specialists with their clinics |

| Consultations → Members | Connects consultations with members |

| Consultations → Specialists | Connects consultations with specialists |

| Consultations → Clinics | Connects consultations with clinics |

| Telemedicine\_Sessions → Consultations | Connects telemedicine sessions with consultations |

| Corporate\_Members → Corporates | Connects corporate members with organizations |

| Corporate\_Members → Members | Connects corporate members with members |

| Package\_Subscriptions → Members | Connects subscriptions with members |

| Package\_Subscriptions → Health\_Packages | Connects subscriptions with healthcare packages |

| Prescriptions → Consultations | Connects prescriptions with consultations |

| Lab\_Tests → Clinics | Connects laboratory tests with clinics |

| Claims → Members | Connects claims with members |

| Claims → Consultations | Connects claims with consultations |

| Staff → Clinics | Connects staff with clinics |

| Billing → Members | Connects billing records with members |

| Billing → Consultations | Connects billing with consultations |

| Payments → Billing | Connects payments with billing records |

| Feedback → Members | Connects feedback with members |

| Feedback → Consultations | Connects feedback with consultations |





\## 7. Database Schema



The database follows a relational structure where healthcare entities are connected through primary and foreign keys. These relationships allow information from multiple tables to be combined for analysis while maintaining data integrity.



!\[HealthPlus Care Database Schema](Screenshots/DB\_schema.png)





\## 8. Data Profiling



Data profiling was performed before analysis to understand the quality and consistency of the database. SQL queries were used to identify missing values, duplicate records, inconsistent categorical values, unwanted spaces, invalid email formats, and missing relationship fields.



The profiling results helped identify records that required correction before the final analysis.



!\[Data Profiling](Screenshots/Data\_profiling.png)







\## 9. Data Cleaning



The identified data-quality issues were reviewed and corrected using SQL queries. The cleaning process included trimming unwanted spaces, standardizing gender values, correcting email formats, and handling inconsistent or missing values.



The cleaned data was validated before analysis to ensure that the database remained consistent.



!\[Data Cleaning](Screenshots/Data\_cleaning.png)







\## 10. Keys \& Constraints



| Key / Constraint | Purpose |

|---|---|

| Primary Key | Uniquely identifies each record in a table |

| Foreign Key | Establishes relationships between related tables |

| NOT NULL | Ensures required fields contain values |

| UNIQUE | Prevents duplicate values in selected fields |

| Referential Integrity | Maintains valid relationships between related tables |





\## 11. SQL Functions \& Concepts Used



| Function / Concept | Purpose |

|---|---|

| SELECT | Retrieves required records |

| WHERE | Filters records based on conditions |

| COUNT() | Counts records |

| SUM() | Calculates total values |

| AVG() | Calculates average values |

| GROUP BY | Groups records for analysis |

| HAVING | Filters grouped results |

| ORDER BY | Sorts query results |

| JOIN | Combines data from related tables |

| CASE | Applies conditional logic |

| Subquery | Performs nested analysis |

| RANK() | Ranks records based on a specific value |

| LEAD() | Retrieves the next row value |

| LAG() | Retrieves the previous row value |

| PARTITION BY | Performs window calculations within groups |





\## 12. Data Analysis



SQL queries were used to analyze healthcare operations and answer business-related questions. The analysis covered member activity, specialist performance, consultations, clinics, billing, payments, laboratory services, healthcare packages, and feedback.



!\[Data Analysis 1](Screenshots/Data\_analysis\_1.png)

!\[Data Analysis 2](Screenshots/Data\_analysis\_2.png)





\## 13. Key Insights



The analysis provided insights into specialist consultation activity, consultation fees, member billing, clinic operations, laboratory costs, payment patterns, and healthcare service usage. Ranking and window functions also helped compare specialists and identify differences within specializations.



The results provide a clearer understanding of healthcare operations and areas that require attention.





\## 14. Recommendations



Healthcare management can use these insights to monitor specialist workload, review consultation pricing, identify high-value services, and improve resource allocation. Regular monitoring of billing, laboratory costs, payments, and member feedback can also help improve operational efficiency and service quality.





\## 15. Conclusion



The HealthPlus Care project demonstrates practical experience in designing a relational healthcare database and working with interconnected healthcare data. It covers database creation, profiling, cleaning, SQL analysis, and business-oriented insights using MySQL.



The project strengthened practical knowledge of relational databases, SQL querying, data quality management, and healthcare data analysis.


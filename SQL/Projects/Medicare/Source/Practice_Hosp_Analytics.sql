CREATE DATABASE hosp_ana_database;

USE hosp_ana_database;

CREATE TABLE Hospitals (
hospital_id VARCHAR(6),
hospital_name VARCHAR(100),
hospital_type VARCHAR(40),
city VARCHAR(50),
state VARCHAR(50),
region VARCHAR(20),
bed_capacity VARCHAR(10),
established_year VARCHAR(6),
contact_number VARCHAR(20) ,
email VARCHAR(100),
CONSTRAINT pk_Hospitals PRIMARY KEY
(hospital_id)
);

CREATE TABLE Departments (
department_id VARCHAR(6),
department_name VARCHAR(80),
hospital_id VARCHAR(6),
floor_number VARCHAR(10),
head_doctor_id VARCHAR(8),
CONSTRAINT pk_Deprtments PRIMARY KEY
(department_id)
);

CREATE TABLE Doctors (
doctor_id VARCHAR(8),
first_name VARCHAR(20),
last_name VARCHAR(20),
gender VARCHAR(8),
specialization VARCHAR(20),
department_id VARCHAR(6),
hospital_id VARCHAR(6),
qualification VARCHAR(20),
experience_year VARCHAR(6),
consultation_fee VARCHAR(15),
phone_number VARCHAR(20),
email VARCHAR(100),
joining_date VARCHAR(14),
CONSTRAINT pk_Doctors PRIMARY KEY
(doctor_id)
);

CREATE TABLE Patients (
patient_id VARCHAR(10),
first_name VARCHAR(20),
last_name VARCHAR(20),
gender VARCHAR(8),
Date_of_birth VARCHAR(14),
age VARCHAR(4),
city VARCHAR(50),
state VARCHAR(50),
phone_number VARCHAR(15),
email VARCHAR(100),
blood_group VARCHAR(6), 
registration_date VARCHAR(14),
CONSTRAINT pk_Patients PRIMARY KEY
(patient_id)
);

CREATE TABLE Rooms (
room_id VARCHAR(10),
hospital_id VARCHAR(6),
room_number VARCHAR(10),
room_type VARCHAR(15),
floor_number VARCHAR(10),
daily_charge VARCHAR(15),
room_status VARCHAR(15),
CONSTRAINT pk_Rooms PRIMARY KEY
(room_id)
);

CREATE TABLE Appointments (
appointment_id VARCHAR(15),
patient_id VARCHAR(15),
doctor_id VARCHAR(8),
hospital_id VARCHAR(6),
appointment_date VARCHAR(15),
appointment_time VARCHAR(15),
status VARCHAR(12),
reason_for_visit VARCHAR(50),
created_at VARCHAR(20),
CONSTRAINT pk_Appointments PRIMARY KEY
(appointment_id)
);

CREATE TABLE Admissions (
admission_id VARCHAR(10),
patient_id VARCHAR(10),
hospital_id VARCHAR(6),
department_id VARCHAR(6),
admitting_doctor_id VARCHAR(8),
room_id VARCHAR(10),
admission_date VARCHAR(15),
discharge_date VARCHAR(15),
admission_type VARCHAR(15),
admission_status VARCHAR(20),
CONSTRAINT pk_Admissions PRIMARY KEY
(admission_id)
);

CREATE TABLE Treatments (
treatment_id VARCHAR(15),
admission_id VARCHAR(15),
patient_id VARCHAR(10),
doctor_id VARCHAR(10),
treatment_name VARCHAR(50),
treatment_date VARCHAR(15),
treatment_cost VARCHAR(15),
treatment_status VARCHAR(15),
CONSTRAINT pk_Treatments PRIMARY KEY
(treatment_id)
);

CREATE TABLE Insurance (
insurance_id VARCHAR(10),
patient_id VARCHAR(10),
insurance_provider VARCHAR(100),
policy_number VARCHAR(15),
coverage_amount VARCHAR(15),
policy_start_date VARCHAR(15),
policy_end_date VARCHAR(15),
claim_status VARCHAR(15),
CONSTRAINT pk_Insurance PRIMARY KEY
(insurance_id)
);

CREATE TABLE Medicines (
medicine_id VARCHAR(10),
medicine_name VARCHAR(100),
category VARCHAR(50),
manufacturer VARCHAR(50),
unit_price VARCHAR(15),
stock_quantity VARCHAR(15),
CONSTRAINT pk_Medicines PRIMARY KEY
(medicine_id)
);

CREATE TABLE Pharmacy (
pharmacy_sale_id VARCHAR(15),
patient_id VARCHAR(15),
medicine_id VARCHAR(15),
hospital_id VARCHAR(6),
quantity VARCHAR(15),
sale_date VARCHAR(15),
total_price VARCHAR(15),
CONSTRAINT pk_Pharmacy PRIMARY KEY
(pharmacy_sale_id)
);

CREATE TABLE Laboratory (
lab_test_id VARCHAR(15),
patient_id VARCHAR(10),
doctor_id VARCHAR(10),
hospital_id VARCHAR(6),
test_name VARCHAR(50),
test_date VARCHAR(15),
test_result VARCHAR(15),
test_cost VARCHAR(15),
test_status VARCHAR(15),
CONSTRAINT pk_Laboratory PRIMARY KEY
(lab_test_id)
);

CREATE TABLE Employees (
employee_id VARCHAR(15),
first_name VARCHAR(20),
last_name VARCHAR(20),
gender VARCHAR(8),
hospital_id VARCHAR(6),
department_id VARCHAR(6),
designation VARCHAR(30),
employment_type VARCHAR(15),
salary VARCHAR(15),
joining_date VARCHAR(15),
phone_number VARCHAR(15),
email VARCHAR(100),
CONSTRAINT pk_Employees PRIMARY KEY
(employee_id)
);

CREATE TABLE Billing (
bill_id VARCHAR(10),
patient_id VARCHAR(10),
admission_id VARCHAR(10),
appointment_id VARCHAR(10),
bill_date VARCHAR(15),
room_charges VARCHAR(15),
doctor_charges VARCHAR(15),
medicine_charges VARCHAR(15),
lab_charges VARCHAR(15),
other_charges VARCHAR(15),
total_amount VARCHAR(15),
bill_status VARCHAR(15),
CONSTRAINT pk_Billing PRIMARY KEY
(bill_id)
);

CREATE TABLE Payments (
payment_id VARCHAR(10),
bill_id VARCHAR(10),
patient_id VARCHAR(10),
payment_date VARCHAR(15),
payment_amount VARCHAR(15),
payment_mode VARCHAR(20),
payment_status VARCHAR(15),
CONSTRAINT pk_Payments PRIMARY KEY
(payment_id)
);
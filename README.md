# ☁️ Azure ETL Pipeline: CSV to SQL Server

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline that processes CSV files stored in Azure Blob Storage, cleans and transforms the data using Python, and loads it into an Azure SQL Database.

---

## 📌 Use Case

This pipeline is ideal for automating the ingestion of external data (e.g. earnings reports, analytics, sales) into a centralized database for further analysis and reporting.

---

## ⚙️ Architecture Overview

1. **Azure Blob Storage** stores raw CSV files.
2. **Azure Data Factory** triggers the pipeline.
3. **Azure Batch / Python script** performs the transformation.
4. **Azure SQL Database** receives the cleaned data.

> 🧠 The pipeline is fully modular and can be adapted to other data sources or destinations.

---

## 📁 Folder Structure


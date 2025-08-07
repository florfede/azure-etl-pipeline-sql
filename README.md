# ☁️ Azure ETL Pipeline: CSV to SQL Server

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline that processes CSV files stored in Azure Blob Storage, cleans and transforms the data using Python, and loads it into an Azure SQL Database.

---

## 📌 Use Case

This pipeline is ideal for automating the ingestion of external data (e.g. earnings reports, analytics, sales) into a centralized database for further analysis and reporting.

---

## ⚙️ Architecture Overview

1. **Azure Blob Storage** stores raw CSV files  
2. **Azure Data Factory** triggers the pipeline  
3. **Azure Batch / Python script** performs the transformation  
4. **Azure SQL Database** receives the cleaned data

> 🧠 The pipeline is fully modular and can be adapted to other data sources or destinations.

---

## 📁 Folder Structure

```
azure-etl-pipeline-sql/
│
├── data/                     # Sample input files  
├── scripts/                  # Python scripts (ETL logic)  
│   ├── transform.py  
│   └── load_to_sql.py  
├── pipeline_config/          # ADF pipeline JSON (optional)  
├── logs/                     # Sample logs or errors  
├── requirements.txt          # Python dependencies  
└── README.md                 # This file
```

---

## 🔄 ETL Flow Details

### 🔹 Extract
- Triggered when a new file lands in Azure Blob Storage  
- File is downloaded for local or batch processing

### 🔹 Transform
- CSV cleaned (headers, encoding, delimiters)  
- Data types normalized  
- Optional: malformed rows detected and logged

### 🔹 Load
- Data is inserted into SQL Server  
- Uses `pyodbc` for connection  
- Includes optional table creation and basic error handling

---

## 🧪 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/tu-usuario/azure-etl-pipeline-sql.git
cd azure-etl-pipeline-sql
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run ETL pipeline manually

```bash
# Step 1: Transform the data
python scripts/transform.py data/sample_data_10k.csv

# Step 2: Load to SQL Server
python scripts/load_to_sql.py data/sample_data_10k.csv royalties_table "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=mydb;UID=sa;PWD=your_password"
```

> ✅ You can also export the connection string to an environment variable and adapt the script to read from it using `os.environ`.

---

## 🧰 Tech Stack

- Azure Blob Storage  
- Azure Data Factory  
- Azure SQL Database  
- Python: `pandas`, `pyodbc`, `azure-storage-blob`  
- (Optional) Azure Batch / Azure Functions

---

## 📚 Optional Enhancements

- Add schema validation with `pandera` or `pydantic`  
- Use Azure Key Vault to store credentials securely  
- CI/CD integration with GitHub Actions

---

## 👩‍💻 Author

**Florencia Federico**  
Data & Machine Learning Engineer  
[LinkedIn](https://www.linkedin.com/in/florenciafederico88/)

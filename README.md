# 📈 Financial Data Integration Pipeline (ETL)

## 📌 Project Overview
An automated ETL (Extract, Transform, Load) pipeline built with Python to monitor real-time foreign exchange rates (USD to BRL). The project extracts live JSON data from a REST API, structures and cleans the data in memory, and persists it into a relational database for historical tracking and financial analysis.

## 🛠️ Technologies & Stack
* **Language:** Python 3
* **Data Extraction:** `requests` (REST API consumption)
* **Data Transformation:** `pandas` (Data manipulation and typing)
* **Data Loading (Database):** `SQLite` & `SQLAlchemy` (Relational modeling and ORM)

## ⚙️ Pipeline Architecture (ETL)

1. **Extract (E):** * Connects to the [AwesomeAPI](https://docs.awesomeapi.com.br/) endpoint.
   * Captures the live JSON payload containing the USD-BRL quote.

2. **Transform (T):**
   * Parses the nested JSON response into a Pandas DataFrame.
   * Selects relevant financial columns.
   * Standardizes column names and converts string values to float data types for mathematical operations.

3. **Load (L):**
   * Establishes a connection to a local SQLite database (`cambio.db`) using SQLAlchemy.
   * Performs an incremental load (`append`), ensuring historical data is preserved without duplication.

## 📊 Database Schema
The pipeline creates and populates the `cotacoes_dolar` table with the following structure:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `moeda` | TEXT | The currency pair (e.g., Dólar Americano/Real Brasileiro) |
| `valor_compra` | REAL | The current bid price (float) |
| `valor_venda` | REAL | The current ask price (float) |
| `data_hora` | TEXT | Timestamp of the quotation |

## 🚀 How to Run the Project

1. **Clone this repository:**
    ```bash
    git clone https://github.com/jobson-menezes/financial_data_pipeline.git

2. **Navigate to the project directory:**
    ```bash
    cd financial_data_pipeline

3. **Create a virtual environment:**
    ```bash
    python -m venv venv

4. **Activate the virtual environment:**
    ```bash
  # On Windows (PowerShell)
    venv\Scripts\activate

  # On Linux/Mac
    source venv/bin/activate

5. **Install the required dependencies:**
    ```bash
    pip install requests pandas sqlalchemy

6. **Run the ETL pipeline:**
    ```bash
    python pipeline.py

Upon successful execution, a cambio.db SQLite file will be generated in the root directory.
  






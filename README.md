# 🗄️ MySQL Data Connection Dashboard

An interactive **Streamlit web application** that connects to a MySQL database and provides an easy interface for viewing, analyzing, and querying data.

This project converts a MySQL data-connection workflow into a user-friendly web dashboard using **Python, Streamlit, Pandas, and MySQL**.

---

## 🚀 Project Overview

The **MySQL Data Connection Dashboard** allows users to connect their MySQL database through a Streamlit interface and perform basic data exploration without directly working with the database every time.

The application can:

* 🔌 Connect to a MySQL database
* 📊 Display important dataset information
* 📋 View database table records
* 🧮 Calculate `TotalSales`
* 🔎 Execute read-only SQL queries
* 🔄 Detect changes in database data
* 📥 Download data as CSV
* 🔐 Keep database credentials outside the GitHub repository

---

## ✨ Features

### 🔌 MySQL Database Connection

The application provides a simple interface for connecting to a MySQL database using:

* Host
* Port
* Username
* Password
* Database name
* Table name

A connection timeout is also used so that the application does not remain stuck indefinitely if the database cannot be reached.

---

### 📊 Dataset Overview

After connecting to MySQL, the dashboard displays:

* Total number of rows
* Number of columns
* Missing values
* Total sales
* Dataset preview
* Column data types
* Non-null values
* Missing values by column

---

### 🧮 Total Sales Calculation

The application calculates total sales using:

```text
TotalSales = UnitsSold × SalesAmount
```

This derived column can then be used for further analysis.

---

### 📋 Data Explorer

The **Data** section allows users to:

* View the complete table
* Scroll through records
* Inspect columns
* Download the displayed dataset

The dataset can be downloaded as a CSV file.

---

### 🔎 SQL Query

The dashboard provides an SQL query interface for running **read-only SELECT queries**.

Example:

```sql
SELECT * FROM data LIMIT 10;
```

Another example:

```sql
SELECT SaleID, UnitsSold, SalesAmount
FROM data
LIMIT 10;
```

For safety, the dashboard only allows queries beginning with `SELECT`.

---

### 🔄 Database Change Detection

The project includes a simple change-detection mechanism.

A **SHA-256 hash** is generated from the loaded dataset.

When the user clicks **Check for Changes**, the application loads the latest data and compares its hash with the previous snapshot.

If the hashes are different:

```text
⚠️ Database data has changed.
```

If they are the same:

```text
✅ No change detected.
```

---

## 🛠️ Technologies Used

| Technology         | Purpose                      |
| ------------------ | ---------------------------- |
| 🐍 Python          | Application development      |
| 🎈 Streamlit       | Web application              |
| 🐼 Pandas          | Data processing and analysis |
| 🗄️ MySQL          | Database                     |
| 🔌 MySQL Connector | Database connectivity        |
| 🔐 SHA-256         | Data change detection        |

---

## 📁 Project Structure

```text
mysql-streamlit-data-dashboard/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── .streamlit/
    └── secrets.toml.example
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mysql-streamlit-data-dashboard.git
```

Move into the project folder:

```bash
cd mysql-streamlit-data-dashboard
```

---

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install streamlit pandas mysql-connector-python
```

---

## 🗄️ MySQL Configuration

Make sure your MySQL server is running.

The application can use a database such as:

```text
Database: eda_sql
Table: data
Host: localhost
Port: 3306
```

You should use **your own MySQL username and password**.

### Test MySQL Connection

Before running the Streamlit application, you can test your MySQL server using:

```sql
SELECT 1;
```

Then test the table:

```sql
USE eda_sql;
```

```sql
SELECT * FROM data LIMIT 10;
```

---

## 🔐 Database Credentials

**Never upload your MySQL password to GitHub.**

The project is designed to keep credentials outside the public repository.

Create:

```text
.streamlit/secrets.toml
```

using the example file:

```text
.streamlit/secrets.toml.example
```

Example:

```toml
[mysql]
host = "localhost"
port = 3306
user = "your_username"
password = "your_password"
database = "eda_sql"
table = "data"
```

The actual `secrets.toml` file should remain private.

---

## ▶️ Run the Application

Start Streamlit using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually it will be available at:

```text
http://localhost:8501
```

---

## 📊 Application Workflow

```text
MySQL Database
       ↓
Database Connection
       ↓
Load Table
       ↓
Pandas Data Processing
       ↓
Calculate TotalSales
       ↓
Streamlit Dashboard
       ↓
 ┌───────────────┬───────────────┬───────────────┐
 │   Overview    │     Data      │   SQL Query   │
 └───────────────┴───────────────┴───────────────┘
                       ↓
              Change Detection
```

---

## 🧪 Troubleshooting

### Error: `No module named 'mysql'`

Install the MySQL connector:

```bash
pip install mysql-connector-python
```

Then restart Streamlit:

```bash
streamlit run app.py
```

---

### Error: `Error Code: 2013`

```text
Lost connection to MySQL server during query
```

First check that the MySQL server is running.

Then test:

```sql
SELECT 1;
```

If that works, test:

```sql
SELECT * FROM data LIMIT 10;
```

Also verify:

* MySQL server is running
* Host is correct
* Port is correct
* Username is correct
* Password is correct
* Database exists
* Table exists

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* 📈 Interactive sales charts
* 📅 Date-based filtering
* 🌍 Region-wise analysis
* 🛍️ Product-category analysis
* 📊 Sales KPI dashboard
* 🔐 User authentication
* 📤 Database update interface
* ☁️ Streamlit Cloud deployment
* 🗄️ Cloud MySQL integration
* 📱 Improved responsive UI

---

## 🎯 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python database connectivity
* MySQL
* SQL queries
* Pandas data analysis
* Streamlit application development
* Data visualization/dashboard concepts
* Data validation
* Database change detection
* Secure handling of credentials
* Git and GitHub project management

---

## 👩‍💻 Author

**Chetna Rajak**

Engineering Student | AI/ML & Data Analytics

Interested in:

* Data Analytics
* Machine Learning
* Artificial Intelligence
* Python
* SQL
* Data Visualization

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📌 Project Summary

> **MySQL Data Connection Dashboard** is a Streamlit-based web application that connects to MySQL, processes database data using Pandas, calculates sales metrics, provides a read-only SQL interface, and detects changes in the underlying dataset.

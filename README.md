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

### 📌 Project Summary

> **MySQL Data Connection Dashboard** is a Streamlit-based web application that connects to MySQL, processes database data using Pandas, calculates sales metrics, provides a read-only SQL interface, and detects changes in the underlying dataset.

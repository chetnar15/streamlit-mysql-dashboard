
import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import hashlib

st.set_page_config(
    page_title="MySQL Data Connection Dashboard",
    page_icon="🗄️",
    layout="wide"
)

st.title("🗄️ MySQL Data Connection Dashboard")
st.caption("Streamlit interface based on the DATA_CONNECTION notebook")

# ---------- Helpers ----------
@st.cache_data(ttl=30)
def fetch_data(host, port, user, password, database, table):
    conn = mysql.connector.connect(
        host=host, port=port, user=user,
        password=password, database=database
    )
    try:
        return pd.read_sql(f"SELECT * FROM `{table}`", conn)
    finally:
        conn.close()

def make_hash(df):
    temp = df.sort_values("SaleID").reset_index(drop=True) if "SaleID" in df.columns else df.reset_index(drop=True)
    return str(pd.util.hash_pandas_object(temp, index=True).sum())

def get_connection(host, port, user, password, database):
    return mysql.connector.connect(
        host=host, port=port, user=user,
        password=password, database=database
    )

# ---------- Sidebar ----------
with st.sidebar:
    st.header("🔐 Database Connection")
    host = st.text_input("Host", "localhost")
    port = st.number_input("Port", min_value=1, max_value=65535, value=3306)
    user = st.text_input("Username", "root")
    password = st.text_input("Password", type="password")
    database = st.text_input("Database", "joins_july")
    table = st.text_input("Table", "data")

    connect = st.button("🔌 Connect to MySQL", use_container_width=True)

if connect:
    try:
        conn = get_connection(host, port, user, password, database)
        conn.close()
        st.session_state["connected"] = True
        st.session_state["db_config"] = (host, port, user, password, database, table)
        st.success("MySQL Connected Successfully!")
        st.rerun()
    except Error as e:
        st.session_state["connected"] = False
        st.error(f"Connection failed: {e}")

connected = st.session_state.get("connected", False)

if not connected:
    st.info("👈 Enter your MySQL details in the sidebar and click **Connect to MySQL**.")
    st.markdown("""
    ### What this webpage does
    - Connects Streamlit to your MySQL database
    - Fetches the `data` table
    - Shows rows, columns and dataset preview
    - Calculates `TotalSales = UnitsSold × SalesAmount`
    - Checks whether the database has changed using a data snapshot/hash
    - Lets you run a safe SELECT query
    """)
    st.stop()

host, port, user, password, database, table = st.session_state["db_config"]

try:
    df = fetch_data(host, port, user, password, database, table)
except Exception as e:
    st.error(f"Could not fetch data: {e}")
    st.stop()

# ---------- Derived column ----------
if {"UnitsSold", "SalesAmount"}.issubset(df.columns):
    df["TotalSales"] = pd.to_numeric(df["UnitsSold"], errors="coerce") * pd.to_numeric(df["SalesAmount"], errors="coerce")

# ---------- Header metrics ----------
m1, m2, m3, m4 = st.columns(4)
m1.metric("Rows", len(df))
m2.metric("Columns", len(df.columns))
m3.metric("Missing Values", int(df.isna().sum().sum()))
if "TotalSales" in df.columns:
    m4.metric("Total Sales", f"{df['TotalSales'].sum():,.2f}")
else:
    m4.metric("Database", database)

tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📋 Data", "🔎 SQL Query", "🔄 Change Detection"])

with tab1:
    st.subheader("Dataset Overview")
    st.dataframe(df.head(10), use_container_width=True)

    if "TotalSales" in df.columns:
        st.subheader("Sales Summary")
        summary = df["TotalSales"].describe().to_frame("TotalSales")
        st.dataframe(summary, use_container_width=True)

with tab2:
    st.subheader("Complete Dataset")
    st.dataframe(df, use_container_width=True, height=500)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download Data as CSV",
        csv,
        "mysql_data.csv",
        "text/csv"
    )

with tab3:
    st.subheader("Run SELECT Query")
    default_query = f"SELECT * FROM `{table}` LIMIT 100"
    query = st.text_area("SQL Query", default_query, height=130)

    if st.button("▶ Run Query"):
        if not query.strip().lower().startswith("select"):
            st.warning("For this dashboard, only SELECT queries are allowed.")
        else:
            try:
                conn = get_connection(host, port, user, password, database)
                result = pd.read_sql(query, conn)
                conn.close()
                st.success(f"Query executed successfully — {len(result)} rows returned.")
                st.dataframe(result, use_container_width=True)
            except Exception as e:
                st.error(f"Query error: {e}")

with tab4:
    st.subheader("Database Change Detection")
    st.write("The notebook uses a hash-based snapshot to compare the current table with a previous snapshot.")

    current_hash = make_hash(df)
    st.code(current_hash, language="text")

    if "snapshot_hash" not in st.session_state:
        st.session_state["snapshot_hash"] = current_hash
        st.success("Initial snapshot created for this Streamlit session.")

    if st.button("🔍 Check for Changes"):
        latest = fetch_data(host, port, user, password, database, table)
        latest_hash = make_hash(latest)

        if latest_hash != st.session_state["snapshot_hash"]:
            st.error("⚠️ DATABASE CHANGED!")
            st.session_state["snapshot_hash"] = latest_hash
        else:
            st.success("✅ No change detected.")

st.divider()
st.caption("Based on your 1_DATA_CONNECTION.ipynb workflow • Streamlit + MySQL + Pandas")

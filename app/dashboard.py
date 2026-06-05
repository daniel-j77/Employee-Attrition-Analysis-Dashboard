import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Employee Attrition Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("../data/employees_clean.csv")

# -----------------------------
# COLORS
# -----------------------------
DARK_GREEN = "#1f5f53"
MEDIUM_GREEN = "#4f9f8f"
LIGHT_GREEN = "#a8d5cd"

# -----------------------------
# KPIs
# -----------------------------
total_employees = len(df)

avg_salary = df["Salary"].mean()

attrition_rate = (
    len(df[df["Attrition"] == "Yes"])
    / total_employees
) * 100

promoted_employees = len(
    df[df["Promotion"] == "Yes"]
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📊 Employee Attrition Analysis Dashboard")

# -----------------------------
# KPI ROW
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Employees",
        total_employees
    )

with col2:
    st.metric(
        "Average Salary",
        f"₹{avg_salary:,.0f}"
    )

with col3:
    st.metric(
        "Attrition Rate",
        f"{attrition_rate:.1f}%"
    )

with col4:
    st.metric(
        "Promoted Employees",
        promoted_employees
    )

st.markdown("---")

# -----------------------------
# ROW 2
# -----------------------------
col5, col6 = st.columns(2)

with col5:

    st.subheader("Employees by Department")

    dept_count = (
        df["Department"]
        .value_counts()
        .reset_index()
    )

    dept_count.columns = [
        "Department",
        "Employees"
    ]

    fig1 = px.bar(
        dept_count,
        x="Employees",
        y="Department",
        orientation="h",
        text="Employees",
        color="Employees",
        color_continuous_scale=[
            DARK_GREEN,
            MEDIUM_GREEN,
            LIGHT_GREEN
        ]
    )

    fig1.update_traces(
        textposition="outside"
    )

    fig1.update_layout(
        xaxis_title="Number of Employees",
        yaxis_title="Department",
        coloraxis_colorbar_title="Employees"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col6:

    st.subheader("Average Salary by Department")

    salary_df = (
        df.groupby("Department")["Salary"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        salary_df,
        x="Department",
        y="Salary",
        text="Salary",
        color="Salary",
        color_continuous_scale=[
            DARK_GREEN,
            MEDIUM_GREEN,
            LIGHT_GREEN
        ]
    )

    fig2.update_traces(
        texttemplate="₹%{text:,.0f}",
        textposition="outside"
    )

    fig2.update_layout(
        xaxis_title="Department",
        yaxis_title="Average Salary (₹)",
        coloraxis_colorbar_title="Salary"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

# -----------------------------
# ROW 3
# -----------------------------
col7, col8 = st.columns(2)

with col7:

    st.subheader(
        "Employee Attrition Distribution"
    )

    attrition_df = (
        df["Attrition"]
        .value_counts()
        .reset_index()
    )

    attrition_df.columns = [
        "Attrition",
        "Count"
    ]

    attrition_df["Status"] = (
        attrition_df["Attrition"]
        .replace({
            "Yes": "Left Company",
            "No": "Stayed"
        })
    )

    fig3 = px.pie(
        attrition_df,
        names="Status",
        values="Count",
        hole=0.55,
        color="Status",
        color_discrete_map={
            "Stayed": DARK_GREEN,
            "Left Company": LIGHT_GREEN
        }
    )

    fig3.update_traces(
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col8:

    st.subheader(
        "Promotion Distribution"
    )

    promotion_df = (
        df["Promotion"]
        .value_counts()
        .reset_index()
    )

    promotion_df.columns = [
        "Promotion",
        "Count"
    ]

    promotion_df["Promotion Status"] = (
        promotion_df["Promotion"]
        .replace({
            "Yes": "Promoted",
            "No": "Not Promoted"
        })
    )

    fig4 = px.pie(
        promotion_df,
        names="Promotion Status",
        values="Count",
        color="Promotion Status",
        color_discrete_map={
            "Promoted": LIGHT_GREEN,
            "Not Promoted": DARK_GREEN
        }
    )

    fig4.update_traces(
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.markdown("---")

# -----------------------------
# DATASET
# -----------------------------
st.subheader("Employee Dataset")

st.dataframe(
    df,
    use_container_width=True
)
import streamlit as st
import pandas as pd
import plotly.express as px

def dashboard():

    st.title("📊 ShopSense Dashboard")

    try:
        # ---------------- LOAD DATA ----------------
        df = pd.read_csv("data/processed/cleaned_data.csv")

        st.write("✅ Data loaded:", df.shape)

        # ---------------- FIX DATE ----------------
        df["order_purchase_timestamp"] = pd.to_datetime(
            df["order_purchase_timestamp"],
            errors="coerce"
        )

        # ---------------- KPI ----------------
        st.subheader("📌 KPIs")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Revenue", f"{df['payment_value'].sum():,.0f}")
        col2.metric("Orders", df["order_id"].nunique())
        col3.metric("Customers", df["customer_unique_id"].nunique())
        col4.metric("Avg Order", f"{df['payment_value'].mean():.2f}")

        st.divider()

        # ---------------- MONTHLY REVENUE ----------------
        st.subheader("📈 Monthly Revenue")

        monthly = df.groupby(
            df["order_purchase_timestamp"].dt.to_period("M")
        )["payment_value"].sum().reset_index()

        monthly["order_purchase_timestamp"] = monthly["order_purchase_timestamp"].astype(str)

        fig1 = px.line(
            monthly,
            x="order_purchase_timestamp",
            y="payment_value"
        )

        st.plotly_chart(fig1, use_container_width=True)

        st.divider()

        # ---------------- TOP STATES ----------------
        st.subheader("📍 Top States")

        top_states = df["customer_state"].value_counts().head(10).reset_index()
        top_states.columns = ["state", "count"]

        fig2 = px.bar(top_states, x="state", y="count")

        st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        # ---------------- PAYMENT ----------------
        st.subheader("💳 Payment Methods")

        pay = df["payment_type"].value_counts().reset_index()
        pay.columns = ["type", "count"]

        fig3 = px.pie(pay, names="type", values="count")

        st.plotly_chart(fig3, use_container_width=True)

        st.divider()

        st.subheader("📊 Raw Insights")
        st.dataframe(df.head())

    except Exception as e:
        st.error("❌ Dashboard crashed")
        st.exception(e)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
st.header("Income Expense Statistics")
df=pd.read_csv(r"C:\Users\91995\Downloads\Inc_Exp_Data.csv")
st.write(df)

st.write(df.head())

st.subheader("Shape")
st.write(df.shape)

st.subheader("Columns")
st.write(df.columns)

st.subheader("Number of Columns")
st.write(len(df.columns))

st.subheader("Description")
st.write(df.describe())

st.subheader("Null values")
st.write(df.isna())

st.subheader("Mean")
st.write(df['Mthly_HH_Expense'].mean())

st.subheader("Median")
st.write(df['Mthly_HH_Expense'].median())

st.subheader("Mode")
st.write(df['Mthly_HH_Expense'].mode())

st.subheader("Highest Qualification Count")

fig1, ax1 = plt.subplots()
df['Highest_Qualified_Member'].value_counts().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# ----- 2️⃣ Income vs Expense Plot -----
st.subheader("Monthly Income vs Monthly Expense")

fig2, ax2 = plt.subplots()
df.plot(x="Mthly_HH_Income", y="Mthly_HH_Expense", ax=ax2)
st.pyplot(fig2)

IQR=df["Mthly_HH_Expense"].quantile(0.75)-df["Mthly_HH_Expense"].quantile(0.25)
st.write(IQR)

st.subheader("Variance")
st.write(df['Mthly_HH_Expense'].var())

st.subheader("Standard Deviation")
st.write(df['Mthly_HH_Expense'].std())

st.subheader("Coefficient of variation")
coef=df['Mthly_HH_Expense'].std()/df['Mthly_HH_Expense'].mean()
st.write(coef)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df=pd.read_csv(r"C:\Users\91995\Downloads\30_sport_analysis_project\FIFA.csv")
st.write(df)

st.subheader("Exploratory Data Analysis")
st.subheader("Preview the dataset")
st.write(df.head())

st.subheader(" View summary of dataset")
st.write(df.info())
st.write(df['Body Type'].value_counts())

st.subheader("Explore Age variable")
st.write("Visualize distribution of Age variable with Seaborn distplot() function")
f,ax=plt.subplots(figsize=(8,6))
x=df['Age']
ax=sns.distplot(x,bins=10)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
x=df['Age']
ax=sns.distplot(x,bins=10,vertical=True)
st.pyplot(f)

st.subheader("Seaborn KDE Plot")
f,ax=plt.subplots(figsize=(8,6))
x=df['Age']
ax=sns.kdeplot(x)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.kdeplot(x,shade=True,color='r')
st.pyplot(f)

st.subheader("Histograms")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.distplot(x,kde=False,rug=True,bins=10)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.distplot(x,hist=False,rug=True,bins=10)
st.pyplot(f)

st.subheader("Explore preferred foot variable")
st.write("Check number of unique values in preferred foot variable")
st.write(df['Preferred Foot'].nunique())
st.write("Check frequency distribution of values in preferred foot variable")
st.write(df['Preferred Foot'].value_counts())

st.subheader("Visualize distribution of values with seaborn countplot() function")
f,ax=plt.subplots(figsize=(8,6))
sns.countplot(x="Preferred Foot",data=df,color="c")
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.countplot(x="Preferred Foot",hue="Real Face",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.countplot(y="Preferred Foot",data=df,color="c")
st.pyplot(f)

st.subheader("Explore International Reputation variable")
st.write("Check the number of unique values in International Reputation variable")
st.write(df['International Reputation'].nunique())
st.write("Check the destribution of values in International Reputation variable")
st.write(df['International Reputation'].value_counts())
f,ax=plt.subplots(figsize=(8,6))
sns.stripplot(x="International Reputation",y="Potential",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.stripplot(x="International Reputation",y="Potential",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.stripplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.stripplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(f)

st.write("eaborn boxplot() function")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x=df["Potential"])
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x="International Reputation",y="Potential",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(f)

st.subheader("ViolinPlot")
f,ax=plt.subplots(figsize=(8,6))
sns.violinplot(x=df["Potential"])
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.violinplot(x="International Reputation",y="Potential",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.violinplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.violinplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df,split=True)
st.pyplot(f)

st.subheader("PointPlot")
f,ax=plt.subplots(figsize=(8,6))
sns.pointplot(x="International Reputation",y="Potential",data=df)
st.pyplot(f)

f, ax = plt.subplots(figsize=(8, 6))
sns.pointplot(x="International Reputation", y="Potential", hue="Preferred Foot", data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.pointplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df,markers=["o","x"],linestyle=['-',"--"])
st.pyplot(f)

st.subheader("BarPlot")
f,ax=plt.subplots(figsize=(8,6))
sns.barplot(x="International Reputation",y="Potential",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.barplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(f)

st.subheader("RelPlot")
g=sns.relplot(x="Overall",y="Potential",data=df)
st.pyplot(g)

f,ax=plt.subplots(figsize=(8,6))
sns.scatterplot(x="Height",y="Weight",data=df)
st.pyplot(f)


st.subheader("LinePlot")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.lineplot(x="Stamina",y="Strength",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.regplot(x="Overall",y="Potential",data=df)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.regplot(x="Overall",y="Potential",data=df,color="g",marker="+")
st.pyplot(f)

st.subheader("LmPlot")
g=sns.lmplot(x="Overall",y="Potential",data=df)
st.pyplot(g)
g=sns.lmplot(x="Overall",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(g)
g=sns.lmplot(x="Overall",y="Potential",hue="Preferred Foot",data=df)
st.pyplot(g)
g=sns.lmplot(x="Overall",y="Potential",data=df)
st.pyplot(g)

st.subheader("FacetGrid")
g=sns.FacetGrid(df,col="Preferred Foot")
st.pyplot(g)
g=sns.FacetGrid(df,col="Preferred Foot")
g=g.map(plt.hist,"Potential")
st.pyplot(g)
g = sns.FacetGrid(df, col="Preferred Foot")
g = g.map(plt.hist, "Potential", bins=10, color="r")
st.pyplot(g)
g=sns.FacetGrid(df,col="Preferred Foot",height=5,aspect=1)
g=g.map(plt.hist,"Potential")
st.pyplot(g)

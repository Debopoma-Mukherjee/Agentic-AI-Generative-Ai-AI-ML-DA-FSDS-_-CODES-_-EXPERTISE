import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

iris=pd.read_csv(r"C:\Users\91995\NIT\31_iris_analysis_project\Iris.csv")
st.header("IRIS DATASET ANALYSIS")
st.write(iris)

st.subheader("Displaying data")
st.write(iris.head())
iris.drop('Id',axis=1,inplace=True)
st.write("iris.head()")

st.subheader("Checking if any missing values are there or not")
st.write(iris.info())

st.write("This data set has three varities of iris plant")
st.write(iris['Species'].value_counts())

st.subheader("Bar plot")
fig,ax=plt.subplots()
ax=sns.countplot(x='Species',data=iris)
st.pyplot(fig)
st.write("we can see there are 50 samples of each of the Iris Species.")


jp=sns.jointplot(x='SepalLengthCm',y="SepalWidthCm",data=iris)
st.pyplot(jp)


ax=sns.jointplot(x='SepalLengthCm',y="SepalWidthCm",data=iris,kind="reg")
st.pyplot(ax)


ax=sns.jointplot(x="SepalLengthCm",y="SepalWidthCm",kind='hex',data=iris)
st.pyplot(ax)

g=sns.FacetGrid(iris,hue='Species')
g.map(plt.scatter,'SepalLengthCm','SepalWidthCm')
st.pyplot(g)

st.subheader("Boxplot")
fig,ax=plt.subplots()
ax=sns.boxplot(x='Species',y='PetalLengthCm',data=iris)
st.pyplot(fig)


st.subheader("Strip plot")
ax=sns.stripplot(x="Species",y="SepalLengthCm",data=iris,hue="Species")
st.pyplot(fig)

ax=sns.boxplot(x="Species",y="SepalLengthCm",data=iris,hue="Species")
st.pyplot(fig)
ax=sns.stripplot(x="Species",y="SepalLengthCm",data=iris,hue="Species")
st.pyplot(fig)

ax=sns.boxplot(x="Species",y="PetalLengthCm",data=iris,hue="Species")
st.pyplot(fig)
ax=sns.stripplot(x="Species",y="PetalLengthCm",data=iris,hue="Species")
st.pyplot(fig)

st.subheader("Violin plot")
fig,ax=plt.subplots()
ax=sns.violinplot(x='Species',y='SepalLengthCm',data=iris,hue="Species")
st.pyplot(fig)


fig,ax=plt.subplots()
plt.subplot(2,2,1)
ax=sns.violinplot(x='Species',y="PetalLengthCm",data=iris,hue="Species")
plt.subplot(2,2,2)
ax=sns.violinplot(x="Species",y="PetalWidthCm",data=iris,hue="Species")
plt.subplot(2,2,3)
ax=sns.violinplot(x="Species",y="SepalWidthCm",data=iris,hue="Species")
plt.subplot(2,2,4)
ax=sns.violinplot(x="Species",y="SepalLengthCm",data=iris,hue="Species")
st.pyplot(fig)

fig,ax=plt.subplots()
ax=sns.pairplot(data=iris,kind="scatter")
st.pyplot(ax)

fig,ax=plt.subplots()
ax=sns.pairplot(iris,hue='Species')
st.pyplot(ax)

st.write("Swarm plot")
fig,ax=plt.subplots()
ax=sns.swarmplot(x="Species",y="PetalLengthCm",data=iris,hue="Species")
st.pyplot(fig)

fig,ax=plt.subplots()
ax=sns.violinplot(x="Species",y="PetalLengthCm",data=iris)
ax=sns.swarmplot(x="Species",y="PetalWidthCm",data=iris)
st.pyplot(fig)


st.write("lmplot")
fig,ax=plt.subplots()
fig=sns.lmplot(x="PetalLengthCm",y="PetalWidthCm",data=iris)
st.pyplot(fig)

st.write("FacetGrid")
g=sns.FacetGrid(iris,hue="Species")
g.map(sns.kdeplot,"PetalLengthCm")
st.pyplot(g)

fig,ax=plt.subplots()
ax=sns.boxenplot(x='Species',y='SepalLengthCm',data=iris,hue="Species")
st.pyplot(fig)

st.write("KDE plot")
fig,ax=plt.subplots()
ax=sns.kdeplot(data=iris,x="SepalLengthCm",y="SepalWidthCm",shade=True)
st.pyplot(fig)

fig,ax=plt.subplots()
sns.distplot(iris['SepalLengthCm'],kde=True,bins=20);
st.pyplot(fig)
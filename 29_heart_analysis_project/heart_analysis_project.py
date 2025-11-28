import pandas as pd
import numpy as np
import streamlit as st

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

import warnings
warnings.filterwarnings('ignore')
st.header("Extensive Analysis + Visualization with Python")
st.write("Heart disease** or **Cardiovascular disease (CVD) is a class of diseases that involve the heart or blood vessels. Cardiovascular diseases are the leading cause of death globally. This is true in all areas of the world except Africa. Together CVD resulted in 17.9 million deaths (32.1%) in 2015.  Deaths, at a given age, from CVD are more common and have been increasing in much of the developing world, while rates have declined in most of the developed world since the 1970s.")
st.write("Exploratory Data Analysis or EDAis a critical first step in analyzing a new dataset. The primary objective of EDA is to analyze the data for distribution, outliers and anomalies in the dataset. It enable us to direct specific testing of the hypothesis. It includes analysing the data to find the distribution of data, its main characteristics, identifying patterns and visualizations.  It also provides tools for hypothesis generation by visualizing and understanding the data through graphical representatio")

st.header("Heart Disease Dataset Viewer")
heart=pd.read_csv(r"C:\Users\91995\Downloads\EDA- HEALTHCARE DOMAIN\heart.csv")
st.subheader(" Heart Dataset Preview")
st.write(heart)

st.write('The shape of the dataset:',heart.shape)

st.subheader("Preview the dataset")
st.write(heart.head())

st.subheader("summary of dataset")
st.write(heart.info())


st.subheader("To find the datatypes")
st.write(heart.dtypes)

st.write(heart.describe())

st.subheader("View column names")
st.write(heart.columns)

st.header("Univariate Analysis")
st.subheader("Check the number of unique values in target variable")
st.write(heart['target'].nunique())

st.subheader("View the unique values in target variable")
st.write(heart['target'].unique())

st.write(heart['target'].value_counts())

st.subheader("Visualize frequency distribution of target variable")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="target",data=heart)
st.pyplot(f)

st.subheader("Frequency Distribution of target variable wrt sex")
st.write(heart.groupby('sex')['target'].value_counts())

f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="sex",hue="target",data=heart)
st.pyplot(f)

st.subheader("we can plot the bars horizontally as follows")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(y="target",hue="sex",data=heart)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="target",data=heart,palette="Set3")
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="target",hue="fbs",data=heart)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="target",hue="exang",data=heart)
st.pyplot(f)

st.subheader("Bivariate Analysis")
correlation=heart.corr()
st.write(correlation)

correlation['target'].sort_values(ascending=False)

st.subheader("Analysis of target and cp variable")
st.write(heart['cp'].nunique())
st.write(heart['cp'].value_counts())

st.subheader("Visualize the frequency distribution of cp variable")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="cp",data=heart)
st.pyplot(f)

st.subheader("Frequency distribution of target variable wrt cp")
st.write(heart.groupby('cp')['target'].value_counts())

f,ax=plt.subplots(figsize=(8,6))
ax=sns.countplot(x="cp",hue="target",data=heart)
st.pyplot(f)

st.subheader("Analysis of target and thalach variable")
st.write(heart['thalach'].nunique())

st.subheader("Visualize the frequency distribution of thallach variable")
f,ax=plt.subplots(figsize=(10,6))
ax=sns.distplot(x=heart['thalach'],bins=10)
st.pyplot(f)

st.subheader("Verital plot")
f,ax=plt.subplots(figsize=(10,6))
x=heart['thalach']
ax=sns.distplot(x,bins=10,vertical=True)
st.pyplot(f)

st.subheader("Seaborn KDE Plot")
f,ax=plt.subplots(figsize=(10,6))
ax=sns.kdeplot(x=heart['thalach'])
st.pyplot(f)

f,ax=plt.subplots(figsize=(10,6))
ax=sns.kdeplot(x=heart['thalach'],shade=True,color='r')
st.pyplot(f)

f,ax=plt.subplots(figsize=(10,6))
x=heart['thalach']
ax=sns.distplot(x,kde=False,rug=True,bins=10)
st.pyplot(f)

st.subheader("Visualize frequency distribution of thalach variable wrt target")
f,ax=plt.subplots(figsize=(8,6))
sns.stripplot(x="target",y="thalach",data=heart)
st.pyplot(f)

st.subheader("Visualize distribution of thalach variable wrt target with boxplot")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x="target",y="thalach",data=heart)
st.pyplot(f)

st.subheader("Multivariate analysis")
f=plt.figure(figsize=(16,12))
a=sns.heatmap(correlation)
st.write(f)

st.subheader("Pair Plot")
num_var=['age','trestbps','chol','thalach','oldpeak','target']
a=sns.pairplot(heart[num_var],kind='scatter',diag_kind='hist')
st.pyplot(a)

st.subheader("Änalysis of age and other variables")
st.write(heart['age'].nunique())
st.write(heart['age'].describe())

st.subheader("Plot the distriution of age variable")
f,ax=plt.subplots(figsize=(10,6))
x=heart['age']
ax=sns.distplot(x,bins=10)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
sns.stripplot(x="target",y="age",data=heart)
st.pyplot(f)
st.subheader("Interpretation")
st.write("We can see that the people suffering from heart disease (target = 1) and people who are not suffering from heart disease (target = 0) have comparable ages.")

st.subheader("Visualize distribution of age variable wrt target with boxplot")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x="target",y="age",data=heart)
st.pyplot(f)
st.subheader("Interpretation")
st.write("The above boxplot tells two different things :")
st.write("The mean age of the people who have heart disease is less than the mean age of the people who do not have heart disease.")
st.write("The dispersion or spread of age of the people who have heart disease is greater than the dispersion or spread of age of the people who do not have heart disease.")



st.subheader("Analyze age and trestbps variable")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.scatterplot(x="age",y="trestbps",data=heart)
st.pyplot(f)
st.subheader("Interpretation")
st.write("The above scatter plot shows that there is no correlation between `age` and `trestbps` variable.")

f,ax=plt.subplots(figsize=(8,6))
ax=sns.regplot(x="age",y="trestbps",data=heart)
st.pyplot(f)
st.subheader("Interpretation")
st.write("The above line shows that linear regression model is not good fit to the data.")


st.subheader("Änalyze age and chol variable")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.scatterplot(x="age",y="chol",data=heart)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.regplot(x="age",y="chol",data=heart)
st.pyplot(f)
st.subheader("Interpretation")
st.write("The above plot confirms that there is a slighly positive correlation between `age` and `chol` variables.")

st.subheader("Analyze chol and thalach variable")
f,ax=plt.subplots(figsize=(8,6))
ax=sns.scatterplot(x="chol",y="thalach",data=heart)
st.pyplot(f)

f,ax=plt.subplots(figsize=(8,6))
ax=sns.regplot(x="chol",y="thalach",data=heart)
st.pyplot(f)

st.subheader("Dealing with missing values")
st.write(heart.isnull().sum())
st.subheader("Interpretation")
st.write("No missing values")

st.header("Check with assert statement")
st.write("We must confirm that our dataset has no missing values.")
st.write("We can write an **assert statement** to verify this.")
st.write(" We can use an assert statement to programmatically check that no missing, unexpected 0 or negative values are present.")
st.write("This gives us confidence that our code is running properly.")
st.write("Assert statement will return nothing if the value being tested is true and will throw an AssertionError if the value is false.")
st.write("assert 1 == 1 (return Nothing if the value is True)")
st.write("assert 1 == 2 (return AssertionError if the value is False)")
assert pd.notnull(heart).all().all()
assert (heart>=0).all().all()
st.subheader("Interpretation")
st.write("The above two commands do not throw any error. Hence, it is confirmed that there are no missing or negative values in the dataset.")
st.write("All the values are greater than or equal to zero.")

st.header("Outlier Detection")
st.write(heart['age'].describe())

st.subheader("Box-plot of age variable")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x=heart['age'])
st.pyplot(f)

st.subheader("Trestbps variable")
heart['trestbps'].describe()

st.subheader("Box plot of trestbps variable")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x=heart['trestbps'])
st.pyplot(f)

st.subheader("chol variable")
st.write(heart['chol'].describe())

st.subheader("box plot of chol variable")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x=heart["chol"])
st.pyplot(f)

st.subheader("Thalach variable")
st.write(heart['thalach'].describe())

st.subheader("Box plot of thalach variable")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x=heart["thalach"])
st.pyplot(f)

st.subheader("Oldpeak variable")
st.write(heart['oldpeak'].describe())

st.subheader("box plot of oldpeak variable")
f,ax=plt.subplots(figsize=(8,6))
sns.boxplot(x=heart["oldpeak"])
st.pyplot(f)

st.subheader("Findings")
st.write("The `age` variable does not contain any outlier.")
st.write("`trestbps` variable contains outliers to the right side.")
st.write("`chol` variable also contains outliers to the right side.")
st.write("`thalach` variable contains a single outlier to the left side.")
st.write("`oldpeak` variable contains outliers to the right side.")
st.write(" Those variables containing outliers needs further investigation.")




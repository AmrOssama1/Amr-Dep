import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

df = pd.read_csv('BankChurners.csv')

st.title('Credit Card Customer Churn Analysis')
st.sidebar.header('Navigation')
st.sidebar.markdown('Created by "Amr Ossama"')
st.sidebar.markdown('Data Source: Kaggle')


sidebar_option = st.sidebar.radio("Choose an Option:", ["Data Overview", "EDA", "Visualizations","Recommendations"])

# Data Overview
if sidebar_option == "Data Overview":
    st.header('Data Overview')
    st.write(df.head())
    st.header('**Summary of Data:**')
    st.write(df.describe())
    if st.sidebar.checkbox('Show Data Sample'):
        st.write(df.sample(10))

# Exploratory Data Analysis
elif sidebar_option == "EDA":
    st.header("Exploratory Data Analysis")

    st.subheader("1. Customer Attrition")
    fig = px.pie(df, names='Attrition_Flag', title='Customer Attrition')
    st.plotly_chart(fig)

    st.subheader("2.Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['Customer_Age'], kde=True , bins=20, ax=ax)
    ax.set_title('Customer Age Distribution')
    st.pyplot(fig)

    st.subheader("3. Outliers Detection")
    fig = px.box(df, y='Customer_Age', title='Outliers Detection in Customer Age')
    st.plotly_chart(fig)

# Visualizations
elif sidebar_option == "Visualizations":
    st.header("1- Income Category ")
    fig1 = px.histogram(df, x='Income_Category', color='Attrition_Flag', title='Income Category Distribution by Attrition Flag')
    st.plotly_chart(fig1)

    st.header("2- Customer Age vs Months on Book ")
    fig2 = px.scatter(df, x='Customer_Age', y='Months_on_book', color='Attrition_Flag', title='Scatterplot of Customer Age vs Months on Book by Attrition Flag')
    st.plotly_chart(fig2)

    st.header("3- Credit Limit ")
    fig3, ax3 = plt.subplots()
    sns.histplot(data=df, x='Credit_Limit', hue='Attrition_Flag', multiple='stack', kde=True, ax=ax3)
    ax3.set_title('Histogram of Credit Limit by Attrition Flag')
    st.pyplot(fig3)

    st.header('4- Avg utilization ratio vs total revolving balance')
    fig4, ax = plt.subplots()
    sns.scatterplot(data=df, x='Total_Revolving_Bal', y='Avg_Utilization_Ratio', hue='Attrition_Flag', ax=ax)
    ax.set_title('Scatterplot of Avg Utilization Ratio vs Total Revolving Balance by Attrition Flag')
    st.pyplot(fig4)
    

    st.header("5- Card Category ")
    fig5 = px.histogram(df, x='Card_Category', color='Attrition_Flag', title='Card Category Distribution by Attrition Flag')
    st.plotly_chart(fig5)

    st.subheader("Groupby Analysis")
    st.title("Card Cateroy by Attrition Flag")
    st.write(df.groupby(['Card_Category', 'Attrition_Flag'])[['Avg_Utilization_Ratio']].mean())


    st.header("6- Correlation Matrix")
    st.title('Visualizing the main columns')
    fig6, ax = plt.subplots()
    corr = df[['Customer_Age', 'Months_on_book', 'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Utilization_Ratio']].corr()
    sns.heatmap(corr, annot=True, ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig6)

    st.header("7- Avg utilization ratio vs Card Category")
    st.title('Heatmap of Avg Utilization Ratio vs Card Category')
    fig7, ax = plt.subplots()
    pivot = df.pivot_table(index='Card_Category', columns='Attrition_Flag', values='Avg_Utilization_Ratio', aggfunc='mean')
    sns.heatmap(pivot, annot=True, ax=ax)
    ax.set_title('Heatmap of Avg Utilization Ratio vs Card Category')
    st.pyplot(fig7)

if sidebar_option == "Recommendations":
    st.header("Recommendations")
    st.write("Based on the analysis, the following recommendations can be made:")
    st.write("The number of attried customers have high utilization ratio which indicates financial stress. "
                     "The clients with less months on book leaves which indicates non satisfaction, so here is an issue for grabbing new clients. "
                     "Blue card holders have higher utilization values but lower engagement which indicates they can leave the bank soon. "
                     "I see here we should focus on clients with less months on book and especially who have blue card category.")


st.sidebar.write("End of App")


    
                    




    


   

        
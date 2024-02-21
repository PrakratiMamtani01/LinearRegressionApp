import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Confused where to travel in India?")
st.header("Here is your Travel Guide")
st.image("TajMahal.jpeg")
input_price = st.slider('Pick a Price Range', 0,4000)


df = pd.read_csv("TopIndianPlacestoVisit.csv")


tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Regression Line"])


tab1.subheader("Google Rating vs Price")
price_by_rating = df.groupby('Google review rating')['Entrance Fee in INR'].mean().reset_index()
price_filtered = price_by_rating[price_by_rating['Entrance Fee in INR'] <= input_price]
tab1.line_chart(price_filtered.set_index('Google review rating'))

tab2.subheader("Number of monuments according to states")
monument_count = df.groupby('State')['Name'].nunique().reset_index()
tab2.bar_chart(monument_count.set_index('State'))

tab3.subheader("Linear Regression line")
x = df[['time needed to visit in hrs', 'Google review rating', 'Number of google review in lakhs']]
y = df['Entrance Fee in INR']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y)

from sklearn.linear_model import LinearRegression
lr= LinearRegression()
lr.fit(x_train, y_train)
pred = lr.predict(x_test)
fig, ax = plt.subplots()
ax.scatter(y_test, pred)
ax.plot(y_test, y_test, color='red')  # plotting the diagonal line
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
tab3.pyplot(fig)


if st.button("Generate Report"):
  import streamlit as st
  import streamlit.components.v1 as components

  # Title for your app
  st.title('Sweetviz Report in Streamlit')

  # Display the Sweetviz report
  report_path = 'report.html'
  HtmlFile = open(report_path, 'r', encoding='utf-8')
  source_code = HtmlFile.read()
  components.html(source_code, height=1000,width=1000)

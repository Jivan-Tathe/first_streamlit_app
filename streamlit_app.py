import streamlit
streamlit.titke('My Parents New Healthy Diner ')

stream.lit.header('Breakfast Favorites')
streamlit.text('🍵omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🥑 Avecado Toast')

streamlite.header('🍌🥭Build Your Own Fruit Smothie🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

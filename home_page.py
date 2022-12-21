import streamlit as st

def bio() -> None:
    with st.container():
            st.markdown(
                '''
                ### Biography

                My name is Andre Jacobs and I am a Data Analyst. I am currently in progress with my Data Analytics bachelors at 
                at the University of North Alabama. I am a college golfer of 4 years. Through my experiences as a student athlete
                I have met many great people and have grown from the experience. I have experience with Data Analysis using various 
                technologies and have a passion for data and driving impact through analysis and building world-class data applications.
                '''
            )

def my_skills() -> None:
    with st.container():
            st.markdown(
                '''
                ### Skills
                - Microsoft Excel -> 5 Years
                    - Pivot tables, VLOOKUP, Data Analysis add in

                - Python Programming -> 3 Years
                    - NumPy, Pandas, SciPy, Sci-kit Learn, Plotly, Streamlit

                - SQL -> 2 Years
                    - SELECT, JOINS, subqueries, CREATE TABLE, CREATE DATABASE

                - R Programming -> 1 Year
                    - Statistical programming with built in functions

                - Microsoft Power BI -> 1 Year
                    - PowerQuery, M Language, DAX, Dashboards
                
                '''
            )

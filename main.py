import streamlit as st
from home_page import *
from projects import *
from education import *

def main() -> None:
    st.title('Andre Jacobs Data Portfolio')

    home, projects, education = st.tabs(['Home', 'My Projects', 'My Education'])

    with home:
        st.markdown('## Andre Jacobs - Data Analyst')

        # created functions in home_page.py to improve readability of code
        bio()
        my_skills()

    with projects:
        st.markdown('## My Data Projects!')

        # created functions in projects.py to improve readability of code
        recommendation_engine()

    with education:
        st.markdown('## My Education')

        # created functions in college.py to improve readability of code
        college()

        

main()
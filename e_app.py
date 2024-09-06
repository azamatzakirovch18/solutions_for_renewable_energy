# In this file, I will connect all pages into main page

# those are important libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# those are pages
from f_introduction import introduction
from g_analysis import analysis
from problems_and_solutions import problemsAndSolutions

# lets get started
st.set_page_config(
    page_title="Global Renewable Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# with this function I can create buttons for different pages
with st.sidebar:
    options = st.selectbox(
        "please choose you oprion",
        options=[
            "Main Page",
            "Analysis Page",
            "Solutions Page"
        ]

    )


# That's part of working pages
if options == "Main Page":
    introduction()
elif options == "Analysis Page":
    analysis()
elif options == "Solutions Page":
    problemsAndSolutions()
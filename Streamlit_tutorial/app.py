import streamlit as st
import pandas as pd
import numpy as np

if st.button('Click Me'):
    st.write('success')

if st.checkbox('Check Here'):
    st.write('Hello')

options = st.multiselect(
    'Which are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue',],
    ['Green', 'Yellow']
)


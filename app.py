import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
from tensorflow.keras.models import load_model


st.title('Predictive Student Dropout Prevention System')
st.write('this is the web app for the predictive student dropout prevention system. Upload your Excel or CSV file to get started.')


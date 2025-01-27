import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
from tensorflow.keras.models import load_model


st.title('Predictive Student Dropout Prevention System')
st.write("""This web application is designed to help educational institutions predict and prevent student dropouts. 
By leveraging machine learning models, the system analyzes student data to identify those at risk of dropping out. 
Upload your Excel or CSV file containing student data to get started. The application will process the data, 
make predictions, and display the results to help you take proactive measures.""")

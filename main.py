# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from utils import apply_background,custom_navbar
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
# Make sure your dataset is preprocessed and saved as 'weather_frankfrut.csv'
df = pd.read_csv('weather_frankfrut.csv')

# Function to classify road conditions based on temperature and precipitation
def road_condition(tavg, prcp):
    if tavg <= 0 or prcp == 0:
        return 0
    elif  tavg == 0  or prcp > 5:
        return 1
    else:
        return 2

# Apply road_condition function to create a new column in the dataset
df['road_condition'] = [road_condition(avg, rain) for avg, rain in zip(df.tavg, df.prcp)]

# Prepare the feature set (X) and the target variable (y)
X = df[['tavg', 'prcp', 'wdir', 'wspd']]
y = df['road_condition']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


apply_background(image_path="./media/image.jpg")
# Streamlit app layout with CSS for background image

# Streamlit app layout
st.title('Road Condition Prediction App')
st.write('This app predicts road conditions (Snow/Ice, Wet, or Dry) based on weather data.')

# User input for weather parameters
st.header('Enter Weather Parameters:')
tavg = st.number_input('Average Temperature (°C)', min_value=-10.0, max_value=50.0, value=15.0)
prcp = st.number_input('Precipitation (mm)', min_value=0.0, max_value=50.0, value=2.0)
wdir = st.number_input('Wind Direction (degrees)', min_value=0.0, max_value=360.0, value=180.0)
wspd = st.number_input('Wind Speed (km/h)', min_value=0.0, max_value=50.0, value=10.0)

# Add a button to submit and predict the road condition
if st.button('Predict Road Condition'):
    # Prepare the user input data for prediction
    user_data = np.array([[tavg, prcp, wdir, wspd]])
    user_df = pd.DataFrame(user_data, columns=['tavg', 'prcp', 'wdir', 'wspd'])

    # Predict road condition based on user input
    prediction = model.predict(user_df)[0]

    # Define a dictionary for human-readable road condition labels
    road_condition_labels = {0: 'Snow/Ice', 1: 'Wet', 2: 'Dry'}
    
    # Display the prediction result
    st.success(f'The predicted road condition is: **{road_condition_labels[prediction]}**')

# Optionally display model accuracy on test data
if st.checkbox('Show Model Accuracy'):
    y_pred_test = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_test)
    st.write(f'Model Accuracy: **{accuracy * 100:.2f}%**')

# Road Condition Prediction Based on Weather Data
## Project Overview
This project aims to predict road conditions (Snow/Ice, Wet, or Dry) using real-time weather data. It leverages machine learning to help forecast road conditions based on factors such as temperature, precipitation, wind direction, and wind speed. This is especially useful for the automotive industry, road safety agencies, and weather-related services to enhance traffic safety and driving conditions.

The model is built using a Random Forest Classifier, which is trained on historical weather data. The application is deployed using Streamlit, providing a user-friendly interface for inputting weather parameters and getting real-time road condition predictions.

## Motivation
In regions with fluctuating weather conditions, understanding the road status in advance can significantly reduce accidents and improve overall road safety. This project addresses the need for an intelligent system to predict hazardous road conditions caused by snow, ice, or rain. The project demonstrates how machine learning can be applied in the automotive industry to improve safety through road condition forecasts.

## Features

- **Real-time Road Condition Prediction**: Predicts road conditions (Snow/Ice, Wet, or Dry) based on user-input weather data.
- **Machine Learning Model**: Utilizes a Random Forest Classifier trained on historical weather data to provide accurate predictions.
- **User-friendly Interface**: Built with **Streamlit** for ease of use, allowing users to input data and receive predictions quickly.
- **Accuracy Evaluation**: Option to display the accuracy of the machine learning model on test data.
- **Customizable Parameters**: Users can adjust weather parameters to simulate different conditions.

  ## How It Works

1. **Input Weather Parameters**: The user can input values for average temperature (°C), precipitation (mm), wind direction (degrees), and wind speed (km/h) via the Streamlit app interface.
2. **Predict Road Conditions**: Click the "Predict Road Condition" button to get a prediction based on the input values.
3. **Check Model Accuracy**: Optionally, users can check the model’s accuracy on the test dataset.

## Installation

To run the app locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/road-condition-prediction.git
   cd road-condition-prediction




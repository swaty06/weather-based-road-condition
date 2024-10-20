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

## How It Works

1. **Input Weather Parameters**: The user can input values for average temperature (°C), precipitation (mm), wind direction (degrees), and wind speed (km/h) via the Streamlit app interface.
2. **Predict Road Conditions**: Click the "Predict Road Condition" button to get a prediction based on the input values.
3. **Check Model Accuracy**: Optionally, users can check the model’s accuracy on the test dataset.

## How to Use

To utilize the Road Condition Prediction tool, follow these steps:

1. **Run the App**:
   - After installing the required dependencies and running the app using:
     ```bash
     streamlit run app.py
     ```
   - The application will open in your default web browser.

2. **Input Weather Parameters**:
   - You will see input fields for the following weather parameters:
     - **Average Temperature (°C)**: Enter the average temperature.
     - **Precipitation (mm)**: Input the amount of precipitation.
     - **Wind Direction (degrees)**: Provide the wind direction.
     - **Wind Speed (km/h)**: Enter the wind speed.

3. **Make Predictions**:
   - Click the **"Predict Road Condition"** button to receive the prediction based on the input values.

4. **View Prediction**:
   - The predicted road condition will be displayed below the input fields, indicating whether the conditions are:
     - **Snow/Ice**
     - **Wet**
     - **Dry**

5. **Check Model Accuracy (Optional)**:
   - If desired, you can check the accuracy of the model on the test dataset by checking the corresponding option in the app.

By following these steps, you can quickly assess road conditions based on various weather parameters using the tool.


## Installation

To run the app locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/road-condition-prediction.git
   cd road-condition-prediction




## Future Improvements

The following enhancements are planned for future versions of the Road Condition Prediction tool:

- **Integration with Real-time Weather APIs**: 
  - Automatically fetch live weather data for continuous updates and more accurate predictions.
  
- **Improved Model Accuracy**: 
  - Experiment with other machine learning models or incorporate additional weather features (e.g., humidity, pressure) to enhance prediction accuracy.
  
- **Deployment Options**: 
  - Deploy the app on cloud platforms like Heroku or AWS for public access, allowing users to utilize the tool without needing to run it locally.
  
- **User Feedback Mechanism**: 
  - Implement a feedback feature to gather user insights and improve the model and user experience based on real-world usage.
  
- **Data Visualization**: 
  - Add visual representations of the predicted road conditions over time, allowing users to track changes and trends.

- **Mobile Compatibility**: 
  - Optimize the web app for mobile devices to enhance accessibility and usability on smartphones and tablets.

- **Enhanced User Interface**: 
  - Improve the app's UI/UX design for better user interaction and experience.






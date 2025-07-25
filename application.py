from flask import Flask, request, render_template 
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'), 
                parental_level_of_education=request.form.get('parental_level_of_education'), 
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'), 
                

                reading_score=int(request.form.get('reading_score')), 
                writing_score=int(request.form.get('writing_score'))  
            )
            
            pred_df = data.get_data_as_data_frame()
            

            print("--- Input Data Received as DataFrame ---")
            print(pred_df)
            print("--------------------------------------")
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            

            final_result = round(results[0], 2)
            
            return render_template('home.html', results=final_result)

        except Exception as e:
    
            print(f"!!!!!!!!!!!!! ERROR IN /predictdata !!!!!!!!!!!!!")
            print(f"Error Type: {type(e).__name__}, Details: {e}")
            print(f"Form Data Received: {request.form}")
            print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            

            return render_template('home.html', error_message=f"An error occurred: {e}")

@app.route('/debug')
def debug():
    return "App is running fine!"    

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5050)
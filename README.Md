# Customer Churn Prediction Model

## Project Goal
The goal of this project is to identify major factors affecting customer churn, and predicting which e-commerce customers are likely to churn, (stop using the platform) our target variable in this dataset is "Churn".

We will develop a suitable model based on the data we have and have it perform automated predictions and send weekly notifications as to which customers are likely to churn, businesses can use this information to intervene when customers are likely to churn

By identifying at-risk customers early, the business can implement targeted retention strategies to reduce churn rates. Keeping customers is imoprtant for maintaining a steady revenue, enhancing customer lifetime value, and optimizing marketing efforts.

### Problem Statement
An E-commerce business wants to predict which customers are likely to churn based on their past behaviour and interaction, so it can pro-actively make efforts to retain them (personalized marketing, service improvement).

Target column - Churn (1 = churned, 0 = retained)





### Points to note
+ __This project aims to make and improve model performance over time, iterating the data process to make sure the model becomes a bit better after every iteration.__
+ __Any missed step or detail in any of the notebooks can be brought up and improved, the project will see the continous improvement of the model and pipeline.__
+ __Some assumptions were made for the sake of this project, in a business setting, it would be more reasonable to ask for clarity or to get additional data from its source__


### Project Workflow

1. **Data Exploration & Cleaning**
   - Performed exploratory data analysis (EDA) to understand patterns and relationships.
   - Handled missing values and outliers using statistical imputation and capping.
   - Encoded categorical variables using appropriate encoding techniques.

2. **Feature Engineering**
   - Separated numerical, ordinal, nominal, and binary features.
   - Applied scaling and encoding pipelines for model readiness.
   - Split data into training and testing sets.

3. **Modeling**
   - Built and tuned a **Logistic Regression model** to predict churn.
   - Evaluated performance using:
     - Accuracy
     - Precision, Recall, F1-score
     - ROC-AUC score and Confusion Matrix

4. **Deployment**
   - **Backend:** FastAPI service hosted on **Render**
   - **Frontend:** Streamlit web app hosted on **Streamlit Cloud**
   - Communication between both happens via REST API endpoints.


### Tech Stack
- Data processing: pandas, numpy
- Data visualization: matplotlib, seaborn, plotly
- Modelling: scikit-learn
- Backend: Python, FastAPI
- Frontend: streamlit
- Deployment: render, streamlit.io


## How to Run Locally

### 1. Clone the repository

<code> 
git clone https://github.com/Danny-Dalo/Ecommerce_Churn.git

cd <Ecommerce_Churn>
</code>

### 2. Create a Virtual Environment
<code>
python -m venv venv
source venv/bin/activate or venv\Scripts\activate on Windows
</code>

### 3. Install Dependencies
<code>
pip install -r requirements.txt
</code>

### 4. Run the FastAPI backend
<code>
cd app
uvicorn main:app --reload
</code>
The API will be live at http://127.0.0.1:8000/docs

### 5. Run the Frontend (Streamlit)
<code>
cd app (if you're not already in the directory)
streamlit run app_frontend.py
</code>



## Live Demo
Frontend (Streamlit): https://dalo-customer-churn-model.streamlit.app
Backend (FastAPI): https://ecommerce-churn-api-p8im.onrender.com/docs


## Future Improvements
- Test performance of different models
- Hyperparameter tuuning with Cross validation techniques
- Improved labelling for analytics visuals
- Improve frontend design and add visualization of probabilities
- Complete analysis review of the data (plots, insights, etc.)


## Author
Daniel Oghinan
Linkedin: https://www.linkedin.com/in/daniel-oghinan
GitHub: https://github.com/Danny-Dalo


## Summary
The projects mirrors a real-world data science project pipeline, from raw data to analysis and predictive insights. The project shows how technical ability can provide actual business benefits
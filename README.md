# 🧠 Mental Health Prediction Web App

This is a Streamlit web application that predicts a user's concentration level based on various mental health indicators such as fatigue, sleep, agitation, hopelessness, etc.

## 📊 Features

- Input form for mental health symptoms
- Predicts concentration level using a trained logistic regression model
- Clean and intuitive UI built with Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

---

## 📁 Project Structure
mental_health_app/
│
├── app.py # Streamlit app file
├── mental_health_model.pkl # Trained ML model
├── scaler.pkl # Feature scaler
├── requirements.txt # Python dependencies
├── README.md # Project overview
└── dataset.csv # Source dataset (optional)


---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-onomeVera/mental_health_app.git
cd mental_health_app

2. Create and activate a virtual environment
On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt



4. Run the app
streamlit run app.py

🚀 Deploy on Streamlit Cloud
Push your code to a GitHub repository.

Go to streamlit.io/cloud.

Connect your GitHub account and select the repo.

Set the main file as app.py.

🧠 Model Training
Model training was done using logistic regression on a dataset with the following features:

Sleep

Appetite

Interest

Fatigue

Worthlessness

Agitation

Suicidal Ideation

Sleep Disturbance

Aggression

Panic Attacks

Hopelessness

Restlessness

Low Energy

The trained model and scaler were serialized with joblib.

🙋‍♀️ Author
Onome Oviero
Integration Manager at AutoVerify





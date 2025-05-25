
# 📉 Customer Churn Prediction

This project uses machine learning to predict whether a telecom customer will churn.

## 🔍 Overview

- **Dataset**: Telco Customer Churn (Kaggle)
- **Models**: Random Forest (default), extensible to XGBoost, etc.
- **Libraries**: Pandas, Scikit-learn, Streamlit

## 📁 Project Structure

- `data/`: Contains the dataset
- `notebooks/`: Jupyter notebooks for EDA and modeling
- `src/`: Python modules for data processing and model training
- `models/`: Directory for saving trained models
- `app.py`: Streamlit web application
- `tests/`: Unit tests for core functionalities
- `requirements.txt`: Python dependencies

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd customer-churn-prediction
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📊 Model Performance

- **ROC-AUC**: ~81%
- **F1 Score**: ~0.79

## ✅ Features Used

- Tenure, Monthly Charges, Contract type, and more.

## 🔧 Improvements & Future Work

- [x] Hyperparameter tuning
- [x] Handle class imbalance
- [x] Model comparison (XGBoost, etc.)
- [ ] CI/CD Integration
- [ ] Docker support

## 📸 App Preview

![App Screenshot](https://via.placeholder.com/600x400.png?text=Streamlit+App+Preview)

## 📜 License

MIT

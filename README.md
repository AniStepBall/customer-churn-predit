
# Customer Churn Prediction

The project demonstrates **data preprocessing, pipeline engineering, hyperparameter tuning, and model persistence**, making it a strong showcase of practical data science skills.  
The project demonstrates an end-to-end approach to solving churn prediction with a focus on scalability, interpretability, and reproducibility and covers the lifecycle of a data science workflow
•	Data ingestion and preprocessing
•	Handling categorical, numerical, and binary features
•	Building reusable preprocessing pipelines with scikit-learn
•	Training a baseline model (Random Forest) and optimizing it with GridSearchCV
•	Evaluating performance with classification metrics and ROC-AUC
•	Saving and loading trained models for deployment


## Overview

- **Dataset**: Telco Customer Churn (Kaggle)
- **Models**: Random Forest (default), extensible to XGBoost, etc.
- **Libraries**: Pandas, Scikit-learn, Streamlit

## Project Structure

- `data/`: Contains the dataset
- `notebooks/`: Jupyter notebooks for EDA and modeling
- `src/`: Python modules for data processing and model training
- `models/`: Directory for saving trained models
- `app.py`: Streamlit web application
- `tests/`: Unit tests for core functionalities
- `requirements.txt`: Python dependencies
- README.md



## How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd customer-churn-prediction
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```

## Model Performance

- **ROC-AUC**: ~81%
- **F1 Score**: ~0.79

## Features Used

- Tenure, Monthly Charges, Contract type, and more.
- Preprocessing Pipelines
  - Handles missing values, categorical encoding, scaling, and binary encoding  
  - Reproducible with `ColumnTransformer` and `Pipeline`
 Modeling
  - Baseline: Random Forest Classifier  
  - Hyperparameter tuning with `GridSearchCV`  
  - Model persistence with `joblib`  

Evaluation Metrics
  - Precision, Recall, F1-Score  
  - ROC-AUC Score for robust performance measurement  


## Improvements & Future Work

- [x] Hyperparameter tuning
- [x] Address class imbalance with SMOTE or class weighting
- [x] Model comparison (XGBoost, etc.)
- [ ] CI/CD Integration
- [ ] Docker support
- [ ] Add XGBoost / LightGBM for improved performance
- [ ] Perform feature importance analysis to understand churn drivers
- [ ] Use SHAP or LIME for interpretability
- [ ] Deploy model via Flask/FastAPI or Streamlit dashboard
- [ ] Automate training with MLflow or DVC
- [ ] Build a real-time churn prediction API

**References**
Dataset: Telco Customer Churn Dataset (Kaggle)
Scikit-learn Documentation: https://scikit-learn.org/stable/



## License

MIT

# Archivo base para el despliegue del Agente en Streamlit
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

transactions = pd.read_csv("data/transactions.csv", parse_dates=["transaction_date"])
customers = pd.read_csv("data/customers.csv", parse_dates=["signup_date", "last_active_date"])

print(f"{len(customers):,} clientes · {len(transactions):,} transacciones")
print(f"Rango de fechas: {transactions['transaction_date'].min().date()} a {transactions['transaction_date'].max().date()}")

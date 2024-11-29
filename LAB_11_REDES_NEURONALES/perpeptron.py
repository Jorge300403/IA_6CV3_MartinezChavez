import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import KFold

# Cargar dataset desde CSV
def cargar_dataset(file_path):
    # Cargar el CSV usando pandas
    data = pd.read_csv(file_path)
    
    # Diagnóstico: revisar las primeras filas
    print("Primeras filas del dataset:")
    print(data.head())
    
    # Verificar valores nulos
    print("Valores nulos en el dataset:")
    print(data.isnull().sum())
    
    # Asumir que la última columna es la etiqueta (y) y el resto son las características (X)
    X = data.iloc[:, :-1].values  # todas las columnas excepto la última
    y = data.iloc[:, -1].values   # solo la última columna
    
    # Si las etiquetas son categóricas, las convertimos en numéricas
    if data.iloc[:, -1].dtype == 'object':  # Si la última columna es categórica
        le = LabelEncoder()
        y = le.fit_transform(y)
    
    return X, y

# Preprocesamiento
def preprocesamiento(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

# Perceptrón
def perceptron_model():
    model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=10000, solver='adam', random_state=42)
    return model

# Métodos de validación

# Hold-out (70/30)
def validacion_holdout(X, y, model, test_size=0.3):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, cm

# Cross-Validation (K-Fold)
def validacion_kfold(X, y, model, k=5):
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=kf)
    accuracy = np.mean(scores)
    
    # Calcular matriz de confusión para el K-Fold
    model.fit(X, y)  # Entrenamos el modelo con todo el dataset
    y_pred = model.predict(X)
    cm = confusion_matrix(y, y_pred)
    
    return accuracy, cm

# Leave-One-Out
def validacion_leave_one_out(X, y, model):
    loo = LeaveOneOut()
    scores = cross_val_score(model, X, y, cv=loo)
    accuracy = np.mean(scores)
    
    # Calcular matriz de confusión para Leave-One-Out
    model.fit(X, y)  # Entrenamos el modelo con todo el dataset
    y_pred = model.predict(X)
    cm = confusion_matrix(y, y_pred)
    
    return accuracy, cm

# Ejecutar el código
if __name__ == "__main__":
    # Cargar dataset desde el archivo CSV
    file_path = "C:/Users/jorge/OneDrive/Documentos/JORGE/ESCOM/9_SEMESTRE/IA/LABORATORIO/11_REDES_NEURONALES/bezdekIris.data"
    X, y = cargar_dataset(file_path)
    X_scaled = preprocesamiento(X)

    # Crear el modelo de perceptrón
    model = perceptron_model()

    # Validación Hold-out (70/30)
    print("Desempeño de Validación Hold-out (70/30):")
    accuracy_holdout, cm_holdout = validacion_holdout(X_scaled, y, model)
    print(f"Accuracy: {accuracy_holdout}")
    print("Matriz de Confusión:")
    print(cm_holdout)

    # Validación Cross-validation (K-Fold)
    print("\nDesempeño de Validación Cross-validation (K-Fold):")
    accuracy_kfold, cm_kfold = validacion_kfold(X_scaled, y, model)
    print(f"Accuracy: {accuracy_kfold}")
    print("Matriz de Confusión::")
    print(cm_kfold)

    # Validación Leave-One-Out
    print("\nDesempeño de Validación Leave-One-Out:")
    accuracy_loo, cm_loo = validacion_leave_one_out(X_scaled, y, model)
    print(f"Accuracy: {accuracy_loo}")
    print("Matriz de Confusión:t:")
    print(cm_loo)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import KFold

# Carga el archivo con la ruta especificada en el código
def cargar_dataset():
    file_path = "C:/Users/jorge/OneDrive/Documentos/JORGE/ESCOM/9_SEMESTRE/IA/LABORATORIO/10_KNN_BAYES/bezdekIris.data"
    try:
        datos = pd.read_csv(file_path, header=None)
        return datos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

# Métodos de validación
def hold_out(modelo, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    return accuracy_score(y_test, y_pred), confusion_matrix(y_test, y_pred)

def cross_validation(modelo, X, y, folds):
    kf = KFold(n_splits=folds, shuffle=True, random_state=42)
    scores = cross_val_score(modelo, X, y, cv=kf)
    modelo.fit(X, y)
    y_pred = modelo.predict(X)
    conf_matrix = confusion_matrix(y, y_pred)
    return np.mean(scores), conf_matrix

def leave_one_out(modelo, X, y):
    loo = LeaveOneOut()
    y_true, y_pred = [], []
    for train_idx, test_idx in loo.split(X):
        modelo.fit(X[train_idx], y[train_idx])
        pred = modelo.predict(X[test_idx])
        y_true.extend(y[test_idx])
        y_pred.extend(pred)
    return accuracy_score(y_true, y_pred), confusion_matrix(y_true, y_pred)

# Ejecutar Naive Bayes
def ejecutar_naive_bayes(X, y):
    modelo = GaussianNB()
    validaciones = {
        "Hold-Out (70/30)": hold_out,
        "10-Fold Cross-Validation": lambda m, X, y: cross_validation(m, X, y, 10),
        "Leave-One-Out": leave_one_out
    }

    resultados = []
    for metodo, funcion_validacion in validaciones.items():
        accuracy, matriz_confusion = funcion_validacion(modelo, X, y)
        resultados.append((metodo, accuracy, matriz_confusion))
    return resultados

if __name__ == "__main__":
    datos = cargar_dataset()
    if datos is not None:
        X = datos.iloc[:, :-1].values
        y = datos.iloc[:, -1].values
        resultados = ejecutar_naive_bayes(X, y)

        for res in resultados:
            print(f"Método de Validación: {res[0]}")
            print(f"Accuracy: {res[1]:.4f}")
            print("Matriz de Confusión:")
            print(res[2])
    else:
        print("No se pudo procesar el dataset.")

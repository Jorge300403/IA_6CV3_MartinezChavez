import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut, KFold
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el archivo con la ruta especificada en el código
def cargar_dataset():
    file_path = "C:/Users/jorge/OneDrive/Documentos/JORGE/ESCOM/9_SEMESTRE/IA/LABORATORIO/9_CLASIFICADORES_EUCLILIANOS_1NN/bezdekIris.data"
    try:
        datos = pd.read_csv(file_path, header=None)
        return datos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

# Calcular la distancia euclidiana
def distancia_euclidiana(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Clasificador basado en distancia euclidiana
def clasificador_euclidiano(X_train, y_train, X_test):
    y_pred = []
    for test_point in X_test:
        # Calcular las distancias entre el punto de prueba y todos los puntos de entrenamiento
        distancias = [distancia_euclidiana(test_point, x_train) for x_train in X_train]
        # Encontrar el índice del punto más cercano
        closest_index = np.argmin(distancias)
        # Predecir la clase del punto más cercano
        y_pred.append(y_train[closest_index])
    return np.array(y_pred)

# Métodos de validación
def hold_out(modelo, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    y_pred = modelo(X_train, y_train, X_test)
    return accuracy_score(y_test, y_pred), confusion_matrix(y_test, y_pred).astype(int)  # Convertir a enteros

def cross_validation(modelo, X, y, folds):
    kf = KFold(n_splits=folds, shuffle=True, random_state=42)
    scores = []
    conf_matrices = []
    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        y_pred = modelo(X_train, y_train, X_test)
        scores.append(accuracy_score(y_test, y_pred))  # Almacena la precisión de cada pliegue
        conf_matrices.append(confusion_matrix(y_test, y_pred).astype(int))  # Convertir a enteros
    avg_accuracy = np.mean(scores)  
    avg_conf_matrix = np.mean(conf_matrices, axis=0)
    return avg_accuracy, avg_conf_matrix

def leave_one_out(modelo, X, y):
    loo = LeaveOneOut()
    y_true, y_pred = [], []
    for train_idx, test_idx in loo.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        y_pred_point = modelo(X_train, y_train, X_test)
        y_true.extend(y_test)
        y_pred.extend(y_pred_point)
    return accuracy_score(y_true, y_pred), confusion_matrix(y_true, y_pred).astype(int)  # Convertir a enteros

# Ejecutar clasificador Euclidiano
def ejecutar_clasificador_euclidiano(X, y):
    validaciones = {
        "Hold-Out (70/30)": hold_out,
        "10-Fold Cross-Validation": lambda m, X, y: cross_validation(m, X, y, 10),
        "Leave-One-Out": leave_one_out
    }

    resultados = []
    for metodo, funcion_validacion in validaciones.items():
        accuracy, matriz_confusion = funcion_validacion(clasificador_euclidiano, X, y)
        resultados.append((metodo, accuracy, matriz_confusion))
    return resultados

if __name__ == "__main__":
    datos = cargar_dataset()
    if datos is not None:
        X = datos.iloc[:, :-1].values
        y = datos.iloc[:, -1].values
        resultados = ejecutar_clasificador_euclidiano(X, y)

        for res in resultados:
            print(f"Método de Validación: {res[0]}")
            print(f"Accuracy: {res[1]:.2f}")
            print("Matriz de Confusión:")
            print(res[2])
    else:
        print("No se pudo procesar el dataset.")

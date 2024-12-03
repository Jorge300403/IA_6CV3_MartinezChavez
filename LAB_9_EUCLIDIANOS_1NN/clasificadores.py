import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Cargar el dataset desde el archivo
archivo = "C:/Users/jorge/OneDrive/Documentos/JORGE/ESCOM/9_SEMESTRE/IA/LABORATORIO/8_DATASETS/iris/bezdekIris.data"
columnas = ['sepal length', 'sepal width', 'petal length', 'petal width', 'target']
iris_df = pd.read_csv(archivo, header=None, names=columnas)

# Separar características y etiquetas
X = iris_df.iloc[:, :-1].values
y = iris_df.iloc[:, -1].values

# Parte 1: Clasificador Euclidiano
def euclidean_classifier(X_train, y_train, X_test):
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    return knn.predict(X_test)

def validation_methods_euclidean(X, y):
    print("== Validación con Clasificador Euclidiano ==")
    
    # Hold Out 70/30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    y_pred = euclidean_classifier(X_train, y_train, X_test)
    print("\nHold Out 70/30")
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    
    # 10-Fold Cross-Validation
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    scores = cross_val_score(knn, X, y, cv=10)
    print("\n10-Fold Cross-Validation")
    print(f"Mean Accuracy: {np.mean(scores)}")
    
    # Leave-One-Out
    loo = LeaveOneOut()
    scores_loo = cross_val_score(knn, X, y, cv=loo)
    print("\nLeave-One-Out Validation")
    print(f"Mean Accuracy: {np.mean(scores_loo)}")

# Parte 2: Clasificador 1NN
def nn_classifier(X_train, y_train, X_test):
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    return knn.predict(X_test)

def validation_methods_1nn(X, y):
    print("\n== Validación con Clasificador 1NN ==")
    
    # Hold Out 70/30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    y_pred = nn_classifier(X_train, y_train, X_test)
    print("\nHold Out 70/30")
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    
    # 10-Fold Cross-Validation
    knn = KNeighborsClassifier(n_neighbors=1)
    scores = cross_val_score(knn, X, y, cv=10)
    print("\n10-Fold Cross-Validation")
    print(f"Mean Accuracy: {np.mean(scores)}")
    
    # Leave-One-Out
    loo = LeaveOneOut()
    scores_loo = cross_val_score(knn, X, y, cv=loo)
    print("\nLeave-One-Out Validation")
    print(f"Mean Accuracy: {np.mean(scores_loo)}")

# Ejecutar validaciones
validation_methods_euclidean(X, y)
validation_methods_1nn(X, y)

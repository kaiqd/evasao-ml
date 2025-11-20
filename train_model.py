import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

# Caminho do CSV (ajuste se o nome for diferente)
DATA_PATH = "data/alunos.csv"
MODEL_PATH = "model/logistic_model.pkl"


def main():
    # 1. Ler dados
    df = pd.read_csv(DATA_PATH)

    # 2. Separar target e features
    target_col = "evasao_ate_1ano"
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 3. Identificar colunas categóricas e numéricas
    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
    num_cols = X.select_dtypes(include=["number"]).columns.tolist()

    print("Colunas categóricas:", cat_cols)
    print("Colunas numéricas:", num_cols)

    # 4. Pré-processamento
    preprocess = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(drop="first", handle_unknown="ignore"),
                cat_cols,
            ),
            ("num", "passthrough", num_cols),
        ]
    )

    # 5. Pipeline (pré-processamento + modelo)
    clf = Pipeline(
        steps=[
            ("preprocess", preprocess),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    # 6. Train / Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y,
    )

    # 7. Treinar
    clf.fit(X_train, y_train)

    # 8. Avaliar
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)[:, 1]

    print("\n=== Métricas no conjunto de teste ===")
    print("Acurácia :", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall   :", recall_score(y_test, y_pred))
    print("F1       :", f1_score(y_test, y_pred))
    print("AUC-ROC  :", roc_auc_score(y_test, y_prob))

    # 9. Salvar modelo treinado
    os.makedirs("model", exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print(f"\n✅ Modelo salvo em: {MODEL_PATH}")


if __name__ == "__main__":
    main()

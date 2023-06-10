from typing import Dict, Tuple
import pandas as pd
import numpy as np
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import logging


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data["Client"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    """Trains the logistic regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for client.

    Returns:
        Trained model.
    """
    mlflow.autolog()
    regressor = LogisticRegression()

    # TODO refactor, causes errors, model has very low r2 score
    param_grid = [
        {'penalty': ['l1', 'l2', 'elasticnet', None],
         'C': np.logspace(-4, 4, 20),
         'solver': ['lbfgs', 'newton-cholesky', 'newton-cg', 'liblinear', 'sag', 'saga'],
         'max_iter': [100, 1000, 2500, 5000]
         }
    ]
    clf = GridSearchCV(regressor, param_grid=param_grid, cv=3, n_jobs=-1, verbose=0)
    clf.fit(X_train, y_train)
    print("Tuned Hyperparameters :", clf.best_params_)
    print("Accuracy :", clf.best_score_)

    regressor.fit(X_train, y_train)

    return regressor


def evaluate_model(
        regressor: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for client.
    """
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)

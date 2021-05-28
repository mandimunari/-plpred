import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle 
from models import PlpredRF, PlpredGB, PlpredSVM, PlpredNN

def train_model(file_path:str) -> PlpredGB:
    """
    Train a ML model to classify membrane proteins.
    Parameters
    ----------
    file_path: str
        Path to the preprocessed dataset.
    
    Returns
    -------
    model: RandomForestClassifier
    """
    df = pd.read_csv(file_path)
    X = df.drop(['membrane'], axis=1)
    y = df['membrane']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = PlpredGB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    report = model.validate(X_test, y_test)
    print(report)

    return model

if __name__ == "__main__":
    model = train_model(file_path='data/processed/processed.csv')
    model.save('data/models/model.pickle')
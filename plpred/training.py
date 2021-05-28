import pandas as pd 
from sklearn.model_selection import train_test_split
from plpred.models import BaseModel, PlpredRF, PlpredGB, PlpredSVM, PlpredNN
import argparse 

def train_model(file_path:str, model:BaseModel) -> BaseModel:
    """
    Train a ML model to classify membrane proteins.
    Parameters
    ----------
    file_path:str
        path to the preprocessed dataset.
    model: BaseModel
        model to be trained.
    
    Returns
    -------
    model: BaseModel
        trained model.
    report: str
        classification report of the trained model.
    """
    df = pd.read_csv(file_path)
    X = df.drop(['membrane'], axis=1)
    y = df['membrane']

    X_train, X_test, y_train, y_test  = train_test_split(X, y)

    model.fit(X_train, y_train)
    report = model.validate(X_test, y_test)

    return model, report

def main():

    models = {
        'random_forest': PlpredRF(),
        'neural_network': PlpredNN(),
        'gradient_boosting': PlpredGB(),
        'svm': PlpredSVM()
    }

    argument_parser = argparse.ArgumentParser(description='plpred-train: model training tool')
    argument_parser.add_argument('-p', '--processed_dataset', required=True, help='processed dataset generated by plpred-preprocess (.csv)')
    argument_parser.add_argument('-o', '--output', required=True, help='path to the output trained model (.pickle)')
    argument_parser.add_argument('-r', '--report', default=False, action='store_true', help='show classification report')
    argument_parser.add_argument('-a', '--algorithm', default='random_forest', choices=['random_forest', 'neural_network', 'gradient_boosting', 'svm'], help='machine learning algorithm')

    arguments = argument_parser.parse_args()

    model, report = train_model(file_path=arguments.processed_dataset, model=models[arguments.algorithm])
    model.save(arguments.output)

    if arguments.report:
        print(report)

if __name__ == "__main__":
    main()
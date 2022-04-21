from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from pandas import DataFrame

from Interfaces.IRead import ReadLabeledData


class Classification(object):
    def __init__(self):
        self.__execute()

    def __execute(self) -> None:
        self.__read_data()
        self.__split_data()
        X_train, X_test, y_train, y_test = self.__split_data()
        self.__train(
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test
        )

    @classmethod
    def __read_data(cls) -> None:
        cls.__df_labeled_data = ReadLabeledData().get_labeled_data

    def __split_into_X_y(self) -> tuple:
        y = self.__df_labeled_data["status"]
        X = self.__df_labeled_data.drop(["status"], axis=1)
        return X, y

    def __split_data(self) -> tuple:
        X, y = self.__split_into_X_y()
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            random_state=42
        )
        return X_train, X_test, y_train, y_test

    @staticmethod
    def __train(
            X_train: DataFrame,
            X_test: DataFrame,
            y_train: DataFrame,
            y_test: DataFrame
                ) -> None:
        cl: DecisionTreeClassifier = DecisionTreeClassifier()
        cl.fit(X_train, y_train)
        y_pred: list[int] = cl.predict(X_test)
        print(classification_report(y_true=y_test, y_pred=y_pred))

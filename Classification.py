from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from pandas import DataFrame

from Interfaces.IRead import ReadLabeledData


class Classification(object):
    def __init__(self):
        self.__X: DataFrame
        self.__y: DataFrame

        self.__X_train: DataFrame
        self.__y_train: DataFrame
        self.__X_test: DataFrame
        self.__y_test: DataFrame

        self.__y_pred: DataFrame

    def train_model(self) -> None:
        self.__read_labeled_data()
        self.__split_into_X_y()
        self.__split_data_into_train_test()
        self.__train()

    def make_predictions(self) -> None:
        self.__read_unlabled_data()
        self.__make_predictions()

    @classmethod
    def __read_unlabled_data(cls) -> None:
        cls.__df_labeled_data: DataFrame = ReadLabeledData().get_data

    @classmethod
    def __read_labeled_data(cls) -> None:
        cls.__df_labeled_data: DataFrame = ReadLabeledData().get_data

    def __split_into_X_y(self) -> None:
        self.__y: DataFrame = self.__df_labeled_data["status"]
        self.__X: DataFrame = self.__df_labeled_data.drop(["status"], axis=1)

    def __split_data_into_train_test(self) -> None:
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(
            self.__X, self.__y,
            random_state=42
        )

    def __train(self) -> None:
        self.__model: DecisionTreeClassifier = DecisionTreeClassifier()
        self.__model.fit(self.__X_train, self.__y_train)
        print(classification_report(
            y_true=self.__y_test,
            y_pred=self.__model.predict(self.__X_test)
        ))

    def __make_predictions(self) -> None:
        self.__y_pred: list[int] = self.__model.predict(self.__X)

    @property
    def get_pred(self) -> list[int]:
        return self.__y_pred

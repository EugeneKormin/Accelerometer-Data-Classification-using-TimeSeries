from abc import abstractmethod
from pandas import DataFrame

from Variables import PATH_TO_LABELED_DATA


class ISave(object):
    @abstractmethod
    def __save(self):
        ...


class SaveLabeledData(ISave):
    def __init__(self, df: DataFrame):
        self.__df: DataFrame = df
        self.__save()

    def __save(self) -> None:
        self.__df.to_csv(PATH_TO_LABELED_DATA)

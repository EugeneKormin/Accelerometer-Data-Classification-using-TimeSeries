from abc import abstractmethod
from pandas import DataFrame, read_csv

from Variables import PATH_TO_LABELED_DATA, PATH_TO_UNLABELED_DATA


class IRead(object):
    @abstractmethod
    def __read_data(self) -> None:
        ...

    @abstractmethod
    def get_data(self) -> DataFrame:
        return ...


class ReadLabeledData(IRead):
    def __init__(self):
        self.__read_data()

    def __read_data(self) -> None:
        self.__df = read_csv(PATH_TO_LABELED_DATA)

    @property
    def get_data(self) -> DataFrame:
        return self.__df


class ReadUnLabeledData(IRead):
    def __init__(self):
        self.__read_data()

    def __read_data(self) -> None:
        self.__df = read_csv(PATH_TO_UNLABELED_DATA)

    @property
    def get_data(self) -> DataFrame:
        return self.__df

from abc import abstractmethod

from ParseData import ParseData
from Classification import Classification


class IRun(object):
    @abstractmethod
    def __run(self):
        ...


class RunTrain(object):
    def __init__(self):
        self.__classification: Classification = Classification()
        self.__run()

    @abstractmethod
    def __run(self):
        ParseData(DATA_TYPE="LabeledData")
        self.__classification.train_model()


class RunPredict(object):
    def __init__(self):
        self.__classification: Classification = Classification()
        self.__run()

    @abstractmethod
    def __run(self):
        ParseData(DATA_TYPE="UnLabeledData")
        self.__classification.make_predictions()

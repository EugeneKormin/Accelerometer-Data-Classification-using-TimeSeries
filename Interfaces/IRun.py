from abc import abstractmethod

from ParseData import ParseData
from Classification import Classification


class IRun(object):
    @abstractmethod
    def __run(self):
        ...


class RunTrain(object):
    def __init__(self):
        self.__run()

    @classmethod
    def __run(cls):
        classification: Classification = Classification()

        ParseData(DATA_TYPE="LabeledData")
        classification.train_model()


class RunPredict(object):
    def __init__(self):
        self.__run()

    @classmethod
    def __run(cls):
        classification: Classification = Classification()

        ParseData(DATA_TYPE="UnLabeledData")
        classification.make_predictions()

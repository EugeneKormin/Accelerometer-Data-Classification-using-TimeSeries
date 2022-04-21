from pandas import DataFrame, Series

from Interfaces.ISave import SaveLabeledData, SaveUnLabeledData
from Variables import PATH_TO_RAW_TRAIN_TXT, PATH_TO_RAW_TEST_TXT


class ParseData(object):
    def __init__(self, DATA_TYPE: str):
        self.__read_txt_data(DATA_TYPE=DATA_TYPE)

        if DATA_TYPE == "LabeledData":
            self.__label_data()

        self.__save_data(DATA_TYPE=DATA_TYPE)

    @classmethod
    def __convert_txt_to_dataframe(cls, PATH: str):
        data: dict = {}

        with open(PATH) as f:
            lines: list[str] = f.readlines()

            for line in lines:
                parsed_data: list[str] = line.split(' | ')

                for index in range(len(parsed_data)):
                    KEY: str = parsed_data[index].split(' = ')[0]
                    VALUE: int or float = parsed_data[index].split(' = ')[1]

                    if KEY not in data:
                        data[KEY] = [float(VALUE)]
                    else:
                        data[KEY] += [float(VALUE)]

        cls.__df = DataFrame(data)

    def __read_txt_data(self, DATA_TYPE: str) -> None:
        PATH: str = ''

        if DATA_TYPE == "LabeledData":
            PATH: str = PATH_TO_RAW_TRAIN_TXT
        elif DATA_TYPE == "UnLabeledData":
            PATH: str = PATH_TO_RAW_TEST_TXT

        self.__convert_txt_to_dataframe(PATH=PATH)

    def __label_data(self) -> None:
        self.__df["time_mark"]: Series[float] = list(map(lambda x: x / 5, list(range(1, 423 + 1))))

        self.__df["status"]: Series[int] = 0

        self.__df.loc[self.__df["time_mark"].between(0, 20), 'status']: Series[int] = 1
        self.__df.loc[self.__df["time_mark"].between(36, 50), 'status']: Series[int] = 1

    def __save_data(self, DATA_TYPE: str):
        if DATA_TYPE == "LabeledData":
            SaveLabeledData(df=self.__df)
        elif DATA_TYPE == "UnLabeledData":
            SaveUnLabeledData(df=self.__df)

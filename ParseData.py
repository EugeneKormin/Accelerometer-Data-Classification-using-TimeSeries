from pandas import DataFrame, Series

from Interfaces.ISave import SaveLabeledData
from Variables import PATH_TO_RAW_TRAIN_TXT


class ParseData(object):
    def __init__(self):
        self.__read_txt_data()
        self.__label_data()
        self.__save_data()

    @classmethod
    def __read_txt_data(cls) -> None:
        data: dict = {}

        with open(PATH_TO_RAW_TRAIN_TXT) as f:
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

    def __label_data(self) -> None:
        self.__df["time_mark"]: Series[float] = list(map(lambda x: x / 5, list(range(1, 423 + 1))))

        self.__df["status"]: Series[int] = 0

        self.__df.loc[self.__df["time_mark"].between(0, 20), 'status']: Series[int] = 1
        self.__df.loc[self.__df["time_mark"].between(36, 50), 'status']: Series[int] = 1

    def __save_data(self):
        SaveLabeledData(df=self.__df)

from ParseData import ParseData
from Classification import Classification

from Variables import RUN_TYPE


def run():
    classification: Classification = Classification()
    if RUN_TYPE == "train":
        ParseData(DATA_TYPE="LabeledData")
        classification.train_model()
    elif RUN_TYPE == "predict":
        ParseData(DATA_TYPE="UnLabeledData")
        classification.make_predictions()


if __name__ == "__main__":
    run()

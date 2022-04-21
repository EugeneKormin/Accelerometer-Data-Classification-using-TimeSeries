from Run import RunTrain, RunPredict
from Variables import RUN_TYPE


def run():
    RunTrain() if RUN_TYPE == "train" else ...
    RunPredict() if RUN_TYPE == "predict" else ...


if __name__ == "__main__":
    run()

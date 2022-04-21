from os import getcwd

PATH_TO_RAW_TRAIN_TXT: str = getcwd() + "/data/box_placing_train.txt"
PATH_TO_RAW_TEST_TXT: str = getcwd() + "/data/box_placing_test.txt"

PATH_TO_LABELED_DATA: str = getcwd() + "/data/labeled_data.csv"
PATH_TO_UNLABELED_DATA: str = getcwd() + "/data/unlabeled_data.csv"

RUN_TYPE: str = "train"

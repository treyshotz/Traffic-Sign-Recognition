import os
import kaggle
import pandas as pd


def download_dataset():
    kaggle.api.authenticate()
    if not os.path.exists("kaggle/"):
        os.mkdir("kaggle/")
    kaggle.api.dataset_download_files(
            'meowmeowmeowmeowmeow/gtsrb-german-traffic-sign', path='kaggle/',
            unzip=True)
    print("Finished downloading dataset, extracting files")


def setup_test_dataset():
    parent_dir = "kaggle/TestWithDirs/"
    for i in range(0, 43):
        try:
            path = os.path.join(parent_dir, str(i)+"/")
            os.makedirs(path)
        except FileExistsError as e:
            pass

    print(os.listdir("kaggle/"))
    test_data = pd.read_csv("kaggle/Test.csv")
    path = test_data['Path']
    class_id = test_data['ClassId']
    for j in range(len(test_data)):
        print(f"current pos: {j}")
        print(f"path of file: {path[j]}")
        filename = path[j].replace("TestWithDirs/", "")
        print(f"class_id of file: {class_id[j]}")
        os.replace("kaggle/" +path[j], f"kaggle/TestWithDirs/{class_id[j]}/"+filename)

#download_dataset()
#setup_test_dataset()

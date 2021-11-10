import os
import kaggle

kaggle.api.authenticate()


url = "https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/download"


if not os.path.exists("kaggle/"):
    os.mkdir("kaggle/")
    kaggle.api.dataset_download_files('GTSRB', path='kaggle/', unzip=True)
    print("Finished downloading dataset, extracting files")


print("Script finished")
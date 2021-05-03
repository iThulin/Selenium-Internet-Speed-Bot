import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer


class Analyzer:
    def __init__(self):
        # Imports then structures the json into a dataframe object with the correct layout
        self.dataset_raw = pd.read_json(r"internet_speed_data.json")
        self.dataset_transposed = self.dataset_raw.transpose()
        self.dataset_ordered = self.dataset_transposed[["ping", "upload", "download"]]

    def preprocess_data(self):
        # Creates 3 datasets corresponding to the colums of our internet_speed_data.json
        ping_data = self.dataset_ordered.iloc[:, [0]]
        upload_data = self.dataset_ordered.iloc[:, [1]]
        download_data = self.dataset_ordered.iloc[:, [2]]

        # Finds missing entries in our data set and replaces them with the mean value of the dataset
        imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
        imputer.fit(ping_data[:, :])
        ping_data[:, :] = imputer.transform(ping_data[:, :])
        imputer.fit(upload_data[:, :])
        upload_data[:, :] = imputer.transform(upload_data[:, :])
        imputer.fit(download_data[:, :])
        download_data[:, :] = imputer.transform(download_data[:, :])

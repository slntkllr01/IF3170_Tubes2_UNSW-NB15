import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

basic_features = pd.read_csv('basic_features_train.csv') 
time_features = pd.read_csv('time_features_train.csv')
content_features = pd.read_csv('content_features_train.csv')
additional_features = pd.read_csv('additional_features_train.csv')
label_features = pd.read_csv('labels_train.csv')
flow_features = pd.read_csv('flow_features_train.csv')

merged_test = pd.merge(basic_features, time_features, how='left', on='id')
merged_test = pd.merge(merged_test, content_features, how='left', on='id')
merged_test = pd.merge(merged_test, additional_features, how='left', on='id')
merged_test = pd.merge(merged_test, label_features, how='left', on='id').drop("label", axis='columns')
merged_test = pd.merge(merged_test, flow_features, how='left', on='id')
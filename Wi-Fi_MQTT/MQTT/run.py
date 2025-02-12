import numpy as np
import pandas as pd
import tpot


dataset_names = ['Malformed_Data_df', 'DoS_Connect_Flood_df', 'DDoS_Connect_Flood_df', 'DoS_Publish_Flood_df', 'DDoS_Publish_Flood_df']

Malformed_Data_df = pd.read_csv('MQTT-Malformed_Data_test.pcap.csv')
DoS_Connect_Flood_df = pd.read_csv('MQTT-DoS-Connect_Flood_test.pcap.csv')
DDoS_Connect_Flood_df = pd.read_csv('MQTT-DDoS-Connect_Flood_test.pcap.csv')
DoS_Publish_Flood_df = pd.read_csv('MQTT-DoS-Publish_Flood_test.pcap.csv')
DDoS_Publish_Flood_df = pd.read_csv('MQTT-DDoS-Publish_Flood_test.pcap.csv')

print(len(Malformed_Data_df.columns))
print(len(DoS_Connect_Flood_df.columns))
print(len(DDoS_Connect_Flood_df.columns))
print(len(DoS_Publish_Flood_df.columns))
print(len(DDoS_Publish_Flood_df.columns))

print(DDoS_Publish_Flood_df.columns == DoS_Publish_Flood_df.columns)







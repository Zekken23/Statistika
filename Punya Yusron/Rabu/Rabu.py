import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

rabu_data = {
    'Pagi': {
        "Waktu": ["07:24", "07:29", "07:34", "07:39", "07:44", "07:49", "07:54", "07:59", "08:04", "08:09", "08:14", "08:19"],
        "Gojek": [2, 2, 2, 2, 2, 1, 3, 3, 2, 4, 5, 0],
        "Maxim": [0, 1, 0, 2, 2, 3, 1, 1, 2, 0, 1, 0],
        "Grab": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    },
    'Siang': {
        "Waktu": ["12:12", "12:17", "12:22", "12:27", "12:32", "12:37", "12:42", "12:47", "12:52", "12:57", "14:02", "14:07"],
        "Gojek": [1, 2, 0, 2, 1, 2, 1, 3, 1, 1, 1, 0],
        "Maxim": [0, 1, 1, 2, 0, 2, 1, 0, 2, 0, 1, 1],
        "Grab": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    },
    'Malam': {
        "Waktu": ["18:51", "18:56", "19:01", "19:06", "19:11", "19:16", "19:21", "19:26", "19:31", "19:36", "19:41", "19:46"],
        "Gojek": [2, 0, 0, 2, 1, 0, 2, 2, 3, 0, 1, 0],
        "Maxim": [0, 2, 3, 0, 0, 1, 0, 0, 1, 2, 0, 1],
        "Grab": [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
    }
}


df_list = []

for period, data in rabu_data.items():
    for provider in ['Gojek', 'Maxim', 'Grab']:
        for waktu, count in zip(data["Waktu"], data[provider]):
            df_list.append([period, waktu, provider, count])

df = pd.DataFrame(df_list, columns=['Period', 'Time', 'Provider', 'Count'])

# Pivot data for heatmap
pivot_table = df.pivot_table(index=['Period', 'Time'], columns='Provider', values='Count', aggfunc='sum', fill_value=0)

# Plot heatmap
plt.figure(figsize=(16, 12))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)
plt.title('Jumlah Pemesanan Berdasarkan Waktu dan Penyedia Layanan')
plt.show()

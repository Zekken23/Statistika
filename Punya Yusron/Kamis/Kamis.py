import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


kamis_data = {
    'Pagi': {
        "Waktu": ["07:35", "07:40", "07:45", "07:50", "07:55", "08:00", "08:05", "08:10", "08:15", "08:20", "08:25", "08:30"],
        "Gojek": [2, 1, 4, 2, 1, 3, 1, 2, 3, 2, 0, 1],
        "Maxim": [0, 3, 0, 2, 0, 0, 0, 1, 1, 2, 1, 0],
        "Grab": [0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    },
    'Siang': {
        "Waktu": ["13:33", "13:38", "13:43", "13:48", "13:53", "13:58", "14:03", "14:08", "14:13", "14:18", "14:23", "14:28"],
        "Gojek": [2, 3, 1, 1, 1, 2, 2, 2, 3, 1, 4, 0],
        "Maxim": [0, 1, 2, 3, 2, 4, 1, 2, 0, 1, 1, 0],
        "Grab": [1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0]
    },
    'Malam': {
        "Waktu": ["17:51", "17:56", "18:01", "18:06", "18:11", "18:16", "18:21", "18:26", "18:31", "18:36", "18:41", "18:46"],
        "Gojek": [3, 2, 1, 2, 1, 0, 2, 1, 3, 2, 4, 0],
        "Maxim": [2, 3, 1, 3, 0, 2, 0, 1, 2, 1, 0, 0],
        "Grab": [0, 0, 2, 0, 2, 0, 1, 0, 0, 2, 1, 1]
    }
}


df_list = []

for period, data in kamis_data.items():
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

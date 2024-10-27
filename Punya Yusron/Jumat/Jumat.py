import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


jumat_data = {
    'Pagi': {
        "Waktu": ["08:11", "08:16", "08:21", "08:26", "08:31", "08:36", "08:41", "08:46", "08:51", "08:56", "09:01", "09:06"],
        "Gojek": [1, 2, 2, 1, 3, 1, 1, 3, 3, 2, 1, 0],
        "Maxim": [0, 2, 3, 2, 4, 2, 1, 2, 1, 2, 0, 0],
        "Grab": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    'Siang': {
        "Waktu": ["11:08", "11:13", "11:18", "11:23", "11:28", "11:33", "11:38", "11:43", "11:48", "11:53", "11:58", "12:03"],
        "Gojek": [0, 2, 2, 4, 1, 4, 2, 3, 2, 1, 0, 1],
        "Maxim": [2, 1, 2, 0, 2, 2, 2, 4, 2, 2, 0, 0],
        "Grab": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0]
    },
    'Malam': {
        "Waktu": ["17:02", "17:07", "17:12", "17:17", "17:22", "17:27", "17:32", "17:37", "17:42", "17:47", "17:52", "17:57"],
        "Gojek": [0, 2, 1, 2, 3, 2, 1, 4, 2, 2, 2, 0],
        "Maxim": [2, 1, 3, 2, 1, 0, 2, 0, 1, 2, 0, 2],
        "Grab": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    }
}

df_list = []

for period, data in jumat_data.items():
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

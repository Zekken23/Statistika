import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

selasa_data = {
    'Pagi': {
        "Waktu": ["08:05", "08:10", "08:15", "08:20", "08:25", "08:30", "08:35", "08:40", "08:45", "08:50", "08:55", "09:00"],
        "Gojek": [4, 3, 5, 2, 3, 3, 1, 2, 3, 3, 2, 1],
        "Maxim": [0, 0, 2, 3, 1, 4, 1, 0, 0, 0, 4, 1],
        "Grab": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    'Siang': {
        "Waktu": ["13:07", "13:12", "13:17", "13:22", "13:27", "13:32", "13:37", "13:42", "13:47", "13:52", "13:57", "14:02"],
        "Gojek": [3, 1, 0, 2, 1, 2, 3, 2, 1, 1, 0, 4],
        "Maxim": [2, 0, 2, 1, 2, 0, 0, 0, 4, 1, 3, 0],
        "Grab": [0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1]
    },
    'Malam': {
        "Waktu": ["17:00", "17:05", "17:10", "17:15", "17:20", "17:25", "17:30", "17:35", "17:40", "17:45", "17:50", "17:55"],
        "Gojek": [0, 2, 0, 1, 3, 0, 2, 0, 3, 1, 2, 0],
        "Maxim": [0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1],
        "Grab": [3, 0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0]
    }
}

df_list = []

for period, data in selasa_data.items():
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

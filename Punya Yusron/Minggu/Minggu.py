import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
minggu_data = {
    'Pagi': {
        "Waktu": ["07:47", "07:52", "07:57", "08:02", "08:07", "08:12", "08:17", "08:22", "08:27", "08:32", "08:37", "08:42"],
        "Gojek": [1, 4, 2, 0, 2, 3, 4, 0, 1, 0, 1, 1],
        "Maxim": [2, 0, 1, 3, 0, 2, 3, 5, 1, 0, 1, 0],
        "Grab": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    },
    'Siang': {
        "Waktu": ["13:33", "13:38", "13:43", "13:48", "13:53", "13:58", "14:03", "14:08", "14:13", "14:18", "14:23", "14:28"],
        "Gojek": [2, 2, 2, 0, 4, 2, 3, 0, 3, 0, 1, 0],
        "Maxim": [2, 0, 0, 3, 1, 0, 0, 3, 0, 3, 0, 0],
        "Grab": [0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    },
    'Malam': {
        "Waktu": ["18:11", "18:16", "18:21", "18:26", "18:31", "18:36", "18:41", "18:46", "18:51", "18:56", "19:01", "19:06"],
        "Gojek": [0, 3, 0, 3, 0, 2, 1, 4, 2, 0, 2, 0],
        "Maxim": [1, 0, 2, 1, 2, 0, 1, 0, 0, 2, 0, 0],
        "Grab": [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0]
    }
}

# Convert data to DataFrame
df_list = []

for period, data in minggu_data.items():
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

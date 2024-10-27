import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

senin_data = {
    'Pagi': {
        "Waktu": ["07:48", "07:53", "07:58", "08:03", "08:08", "08:13", "08:18", "08:23", "08:28", "08:33", "08:38", "08:43"],
        "Gojek": [0, 1, 0, 2, 1, 4, 1, 4, 2, 1, 2, 1],
        "Maxim": [1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 3, 2],
        "Grab": [0, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 4]
    },
    'Siang': {
        "Waktu": ["13:13", "13:18", "13:23", "13:28", "13:33", "13:38", "13:43", "13:48", "13:53", "13:58", "14:03", "14:08"],
        "Gojek": [4, 2, 2, 0, 1, 2, 0, 2, 1, 2, 0, 2],
        "Maxim": [0, 3, 4, 2, 2, 1, 4, 0, 0, 0, 1, 0],
        "Grab": [0, 2, 0, 0, 0, 3, 2, 0, 1, 0, 0, 2]
    },
    'Malam': {
        "Waktu": ["17:21", "17:26", "18:31", "18:36", "18:41", "18:46", "18:51", "18:56", "19:01", "19:06", "19:11", "19:16"],
        "Gojek": [2, 1, 2, 0, 1, 0, 2, 1, 0, 2, 1, 0],
        "Maxim": [1, 2, 0, 2, 0, 3, 1, 3, 0, 0, 2, 0],
        "Grab": [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    }
}

df_list = []

for period, data in senin_data.items():
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

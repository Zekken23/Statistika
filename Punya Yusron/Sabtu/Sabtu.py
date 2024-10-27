import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


sabtu_data = {
    'Pagi': {
        "Waktu": ["06:43", "06:48", "06:53", "06:58", "07:03", "07:08", "07:13", "07:18", "07:23", "07:28", "07:33", "07:38"],
        "Gojek": [1, 3, 1, 2, 3, 0, 0, 1, 0, 1, 2, 0],
        "Maxim": [1, 0, 0, 0, 2, 3, 0, 0, 1, 2, 1, 0],
        "Grab": [0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0]
    },
    'Siang': {
        "Waktu": ["13:32", "13:37", "13:42", "13:47", "13:52", "13:57", "14:02", "14:07", "14:12", "14:17", "14:22", "14:27"],
        "Gojek": [0, 1, 0, 2, 1, 4, 1, 4, 2, 1, 0, 0],
        "Maxim": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        "Grab": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    'Malam': {
        "Waktu": ["17:12", "17:17", "17:22", "17:27", "17:32", "17:37", "17:42", "17:47", "17:52", "17:57", "18:02", "18:07"],
        "Gojek": [0, 2, 1, 4, 1, 0, 1, 1, 1, 0, 2, 0],
        "Maxim": [1, 0, 0, 0, 0, 0, 1, 0, 3, 1, 0, 0],
        "Grab": [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0]
    }
}


df_list = []

for period, data in sabtu_data.items():
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

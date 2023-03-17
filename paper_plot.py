import matplotlib.pyplot as plt
import numpy as np

# Data
paths = [
        "no_recovery_usage",
        "reexecute_usage",
        "unutil_usage",
        "util_usage"
        ]
colors = [
         "black",
         "orange",
         "red",
         "blue"
         ]
markers = [
         "o",
         "o",
         "*",
         "o"
         ]

bound = 30
timestamp = 0
timestep = 0.5

# Plot
marker_size = 5
fig_x = 10
fig_y = 5
font_size = 24
x_label = "Time (secs)"
y_label = "CPU usage (%)"
y_min = 0
y_max = 100
fig_name = "cpu_usage_data.png"

data_list = []
idx_list = []
timestamps = []

profile_data = {}

for path in paths:
  datas = open("../" + path + ".txt")
  for line in datas.readlines():
    # print(line[11:-55])
    data = line[11:-55]

    data_list.append(float(data))
    idx_list.append(float(timestamp))
    timestamp += timestep

    if timestamp == bound:
      profile_data[path] = data_list.copy()
      if not timestamps:
        timestamps = idx_list.copy()
      idx_list.clear()
      data_list.clear()
      timestamp = 0
      break

plt.figure(figsize=(fig_x, fig_y))
plt.xlabel(x_label, fontsize=font_size)
plt.ylabel(y_label, fontsize=font_size)
plt.ylim(y_min, y_max)

for key, value, mark, col in zip(profile_data.keys(), profile_data.values(), markers, colors):
# for key, value, col in profile_data.items():
  # random color
  # col = (np.random.random(), np.random.random(), np.random.random())
  plt.plot(timestamps, value, marker=mark, markersize=marker_size, color=col, label=key)

plt.legend()
plt.tight_layout()
plt.savefig(fig_name)
plt.show()

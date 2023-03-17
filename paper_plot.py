import matplotlib.pyplot as plt
import numpy as np

paths = [
        "normal_usage",
        "reexecute_usage",
        "util_usage",
        "unutil_usage",
        "replica_no_util_usage",
        "replica_yes_util_usage"
        ]

data_list = []
idx = float(0.5)
idx_list = []
datas = open("../" + paths[5] + ".txt")
for line in datas.readlines():
  print(line[11:-55])
  data = line[11:-55]
  data_list.append(float(data))
  idx_list.append(float(idx))
  idx += 0.5
  if idx == 30:
    break
plt.figure(figsize=(10, 5))
plt.xlabel('Time (secs)', fontsize=24)
plt.ylabel('CPU usage (%)', fontsize=24)
plt.ylim(0, 100)

plt.plot(idx_list, data_list, color = "red")
# plt.plot(np.array(idx_list), np.array(data_list), color = "red")
# plt.legend()
plt.tight_layout()
plt.show()

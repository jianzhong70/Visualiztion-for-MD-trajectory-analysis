import matplotlib.pyplot as plt
import numpy as np


file_paths = ['D:/cjzdat/3CLP/catdat/7vu6-145-306.dat',  'D:/cjzdat/3CLP/catdat/7vth-145-306.dat', 
              'D:/cjzdat/3CLP/catdat/7lmf-145-306.dat']
labels = ['C145:N-7YY:09O', 'C145:N-7XB:08O', 'C145:N-Y6G:08O']
#colors = ['blue', 'orange', 'green', 'red']

all_data = []
for file_path in file_paths:
    data = np.loadtxt(file_path)
    all_data.append(data)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
i = 0
for data in all_data:
    x = 0.004*data[:, 0]
    y = data[:, 1]
    #plt.plot(x, y, label=labels[i], color=colors[i])
    ax.plot(x, y, label=labels[i])
    i = i + 1

ax.axis([0, 3000, 0, 23])

ax.set_xlabel('Simulation times(ns)', fontweight='bold',fontsize=18)
ax.set_ylabel('C145-inhibitor distance(Å)',fontweight='bold', fontsize=18)

save_path='D:/cjzdat/3CLP/pyfigure/C145-lig-distance.png'
show_grid=True

#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(14)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(14)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)
# 设置图例的字体大小和粗体
for text in legend.get_texts():
    text.set_fontsize(13)  # 设置字体大小
    text.set_fontweight('bold')  # 设置字体粗体

for line in legend.get_lines():
    line.set_linewidth(3)  # 设置图例线条的粗细

#for residue in residue_lst:
    #plt.axvline(x=residue, color='black', linestyle='--', dashes=(5, 2))

plt.grid(show_grid)
plt.savefig(save_path, dpi=600, bbox_inches='tight')
#plt.ion()
#plt.pause(300)
plt.show()
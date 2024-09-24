import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file_paths = ['D:/cjzdat/3CLP/3pcl-python/rmsd/apo-rmsf.dat',  'D:/cjzdat/3CLP/3pcl-python/rmsd/7vu6-rmsf.dat', 
              'D:/cjzdat/3CLP/3pcl-python/rmsd/7vth-rmsf.dat', 'D:/cjzdat/3CLP/3pcl-python/rmsd/7lmf-rmsf.dat']


labels = ['APO', '7YY', '7XB', 'Y6G']

xlabel='Residue Sequence'
ylabel='RMSF(Å)'
offset=0


save_path = 'rmsf.png'

show_grid=True


all_data = []

for file_path in file_paths:
    data = np.loadtxt(file_path) # np.loadtxt 函数默认会忽略以 # 字符开头的行，将其视为注释行，并且不会加载这些行作为数据。
    all_data.append(data)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
i = 0
for data in all_data:
    x = data[:, 0]
    y = data[:, 1]
    #plt.plot(x, y, label=labels[i], color=colors[i])
    ax.plot(x + offset, y, label=labels[i])
    i = i + 1

ax.set_xlabel(xlabel, fontweight='bold', fontsize=18)
ax.set_ylabel(ylabel, fontweight='bold', fontsize=18)
ax.axis([0, 305, 0, 10])
plt.xticks(fontweight='bold', fontsize=16)
plt.yticks(fontweight='bold', fontsize=16)





#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(13)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(13)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
plt.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), framealpha=0.5)
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
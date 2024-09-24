import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Neglecting the
file_paths = ['D:/cjzdat/3CLP/3pcl-python/rmsd/7vu6-rmsd-lig.dat',  'D:/cjzdat/3CLP/3pcl-python/rmsd/7vth-rmsd-lig.dat', 
              'D:/cjzdat/3CLP/3pcl-python/rmsd/7lmf-rmsd-lig.dat']
labels = ['7YY', '7XB', 'Y6G']
#colors = ['blue', 'orange', 'green', 'red']

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

all_data = []
category_lst = []
i = 0
for file_path in file_paths:
    data = np.loadtxt(file_path)  # np.loadtxt 函数默认会忽略以 # 字符开头的行，将其视为注释行，并且不会加载这些行作为数据。
    for row in data:
        all_data.append(row[1])
        category_lst.append(labels[i])
    i = i + 1


df = pd.DataFrame({
    'value': np.array(all_data),
    'category': category_lst
})

#ax.boxplot(all_data)
sns.violinplot(x="category", y="value", data=df)


#ax.axis([0, 3000, 0, 20])

ax.set_xlabel('Simulation times(ns)', fontweight='bold',fontsize=18)
ax.set_ylabel('RMSDs of inhibitors(Å)',fontweight='bold', fontsize=18)

save_path='D:/cjzdat/3CLP/pyfigure/rmsd-lig-violet.png'
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
#legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)
# 设置图例的字体大小和粗体
#for text in legend.get_texts():
#    text.set_fontsize(13)  # 设置字体大小
#    text.set_fontweight('bold')  # 设置字体粗体

#for line in legend.get_lines():
#    line.set_linewidth(3)  # 设置图例线条的粗细

#for residue in residue_lst:
    #plt.axvline(x=residue, color='black', linestyle='--', dashes=(5, 2))

plt.grid(show_grid)
plt.savefig(save_path, dpi=600, bbox_inches='tight')
#plt.ion()
#plt.pause(300)
plt.show()
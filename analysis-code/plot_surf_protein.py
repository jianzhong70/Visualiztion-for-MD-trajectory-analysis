import matplotlib.pyplot as plt
import numpy as np


file_paths = ['D:/cjzdat/3CLP/3pcl-python/rmsd/apo-surf.dat','D:/cjzdat/3CLP/3pcl-python/rmsd/7vu6-surf.dat',  
              'D:/cjzdat/3CLP/3pcl-python/rmsd/7vth-surf.dat', 'D:/cjzdat/3CLP/3pcl-python/rmsd/7lmf-surf.dat']
labels = ['APO','7YY', '7XB', 'Y6G']
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

ax.axis([0, 3000, 12500, 17500])

ax.set_xlabel('Simulation times(ns)', fontweight='bold',fontsize=18)
ax.set_ylabel('Surface($\mathring{A}^2$)',fontweight='bold', fontsize=18)

save_path='D:/cjzdat/3CLP/pyfigure/surf-protein.png'
show_grid=True


for label in ax.get_xticklabels():
    label.set_fontsize(14)  
    label.set_fontweight('bold')  

for label in ax.get_yticklabels():
    label.set_fontsize(14) 
    label.set_fontweight('bold')  


legend = ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0), framealpha=0.5)

for text in legend.get_texts():
    text.set_fontsize(13) 
    text.set_fontweight('bold')  

for line in legend.get_lines():
    line.set_linewidth(3)  

plt.grid(show_grid)
plt.savefig(save_path, dpi=600, bbox_inches='tight')
plt.show()
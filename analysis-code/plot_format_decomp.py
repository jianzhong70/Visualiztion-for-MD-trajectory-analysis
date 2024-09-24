import csv
import matplotlib.pyplot as plt
import numpy as np
# 打开文件
filename='D:/cjzdat/3CLP/decomp/7lmf-decomp.dat'
#全部统计表格
output_all_file='D:/cjzdat/3CLP/decomp/7lmf_all.dat'
#重要残基统计表格
output_key_file='D:/cjzdat/3CLP/decomp/7lmf_key.dat'

offset = 0
threshold=-0.8

png_save_path='D:/cjzdat/3CLP/decomp/7lmf_decomp.png'
max_residue=305 #最大残基号，画的最大残基号
xlabel='Residue sequence'
ylabel='Energy contributions(kcal/mol)'

residue_list=[]

#markers = ['o', 's', '^', 'D', '*', 'P', 'X', 'H', '+', 'x', '|', '_']
#labels=['19','27','98','101','103','107','152','163','41']


head=['#Number','S_vdw','B_vdw','T_vdw','S_ele', 'B_ele','T_ele','S_gb','B_gb','T_gb','Total']
flag_begin = False
flag_total = False
flag_sidechain = False
flag_backbone = False

cnt_total = 0
cnt_sidechain = 0
cnt_backbone = 0
total_line=[]
sidechain_line=[]
backbone_line = []
with open(filename, 'r') as file:
    # 创建 csv.reader 对象
    reader = csv.reader(file)

    # 读取数据行并打印
    for row in reader:
        for element in row:
            if 'DELTAS' in element:
                # 如果包含目标单词，则打印当前行
                flag_begin = True
                break
            if flag_begin and ('Total' in element):
                flag_total = True
                break
            if flag_begin and ('Sidechain' in element):
                flag_sidechain = True
                break
            if flag_begin and ('Backbone' in element):
                flag_backbone = True
                break
        if flag_begin and flag_total:
            cnt_total = cnt_total + 1
        if flag_begin and flag_sidechain:
            cnt_sidechain = cnt_sidechain + 1
        if flag_begin and flag_backbone:
            cnt_backbone = cnt_backbone + 1

        if cnt_total >= 4 and len(row) > 1 and cnt_sidechain == 0:
            line = [row[0], round((float)(row[5]), 2), round((float)(row[8]), 2), round((float)(row[11]), 2), round((float)(row[17]), 2)]
            #print(line)
            total_line += [line]
        if cnt_sidechain >= 4 and len(row) > 1 and cnt_backbone == 0:
            line = [row[0], round((float)(row[5]), 2), round((float)(row[8]), 2), round((float)(row[11]), 2)]
            #print(line)
            sidechain_line += [line]
        if cnt_backbone >= 4 and len(row)>1:
            line = [row[0], round((float)(row[5]), 2), round((float)(row[8]), 2), round((float)(row[11]), 2)]
            #print(line)
            backbone_line += [line]
    #print(sidechain_line)

with open(output_all_file, 'w') as file:
    # 遍历数据，逐行写入文件
    line = f"{head[0]:<{10}} {head[1]:<{10}} {head[2]:<{10}} {head[3]:<{10}} {head[4]:<{10}} {head[5]:<{10}} {head[6]:<{10}} {head[7]:<{10}} {head[8]:<{10}} {head[9]:<{10}} {head[10]:<{10}} \n"
    file.write(line)
    for i in range(len(total_line)):
        row_total = total_line[i]
        row_sidechain = sidechain_line[i]
        row_backbone =backbone_line[i]
        residue_name = row_sidechain[0].split()[0]
        residue_number = row_sidechain[0].split()[1]
        residue_number = (int)(residue_number) + offset
        line = f"{residue_number:<{10}} {row_sidechain[1]:<{10}} {row_backbone[1]:<{10}} {row_total[1]:<{10}} {row_sidechain[2]:<{10}} {row_backbone[2]:<{10}} {row_total[2]:<{10}} {row_sidechain[3]:<{10}} {row_backbone[3]:<{10}}  {row_total[3]:<{10}} {row_total[4]:<{10}}  \n"
        file.write(line)

        if (float)(row_total[4]) <= threshold:
            print(residue_name, residue_number,row_total[4])
            residue_list.append(residue_number)

with open(output_key_file, 'w') as file:
    # 遍历数据，逐行写入文件
    line = f"{head[0]:<{10}} {head[1]:<{10}} {head[2]:<{10}} {head[3]:<{10}} {head[4]:<{10}} {head[5]:<{10}} {head[6]:<{10}} {head[7]:<{10}} {head[8]:<{10}} {head[9]:<{10}} {head[10]:<{10}} \n"
    file.write(line)
    for i in range(len(total_line)):
        row_total = total_line[i]
        row_sidechain = sidechain_line[i]
        row_backbone = backbone_line[i]
        residue_name = row_sidechain[0].split()[0]
        residue_number = row_sidechain[0].split()[1]
        residue_number = (int)(residue_number) + offset
        for residue in residue_list:
                if (int)(residue) == residue_number:
                    line = f"{residue_number:<{10}} {row_sidechain[1]:<{10}} {row_backbone[1]:<{10}} {row_total[1]:<{10}} {row_sidechain[2]:<{10}} {row_backbone[2]:<{10}} {row_total[2]:<{10}} {row_sidechain[3]:<{10}} {row_backbone[3]:<{10}}  {row_total[3]:<{10}} {row_total[4]:<{10}}  \n"
                    file.write(line)

data = np.loadtxt(output_all_file) # np.loadtxt 函数默认会忽略以 # 字符开头的行，将其视为注释行，并且不会加载这些行作为数据。

x_values = data[:, 0]
y_values = data[:, 10]

i = 0
for x, y in zip(x_values, y_values):
    if x > max_residue:
        break
    if y > 0:
        plt.vlines(x, ymin=0, ymax=y, color='black', linewidth=2)
    else:
        plt.vlines(x, ymin=y, ymax=0, color='black', linewidth=2)
    #if y <= threshold:
       # plt.scatter(x, y, marker=markers[i], color='black', label=labels[i])
       # i = i + 1

plt.axhline(y=0,color='black')
plt.axhline(y=threshold, linestyle='--',color='black')

plt.xlabel(xlabel, fontweight='bold', fontsize=18)
plt.ylabel(ylabel, fontweight='bold', fontsize=14)


ax = plt.gca()

# 设置 x 轴刻度字体大小和粗体
for label in ax.get_xticklabels():
    label.set_fontsize(12)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

# 设置 y 轴刻度字体大小和粗体
for label in ax.get_yticklabels():
    label.set_fontsize(12)  # 设置字体大小
    label.set_fontweight('bold')  # 设置字体粗体

#plt.title('')
#plt.legend()
#legend = plt.legend()

# 设置图例的字体大小和粗体
#for text in legend.get_texts():
    #text.set_fontsize(12)  # 设置字体大小
    #text.set_fontweight('bold')  # 设置字体粗体

#for line in legend.get_lines():
    #line.set_linewidth(3)  # 设置图例线条的粗细

plt.savefig(png_save_path, dpi=600, bbox_inches='tight')
plt.show()
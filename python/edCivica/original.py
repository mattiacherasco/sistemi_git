import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
scuola = []
gioco = []
temp=[]
giacca=[]
data_file = open("nomeFile.csv")
data_reader = csv.reader(data_file, delimiter=',')
#next(data_reader)
for row in data_reader:
    mesi_n.append(row[0])
    temp.append(float(row[2]))
    giacca.append(float(row[3]))
    scuola.append(float(row[4]))
    gioco.append(float(row[5]))
    
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(4,10))
fig.suptitle('grafi con correlazione e causalita')

ax1.plot(mesi_n, temp, 'red')
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperatura[C]')
ax1.grid()

ax2.plot(mesi_n, giacca, 'green')
ax2.set_xlabel('Mese')
ax2.set_ylabel('giacca')
ax2.grid()

ax3.plot(mesi_n, scuola, 'blue')
ax3.set_xlabel('Mese')
ax3.set_ylabel('scuola')
ax3.grid()

ax4.plot(mesi_n, gioco, 'yellow')
ax4.set_xlabel('Mese')
ax4.set_ylabel('gioco')
ax4.grid()

plt.show()
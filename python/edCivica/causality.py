import matplotlib.pyplot as plt
import csv

startTemp = 5.4  # temp media febbraio 2000
startCo2 = 25.5  # CO2 media febbraio 2000
temp = []
Co2 = []
year = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# Lettura dei dati dalla CSV per la temperatura
with open("./temp.csv") as temp_file:
    data_reader = csv.reader(temp_file)
    next(data_reader)
    for i, row in enumerate(data_reader):
        if i >= len(year):
            break
        startTemp += float(row[0])
        temp.append(startTemp)
        startTemp -= float(row[0])

# Lettura dei dati dalla CSV per il CO2
with open("./Co2.csv") as Co2_file:
    data_reader = csv.reader(Co2_file)
    next(data_reader)
    for i, row in enumerate(data_reader):
        if i >= len(year):
            break
        startCo2 += float(row[0])
        Co2.append(startCo2)
        startCo2 -= float(row[0])

fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot della temperatura
ax1.plot(range(1, len(temp) + 1), temp, 'red', label='Temperatura')
ax1.set_xticks(range(1, len(temp) + 1))
ax1.set_xticklabels(year[:len(temp)], rotation=45)
ax1.set_xlabel('Each february')
ax1.set_ylabel('Temp [°C]')
ax1.grid()

# Creazione di un secondo asse y per il CO2
ax2 = ax1.twinx()
ax2.plot(range(1, len(Co2) + 1), Co2, 'blue', label='CO2')
ax2.set_ylabel('CO2 [ppm]')

# Gestione della legenda
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.tight_layout()
plt.show()

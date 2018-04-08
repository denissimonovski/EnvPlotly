#!/usr/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib import style
from datetime import datetime, date
import csv

ss1 = 'SS1\n'
ss24 = '24x7\n'
humidity = 'Humidity\n'
plafon = 'Plafon\n'
start_date = date(2017, 10, 23)
end_date = date(2017, 10, 29)
envlozi = ['envlog.csv', 'envlog(1).csv']


def first():
    with open('data_log.txt') as f1:
        lines = f1.readlines()
        for i, line in enumerate(lines):
            moj_datum = datetime.strptime(str(line[:10]), '%d-%m-%Y')
            if start_date <= moj_datum.date() <= end_date:
                stringce = line[:10] + '-' + line[11:13] + '-' + line[14:16] + '-' + line[17:19] + ','
                if line.endswith(ss1):
                    with open('ss1.txt', 'a') as nov:
                        nov.write(stringce + line[32:36] + '\n')
                if line.endswith(ss24):
                    with open('ss24.txt', 'a') as nov:
                        nov.write(stringce + line[32:36] + '\n')
                if line.endswith(humidity):
                    with open('humidity.txt', 'a') as nov:
                        nov.write(stringce + line[29:33] + '\n')
                if line.endswith(plafon):
                    with open('plafon.txt', 'a') as nov:
                        nov.write(stringce + line[29:33] + '\n')
    for i in range(2):
        with open(envlozi[i]) as csvfile:
            csvfile.__next__()
            if i == 0:
                readCSV = csv.reader(csvfile, delimiter=',')
                temp = 'tempss2.txt'
                hum = 'vlagass2.txt'
            if i == 1:
                readCSV = csv.reader(csvfile, delimiter='\t')
                temp = 'tempohrid.txt'
                hum = 'vlagaohrid.txt'
            for row in readCSV:
                moj_datum = datetime.strptime(str(row[0]), '%m/%d/%Y')
                with open(temp, 'a') as f2:
                    if start_date <= moj_datum.date() <= end_date:
                        newrow = str(row)
                        f2.write(newrow[2:4] + '-' + newrow[5:7] + '-' + newrow[8:12] + '-' + newrow[16:18]
                                 + '-' + newrow[19:21] + '-' + newrow[22:24] + ',' + newrow[28:30] + '\n')
                with open(hum, 'a') as f3:
                    if start_date <= moj_datum.date() <= end_date:
                        newrow = str(row)
                        f3.write(newrow[2:4] + '-' + newrow[5:7] + '-' + newrow[8:12] + '-' + newrow[16:18]
                                 + '-' + newrow[19:21] + '-' + newrow[22:24] + ',' + newrow[34:36] + '\n')


style.use('bmh')


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def figure():
    fig = plt.figure()
    ax1 = plt.subplot2grid((8, 1), (0, 0), rowspan=2, colspan=1)
    plt.title('Temperatura Report nedela')
    plt.ylabel('Temperatura SS1')
    ax2 = plt.subplot2grid((8, 1), (2, 0), rowspan=2, colspan=1)
    plt.ylabel('Temperatura SS24x7')
    ax3 = plt.subplot2grid((8, 1), (4, 0), rowspan=2, colspan=1)
    plt.ylabel('Temperatura SS2')
    ax4 = plt.subplot2grid((8, 1), (6, 0), rowspan=2, colspan=1)
    plt.ylabel('Temperatura Ohrid')
    files = ['ss1.txt', 'ss24.txt', 'tempss2.txt', 'tempohrid.txt']
    datumi = ['%d-%m-%Y-%H-%M-%S', '%d-%m-%Y-%H-%M-%S', '%m-%d-%Y-%H-%M-%S', '%m-%d-%Y-%H-%M-%S']
    axovi = [ax1, ax2, ax3, ax4]
    for z in range(4):
        x, y = np.loadtxt(files[z], delimiter=',', unpack=True, converters={0: bytespdate2num(datumi[z])})
        axovi[z].plot_date(x, y, '-')
        for label in axovi[z].xaxis.get_ticklabels():
            label.set_rotation(0)
        axovi[z].grid(True, color='g', linestyle='dotted')

    plt.xlabel('Saati')
    plt.legend()
    plt.subplots_adjust(left=0.04, bottom=0.05, right=0.99, top=0.97, wspace=0.2, hspace=0.25)

    fig2 = plt.figure()
    ax5 = plt.subplot2grid((8, 1), (0, 0), rowspan=2, colspan=1)
    plt.title('Vlaznost Report nedela')
    plt.ylabel('Vlaznost SS1')
    ax6 = plt.subplot2grid((8, 1), (2, 0), rowspan=2, colspan=1)
    plt.ylabel('Vlaznost SS24x7')
    ax7 = plt.subplot2grid((8, 1), (4, 0), rowspan=2, colspan=1)
    plt.ylabel('Vlaznost SS2')
    ax8 = plt.subplot2grid((8, 1), (6, 0), rowspan=2, colspan=1)
    plt.ylabel('Vlaznost Ohrid')
    files = ['humidity.txt', 'plafon.txt', 'vlagass2.txt', 'vlagaohrid.txt']
    axovi = [ax5, ax6, ax7, ax8]
    for z in range(4):
        x, y = np.loadtxt(files[z], delimiter=',', unpack=True, converters={0: bytespdate2num(datumi[z])})
        axovi[z].plot_date(x, y, '-')
        for label in axovi[z].xaxis.get_ticklabels():
            label.set_rotation(0)
        axovi[z].grid(True, color='g', linestyle='dotted')

    plt.xlabel('Saati')
    plt.legend()
    plt.subplots_adjust(left=0.04, bottom=0.05, right=0.99, top=0.97, wspace=0.2, hspace=0.25)

first()
figure()

print(plt.style.available)
plt.show()

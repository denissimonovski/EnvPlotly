from datetime import datetime, date
import plotly as py
import plotly.graph_objs as go
import pandas as pd
import csv


def get_time_stamp(datum, vreme):
    stapka = datetime.strptime(datum + " " + vreme, "%m/%d/%Y %H:%M:%S")
    return stapka


def fajlovi():
    ss1 = 'SS1\n'
    ss24 = '24x7\n'
    humidity = 'Humidity\n'
    plafon = 'Plafon\n'
    start_date = date(2018, 4, 2)
    end_date = date(2018, 4, 8)
    envlozi = ['envlog.csv', 'envlog(1).csv']

    with open("data_log.txt") as fajl:
        lines = fajl.readlines()
        ss1_prv = "Date,TempSS1\n"
        ss24_prv = "Date,TempSS24\n"
        hum_prv = "Date,Humidity\n"
        pla_prv = "Date,Plafon\n"
        a, b, c, d = 0, 0, 0, 0
        for i, line in enumerate(lines):
            moj_datum = datetime.strptime(str(line[:10]), '%d-%m-%Y')
            if start_date <= moj_datum.date() <= end_date:
                stringce = line[6:10] + '-' \
                           + line[3:5] + '-' \
                           + line[:2] + ' ' \
                           + line[11:19] + ','
                if line.endswith(ss1):
                    with open('ss1.csv', 'a') as nov:
                        if a == 0:
                            nov.write(ss1_prv)
                            nov.write(stringce + line[32:36] + '\n')
                            a += 1
                        else:
                            nov.write(stringce + line[32:36] + '\n')
                if line.endswith(ss24):
                    with open('ss24.csv', 'a') as nov:
                        if b == 0:
                            nov.write(ss24_prv)
                            nov.write(stringce + line[32:36] + '\n')
                            b += 1
                        else:
                            nov.write(stringce + line[32:36] + '\n')
                if line.endswith(humidity):
                    with open('humidity.csv', 'a') as nov:
                        if c == 0:
                            nov.write(hum_prv)
                            nov.write(stringce + line[29:33] + '\n')
                            c += 1
                        else:
                            nov.write(stringce + line[29:33] + '\n')
                if line.endswith(plafon):
                    with open('plafon.csv', 'a') as nov:
                        if d == 0:
                            nov.write(pla_prv)
                            nov.write(stringce + line[29:33] + '\n')
                            d += 1
                        else:
                            nov.write(stringce + line[29:33] + '\n')

    for i in range(2):
        with open(envlozi[i]) as csvfile:
            csvfile.__next__()
            if i == 0:
                readCSV = csv.reader(csvfile, delimiter=',')
                fajl = 'novss2.csv'
                with open(fajl, "w") as f:
                    f.write("Date,Temperature,Humidity\n")
            if i == 1:
                readCSV = csv.reader(csvfile, delimiter='\t')
                fajl = 'novoh.csv'
                with open(fajl, "w") as f:
                    f.write("Date,Temperature,Humidity\n")
            for row in readCSV:
                moj_datum = datetime.strptime(str(row[0]), '%m/%d/%Y')
                with open(fajl, 'a') as f2:
                    if start_date <= moj_datum.date() <= end_date:
                        mesec, den, godina = row[0].split("/")
                        f2.write(godina + "-"
                                 + mesec + '-'
                                 + den + ' '
                                 + row[1] + ','
                                 + row[2] + ','
                                 + row[3] + '\n')


def iscrtaj():
    df1 = pd.read_csv("ss1.csv")
    trace1 = go.Scatter(x=df1.Date,
                        y=df1['TempSS1'],
                        name="Temperatura SS1",
                        line=dict(
                            color="red",
                            width=3,
                            dash='line'
                        ),
                        yaxis=dict(
                            title="Temperatura SS1"
                        )
                        )
    df2 = pd.read_csv("ss24.csv")
    trace2 = go.Scatter(x=df2.Date,
                        y=df2['TempSS24'],
                        name="Temperature SS24",
                        line=dict(
                            color="blue",
                            width=3,
                            dash='line'
                        )
                        )
    df3 = pd.read_csv("novss2.csv")
    trace3 = go.Scatter(x=df3.Date,
                        y=df3['Temperature'],
                        name="Temperature SS2",
                        line=dict(
                            color="orange",
                            width=3,
                            dash='line'
                        )
                        )
    df4 = pd.read_csv("novoh.csv")
    trace4 = go.Scatter(x=df4.Date,
                        y=df4['Temperature'],
                        name="Temperature OH",
                        line=dict(
                            color="purple",
                            width=3,
                            dash='line'
                        ))
    df5 = pd.read_csv("humidity.csv")
    trace5 = go.Scatter(x=df5.Date,
                        y=df5['Humidity'],
                        name="Vlaznost SS1",
                        line=dict(
                            color="red",
                            width=3,
                            dash='line'
                        ))
    df6 = pd.read_csv("plafon.csv")
    trace6 = go.Scatter(x=df6.Date,
                        y=df6['Plafon'],
                        name="Vlaznost SS24",
                        line=dict(
                            color="blue",
                            width=3,
                            dash='line'
                        ))
    trace7 = go.Scatter(x=df3.Date,
                        y=df3['Humidity'],
                        name="Vlaznost SS2",
                        line=dict(
                            color="orange",
                            width=3,
                            dash='line'
                        ))
    trace8 = go.Scatter(x=df4.Date,
                        y=df4['Humidity'],
                        name="Vlaznost OH",
                        line=dict(
                            color="purple",
                            width=3,
                            dash='line'
                        ))
    fig1 = py.tools.make_subplots(rows=4, cols=1)
    fig1.append_trace(trace1, 1, 1)
    fig1.append_trace(trace2, 2, 1)
    fig1.append_trace(trace3, 3, 1)
    fig1.append_trace(trace4, 4, 1)
    fig1['layout']['yaxis1'].update(title='Temperatura SS1')
    fig1['layout']['yaxis2'].update(title='Temperatura SS24x7')
    fig1['layout']['yaxis3'].update(title='Temperatura SS2')
    fig1['layout']['yaxis4'].update(title='Temperatura Ohrid')
    fig1['layout'].update(title='Temperatura - Nedelen Report')
    fig1['layout'].update(paper_bgcolor='rgb(238,238,238)')
    fig1['layout'].update(plot_bgcolor='rgb(238,238,238)')
    py.offline.plot(fig1, filename='temperature.html')
    fig2 = py.tools.make_subplots(rows=4, cols=1)
    fig2.append_trace(trace5, 1, 1)
    fig2.append_trace(trace6, 2, 1)
    fig2.append_trace(trace7, 3, 1)
    fig2.append_trace(trace8, 4, 1)
    fig2['layout']['yaxis1'].update(title='Vlaznost SS1')
    fig2['layout']['yaxis2'].update(title='Vlaznost SS24x7')
    fig2['layout']['yaxis3'].update(title='Vlaznost SS2')
    fig2['layout']['yaxis4'].update(title='Vlaznost Ohrid')
    fig2['layout'].update(title='Vlaznost - Nedelen Report')
    fig2['layout'].update(paper_bgcolor='rgb(238,238,238)')
    fig2['layout'].update(plot_bgcolor='rgb(238,238,238)')
    py.offline.plot(fig2, filename='humidity.html')


fajlovi()
iscrtaj()

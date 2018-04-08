from datetime import datetime, date
import csv
from itertools import zip_longest

# start_date = date(2017, 10, 23)
# end_date = date(2017, 10, 29)
# ss1 = 'SS1\n'
# ss24 = '24x7\n'
# humidity = 'Humidity\n'
# plafon = 'Plafon\n'

def get_time_stamp(datum, vreme):
    stapka = datetime.strptime(datum+" "+vreme, "%m/%d/%Y %H:%M:%S")
    return stapka

with open("oh.csv") as starss2:
    with open("novoh.csv","w") as novss2:
        i = 0
        read = csv.reader(starss2)
        for row in read:
            if i==0:
                novss2.write("Date,Time,Temperature,Humidity\n")
                i+=1
            else:
                datum = get_time_stamp(row[0], row[1])
                novred=datum.strftime("%Y-%m-%d %H:%M:%S")+","+row[2]+","+row[3]+"\n"
                novss2.write(novred)
# with open("ss2.csv") as ss2:
#     with open("oh.csv") as oh:
#         with open("celosen.csv", "w") as cel:
#             prv_red = "Date,Time,Humidity SS2,Humidity OH\n"
#             cel.write(prv_red)
#             ss2.__next__()
#             oh.__next__()
#             ss2csv = csv.reader(ss2, delimiter=',')
#             ohcsv = csv.reader(oh, delimiter=',')
#             for ss2_linija, oh_linija in zip_longest(ss2csv, ohcsv):
#                 if ss2_linija:
#                     if get_time_stamp(ss2_linija[0], ss2_linija[1]) <= get_time_stamp(oh_linija[0], oh_linija[1]):
#                         prv_red = ss2_linija[0]+","+ss2_linija[1]+","+ss2_linija[3]+","+"\n"
#                         vtor_red = oh_linija[0]+","+oh_linija[1]+","+","+oh_linija[3]+"\n"
#                     else:
#                         prv_red = oh_linija[0]+","+oh_linija[1]+","+","+oh_linija[3]+"\n"
#                         vtor_red = ss2_linija[0]+","+ss2_linija[1]+","+ss2_linija[3]+","+"\n"
#                     cel.write(prv_red)
#                     cel.write(vtor_red)
#                 else:
#                     prv_red = oh_linija[0] + "," + oh_linija[1] + "," + "," + oh_linija[3] + "\n"
#                     cel.write(prv_red)

# with open('envlog.csv','r') as csvfile:
#     with open('test.csv', 'w') as newcsvfile:
#         starcsv = csv.reader(csvfile)
#         novcsv = csv.writer(newcsvfile)
#         for row in starcsv:
#             if 'Date' in row:
#                 novcsv.writerow(row)
#             else:
#                 moj_datum = datetime.strptime(str(row[0]), '%m/%d/%Y')
#                 if start_date <= moj_datum.date() <= end_date:
#                     novcsv.writerow(row)
#
#
# with open("data_log.txt") as txtfile:
#     linie = txtfile.readlines()
#     for i, linija in enumerate(linie):
#         datum = datetime.strptime(linija[:19], "%d-%m-%Y\t%H:%M:%S")
#         if linija.endswith(ss1) and start_date <= datum.date() <= end_date:
#             if not os.path.isfile('./temp.csv'):
#                 with open("temp.csv", "w") as tempcsv:
#                     prva_linija = "Date,Time,Temperatura SS1\n"
#                     tempcsv.write(prva_linija)
#             else:
#                 with open("temp.csv", "a") as tempcsv:
#                     drugi_linie = datum.strftime("%m/%d/%Y,%H:%M:%S")+','+linija[32:36]+'\n'
#                     tempcsv.write(drugi_linie)



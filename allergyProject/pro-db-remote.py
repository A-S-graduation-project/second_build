import requests
import json
import sqlite3


def Processed(dict, list):

    procData = []

    # if 'rnum' in list: procData.append(dict['rnum'])
    # else: procData.append('')

    if 'prdlstReportNo' in list: procData.append(dict['prdlstReportNo'])
    else: procData.append('')

    if 'prdlstNm' in list: procData.append(dict['prdlstNm'])
    else: procData.append('')

    # if 'productGb' in list: procData.append(dict['productGb'])
    # else: procData.append('')

    if 'prdkind' in list: procData.append(dict['prdkind'])
    else: procData.append('')

    if 'rawmtrl' in list: procData.append(dict['rawmtrl'])
    else: procData.append('')

    if 'allergy' in list: procData.append(dict['allergy'])
    else: procData.append('')

    if 'imgurl1' in list: procData.append(dict['imgurl1'])
    else: procData.append('')

    if 'manufacture' in list: procData.append(dict['manufacture'])
    else: procData.append('')

    # if 'imagurl2' in list: procData.append(dict['imagurl2'])
    # else: procData.append('')

    return procData


serviceKey = 'KRFgFYY3tfo9A3cGfNrr%2Bzaib9lhbXTPnsWS149Apg2Vg%2Frl%2BaI9cVAVMQoMPFzLW23jYOdrysnHWISruWgzTA%3D%3D'
pageNo = 1

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS searchapp_product(
    prdlstReportNo INTEGER RIMARY KEY NOT NULL,
    prdlstNm varchar(200),
    prdkind varchar(200),
    rawmtrl TEXT,
    allergy TEXT,
    image varchar(100),
    manufacture varchar(200))""")


while True:
    URL = f"https://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?serviceKey={serviceKey}"
    parameters = {'pageNo' : str(pageNo), 'returnType' : 'json'}

    res = requests.get(URL, params=parameters, verify=False)
    
    if res:
        data = json.loads(res.text)

        body = data['body']
        item_lst = body['items']

        for i in item_lst:
            prdlst = i['item']
            field = prdlst.keys()

            procData = Processed(prdlst, field)

            cur.execute("INSERT INTO searchapp_product VALUES (?, ?, ?, ?, ?, ?, ?)", procData)
            conn.commit()

        pageNo += 1

    else:
        break

conn.close()

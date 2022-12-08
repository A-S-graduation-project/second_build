import sqlite3, os
import pandas as pd
from math import sqrt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def uexport(c, li):
    li += "\n"

    for row in c.execute('SELECT * FROM searchapp_userdata'):
        for m in range(7):
            if m != 6:
                if m == 3:
                    li = li + '"' + str(row[m]) + '"' + ","
                else:
                    li = li + str(row[m]) + ","
            else:
                li = li + str(row[m])
        
        li += "\n"

    f = open("C:/Users/user/Project/second_build/allergyProject/UserData.csv", "w", encoding='utf-8')
    f.write(li)
    f.close

    return


def pexport(c, li):
    li += "\n"

    for row in c.execute('SELECT * FROM searchapp_product'):
        for m in range(7):
            if m != 6:
                if m == 2:
                    li = li + '"' + str(row[m]) + '"' + ","
                else:
                    li = li + str(row[m]) + ","
            else:
                li = li + str(row[m])
        
        li += "\n"

    f = open("C:/Users/user/Project/second_build/allergyProject/Product.csv", "w", encoding='utf-8')
    f.write(li)
    f.close

    return

conn = sqlite3.connect('C:/Users/user/Project/second_build/allergyProject/db.sqlite3')
c = conn.cursor()

user_te = "rnum,gender,older,allergy,prdlstNm,rating,prdlstReportNo"
pro_te = "prdlstReportNo,prdlstNm,rawmtrl,allergy,prdkind,manufacture,image"

uexport(c, user_te)

# 시간상 생략
# pexport(c, pro_te)

c.close()

print("export done")

##############################################################################################

def sim_person(data, allergy1, allergy2):
    sumX=0
    sumY=0
    sumPowX=0
    sumPowY=0
    sumXY=0
    count=0

    for i in data[allergy1].keys():
        if i in data[allergy2].keys():
            sumX+=data[allergy1][i]
            sumY+=data[allergy2][i]
            sumPowX+=pow(data[allergy1][i],2)
            sumPowY+=pow(data[allergy2][i],2)
            sumXY+=data[allergy1][i]*data[allergy2][i]
            count+=1

    return ( sumXY- ((sumX*sumY)/count) )/ sqrt( (sumPowX - (pow(sumX,2) / count)) * (sumPowY - (pow(sumY,2)/count)))


def top_match(data, allergy, index=3, sim_function=sim_person):
    li=[]
    for i in data:
        if allergy != i:
            li.append((sim_function(data,allergy,i), i))
    li.sort()
    li.reverse()

    return li[:index]


def getRecommendation (data, allergy, sim_function=sim_person):
    result = top_match(product_allergy_data, allergy, len(data))

    simSum=0
    score=0
    li=[]
    score_dic={}
    sim_dic={}

    for sim, al in result:
        if sim < 0 : continue
        for product in data[al].keys():
            if data[al][product] == 0:
                score += sim * data[allergy][product]
                score_dic.setdefault(product,0)
                score_dic[product] += score

                sim_dic.setdefault(product, 0)
                sim_dic[product] += sim
            
            score = 0

    for key in score_dic:
        score_dic[key] = score_dic[key]/sim_dic[key]
        if score_dic[key] != 0:
            li.append((score_dic[key],key))

    li.sort()
    li.reverse()

    return li


# user data, product data 읽기
choice_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/UserData.csv', on_bad_lines='skip')
product_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/Product.csv', on_bad_lines='skip')

# product data 전처리
product_data.drop('rawmtrl', axis=1, inplace=True)
product_data.drop('allergy', axis=1, inplace=True)
product_data.drop('prdkind', axis=1, inplace=True)
product_data.drop('manufacture', axis=1, inplace=True)

# choice data 전처리
choice_data.drop('rnum', axis=1, inplace=True)

# 병합
merge_data = pd.concat([product_data, choice_data], join='outer')

# 데이터 분포
product_allergy_data = merge_data.pivot_table('rating', index='prdlstReportNo', columns='allergy')

# NaN값 0으로 대체
product_allergy_data.fillna(0, inplace=True)

# print(product_allergy_data)

allergy1 = '난류'
# allergy2 = '고등어, 땅콩, 게, 복숭아, 호두, 메밀'

# 결과 나옴
# print(sim_person(product_allergy_data, allergy1, allergy2))

# 결과 나옴
# print(top_match(product_allergy_data, allergy1, 10))

# 결과 나옴
re_li = getRecommendation(product_allergy_data, allergy1)

# print(re_li)

###############################################################################################################

# 음식 csv 파일 가져오기
food_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/Product.csv') # csv 파일 위치로 바꾸기
fmaterial=[]   # 재료 넣을 list
fname=[]       # 음식 이름 넣을 list

# 전처리
food_data.drop('allergy',axis=1, inplace=True)
food_data.drop('prdkind',axis=1, inplace=True)
food_data.drop('manufacture',axis=1, inplace=True)

# food_data의 식품 이름과 재료들을 리스트에 넣기
for row_index, row in food_data.iterrows():
    fname.append(row.loc["prdlstReportNo"])
    fmaterial.append( row.loc["rawmtrl"])

# count vector로 만들어서 cosine similar 만들기
vectorizer = CountVectorizer()
food_vector = vectorizer.fit_transform(fmaterial)
# print(food_vector)                 # (n,m) n은 재료 번호, m은 몇번째 음식에서 나왔는지
# print(food_vector.toarray())       # (vector화 된 행렬)
food_simi_cate = cosine_similarity(food_vector, food_vector)
print(food_simi_cate)

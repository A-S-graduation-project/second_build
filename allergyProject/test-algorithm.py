import pandas as pd

# user data, product data 읽기
choice_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/UserData.csv')
product_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/Product.csv')

# product data 전처리
product_data.drop('rawmtrl', axis=1, inplace=True)
product_data.drop('allergy', axis=1, inplace=True)
product_data.drop('prdkind', axis=1, inplace=True)
product_data.drop('manufacture', axis=1, inplace=True)

print(choice_data.head(2))
print(product_data.head(2))

# 병합
product_choice_data = pd.merge(product_data, choice_data, on='prdlstNm')
print(product_choice_data.head(5))

# rating의 필요성?

# 데이터 분포 (오류)
# data = product_choice_data.pivot_table('prdlstRepotNo', index='allergy', columns='prdlstNm')
# print(data.head(5))

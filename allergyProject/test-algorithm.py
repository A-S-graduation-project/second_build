import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# user data, product data 읽기
choice_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/UserData.csv', encoding='cp949')
product_data = pd.read_csv('C:/Users/user/Project/second_build/allergyProject/Product.csv')

# product data 전처리
product_data.drop('rawmtrl', axis=1, inplace=True)
product_data.drop('allergy', axis=1, inplace=True)
product_data.drop('prdkind', axis=1, inplace=True)
product_data.drop('manufacture', axis=1, inplace=True)

# 병합
merge_data = pd.merge(product_data, choice_data, on='prdlstNm')

# 데이터 분포 (오류)
allergy_product_data = merge_data.pivot_table('rating', index='allergy', columns='prdlstNm')
# product_allergy_data = merge_data.pivot_table('rating', index='prdlstNm', columns='allergy')

# NaN값 0으로 대체
allergy_product_data.fillna(0, inplace=True)

# 코사인 유사도 사용
allergy_based_collabor = cosine_similarity(allergy_product_data)

# allergy based 유사도 생성
allergy_based_collabor = pd.DataFrame(data = allergy_based_collabor, index = allergy_product_data.index, columns = allergy_product_data.index)
print(allergy_based_collabor.head())

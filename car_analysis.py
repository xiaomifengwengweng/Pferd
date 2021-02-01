import pandas as pd
#读取文件
f = pd.read_csv('./car_complain.csv')
#print(f)

#将problem进行分段
#f.drop('列名'，axis=1)表示删除某一列。axis=0 表示删除行。
#join是一种快速合并的方法。它默认以index作为对齐的列
#one-hot的基本思想：将离散型特征的每一种取值都看成一种状态，若这一特征中有N个不相同的取值，那么我们就可以将该特征抽象成N种不同的状态。
#one-hot编码保证了每一个取值只会使得一种状态处于“激活态”，也就是说这N种状态中只有一个状态位值为1，其他状态位都是0。
f2 = f.drop('problem', axis=1).join(f.problem.str.get_dummies(','))
#数据清洗
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x
f2['brand'] = f2['brand'].apply(f)

#默认情况对分组之后其他列进行聚合，这里指明是[id]列？agg(['min', 'mean', 'max'])
#计算每个品牌的投诉总数
f3 = f2.groupby(['brand'])['id'].agg(['count'])
#将问题拆分开，计算每个品牌的每个问题的数量
tags = f2.columns[7:]
f4 = f2.groupby(['brand'])[tags].agg(['sum'])
#合并起来
f5 = f3.merge(f4, left_index=True, right_index=True, how='left')
#索引列恢复正常
f5.reset_index(inplace=True)
f6 = f5.sort_values('count', ascending=False)
f6.to_excel('./car_complain_bybrand.xlsx')

#计算每个品牌每个车型的投诉总数
f7 = f2.groupby(['brand', 'car_model'])['id'].agg(['count'])
f8 = f7.sort_values('count', ascending=False)
f8.to_excel('./car_complain_bycar.xlsx')
#计算每个品牌平均车型的投诉
f9 = f7.groupby('brand')['count'].agg(['mean'])
f10 = f9.sort_values('mean', ascending=False)
f10.to_excel('./car_complain_bycarmean.xlsx')
import pandas as pd
f = pd.read_excel('./student_result1.xlsx', index_col=0)
print(f)
fmean = f.mean(axis=1)
fmax = f.max(axis=1)
fmin = f.min(axis=1)
fvar = f.var(axis=1)
fstd = f.std(axis=1)
fsum = f.sum(axis=1)

f['平均成绩'] = fmean
f['最大成绩'] = fmax
f['最小成绩'] = fmin
f['方差'] = fvar
f['标准差'] = fstd
f['总成绩'] = fsum

print(f)
fp = f.sort_values(by='总成绩', ascending=False)
print(fp)
fp.to_excel(r'G:\pythons\student_result2.xlsx')

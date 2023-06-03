import pandas as pd

t = pd.read_csv('data_set_ALL_AML_train.csv')
i = pd.read_csv('data_set_ALL_AML_independent.csv')
a = pd.read_csv('actual.csv')

# get train patients number
t_int_cols = t.columns[t.dtypes == int].tolist()
t_int_cols = [int(col) - 1 for col in t_int_cols]
# get independent patients number
i_int_cols = i.columns[i.dtypes == int].tolist()
i_int_cols = [int(col) - 1 for col in i_int_cols]

# sum of P,M,A number in train patients
t_P = t.filter(like='call').apply(lambda x: x.str.count('P')).sum()
t_M = t.filter(like='call').apply(lambda x: x.str.count('M')).sum()
t_A = t.filter(like='call').apply(lambda x: x.str.count('A')).sum()
# sum of P,M,A number in indepedent patients
i_P = i.filter(like='call').apply(lambda x: x.str.count('P')).sum()
i_M = i.filter(like='call').apply(lambda x: x.str.count('M')).sum()
i_A = i.filter(like='call').apply(lambda x: x.str.count('A')).sum()

# fill into actual.csv
a.loc[t_int_cols, 'train_P'] = t_P.values
a.loc[t_int_cols, 'train_M'] = t_M.values
a.loc[t_int_cols, 'train_A'] = t_A.values

a.loc[i_int_cols, 'test_P'] = i_P.values
a.loc[i_int_cols, 'test_M'] = i_M.values
a.loc[i_int_cols, 'test_A'] = i_A.values

# sum of all P,M,A in ALL and AML
a.loc[0, 'sum_ALL_P'] = a.loc[a['cancer'] == 'ALL', 'train_P'].sum() + a.loc[a['cancer'] == 'ALL', 'test_P'].sum()
a.loc[0, 'sum_ALL_M'] = a.loc[a['cancer'] == 'ALL', 'train_M'].sum() + a.loc[a['cancer'] == 'ALL', 'test_M'].sum()
a.loc[0, 'sum_ALL_A'] = a.loc[a['cancer'] == 'ALL', 'train_A'].sum() + a.loc[a['cancer'] == 'ALL', 'test_A'].sum()

a.loc[0, 'sum_AML_P'] = a.loc[a['cancer'] == 'AML', 'train_P'].sum() + a.loc[a['cancer'] == 'AML', 'test_P'].sum()
a.loc[0, 'sum_AML_M'] = a.loc[a['cancer'] == 'AML', 'train_M'].sum() + a.loc[a['cancer'] == 'AML', 'test_M'].sum()
a.loc[0, 'sum_AML_A'] = a.loc[a['cancer'] == 'AML', 'train_A'].sum() + a.loc[a['cancer'] == 'AML', 'test_A'].sum()

# convert float to integer
c = a.columns[2:]
a[c] = a[c].astype(float).astype('Int64')
# add dash "-"
c = a.columns[2:8]  # columns 3 to 8
a[c] = a[c].astype('object').fillna('—')

#print(a)
a.to_csv('final.csv', index = False)

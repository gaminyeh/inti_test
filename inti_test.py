import pandas as pd

t = pd.read_csv('data_set_ALL_AML_train.csv')
i = pd.read_csv('data_set_ALL_AML_independent.csv')
a = pd.read_csv('actual.csv')

t_P = t.filter(like='call').apply(lambda x: x.str.count('P')).sum()
t_M = t.filter(like='call').apply(lambda x: x.str.count('M')).sum()
t_A = t.filter(like='call').apply(lambda x: x.str.count('A')).sum()

i_P = i.filter(like='call').apply(lambda x: x.str.count('P')).sum()
i_M = i.filter(like='call').apply(lambda x: x.str.count('M')).sum()
i_A = i.filter(like='call').apply(lambda x: x.str.count('A')).sum()

a.loc[:37, 'train_P'] = t_P.values
a.loc[:37, 'train_M'] = t_M.values
a.loc[:37, 'train_A'] = t_A.values

a.loc[38:, 'test_P'] = i_P.values
a.loc[38:, 'test_M'] = i_M.values
a.loc[38:, 'test_A'] = i_A.values

t_P_sum_ALL = a.loc[a['cancer'] == 'ALL', 'train_P'].sum()
i_P_sum_ALL = a.loc[a['cancer'] == 'ALL', 'test_P'].sum()

t_M_sum_ALL = a.loc[a['cancer'] == 'ALL', 'train_M'].sum()
i_M_sum_ALL = a.loc[a['cancer'] == 'ALL', 'test_M'].sum()

t_A_sum_ALL = a.loc[a['cancer'] == 'ALL', 'train_A'].sum()
i_A_sum_ALL = a.loc[a['cancer'] == 'ALL', 'test_A'].sum()

a.loc[0, 'sum_ALL_P'] = t_P_sum_ALL + i_P_sum_ALL
a.loc[0, 'sum_ALL_M'] = t_M_sum_ALL + i_M_sum_ALL
a.loc[0, 'sum_ALL_A'] = t_A_sum_ALL + i_A_sum_ALL

t_P_sum_AML = a.loc[a['cancer'] == 'AML', 'train_P'].sum()
i_P_sum_AML = a.loc[a['cancer'] == 'AML', 'test_P'].sum()

t_M_sum_AML = a.loc[a['cancer'] == 'AML', 'train_M'].sum()
i_M_sum_AML = a.loc[a['cancer'] == 'AML', 'test_M'].sum()

t_A_sum_AML = a.loc[a['cancer'] == 'AML', 'train_A'].sum()
i_A_sum_AML = a.loc[a['cancer'] == 'AML', 'test_A'].sum()

a.loc[0, 'sum_AML_P'] = t_P_sum_AML + i_P_sum_AML
a.loc[0, 'sum_AML_M'] = t_M_sum_AML + i_M_sum_AML
a.loc[0, 'sum_AML_A'] = t_A_sum_AML + i_A_sum_AML

# convert to int
c = a.columns[2:]
a[c] = a[c].astype(float).astype('Int64')

#print(a)
a.to_csv('final.csv', index=False)


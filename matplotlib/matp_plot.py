import matplotlib.pyplot as plt
import pandas as pd
import cal_list

from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'

rate = 3.5  #年利率
years = 10  # 年限
total = 30.00  # 本金，以w为单位
loan_type = "capital"  # 等额本金capital  等额本息 interest

test = cal_list.Cal
amount_dict, interest_total, repay_amount = test.cal_func(total,years,rate,loan_type)

# 画图数据准备
df = pd.DataFrame(amount_dict)  #将list转为excel
# print(df)
df.plot(df.drop('months', axis=1, inplace=True))

plt.title(loan_type)
plt.legend(['偿还利息', '偿还本金', '偿还本息'])

plt.savefig("test_plot.png")
plt.show()



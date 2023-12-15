import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cal_list

from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'


rate = 3.5  #年利率
years = 10  # 年限
total = 30.00  # 本金，以w为单位
loan_type = "interest"  # 等额本金capital  等额本息 interest

test = cal_list.Cal
amount_list, interest_total, repay_amount = test.cal_func(total,years,rate,loan_type)

# 画图数据准备
df = pd.DataFrame(amount_list)  #将list转为excel

x = df.months

# 设置画图区域
fig = plt.figure(figsize=(8, 5))
ax = fig.subplots(1,3)

ax[0].set(title = "偿还利息")
ax[0].plot(x, df.interest_month, c='r')
ax[1].set(title = "偿还本金")
ax[1].plot(x, df.capital_month, c='g')
ax[2].set(title = "偿还本息")
ax[2].plot(x, df.total_month)

plt.show()
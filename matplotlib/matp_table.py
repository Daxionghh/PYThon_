import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cal_list

from pandas import Series, DataFrame
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'

rate = 3.5  #年利率
years = 10  # 年限
amount_total = 30.00  # 本金，以w为单位
loan_type = "interest"  # 等额本金capital  等额本息 interest

test = cal_list.Cal
amount_list, interest_total, repay_amount = test.cal_func(amount_total,years,rate,loan_type)

# 画图数据准备
# df = pd.DataFrame(amount_list).head(10)  #将list转为excel
# data = [df.months, df.interest_month.round(2), df.capital_month.round(2), df.total_month.round(2)]

cus_type = np.dtype([('month','i'),('ins','f'),('cap','f'),('total','f')])
datas = np.array([],dtype=cus_type)
i = 0
for x in amount_list:
    data = np.array([(x.get('months'),x.get('interest_month'),x.get('capital_month'),x.get('total_month'))],dtype=cus_type)
    datas = np.append(datas, data)    
  
# trans_data = np.transpose(datas)
trans_data = datas

# 设置画图区域
fig, ax = plt.subplots(figsize=(10, 20))

col_labels = ["期次", "偿还利息", "偿还本金", "偿还本息"]
ax.axis('off')
ax.table(
    colLabels = col_labels,
    cellText = trans_data,
    loc= "center")

plt.savefig("test_table.png")
plt.show()

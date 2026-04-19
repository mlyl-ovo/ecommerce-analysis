import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("orders.csv")
print(df.columns.to_list())
print(f"一共有{df['订单日期'].count()}条订单")
print(f"有{df['用户ID'].unique().size}个不同的用户")
print(f"总的销售额为{df['销售额'].sum():.2f}元")
print(f"平均每单销售额为{df['销售额'].mean():.2f}元")
print(f"最高订单金额为{df['销售额'].max():.2f}元，最低订单金额为：{df['销售额'].min():.2f}元")
print(f"类别卖得最多的商品是{df.groupby('商品类别')['商品类别'].count().idxmax()}，数量为{df.groupby('商品类别')['商品类别'].count().max()}件")
print(f"销售额最高的类别为{df.groupby('商品类别')['销售额'].sum().idxmax()}，销售额为{df.groupby('商品类别')['销售额'].sum().max():.2f}元")
df['订单日期']=pd.to_datetime(df['订单日期'])
df['月份']=df['订单日期'].dt.strftime('%Y-%m')
print(f"销售额最高的月份是{df.groupby('月份')['销售额'].sum().idxmax()}月")
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
monthly_sales = df.groupby('月份')['销售额'].sum().reset_index()
plt.plot(monthly_sales['月份'], monthly_sales['销售额'], marker='o', color='blue', linewidth=2, label='销售额', alpha=0.7, linestyle='--', markersize=8, markerfacecolor='red', markeredgewidth=1.5, markeredgecolor='green')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.title('销售额趋势图')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
top5=df.groupby('用户ID')['销售额'].sum().sort_values(ascending=False).head(5)
print(f"消费最高的前5名用户ID分别是：")
for user_id,sales in top5.items():
    print(f"{user_id}")
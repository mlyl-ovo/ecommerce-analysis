import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 生成示例数据（模拟电商订单）
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
categories = ['电子产品', '服装', '图书', '家居', '食品']

data = []
for i in range(500):
    date = np.random.choice(dates)
    category = np.random.choice(categories)
    sales = np.random.randint(50, 5000)
    user_id = np.random.randint(1, 101)
    data.append([date, category, sales, user_id])

df = pd.DataFrame(data, columns=['订单日期', '商品类别', '销售额', '用户ID'])

# 保存为 CSV
df.to_csv('data/orders.csv', index=False, encoding='utf-8-sig')
print("数据已生成：orders.csv")
print(f"共 {len(df)} 条订单")
print(df.head())
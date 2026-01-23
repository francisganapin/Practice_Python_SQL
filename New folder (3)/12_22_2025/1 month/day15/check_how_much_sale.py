from collections import Counter


transactions = ['item-101','item-101','item-102','item-103','item-101','item-102']

report = Counter(transactions)

for item,count in report.items():
    print(f'Item {item} sold:{count}')
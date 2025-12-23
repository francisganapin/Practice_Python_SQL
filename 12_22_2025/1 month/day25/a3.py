rows = [
    {'name':"Phone","stock":12},
    {"name":"Laptop","stock":0},
    {"name":"Mouse","stock":8}
]


for row in rows:
    if row['stock'] == 0:
        print(f'{row['name']} is out of stock')
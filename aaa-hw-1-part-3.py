orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

sum_amount = 0
for order in orders:
    if order['status'] == 'returned':
        sum_amount += order['amount']
print(sum_amount)

print(set([order['buyer'] for order in orders if order['status'] == "returned"]))

from collections import Counter

print(dict(Counter(order['buyer'] for order in orders if order['status'] == "delivered")))

print(sum(order["amount"] for order in orders if order["status"] == "delivered") / len(
    [order["id"] for order in orders if order["status"] == "delivered"]))
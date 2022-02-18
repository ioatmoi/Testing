userIds = ['U01', 'U02', 'U03'] 
orderIds = ['T01', 'T02', 'T03', 'T04'] 
userOrders = [{ 'userId': 'U01', 'orderIds': ['T01', 'T02'] },
 	          { 'userId': 'U02', 'orderIds': [] },
 	          { 'userId': 'U03', 'orderIds': ['T03'] },
             ]
userData = { 'U01': 'Tom', 'U02': 'Sam', 'U03': 'John' } 
orderData = {'T01': { 'name': 'A', 'price': 499 }, 
             'T02': { 'name': 'B', 'price': 599 },
             'T03': { 'name': 'C', 'price': 699 }, 
             'T04': { 'name': 'D', 'price': 799 }
            } 

result = []
for item in userOrders:
    order_list = []
    for i in item['orderIds']:
        order_list.append({'id':i, 'name':orderData[i]['name'], 'price':orderData[i]['price']})
    temp = {'user': {'id':item['userId'],'name':userData[item['userId']]},
            'orders': order_list}
    result.append(temp)
print(result)
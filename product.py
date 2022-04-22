product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	product.append([name, price])
	# p=[]
	# p.append(name)
	# p.append(price)
	# product.append(p)
print(product)

for p in product:  #把product清單中的每一個p拿出來看
	print(p[0],'的價格是',p[1])

with open('product.csv', 'w') as f:
	for p in product:
		f.write(p[0]+','+p[1]+'\n')

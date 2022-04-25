import os #operating system



#先檢查檔案有無存在檔案夾裡，再讀取檔案
products = []
if os.path.isfile('product.csv'):   #os.path.isfile是內建library 檢查檔案在不在
	print('找到檔案')
	with open('product.csv','r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
	print(products)
else:
	print('找不到檔案')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	products.append([name, price])
	# p=[]
	# p.append(name)
	# p.append(price)
	# products.append(p)
print(products)

#印出所有購買紀錄 
for p in products:  #把product清單中的每一個p拿出來看
	print(p[0],'的價格是',p[1])

#寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f: #utf-8為世界通用的編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')

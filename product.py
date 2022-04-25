import os #operating system
#讀取檔案
def read_file(filename):
    products = []
    with open(filename,'r', encoding='utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])
    return products #products這個清單會裝著所有的資料

#讓使用者輸入
def user_input(products):
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
    return products #因為清單有加入新的內容，所以要再回傳新的結果一遍


#印出所有購買紀錄 
def print_products(products):
    for p in products:  #把product清單中的每一個p拿出來看
        print(p[0],'的價格是',p[1])
        #因為只是印出，沒有產生新的內容，所以不需回傳

#寫入檔案
def write_file(filename,products): #在這裡宣告products
    with open(filename, 'w', encoding='utf-8') as f: #utf-8為世界通用的編碼
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0]+','+p[1]+'\n')
            #只是寫入檔案，所以不需回傳

#-------

def main():
#先檢查檔案有無存在檔案夾裡，再讀取檔案
    filename = 'products.csv' #先宣告變數，降低重複性
    if os.path.isfile(filename):   #os.path.isfile是內建library 檢查檔案在不在
        print('找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')
    products = read_file('products.csv')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)
#------function的定義，下面才正式開始執行程式--------

main()
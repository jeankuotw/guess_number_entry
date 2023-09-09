#載入模組random
import random 

r = random.randint(1, 100) #使用random模組中的函式(功能)randint(隨機產生整數),數字界在1~100的整數

#題目：隨機產生一個1-100的數字
#讓使用者重複輸入數字去猜
#如果猜對了,要顯示"你答對了"
#如果猜錯了,要提示比答案 大/小

count = 0

while True:
	keyin = input('請猜數字1~100：') #使用者輸入的內容為字串,括號內記得要用''
	keyin = int(keyin) #型別轉換，將字串轉為整數

	count += 1  #count = count +1 的快寫法

	if keyin > 0 and keyin <= 100:
		if keyin == r :
			print('你答對了')
			print('這是你猜的第',count,'次')
			break
		elif keyin > r:
			print('比答案大')
		else:
			print('比答案小')
		print('這是你猜的第',count,'次')
	else:
		print('輸入錯誤,請輸入1~100的數字')

# -*- coding: UTF-8 -*-
# 猜数字小游戏

import random

guess = random.randint(100,999)
print('猜猜当前的数字,当前数字范围在100到999之间')
i = 0

while True:
	if i == 10:
		print('挑战失败，游戏结束')
		break
	else:
		num = int(input("请再次输入:"))
		if guess == num:
			print('恭喜你，猜对了，游戏结束')
			break
		else:
			if num > guess :
				print('大了大了')
			else:
				print('小了小了')
		i=i+1
		if i != 10:
			print('请再猜,您还有' + str(10-i))


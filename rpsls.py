#coding:gbk
"""
目的：通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
作者：黄洁
2019/11/14
"""

import random#引用Random使计算机产生随机数



#0 - 石头
#1 - 史波克
#2 - 纸
#3 - 蜥蜴
#4 - 剪刀


def name_to_number(name):#定义函数使玩家输入的名字转变为数字
	
	if name=="石头":
		return 0
	elif name=="史波克":
		return 1
	elif name=="纸":
		return 2
	elif name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4
	else:
		print("Error: No Correct Name")
	return(name)
	
	
	
	
def number_to_name(number):#定义函数使计算机产生的随机数转变为名字
	
	if number==0:
		return "石头"
	elif number==1:
		return "史波克"
	elif number==2:
		return "纸"
	elif number==3:
		return "蜥蜴"
	elif number==4:
		return "剪刀"
	else:
		print("Error: No Correct Name")
	return(number)
	
	

	
def rpsls(player_choice):
	print("------------")

	
	player_choice_number = name_to_number(player_choice)#变量的转换赋值
	
	
	
	import random#引用函数random
	comp_number=random.randrange(0,5)
	
	
	computer_choice = number_to_name(comp_number)#变量的转换赋值
	
	print("您的选择是%s"%player_choice)
	print("计算机选择的是%s"%computer_choice)
	
	player_win = [(4,2),(4,3),(1,4),(1,0),(2,0),(2,1),(0,4),(0,3),(3,1),(3,2)]#使用列表列出游戏中的四种情况，简化程序
	computer_win = [(2,4),(3,4),(4,1),(0,1),(0,2),(1,2),(4,0),(3,0),(1,3),(2,3)]
	average = [(0,0),(1,1),(2,2),(3,3),(4,4)]	
	if (player_choice_number,comp_number) in player_win:#对自定义列表的使用
		print("您赢了")
	elif (player_choice_number,comp_number) in computer_win:
		print("计算机赢了")
	elif (player_choice_number,comp_number) in average:
		print("您和计算机出的一样呢")
	else:
		print("Error: No Correct Name")
	
	
	# if player_choice_number==4 and comp_number==2:#分别列出若干种游戏中可能会产生的情况，一一输出结果
		# print("您赢了")
	# if player_choice_number==4 and comp_number==3:
		# print("您赢了")
	# if player_choice_number==1 and comp_number==4:
		# print("您赢了")
	# if player_choice_number==1 and comp_number==0:
		# print("您赢了")
	# elif player_choice_number==2 and comp_number==0:
		# print("您赢了")
	# elif player_choice_number==2 and comp_number==1:
		# print("您赢了")
	# elif player_choice_number==0 and comp_number==4:
		# print("您赢了")
	# elif player_choice_number==0 and comp_number==3:
		# print("您赢了")
	# elif player_choice_number==3 and comp_number==1:
		# print("您赢了")
	# elif player_choice_number==3 and comp_number==2:
		# print("您赢了")
	# elif comp_number==4 and player_choice_number==2:
		# print("计算机赢了")
	# elif comp_number==4 and player_choice_number==3:
		# print("计算机赢了")
	# elif comp_number==2 and player_choice_number==0:
		# print("计算机赢了")
	# elif comp_number==2 and player_choice_number==1:
		# print("计算机赢了")
	# elif comp_number==0 and player_choice_number==4:
		# print("计算机赢了")
	# elif comp_number==0 and player_choice_number==3:
		# print("计算机赢了")
	# elif comp_number==1 and player_choice_number==4:
		# print("计算机赢了")
	# elif comp_number==1 and player_choice_number==0:
		# print("计算机赢了")
	# elif comp_number==3 and player_choice_number==1:
		# print("计算机赢了")
	# elif comp_number==3 and player_choice_number==2:
		# print("计算机赢了")
	# elif comp_number==0 and player_choice_number==0:
		# print("您和计算机出的一样呢")
	# elif comp_number==1 and player_choice_number==1:
		# print("您和计算机出的一样呢")
	# elif comp_number==2 and player_choice_number==2:
		# print("您和计算机出的一样呢")
	# elif comp_number==3 and player_choice_number==3:
		# print("您和计算机出的一样呢")
	# elif comp_number==4 and player_choice_number==4:
		# print("您和计算机出的一样呢")
	# else:
		# print("Error: No Correct Name")
		


print("欢迎使用RPSLS游戏")#进行游戏的检测    
print("----------------")
print("请输入您的选择:")
player_choice=input()
rpsls(player_choice)


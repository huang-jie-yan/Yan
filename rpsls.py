#coding:gbk
"""
Ŀ�ģ�ͨ���Զ��庯����ʵ��RPSLS��Ϸ�����û�ͨ��������������һ��ѡ��ʯͷ/����/��/����/ʷ���ˣ���������Զ�����һ�����ѡ�񣬸���RPSLS���򣬲������յĽ��
���ߣ��ƽ�
2019/11/14
"""

import random#����Randomʹ��������������



#0 - ʯͷ
#1 - ʷ����
#2 - ֽ
#3 - ����
#4 - ����


def name_to_number(name):#���庯��ʹ������������ת��Ϊ����
	
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="ֽ":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error: No Correct Name")
	return(name)
	
	
	
	
def number_to_name(number):#���庯��ʹ����������������ת��Ϊ����
	
	if number==0:
		return "ʯͷ"
	elif number==1:
		return "ʷ����"
	elif number==2:
		return "ֽ"
	elif number==3:
		return "����"
	elif number==4:
		return "����"
	else:
		print("Error: No Correct Name")
	return(number)
	
	

	
def rpsls(player_choice):
	print("------------")

	
	player_choice_number = name_to_number(player_choice)#������ת����ֵ
	
	
	
	import random#���ú���random
	comp_number=random.randrange(0,5)
	
	
	computer_choice = number_to_name(comp_number)#������ת����ֵ
	
	print("����ѡ����%s"%player_choice)
	print("�����ѡ�����%s"%computer_choice)
	
	player_win = [(4,2),(4,3),(1,4),(1,0),(2,0),(2,1),(0,4),(0,3),(3,1),(3,2)]#ʹ���б��г���Ϸ�е�����������򻯳���
	computer_win = [(2,4),(3,4),(4,1),(0,1),(0,2),(1,2),(4,0),(3,0),(1,3),(2,3)]
	average = [(0,0),(1,1),(2,2),(3,3),(4,4)]	
	if (player_choice_number,comp_number) in player_win:#���Զ����б��ʹ��
		print("��Ӯ��")
	elif (player_choice_number,comp_number) in computer_win:
		print("�����Ӯ��")
	elif (player_choice_number,comp_number) in average:
		print("���ͼ��������һ����")
	else:
		print("Error: No Correct Name")
	
	
	# if player_choice_number==4 and comp_number==2:#�ֱ��г���������Ϸ�п��ܻ�����������һһ������
		# print("��Ӯ��")
	# if player_choice_number==4 and comp_number==3:
		# print("��Ӯ��")
	# if player_choice_number==1 and comp_number==4:
		# print("��Ӯ��")
	# if player_choice_number==1 and comp_number==0:
		# print("��Ӯ��")
	# elif player_choice_number==2 and comp_number==0:
		# print("��Ӯ��")
	# elif player_choice_number==2 and comp_number==1:
		# print("��Ӯ��")
	# elif player_choice_number==0 and comp_number==4:
		# print("��Ӯ��")
	# elif player_choice_number==0 and comp_number==3:
		# print("��Ӯ��")
	# elif player_choice_number==3 and comp_number==1:
		# print("��Ӯ��")
	# elif player_choice_number==3 and comp_number==2:
		# print("��Ӯ��")
	# elif comp_number==4 and player_choice_number==2:
		# print("�����Ӯ��")
	# elif comp_number==4 and player_choice_number==3:
		# print("�����Ӯ��")
	# elif comp_number==2 and player_choice_number==0:
		# print("�����Ӯ��")
	# elif comp_number==2 and player_choice_number==1:
		# print("�����Ӯ��")
	# elif comp_number==0 and player_choice_number==4:
		# print("�����Ӯ��")
	# elif comp_number==0 and player_choice_number==3:
		# print("�����Ӯ��")
	# elif comp_number==1 and player_choice_number==4:
		# print("�����Ӯ��")
	# elif comp_number==1 and player_choice_number==0:
		# print("�����Ӯ��")
	# elif comp_number==3 and player_choice_number==1:
		# print("�����Ӯ��")
	# elif comp_number==3 and player_choice_number==2:
		# print("�����Ӯ��")
	# elif comp_number==0 and player_choice_number==0:
		# print("���ͼ��������һ����")
	# elif comp_number==1 and player_choice_number==1:
		# print("���ͼ��������һ����")
	# elif comp_number==2 and player_choice_number==2:
		# print("���ͼ��������һ����")
	# elif comp_number==3 and player_choice_number==3:
		# print("���ͼ��������һ����")
	# elif comp_number==4 and player_choice_number==4:
		# print("���ͼ��������һ����")
	# else:
		# print("Error: No Correct Name")
		


print("��ӭʹ��RPSLS��Ϸ")#������Ϸ�ļ��    
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)


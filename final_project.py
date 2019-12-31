#encoding=utf-8
"""
项目名：基于Python和Gelphi的《黎明破晓的街道》人物关系图谱构建
作者：黄洁
2019/12/30
"""
import jieba#引入jieba和jieba库，进行词频统计和分词
import jieba.posseg as pseg

jieba.load_userdict("dict.txt")	#导入我自己设定的人物名库
names = {}#人物名称存储的字典
relationships = {}#分析关系
paranames = []#为行之间的人物名，以此构建关系

with open("黎明破晓的街道.txt","r",encoding="utf-8") as f:#打开文本文件，确保准确读取汉字
	for line in f.readlines():
		words = pseg.cut(line)#分词
		paranames.append([])#为本行人物新建列表
		for i in words:
			if i.flag != "nr" or len(i.flag) < 2:#去掉不满足条件的词语，满足条件的人物名则加1,"nr"表示人名，是词性
				continue
			paranames[-1].append(i.word)
			if names.get(i.word) is None:
				names[i.word] = 0
				relationships[i.word] = {}
			names[i.word] += 1

for line in paranames:#处理权，建立人物间的关系
	for name1 in line:
		for name2 in line:
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:
				relationships[name1][name2] = 1
			else:
				relationships[name1][name2] = relationships[name1][name2] + 1
				
with open("node.txt","w",encoding="utf-8") as f:#建立点文件
	f.write("ID" + "," + "Label" + "," + "Weight\n")
	for name, times in names.items():
		if name in ["小姐","老公","连","耶","明白","东白乐","阿姨","平安夜","滑雪"]:#去掉不符合条件的词
			continue
		if times > 10:
			f.write(name + "," + name + "," + str(times) + "\n")#写入文件
			
with open("edge.txt","w",encoding="utf-8") as f:#建立边文件
	f.write("Source" + "," + "Target" + "," + "Weight\n")
	for name, relations in relationships.items():
		for t, w in relations.items():
			if name in ["小姐","明白","阿姨","平安夜","宣言"] or t in ["小姐","明白","阿姨","平安夜","宣言"]:#去掉不符合条件的词
				continue
			if w > 10:#借权重确保输出为人物名
				f.write(name + "," + t + "," + str(w) + "\n")#写入文件
				


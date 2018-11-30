# -*-coding=utf-8 -*-
token_dict = {}
import io
cnt = 0
for line in io.open("word.out","r"):
	print(cnt)
	cnt += 1
	for a in line.split():
		if a in token_dict:
			token_dict[a] += 1
		else:
			token_dict[a] = 1
	# line = data.readline()

# data.close()	
result = open("result.out","r+")
for k,v in token_dict.items():
	result.write(k)
	result.write('\t')
	result.write(str(v))
	result.write('\n')
result.close()



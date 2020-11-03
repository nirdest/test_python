import re


file = open('./log.txt', 'r')
my_list=[]

for line in file:
	result = re.split('&', line)
	for line2 in result:
		result2 = re.split('=', line2)
		#print(result2)
		my_list.append(result2)   

#print(my_list[1])
i=0
n=0
final=[[]]
#final=
title=[]
u=0
o=0


for n in my_list:
	i=i+1
	#print(my_list[i][0])
	if i==1:
		ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", my_list[u][0])
#		print(ip_candidates[0])
		if ip_candidates[0]=="10.1.192.38":
			print(my_list[u][1])
			print(ip_candidates[0])
		my_list[u][0]=ip_candidates[0]

	if o<14:
		title.append(my_list[i-1][0])
		o=o+1
		#print(my_list[u][0])
	if o==14:
		title.append('ip')
		o=o+1
	if i == 14:
#		print("14")
#		print(my_list[u][0])
		i=0
	u=u+1
print()
print(my_list)
print()
print(title)

#rr=
#for rr in my_list:
#	if  

#ff = a.replace("\n","")


#print(len(my_list))

#ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", my_list[0][0])
#print(ip_candidates[0])
# It Works


#print(result[0][0]+result[0][1])
#ut = re.search(r'sid', result[0])
#print()

file.close()



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
	#print(n)
	if i==1:
		ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", my_list[u][0])
		my_list[u][1]=my_list[u][1][(1):(len(my_list[u][1])-1)]
#		print(ip_candidates[0])
#		if ip_candidates[0]=="10.1.192.38":
#			print(my_list[u][1]) # sid
			
			#print(my_list[u])
		#my_list[u][0]=ip_candidates[0]
		my_list[u][0]='sid'
		my_list.insert(u, ["ip", ip_candidates[0]])

	#if o<14:
		#title.append(my_list[i-1][0])
	#	o=o+1
		#print(my_list[u][0])
#	if o==15:
		#title.append('ip')
#		o=o+1
	if i == 15:
		#print("14")
#		print()
		http = re.split(' ', my_list[u][1], maxsplit=1)
		my_list[u][1]=http[0]
		my_list.insert(u+1, ["browser", http[1]])
		#print(http[1])
		
	if i == 16:
		i=0

	u=u+1
	
html_file = open("index.html", "w")
html_file.write(r'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Example</title></head><body style="background-color: #FFF5EE;">')
	
	


	

#for n in my_list:
#	print(n)

html_file.write(r'<h2>&nbsp;&nbsp;&nbsp;&nbsp;Первоначальные данные, обработанные для таблицы</h2>' + '\n')	
html_file.write(r'<table border="1" bordercolor=#FFF5EE>' + '\n' + '<tr style="text-align:center">')	

 #style="display: table-row; vertical-align: inherit; border-color: red;
for n in my_list:
	html_file.write(r'<td><b>' + n[0] + "</b></td>")
	if i == 15:
		html_file.write(r'</tr>')
		break
	i+=1
i=0
html_file.write(r"<tr>")

for n in my_list:
#	if i == 0:
#		print()
	i=i+1	
	html_file.write(r'<td>' + n[1] + "</td>")
	if i == 16:
		i=0
		html_file.write(r'</tr>')
		
html_file.write(r'</table>')
	#print(n[1])
	
	
i=False
sid=[]

for n in my_list:
	if i==True:
		i=False
		sid.append(n[1])
#		print(n) # sid
	if n[1]=="10.1.192.38":
		i=True
sid = sorted(sid)

print("Фильтрованные данные по ip и отсортированные по алфавиту (Более подробно в ./index.html):")
for n in sid:
	print(n)


html_file.write(r'<h2>&nbsp;&nbsp;&nbsp;&nbsp;Фильтрованные данные по ip и отсортированные по алфавиту</h2>' + '\n' + '<ul>')
for n in sid:
	html_file.write('<li>' + n + '</li>' + '\n\r')	
html_file.write(r'</ul>')	
	
	
	
	
html_file.write(r'</body></html>')	
html_file.close()
	
#print()
#print(my_list)


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



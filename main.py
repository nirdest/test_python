import re

file = open('./log.txt', 'r')
my_list=[]

for line in file:
	result = re.split('&', line)  # Split string "line" with symbol "&" in "mode=0&screenid=58"   
	for line2 in result:
		result2 = re.split('=', line2) # Split string "line2" with symbol "=" in "screenid=58" 
		my_list.append(result2)   # Adding all data in list "my_list"

i=0
u=0

for n in my_list:
	i=i+1
	if i==1: # if first row in list
		ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", my_list[u][0]) # Find and replace ip address from rows
		my_list[u][1]=my_list[u][1][(1):(len(my_list[u][1])-1)] # Cut first and last symbol in SID
		my_list[u][0]='sid'  # Adding right name to columns 
		my_list.insert(u, ["ip", ip_candidates[0]]) # Adding list IP in main list
	if i == 15:   # rows - to=2020-08-14%2006%3A00%3A00 HTTP/1.1" 200 873 "Chrome/84.0.4147.125 Safari/537.36"
		http = re.split(' ', my_list[u][1], maxsplit=1) # Split string "line" with first symbol " " in "to=2020-08-14%2006%3A00%3A00 HTTP/1.1" 200 873 "Chrome/84.0.4147.125 Safari/537.36""   
		my_list[u][1]=http[0] # first part - 2020-08-14%2006%3A00%3A00 
		my_list.insert(u+1, ["browser", http[1]]) # Adding list "browser" in main list  -  HTTP/1.1" 200 873 "Chrome/84.0.4147.125 Safari/537.36"
	if i == 16:  # End of row in list 
		i=0
	u=u+1 # Service magic number. u=n 
	
html_file = open("index.html", "w")
html_file.write(r'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Example</title></head><body style="background-color: #FFF5EE;">')
html_file.write(r'<h2>&nbsp;&nbsp;&nbsp;&nbsp; Первоначальные данные, обработанные для таблицы</h2>' + '\n')	
html_file.write(r'<table border="1" bordercolor=#FFF5EE>' + '\n' + '<tr style="text-align:center">')	


for n in my_list: # Print first row in list. Title 
	html_file.write(r'<td><b>' + n[0] + "</b></td>") 
	if i == 15:
		html_file.write(r'</tr>')
		break
	i+=1
i=0

html_file.write(r"<tr>")

for n in my_list: # Print all data in list
	i=i+1	
	html_file.write(r'<td>' + n[1] + "</td>")
	if i == 16:
		i=0
		html_file.write(r'</tr>')
html_file.write(r'</table>')	
	
i=False
sid=[]

for n in my_list: # Find right IP 
	if i==True:
		i=False
		sid.append(n[1])
	if n[1]=="10.1.192.38":
		i=True
sid = sorted(sid) # Sorted from A to Z

print("Фильтрованные данные по ip и отсортированные по алфавиту (Более подробно в ./index.html):")

for n in sid:
	print(n) # Print answer in terminal 

html_file.write(r'<h2>&nbsp;&nbsp;&nbsp;&nbsp; Фильтрованные данные по ip и отсортированные по алфавиту</h2>' + '\n' + '<ul>')

for n in sid:
	html_file.write('<li>' + n + '</li>' + '\n\r')

html_file.write(r'</ul>')

html_file.write(r'<h2>&nbsp;&nbsp;&nbsp;&nbsp; Отсортированные  данные по timestamp, от большего к меньшему</h2>' + '\n')

html_file.write(r'<table border="1" bordercolor=#FFF5EE>' + '\n' + '<tr style="text-align:center">')	


for n in my_list: # Print first row in list. Title 
	if i==0:
		html_file.write(r'<td><b>' + n[0] + "</b></td>") 
	if i==1:
		html_file.write(r'<td><b>' + n[0] + "</b></td>") 
	if i==4:
		html_file.write(r'<td><b>' + n[0] + "</b></td>") 
	
	if i == 15:
		html_file.write(r'</tr>')
		break
	i+=1
i=0
u=0
html_file.write(r"<tr>")

ip = []
sid=[]
timestamp = []

for n in my_list: # Print all data in list
	if i==0:
		ip.append(n[1])
	if i==1:
		sid.append(n[1])
	if i==4:
		timestamp.append(n[1])
	i=i+1
	#html_file.write(r'<td>' + n[1] + "</td>")
	if i == 16:
		i=0
		html_file.write(r'</tr>')

i=0
tt = len(ip) -1
#print(ip, sid, timestamp)
for dd in range(0,tt):
	for ff in range(0,tt):
		if timestamp[ff]<timestamp[ff+1]:
			timestamp[ff],timestamp[ff+1]=timestamp[ff+1],timestamp[ff]		
			sid[ff],sid[ff+1]=sid[ff+1],sid[ff]
			ip[ff],ip[ff+1]=ip[ff+1],ip[ff]
	
#print(ip, sid, timestamp)

for dd in range(0,tt+1):# Print first row in list. Title 
	html_file.write(r'<tr>')
	html_file.write(r'<td>' + ip[dd] + "</b>") 
	html_file.write(r'<td>' + sid[dd] + "</b>") 
	html_file.write(r'<td>' + timestamp[dd] + "</b>") 
	html_file.write(r'</tr>')
	




html_file.write(r'</table>')	



		
		
html_file.write(r'</body></html>')	

html_file.close()
file.close()



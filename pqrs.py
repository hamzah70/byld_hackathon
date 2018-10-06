import ast
def movie_id(name):
	file1 = open("moviename_id.txt", "r", encoding = "ISO-8859-1")
	contents1 = file1.read()
	movie_name_index = contents1.find(name)
	movie_id_index = contents1.rfind("/m/",0,movie_name_index)
	content_half = contents1[:movie_id_index]
	content_half = content_half.split()
	length = len(content_half) - 1
	movie_wiki_id = content_half[length]
	file1.close()
	return str(movie_wiki_id)
	

def function2(id):
	scoreold=0
	f1=open("dict.txt","r")
	for line1 in f1:
		dict1=ast.literal_eval(line1)	
		if dict1['id']==id:	
			keywords=dict1.keys()	
	f1.close()
	f2=open("dict.txt","r")
	for line2 in f2:
		dict2=ast.literal_eval(line2)
		scorenew=0
		keys=dict2.keys()
		for i in keys:
			if dict2[i]==id:
				break

			elif i!="id":
				if i in keywords:
					scorenew+=int(dict2[i])
		if scorenew>scoreold:
			scoreold=scorenew
			best=dict2["id"]
	return(best)
	f2.close() 

def movie_name(id):
	file1 = open("moviename_id.txt", "r", encoding = "ISO-8859-1")
	for line in file1:
		index=line.find("\t")
		number=line[:index]
		name_of_movie=""
		t=20
		c=1
		if number==id:
			while c!=0:
				if line[t].isdigit():
					c=0;
					return name_of_movie
				if c!=0:	
					name_of_movie+=line[t]	
				t=t+1	

x=input()
i=movie_id(x)
s=function2(i)
name=movie_name(s)
print(name)

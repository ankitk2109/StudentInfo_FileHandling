f = open('Students.txt','r')
students = f.readlines()
f.close()
#print students

f = open('Marks.txt','r')
marks = f.readlines()
f.close()


stud = {}
for i in range(len(students)):
	temp = students[i]
	templist = temp.split(",")
	templist[4] =templist[4].replace("\n", "")
	stud[templist[0]]=templist[1:]


sub_mark={}
for j in range(len(marks)):
	temp2 = marks[j]
	templist2 = temp2.split(",")
	templist2[10] =templist2[10].replace("\n", "")
	sub_mark[templist2[0]]=templist2[1:]


for key in stud:
	sub={}
	if key in sub_mark:
		temp_list=sub_mark[key]
		for i in range(0,len(temp_list),2):
			sub[temp_list[i]]=temp_list[i+1]
		stud[key].append(sub)
print stud
flag=1

while flag==1:
	print "-----------------------"
	print "MENU"
	print "1.Add New Student\n2.Show total Boys and Girls in school\n3.Percentage of all student\n4.Class topper\n5.Total Student in Every year\n6.Display student info\n7.Exit"
	print "-----------------------"
	choice=int(raw_input('Enter youe choice:'))
	if choice==1:
		loc_sub={'SUB1':'','SUB2':'','SUB3':'','SUB4':'','SUB5':''}
		name=raw_input('Enter student name:')
		gender=raw_input('Enter gender(M/F):')
		clas=raw_input('Enter class(FE/SE/TE/BE):')
		div=raw_input('Enter division(A/B/C/D):')
		for s in loc_sub:
			loc_sub[s]=raw_input('Enter marks for %s:' %s)
		roll=str(len(stud)+1)
		stud[roll]=[name,gender.upper(),clas.upper(),div.upper(),loc_sub]
		print 'Student Added'
		print stud

	elif choice==2:
		boys=0
		girls=0
		for key in stud:
			if(stud[key][1]=='M'):
				boys=boys+1
			else:
				girls=girls+1
		print 'Total Boys:',boys
		print 'Total Girls:',girls

	elif choice==3:
		for key in stud:
			total_mrk=0
			for s in stud[key][4]:
				total_mrk+=int(stud[key][4][s])
			perc=(total_mrk/5)
			print "Roll no %s %s has percentage: %d%%" %(key,stud[key][0],perc)

	elif choice==4:
		flg=1
		temp_stud={}
		marks_dict={}
		while flg==1:
			#checking if correct class and divison is being entered
			clas=raw_input('Enter the class(FE/SE/TE/BE):').upper()
			if (clas=='FE' or clas=='SE' or clas=='TE' or clas=='BE'):
				div=raw_input('Enter division(A/B/C/D):').upper()
				if(div=='A' or div=='B' or div=='C' or div=='D'):
					flg=0
					for k in stud:
						if stud[k][2]==clas and stud[k][3]==div:
							temp_stud[k]=stud[k]
					if ( temp_stud=={}):
						print "Sorry! No student found class:%s and div: %s" %(clas,div)
					#Calculating total marks of each student and creating dictionary of roll number and marks
					for st in temp_stud:
						total_mark=0
						subjects=temp_stud[st][4]
						for sub in subjects:
							total_mark+=int(subjects[sub])
						marks_dict[st]=total_mark
					#print marks_dict

					#Finding topper out of dictionary
					v=marks_dict.values()
					k=marks_dict.keys()
					topper=k[v.index(max(v))]
					print "class topper is roll no:%s" %topper
				else:
					print 'Wrong division. Please enter again.'
			else:
				print 'Wrong Class. Please enter again.'

	elif choice==5:
		flg=1
		while flg==1:
			clas=raw_input('Enter the class(FE/SE/TE/BE):').upper()
			if (clas=='FE' or clas=='SE' or clas=='TE' or clas=='BE'):
				flg=0
				class_count=0
				for st in stud:
					if stud[st][2]==clas:
						class_count+=1
				print "Total student in %s are: %d" %(clas,class_count)

			else:
				print "Wrong class entered! Please try again."
	elif choice==6:
		flg=1
		while flg==1:
			clas=raw_input('Enter the class(FE/SE/TE/BE):').upper()
			if (clas=='FE' or clas=='SE' or clas=='TE' or clas=='BE'):
				div=raw_input('Enter division(A/B/C/D):').upper()
				if(div=='A' or div=='B' or div=='C' or div=='D'):
					flg=0
					roll=raw_input("Enter roll number:")
					if roll in stud:
						if stud[roll][2]==clas and stud[roll][3]==div:
							print "Student Name:%s \nGender:%s" %(stud[roll][0],stud[roll][1])
							for sub in stud[roll][4]:
								print "Subject:%s, Marks:%s" %(sub,stud[roll][4][sub])
						else:
							print "No student with roll no:%s in this class" %roll
					else:
						print "No student with roll no:%s" %roll

				else:
					print 'Wrong division. Please enter again.'

			else:
				print "Wrong class entered! Please try again."
	

	elif choice==7:
		list1=[]
		for key in range (1,len(stud)+1):
			if key!= len(stud):
				temp=str(key)+","+str(stud[str(key)][0])+","+str(stud[str(key)][1])+","+str(stud[str(key)][2])+","+str(stud[str(key)][3])+"\n"
				list1.append(temp)
			else:
				temp=str(key)+","+str(stud[str(key)][0])+","+str(stud[str(key)][1])+","+str(stud[str(key)][2])+","+str(stud[str(key)][3])
				list1.append(temp)

		list2=[]
		for key in range (1,len(stud)+1):
			subject=stud[str(key)][4]
			if key!= len(stud):
				temp2=str(key)+","+"SUB1"+","+subject['SUB1']+","+"SUB2"+","+subject['SUB2']+","+"SUB3"+","+subject['SUB3']+","+"SUB4"+","+subject['SUB4']+","+"SUB5"+","+subject['SUB5']+"\n"
				list2.append(temp2)
			else:
				temp2=str(key)+","+"SUB1"+","+subject['SUB1']+","+"SUB2"+","+subject['SUB2']+","+"SUB3"+","+subject['SUB3']+","+"SUB4"+","+subject['SUB4']+","+"SUB5"+","+subject['SUB5']
				list2.append(temp2)

		f=open("Students.txt",'w')
		f.writelines(list1)
		f.close()

		f=open("Marks.txt",'w')
		f.writelines(list2)
		f.close()

		print "Data updated in file"
		print "Bye!"
		flag=0
	else:
		print 'Wrong Input! Try again..'
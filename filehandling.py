a=open("file handling.txt","r")#read is used for read the the one file or data
#a=open("file handling.txt","w")#this like a override,override meaning is delete existing data and add the new value of data.
#a=open("file handling.txt","a")#a is append,it's used for add the new value in existing file
#print(a.read())
a.write("banana")#a.close() #if you use write function it it will be create a new data or values and errase the existing datas
a.write("graes","nuts")

a.close()
print(a.read)



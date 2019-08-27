
file = open('/home/agustina/da-academy/week0/text.txt', 'w')

file.write("this is my first file \n")
file.write("this is the second line \n")
file.write("this is the third line \n")
file.write("this is the fourth line \n")
file.close()

file = open('/home/agustina/da-academy/week0/text.txt', 'r')
listdata = file.readlines()
print(listdata)
listdata[2] = "This is the SECOND LINE \n"
print(listdata)
file.close()

file = open('/home/agustina/da-academy/week0/text.txt', 'w')
file.writelines(listdata)
file.close()

file = open('/home/agustina/da-academy/week0/text.txt', 'r')
print(file.readlines())
file.close()

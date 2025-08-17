# Append to an existing file called rayan malik.txt
# it should add data about rayan malik's Hometown

f = open("17_FILES/rayan malik.txt","a")
string = '''
Rayan malik initially lived in phoenix , Arizona. He is a very nice guy
'''
f.write(string)

f.close()
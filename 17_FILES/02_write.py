# write to a file called rayan malik.txt
# it should contain data about rayan malik

f = open("rayan malik.txt","w")
string = '''
 Rayan is a nice guy. He lives in the Nyc and he works with python 
 his favorite package is pandas
'''
f.write(string)

f.close()
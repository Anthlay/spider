import string
d1 = "I like to watch the sun set with my friend"
d2 = "The Best Places To Watch The Sunset"
d3 = "My friend watch the sun come up"
str = input("please input a word: ")
if(d1.find(str,len(d1))==-1):
    print("d1")
elif(d2.find(str,len(d2))==-1):
    print("d2")
elif(d3.find(str,len(d3))==-1):
    print("d3")
else: 
    print("no match!")




'''
if(re.match(str,d1)!=None):
    print("d1")
elif(re.match(str,d2)!=None):
    print("d2")
elif(re.match(str,d3)!=None):
    print("d3")
else:
    print("nothing matched!")
    '''
    
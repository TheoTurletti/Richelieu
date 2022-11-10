import os 

f = open("french_passwords_top20000.txt", "r")
fw = open("new.txt" , "w")

for line in f :
    fw.write(line.title())


f.close()
fw.close()
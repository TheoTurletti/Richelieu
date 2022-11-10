f = open("richelieu_40k_min_maj.txt", "r")
fw = open("richelieu_min_maj_depart_4M.txt" , "w")

for line in f :
    fw.write(line)

for i in range(100):
    f.close()
    f = open("richelieu_40k_min_maj.txt", "r")
    for line in f :    
        j = "%02d" % i
        fw.write(line.replace('\n', j + '\n'))


f.close()
fw.close()
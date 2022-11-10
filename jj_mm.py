f = open("richelieu_40k_min_maj.txt", "r")
fw = open("richelieu_min_maj_jj_mm_15M.txt" , "w")


for i in range(33):
    for k in range(13):
        f.close()
        f = open("richelieu_40k_min_maj.txt", "r")
        for line in f :    
            j = "%02d" % i
            z = "%02d" % k
            fw.write(line.replace('\n', j + z+'\n'))


f.close()
fw.close()
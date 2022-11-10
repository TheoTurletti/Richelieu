f = open("richelieu_40k_min_maj.txt", "r")
fw = open("richelieu_min_maj_annee.txt" , "w")

for i in range(1970,2030):
    f.close()
    f = open("richelieu_40k_min_maj.txt", "r")
    for line in f :    
        fw.write(line.replace('\n', str(i) + '\n'))


f.close()
fw.close()
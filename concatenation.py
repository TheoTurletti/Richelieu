# Il faut ajouter une ligne vide à la fin de chaque fichier

filesname = ["richelieu_min_maj_depart_4M.txt","richelieu_min_maj_annee.txt","richelieu_min_maj_jj_mm_15M.txt"]

new_file = "Richelieu_23M_maj_depart_annee_jj_mm.txt"
with open(new_file, "w") as new_file:
    for name in filesname:
        with open(name) as f:
            for line in f:
                new_file.write(line)
            
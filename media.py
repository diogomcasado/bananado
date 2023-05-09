import glob
import math
import os
from statistics import mean 

media_txt = "site/precos/media.txt"

avg_valores_rounded = 0


def getMedia():
    file_list = glob.glob(os.path.join(os.getcwd(), "site\\precos", "*.txt"))

    file_list.remove(os.path.join(os.getcwd(), "site\\precos\\last_update.txt"))

    try:
        file_list.remove(os.path.join(os.getcwd(), "site\\precos\\media.txt"))
    except:
        pass

    valores_orig = []

    #le valores do ficheiro
    for file_path in file_list:
        with open(file_path) as f_input:
            valores_orig.append(f_input.read())

    #converte list to float
    valores_float = [float(x.strip(' "')) for x in valores_orig] 

    #calcula media
    avg_valores = mean(valores_float) 

    #arrendonda para 2 casas decimais
    avg_valores_rounded =  round(avg_valores, 2)

    print("Media de preços: " + str(avg_valores_rounded))

    file_object = open(media_txt, 'a')
    file_object.write(str(avg_valores_rounded))
    file_object.close()




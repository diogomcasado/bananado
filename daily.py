from datetime import date
import json

#import os
#clear = lambda: os.system('cls')
#clear()
def recordDaily():
    today = date.today()


    last_update_txt = "registos/last_update_registo.txt"

    continente_txt = "site/precos/continente.txt"
    auchan_txt = "site/precos/auchan.txt"
    aperinha_txt = "site/precos/aperinha.txt"
    minipreco_txt = "site/precos/minipreco.txt"

    continente_preco = 0
    auchan_preco = 0
    aperinha_preco = 0
    minipreco_preco = 0

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("Data de hoje: ", d1)


    with open(last_update_txt) as f:
        lines = f.readlines()
        last_update_datetime = lines[0]
        last_update = last_update_datetime[0:10]
        print("last_update =", last_update)

    if last_update == d1:
        print("Data de hoje já foi registada")

    else:
        print("Data de hoje ainda não foi registada")
        with open(continente_txt) as f:
            lines = f.readlines()
            continente_preco = lines[0]
            print("continente_preco =", continente_preco)

        with open(auchan_txt) as f:
            lines = f.readlines()
            auchan_preco = lines[0]
            print("auchan_preco =", auchan_preco)

        with open(aperinha_txt) as f:
            lines = f.readlines()
            aperinha_preco = lines[0]
            print("aperinha_preco =", aperinha_preco)
        
        with open(minipreco_txt) as f:
            lines = f.readlines()
            minipreco_preco = lines[0]
            print("minipreco_preco =", minipreco_preco)

        with open('registos/diario.txt') as f:
            data = f.read()

            print("Data type before reconstruction : ", type(data))

            json_daily = json.loads(data)

            print(json_daily)

            json_daily["data"].append(d1)
            json_daily["continente"].append(continente_preco)
            json_daily["auchan"].append(auchan_preco)
            json_daily["aperinha"].append(aperinha_preco)
            json_daily["minipreco"].append(minipreco_preco)

            with open("registos/diario.txt", "w") as outfile:
                json.dump(json_daily, outfile)
                print("Novo registo diário adicionado")

        # escreve data no ficheiro

        file_object = open(last_update_txt, 'w')
        file_object.write(d1)
        file_object.close()

        # executa script para obter media
        # getMedia()

        # executa script para obter grafico
        # graph()

        # executa script para obter media e grafico
        # daily()

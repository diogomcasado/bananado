def processar_preco(antes): 

    depois = antes

    depois = depois.replace("\n", "").strip()

    depois = depois.replace("€", "").strip()
    depois = depois.replace("/Kg", "").strip()
    depois = depois.replace("(", "").strip()
    depois = depois.replace(")", "").strip()
    depois = depois.replace(" .", "").strip()

    depois = depois.replace(",", ".").strip()

    #depois = depois + "€"

    return depois

def clean(txt):
    open(txt, 'w').close()


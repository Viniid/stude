def prever_fruta(peso, textura, cor):
    if peso >= 0.130 and textura == "rough" and cor == "red":
        return "A fruta é uma maça!"
    elif peso >= 0.120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 0.150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 0.150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
      return "Não foi possível classificar a fruta."    

peso_fruta = float(input("quantas gramas?"))
textura_fruta = input("smooth ou rough ?")
cor_fruta = input("qual é a cor ?")

resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

print(resultado)
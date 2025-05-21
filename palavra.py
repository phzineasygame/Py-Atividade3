vogais = "aeiou"
contador_de_vogais = 0
palavra = input("Digite sua palavra.")


for letra in "palavra":
    if letra in vogais:
     contador_de_vogais += 1   
    
print(f"a palavra tem {contador_de_vogais} vogais presentes.")

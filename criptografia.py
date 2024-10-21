#Esse é um codigo simples que criptografa a letra pelo numero da posição dele no alfabeto! 

def criptografar(texto):
    resultado = []
    
    for x in texto:
        if x.isalpha():
            posicao = ord(x.lower()) - ord('a') + 1
            resultado.append(str(posicao))
        else:
            resultado.append(x)
        
    return " ".join(resultado)

texto = input("Digite a palavra que deseja criptografar: ")
criptografado = criptografar(texto)

print("Texto criptografado:", criptografado)
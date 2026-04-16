def sao_anagramas(string1, string2):
    # Todos: Implementar a lógica  
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()
    
    
    return sorted(s1) == sorted(s2) 
    
    pass

def cifra_de_cesar(texto, deslocamento):
    # Todos: Implementar a lógica
    resultado = ""

    for char in texto:
        if char.isalpha():
            
            base = ord('A') if char.isupper() else ord('a')
            #comentario
            
            nova_letra = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            resultado += char

    return resultado
    pass

def valida_cpf(cpf_string):
    # Todos: Implementar a lógica
    palavras = frase.split()
    maior = ""

    for palavra in palavras:
        # Remove pontuação
        palavra_limpa = palavra.strip(string.punctuation)

        if len(palavra_limpa) > len(maior):
            maior = palavra_limpa

    return maior
    
    pass
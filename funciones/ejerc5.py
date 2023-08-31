def verificarContrasenia(contrasenia):
    largo = len(contrasenia)
    if largo < 8:
        return False
    
    mayus = 0
    min = 0
    digit = 0

    
    for caracter in contrasenia:
        if caracter.isupper():
            mayus += 1
        if caracter.islower():
            min += 1
        if caracter.isdigit():
            digit += 1
        
    if mayus and min and digit > 0 :
        return True
    return False
    
print(verificarContrasenia("yasdasd6"))


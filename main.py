
def primo(x):
    i = 0
    for n in range(2, x):
        if n % 2 != 0:
            i += 1
    
    if i > 0:
        return False
        
    return True
    
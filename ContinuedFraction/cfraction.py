def generateContinuedFraction(number: int, maxDepth: int):
    
    f = number % 1 # Parte frazionaria
    i = number - f # Parte intera
    
    if f == 0 or maxDepth == 0:
        return [int(i)]
    
    return [int(i)] + generateContinuedFraction(1/f, maxDepth-1)
    
# Alla prima chiamata si salva il risultato e ritorna sempre quello. Adatta se la funzione è costante
def constantCache(function):
    def wrapper(*args, **kwargs):
        if 'result' not in wrapper.__dict__:
            wrapper.result = function(*args, **kwargs)
        return wrapper.result
    return wrapper 

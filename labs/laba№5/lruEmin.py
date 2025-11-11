
def lru(func):
    cache = {}  
    max_size = 5  

    def wrapper(n):
        if n in cache:
            return cache[n]  
        result = func(n)  
        cache[n] = result
        
        if len(cache) > max_size:
            del cache[next(iter(cache))]
        return result

    return wrapper


    




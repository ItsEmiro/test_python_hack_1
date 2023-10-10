"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    entrada = [1,2,3]
    result = []
    i = 0

    while i < len(entrada):
        result.append(entrada[i])
        result.append('@')
        i += 1
    
    return result  


print(fn_hack_9())
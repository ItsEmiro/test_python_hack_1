"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    text = "fooziman"
    result = []
    text = text.replace("o",'0').replace('i','1').replace('a','@')

    for letra in text:
        result.append(letra.capitalize())
    
   
    return result  


print(fn_hack_10())


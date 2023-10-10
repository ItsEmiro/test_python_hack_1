"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    upper = result[:-1] + result[-1].capitalize()
    return upper


print(fn_hack_4())
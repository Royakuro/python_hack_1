"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 0
    while i < 7:
        result.insert(i+1, '@')
        i += i+2
    return result

fn_hack_9()

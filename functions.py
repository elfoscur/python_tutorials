def thing():
    print('hello im a function')

thing()

def thing_with_inputs(i_par1,i_par2,i_par3):
    print(i_par1)
    print(i_par2)
    print(i_par3)

thing_with_inputs(3,4,5)

def greet(lang):
    if lang == 'es':
        print('hola')
        return('hola')
    elif lang == 'eng':
        print('hello')
        return('hello')
    elif lang =='it':
        print('ciao')
        return('ciao')
    else:
        print('boooooooooooh')
        return('boooooooooooh')

v_greet = greet('jp')
print('vgreet='+v_greet)


def addtwo(a,b):
    added=a+b
    return added

print(addtwo(1,2))    

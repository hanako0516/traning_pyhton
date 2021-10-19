import src.parts.dic_and_method as dic_and_method

def logic(num1,num2):
    if num1>num2 :
        val = dic_and_method.calcuration('hiki',num1,num2)
    elif num1 == num2  :
        val = dic_and_method.calcuration('add',num1,num2)
    else:
        val = dic_and_method.calcuration('kake',num1,num2)

    return 'リターンは'+ str(val) + 'です。'
    

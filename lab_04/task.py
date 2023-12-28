mathSymb = ('-', '*', '+', '^', '/')
numbers = ('0','1','2','3','4','5','6','7','8','9')

def Response(input):

    stack = []
    output = []
    
    for token in input:

        if Ncheck(token):
            output.append(token)
            continue
            
        if token == '(':
            stack.append(token)
            continue
        
        if token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            continue    
        
        if token in mathSymb:

            opPrior = prior(token)
            while stack and stack[-1] in mathSymb and prior(stack[-1]) >= opPrior:
                output.append(stack.pop())
            stack.append(token)
            
    while stack:

        output.append(stack.pop())
        
    return output

def Ncheck(numm):
    return all(char in numbers for char in numm)

def mat(respons):

    stack = []
    
    for token in respons:

        if Ncheck(token):

            stack.append(int(token))
        else:
            operandNumTwo = stack.pop()
            operandNumOne = stack.pop()
            result = 0
            
            if token == '+':
                result = operandNumOne + operandNumTwo
            elif token == '-':
                result = operandNumOne - operandNumTwo
            elif token == '*':
                result = operandNumOne * operandNumTwo
            elif token == '/':
                result = operandNumOne / operandNumTwo
            elif token == '^':
                result = operandNumOne ** operandNumTwo
                
            stack.append(result)
            
    return stack
    
def prior(operation):

    if operation in ('+', '-'):
        return 0
    elif operation in ('*','/'):
        return 1
    elif operation == '^':
        return 2 
    
if __name__ == '__main__':
    input = "5-3^2+(7-2)^4"
    respons = Response(input)
    
    print("Reverse: ", respons)
    print("Result: ", mat(respons))
                


        

def linha(bar):
    return print("-" * bar)
    
def Ver_CPF(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    else:
        cpf = [int(digit) for digit in cpf]
        soma1 = sum(cpf[i] * (10 - i) for i in range(9))
        digito1 = (soma1 * 10 % 11) % 10
        soma2 = sum(cpf[i] * (11 - i) for i in range(10))
        digito2 = (soma2 * 10 % 11) % 10
        return digito1 == cpf[9] and digito2 == cpf[10]
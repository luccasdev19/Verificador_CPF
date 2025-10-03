import re
import sys

entrada = input ('Digite o CPF : ')
cpf_enviado = re.sub(r'[^0-9]', '', entrada )

if len(cpf_enviado) !=  11 :
    print('O CPF deve constar 11 digitos!')
    sys.exit() 

entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len (cpf_enviado)

if entrada_e_sequencial : 
    print ('Você digitou dados Sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado[:9]  
contador_regressivo = 10 

resultado  = 0 

for digito in nove_digitos : 
    resultado += int(digito) * contador_regressivo 
    contador_regressivo -= 1 

digito_1 =  ((resultado * 10)  % 11 ) 
digito_1 = digito_1 if digito_1 <= 9 else 0 

dez_digitos = nove_digitos + str ( digito_1)
contador_regressivo_2 = 11

resultado_2 = 0 

for digito in dez_digitos : 
    resultado_2 += int (digito) * contador_regressivo_2
    contador_regressivo_2 -= 1 

digito_2 = ((resultado_2 * 10 ) % 11) 
digito_2 = digito_2 if digito_2 <= 9 else 0 

cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado_calculo == cpf_enviado : 
    print (f'{cpf_gerado_calculo} é um CPF valido! ')
else : 
    print('Cpf invalido, tente novamente. ')


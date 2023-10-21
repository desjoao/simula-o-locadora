#Prorama para locadora
#Variáveis a serem lidas do usuário: taxa fixa/dia; taxa por km rodado; nº de dias; nº por km rodado.
#Cálculo do valor: Taxa fixa/dia*0,9 + taxa km rodado
#Informações a serem exibidas: Valor total do aluguel; desconto dado; número de dias; km rodados.

dia = int(input('Insira a quantidade de diárias: '))
km = float(input('Insira o número de kilometros rodados: '))
tx_dia = float(input('Insira a taxa incidente sobre as diárias: '))
tx_km = float(input('Insira a taxa incidente sobre os kilometros rodados: '))

print(f'O valor final do aluguel para {dia} diárias, com {km} kilometros rodados é de: R${dia*tx_dia*0.9 + km*tx_km:.2f} reais, sendo o desconto total de R${dia*tx_dia*0.1:.2f} reais.')

      

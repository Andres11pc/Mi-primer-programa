
pokemon_elegido = input('¿Contra que pokemon quieres luchar? (Squirtle / Charmander / Bulbasaur): ').upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == 'SQUIRTLE':
    vida_enemigo = 90

if pokemon_elegido == 'CHARMANDER':
    vida_enemigo = 80

if pokemon_elegido == 'BULBASAUR':
    vida_enemigo = 100

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input('¿Qué ataque vamos a usar? (Chispazo / Bola voltio): ').upper()
    if ataque_elegido == 'CHISPAZO':
        vida_enemigo -= 10
    if ataque_elegido == 'BOLA VOLTIO':
        vida_enemigo -= 12

    if pokemon_elegido =='SQUIRTLE':
        print('Squirtle te hace un ataque de 8 de daño')
        vida_pikachu -= 8
    if pokemon_elegido == 'CHARMANDER':
        print('Charmander te hace un ataque de 7 de daño')
        vida_pikachu -= 7
    if pokemon_elegido == 'BULBASAUR':
        print('Bulbasaur te hace un ataque de 10 de daño')
        vida_pikachu -= 10



print('El combate ha terminado')
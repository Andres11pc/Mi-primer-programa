

apetece_helado_input = input('¿Te apetece un helado? (Si / No): ').upper()

if apetece_helado_input == 'SI':
    apetece_helado = True
elif apetece_helado_input == 'NO':
    apetece_helado = False
else:
    print('Te he dicho que me digas si o no, no se que has dicho pero cuento como que no')
    apetece_helado = False

tiene_dinero_input = input('¿Tienes dinero para un helado? (Si / No): ').upper()

if tiene_dinero_input == 'SI':
    tiene_dinero = True
elif tiene_dinero_input == 'NO':
    tiene_dinero = False
else:
    print('Te he dicho que me digas si o no, no se que has dicho pero cuento como que no')
    tiene_dinero = False

esta_el_senor_helados_input = input('¿Esta de señor de los helados? (Si / No): ').upper()

if esta_el_senor_helados_input == 'SI':
    esta_el_senor_helados = True
elif esta_el_senor_helados_input == 'NO':
    esta_el_senor_helados = False
else:
    print('Te he dicho que me digas si o no, no se que has dicho pero cuento como que no')
    esta_el_senor_helados = False

esta_tu_tia_input = input('¿Estas con tu tia? (Si / No): ').upper()

if esta_tu_tia_input == 'SI':
    esta_tu_tia = True
elif esta_tu_tia_input == 'NO':
    esta_tu_tia = False
else:
    print('Te he dicho que me digas si o no, no se que has dicho pero cuento como que no')
    esta_tu_tia = False

puede_permitirselo = tiene_dinero_input == 'SI' or esta_tu_tia_input == 'SI'
esta_el_senor_helados = esta_el_senor_helados_input == 'SI'


if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print('Pues comete un helado')
else:
    print('Pues nada')
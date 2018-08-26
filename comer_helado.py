
apetece_helado_input = input('¿Te apetece un helado? (Si / No): ').upper()
tiene_dinero_input = input('¿Tienes dinero para un helado? (Si / No): ').upper()
esta_el_senor_helados_input = input('¿Esta de señor de los helados? (Si / No): ').upper()
esta_tu_tia_input = input('¿Estas con tu tia?').upper()

apetece_helado = apetece_helado_input == 'SI'
puede_permitirselo = tiene_dinero_input == 'SI' or esta_tu_tia_input == 'SI'
esta_el_senor_helados = esta_el_senor_helados_input == 'SI'


if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print('Pues comete un helado')
else:
    print('Pues nada')
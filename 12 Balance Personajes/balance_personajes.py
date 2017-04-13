caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

caballero['vida'], caballero['defensa'] = guerrero['vida']*2, guerrero['defensa'] *2
guerrero['ataque'], guerrero['alcance'] = caballero['ataque']*2, caballero['alcance'] *2
arquero['vida'], arquero['ataque'] = guerrero['vida'], guerrero['ataque']
arquero['defensa'], arquero['alcance'] = guerrero['defensa']/2, guerrero['alcance']*2

print('Caballero stats: ',caballero)
print('Guerrero stats: ',guerrero)
print('Arquero stats: ',arquero)

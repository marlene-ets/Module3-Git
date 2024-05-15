""""
Ce script affiche des messages de bienvenue
"""

flag_polite = input('Pouvons nous vous tutoyer ? [oui/non]\n')

if flag_polite == 'oui':
    last_name = input('Quel est ton nom de famille ?\n')
    first_name = input('Quel est ton prenom ?\n')
    message = f"Salut à toi {first_name} {last_name} ! Content de te compter dans l'équipe."
else:
    last_name = input('Quel est votre nom de famille ?')
    first_name = input('Quel est votre prenom ?')
    message = f'Bienvenue {first_name} {last_name} ! Nous sommes très fiers de vous comptez parmi nous'


print(message)


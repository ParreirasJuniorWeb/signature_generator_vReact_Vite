"""
Configurações de cores para geração de assinaturas.
Define as cores utilizadas na assinatura de e-mail.
"""

# Cores RGB utilizadas na assinatura
COLORS = {
    'purple': (131, 35, 112),
    'darkPurple': (122, 48, 100),
    'purpleLight': (137, 71, 118),
    'orange': (254, 159, 33),
    'orangeLight': (207, 163, 105)
}

# Mapeamento de cores por elemento
COLOR_MAPPING = {
    'name': 'purple',
    'jobTitle': 'purple',
    'department': 'orange',
    'phoneNumber': 'darkPurple',
    'telephoneNumber': 'darkPurple',
    'email': 'darkPurple',
    'adress': 'darkPurple'
}

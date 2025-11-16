"""
Configurações de coordenadas para posicionamento de texto na assinatura.
Define as posições (x, y) onde cada elemento será desenhado na imagem.
"""

# Coordenadas (x, y) para cada elemento da assinatura
COORDS = {
    'name': (53, 68),
    'nameSmall': (53, 80),
    'jobTitle': (53, 117),
    'department': (53, 160),
    'phoneNumber': (90, 285),
    'telephoneNumber': (216, 285),
    'email': (90, 325),
    'adress': (90, 368)
}

# Tamanho final da imagem
FINAL_SIZE = (800, 641)

# Margens e espaçamentos
MARGINS = {
    'left': 53,
    'top': 68,
    'between_lines': 10
}

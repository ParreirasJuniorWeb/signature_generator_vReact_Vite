"""
Configurações de fontes para geração de assinaturas.
"""
import os
from pathlib import Path

# Diretório base das fontes
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FONTS_DIR = BASE_DIR / 'static' / 'fonts'

# Caminhos das fontes
FONTS = {
    'default': str(FONTS_DIR / 'arial.ttf'),
    'negrito': str(FONTS_DIR / 'ariblk.ttf'),
    'negritoLow': str(FONTS_DIR / 'arialbd.ttf'),
    'semicond': str(FONTS_DIR / 'arialnb.TTF')
}

# Configurações de tamanhos de fonte
FONTS_CONFIG = {
    'name': {
        'font': 'negrito',
        'sizes': {
            'extra_large': 40,  # < 19 caracteres
            'large': 28,        # 20-27 caracteres
            'medium': 20,       # 28-39 caracteres
            'small': 16,        # 40-49 caracteres
            'extra_small': 14,  # 50-58 caracteres
            'tiny': 12          # > 58 caracteres
        },
        'thresholds': {
            'extra_large': 19,
            'large': 27,
            'medium': 39,
            'small': 49,
            'extra_small': 58
        }
    },
    'jobTitle': {
        'font': 'negrito',
        'sizes': {
            'large': 20,        # < 35 caracteres
            'medium': 18,       # 36-45 caracteres
            'small': 14,        # 46-59 caracteres
            'extra_small': 12   # > 59 caracteres
        },
        'thresholds': {
            'large': 35,
            'medium': 45,
            'small': 59
        }
    },
    'department': {
        'font': 'semicond',
        'size': 18
    },
    'info': {
        'font': 'negritoLow',
        'size': 18
    },
    'infoBold': {
        'font': 'semicond',
        'size': 22
    }
}

# Tamanhos máximos
MAX_SIZE_MEDIUM = 22
MAX_SIZE_LONG = 30

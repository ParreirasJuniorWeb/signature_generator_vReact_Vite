"""
Serviço de geração de assinaturas.
Responsável por gerar a imagem da assinatura de e-mail.
"""
import io
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Any

from app.constants import FONTS, COLORS, COORDS, FONTS_CONFIG
from app.constants.coordinates import FINAL_SIZE
from app.utils.exceptions import ImageGenerationError, FileNotFoundError as CustomFileNotFoundError
from app.utils.logger import get_logger

logger = get_logger(__name__)


class SignatureService:
    """Serviço responsável pela geração de assinaturas."""
    
    def __init__(self, config):
        """
        Inicializa o serviço de assinatura.
        
        Args:
            config: Configuração da aplicação
        """
        self.config = config
        self.signature_template = config.get('SIGNATURE_TEMPLATE')
        self.fonts_folder = config.get('FONTS_FOLDER')
        
    def _get_font_size_for_text(self, text: str, field: str) -> int:
        """
        Determina o tamanho da fonte baseado no comprimento do texto.
        
        Args:
            text: Texto a ser renderizado
            field: Campo (name ou jobTitle)
            
        Returns:
            Tamanho da fonte
        """
        text_length = len(text)
        font_config = FONTS_CONFIG.get(field, {})
        thresholds = font_config.get('thresholds', {})
        sizes = font_config.get('sizes', {})
        
        if field == 'name':
            if text_length <= thresholds.get('extra_large', 19):
                return sizes.get('extra_large', 40)
            elif text_length <= thresholds.get('large', 27):
                return sizes.get('large', 28)
            elif text_length <= thresholds.get('medium', 39):
                return sizes.get('medium', 20)
            elif text_length <= thresholds.get('small', 49):
                return sizes.get('small', 16)
            elif text_length <= thresholds.get('extra_small', 58):
                return sizes.get('extra_small', 14)
            else:
                return sizes.get('tiny', 12)
        
        elif field == 'jobTitle':
            if text_length <= thresholds.get('large', 35):
                return sizes.get('large', 20)
            elif text_length <= thresholds.get('medium', 45):
                return sizes.get('medium', 18)
            elif text_length <= thresholds.get('small', 59):
                return sizes.get('small', 14)
            else:
                return sizes.get('extra_small', 12)
        
        return 18  # Tamanho padrão
    
    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """
        Carrega todas as fontes necessárias.
        
        Returns:
            Dicionário com as fontes carregadas
            
        Raises:
            CustomFileNotFoundError: Se alguma fonte não for encontrada
        """
        try:
            fonts_pil = {
                'name': ImageFont.truetype(FONTS['negrito'], 40),
                'fontLarge': ImageFont.truetype(FONTS['negrito'], 28),
                'fontMedium': ImageFont.truetype(FONTS['negrito'], 20),
                'fontDefault': ImageFont.truetype(FONTS['negrito'], 18),
                'fontSmall': ImageFont.truetype(FONTS['negrito'], 16),
                'fontMoreSmall': ImageFont.truetype(FONTS['negrito'], 14),
                'fontMoreSmall2': ImageFont.truetype(FONTS['negrito'], 12),
                'department': ImageFont.truetype(FONTS['semicond'], 18),
                'info': ImageFont.truetype(FONTS['negritoLow'], 18),
                'infoBold': ImageFont.truetype(FONTS['semicond'], 22)
            }
            return fonts_pil
        except OSError as e:
            logger.error(f"Erro ao carregar fontes: {e}")
            raise CustomFileNotFoundError(f"Fonte não encontrada: {e}")
    
    def _wrap_text(self, text: str, max_chars: int) -> list:
        """
        Quebra o texto em múltiplas linhas se necessário.
        
        Args:
            text: Texto a ser quebrado
            max_chars: Número máximo de caracteres por linha
            
        Returns:
            Lista de linhas
        """
        if len(text) <= max_chars:
            return [text]
        
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word)
            # +1 para o espaço
            if current_length + word_length + len(current_line) <= max_chars:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = word_length
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def _draw_name(self, draw: ImageDraw.Draw, name: str, fonts: Dict) -> None:
        """
        Desenha o nome na assinatura.
        
        Args:
            draw: Objeto ImageDraw
            name: Nome a ser desenhado
            fonts: Dicionário de fontes
        """
        name_length = len(name)
        
        # Para nomes muito longos (> 70 caracteres), quebra em múltiplas linhas
        if name_length > 70:
            lines = self._wrap_text(name, 60)
            font = fonts['fontMoreSmall2']
            y_offset = COORDS['nameSmall'][1]
            line_height = 14  # Altura da linha para fonte tamanho 12
            
            for i, line in enumerate(lines[:2]):  # Máximo 2 linhas
                draw.text(
                    (COORDS['nameSmall'][0], y_offset + (i * line_height)),
                    line,
                    font=font,
                    fill=COLORS['purple']
                )
        elif name_length > 58:
            draw.text(COORDS['nameSmall'], name, font=fonts['fontMoreSmall2'], fill=COLORS['purple'])
        elif name_length > 49:
            draw.text(COORDS['nameSmall'], name, font=fonts['fontMoreSmall'], fill=COLORS['purple'])
        elif name_length > 39:
            draw.text(COORDS['nameSmall'], name, font=fonts['fontSmall'], fill=COLORS['purple'])
        elif name_length > 27:
            draw.text(COORDS['name'], name, font=fonts['fontMedium'], fill=COLORS['purple'])
        elif name_length > 19:
            draw.text(COORDS['name'], name, font=fonts['fontLarge'], fill=COLORS['purple'])
        else:
            draw.text(COORDS['name'], name, font=fonts['name'], fill=COLORS['purple'])
    
    def _draw_job_title(self, draw: ImageDraw.Draw, job_title: str, fonts: Dict) -> None:
        """
        Desenha o cargo na assinatura.
        
        Args:
            draw: Objeto ImageDraw
            job_title: Cargo a ser desenhado
            fonts: Dicionário de fontes
        """
        job_length = len(job_title)
        
        if job_length > 59:
            draw.text(COORDS['jobTitle'], job_title, font=fonts['fontMoreSmall2'], fill=COLORS['purple'])
        elif job_length > 45:
            draw.text(COORDS['jobTitle'], job_title, font=fonts['fontMoreSmall'], fill=COLORS['purple'])
        elif job_length > 35:
            draw.text(COORDS['jobTitle'], job_title, font=fonts['fontDefault'], fill=COLORS['purple'])
        else:
            draw.text(COORDS['jobTitle'], job_title, font=fonts['fontMedium'], fill=COLORS['purple'])
    
    def generate_signature(self, user_data: Dict[str, Any]) -> io.BytesIO:
        """
        Gera a imagem da assinatura.
        
        Args:
            user_data: Dados normalizados do usuário
            
        Returns:
            BytesIO contendo a imagem PNG
            
        Raises:
            ImageGenerationError: Se houver erro na geração
        """
        logger.info("Iniciando geração da assinatura")
        
        try:
            # Verifica se o template existe
            if not self.signature_template.exists():
                raise CustomFileNotFoundError(str(self.signature_template))
            
            # Carrega a imagem template
            img = Image.open(self.signature_template).convert("RGBA")
            draw = ImageDraw.Draw(img)
            
            # Carrega as fontes
            fonts = self._load_fonts()
            
            # Desenha o nome
            self._draw_name(draw, user_data.get('fullName', ''), fonts)
            
            # Desenha o cargo
            self._draw_job_title(draw, user_data.get('jobTitle', ''), fonts)
            
            # Desenha o departamento
            draw.text(
                COORDS['department'],
                user_data.get('department', ''),
                font=fonts['department'],
                fill=COLORS['orange']
            )
            
            # Desenha o telefone
            draw.text(
                COORDS['phoneNumber'],
                user_data.get('phoneNumber', ''),
                font=fonts['info'],
                fill=COLORS['darkPurple']
            )
            
            # Desenha o celular (se fornecido)
            telephone_number = user_data.get('telephoneNumber')
            if telephone_number:
                draw.text(
                    COORDS['telephoneNumber'],
                    f"/ {telephone_number}",
                    font=fonts['info'],
                    fill=COLORS['darkPurple']
                )
            
            # Desenha o e-mail
            draw.text(
                COORDS['email'],
                user_data.get('email', ''),
                font=fonts['info'],
                fill=COLORS['darkPurple']
            )
            
            # Desenha o endereço
            draw.text(
                COORDS['adress'],
                user_data.get('adress', ''),
                font=fonts['info'],
                fill=COLORS['darkPurple']
            )
            
            # Redimensiona a imagem
            img_resized = img.resize(FINAL_SIZE, Image.Resampling.LANCZOS)
            
            # Salva em buffer de memória
            buffer_memory = io.BytesIO()
            img_resized.save(buffer_memory, format=self.config.get('IMAGE_FORMAT', 'PNG'))
            buffer_memory.seek(0)
            
            logger.info("Assinatura gerada com sucesso")
            return buffer_memory
            
        except CustomFileNotFoundError as e:
            logger.error(f"Arquivo não encontrado: {e}")
            raise ImageGenerationError(
                "Erro ao gerar assinatura: arquivo de template não encontrado",
                details=str(e)
            )
        except Exception as e:
            logger.error(f"Erro inesperado ao gerar assinatura: {e}")
            raise ImageGenerationError(
                "Ocorreu um erro inesperado durante a geração da assinatura",
                details=str(e)
            )

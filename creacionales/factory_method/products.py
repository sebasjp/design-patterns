import pandas as pd
from PIL import Image
from PyPDF2 import PdfReader
from abc import ABC, abstractmethod


# processor base o product base
class BaseDocumentProcessor(ABC):
    """
    Similar to Product:
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def extract_text(self, file_path: str) -> str:
        pass


# processor concretos o productos concretos
"""
Concrete Products provide various implementations of the Product interface.
"""

class PDFProcessor(BaseDocumentProcessor):
    def extract_text(self, file_path):
        # Ejemplo simplificado
        # concatenacion de todas las paginas separadas salto de linea
        reader = PdfReader(file_path)
        return "\n\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

class ImageProcessor(BaseDocumentProcessor):
    def extract_text(self, file_path):
        # Aquí se podría usar un LLM o visión por IA
        img = Image.open(file_path)
        return f"Descripción generada para imagen: {file_path}"

class ExcelProcessor(BaseDocumentProcessor):
    def extract_text(self, file_path):
        # La idea aquí es implementar la logica para procesar exceles
        df = pd.read_excel(file_path)
        return df.to_string(index=False)

from abc import ABC, abstractmethod
from creacionales.factory_method.products import (
    BaseDocumentProcessor, 
    PDFProcessor, 
    ImageProcessor, 
    ExcelProcessor
)

# creator class
class DocumentProcessorFactory(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    @abstractmethod
    def create_processor(self) -> BaseDocumentProcessor:
        pass


# creators concrete
"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""

class PDFProcessorFactory(DocumentProcessorFactory):
    def create_processor(self):
        return PDFProcessor()

class ImageProcessorFactory(DocumentProcessorFactory):
    def create_processor(self):
        return ImageProcessor()

class ExcelProcessorFactory(DocumentProcessorFactory):
    def create_processor(self):
        return ExcelProcessor()

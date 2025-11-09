from creacionales.factory_method.creators import DocumentProcessorFactory

def index_document(factory: DocumentProcessorFactory, file_path: str):
    """
    El código del cliente trabaja con una instancia de un creador concreto, 
    aunque a través de su interfaz base.
    Por ejemplo en este caso, la idea de esta funcion es indexar cualquiera
    de los tipos de documentos implementados (productos)
    """
    processor = factory.create_processor()
    text = processor.extract_text(file_path)
    print(f"Indexando: {text[:200]}...")
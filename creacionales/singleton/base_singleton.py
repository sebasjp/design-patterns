class SingletonMeta(type):
    
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            print(f"[SingletonMeta] Creating new instance: {cls.__name__}")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"[SingletonMeta] Using an existing instance: {cls.__name__}")
        return cls._instances[cls]
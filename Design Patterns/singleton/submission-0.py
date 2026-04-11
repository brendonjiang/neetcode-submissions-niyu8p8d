class Singleton:

    # In python consider this method as the 'getInstance'
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = 0
        return cls._instance

    def getValue(self) -> str:
        return self._instance.value

    def setValue(self, value: str):
        self._instance.value = value

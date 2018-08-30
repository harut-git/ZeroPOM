class Singleton(type):
    __instance = None

    @staticmethod
    def inst():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton(type)
        return Singleton.__instance

    # single call check
    def __init__(self):
        print("Constructor called!")


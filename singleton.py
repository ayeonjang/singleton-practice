class Singleton:
    """하나의 인스턴스만 생성하고 재사용하는 Singleton 클래스."""

    _instance = None

    def __new__(cls):
        # 인스턴스가 없을 때만 새 객체를 만들고,
        # 이후 호출에서는 기존 객체를 반환한다.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Singleton()이 여러 번 호출되어도 상태를 초기화하지 않는다.
        if not hasattr(self, "count"):
            self.count = 0

    @classmethod
    def get_instance(cls):
        """Singleton 인스턴스를 반환한다."""
        return cls()

    def increment(self):
        """공유 카운터를 1 증가시킨다."""
        self.count += 1

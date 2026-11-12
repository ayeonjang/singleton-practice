from singleton import Singleton


def main():
    # 서로 다른 변수에 Singleton 인스턴스를 각각 저장한다.
    instance_a = Singleton.get_instance()
    instance_b = Singleton.get_instance()

    # 두 변수가 실제로 같은 객체를 가리키는지 확인한다.
    print("동일한 인스턴스인가?", instance_a is instance_b)
    print("instance_a id:", id(instance_a))
    print("instance_b id:", id(instance_b))

    # 첫 번째 참조로 상태를 변경하고 두 번째 참조로 확인한다.
    instance_a.increment()
    print("instance_a에서 증가시킨 후")
    print("instance_b에서 확인한 count:", instance_b.count)


if __name__ == "__main__":
    main()

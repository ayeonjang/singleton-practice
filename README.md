# Python Singleton 실습

## 1. 실습 개요

Python으로 Singleton(싱글톤) 패턴을 구현하고, 여러 참조가 하나의 인스턴스를 공유하는지 확인하는 실습입니다.

## 2. 개발 환경

- 언어: Python
- 실행 환경: Python 3.13.5
- 별도 외부 패키지: 없음

## 3. 파일 구성

- `singleton.py`: Singleton 클래스 구현
- `main.py`: 인스턴스 동일성 및 상태 공유 확인
- `.gitignore`: Python 캐시 및 가상환경 등 Git 제외 항목

## 4. 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
python main.py
```

Python 명령어가 `python3`으로 등록된 환경이라면 다음과 같이 실행할 수 있습니다.

```bash
python3 main.py
```

## 5. 실행 결과

```text
동일한 인스턴스인가? True
instance_a id: 139780240888096
instance_b id: 139780240888096
instance_a에서 증가시킨 후
instance_b에서 확인한 count: 1
```

`id()` 값은 실행할 때마다 달라질 수 있지만, 한 번의 실행 안에서는 두 값이 동일해야 합니다.

## 6. 구현 설명

Singleton 인스턴스는 `singleton.py`의 클래스 변수 `_instance`에 보관합니다. `__new__()` 메서드는 `_instance`가 비어 있을 때만 객체를 생성하고, 이후 요청에서는 이미 만들어진 객체를 반환합니다. 따라서 `get_instance()`를 여러 번 호출해도 새로운 객체가 만들어지지 않고 기존 객체가 반환됩니다. `instance_a is instance_b`의 결과가 `True`이고 두 변수에서 같은 `count` 값을 확인할 수 있으므로, 두 변수가 하나의 인스턴스와 그 상태를 공유한다는 것을 알 수 있습니다.

## 7. 확인 사항

- [x] Singleton 클래스 구현
- [x] 인스턴스 2회 요청
- [x] `is` 연산자로 동일 객체 비교
- [x] 첫 번째 참조에서 상태 변경
- [x] 두 번째 참조에서 변경된 상태 확인
- [x] 실행 결과 README 기록

"""리스트 작업에 사용하는 유틸리티."""

from collections.abc import Hashable, Iterable
from typing import TypeVar

T = TypeVar("T", bound=Hashable)


def remove_duplicates(items: Iterable[T]) -> list[T]:
    """처음 등장한 순서를 유지하며 중복을 제거한 새 리스트를 반환."""
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 3, 4]))

"""숫자 계산에 사용하는 유틸리티."""

from collections.abc import Sequence


def calculate_average(numbers: Sequence[float]) -> float:
    """숫자 시퀀스의 산술 평균을 반환한다.

    Args:
        numbers: 평균을 구할 숫자들의 리스트 또는 튜플.

    Returns:
        모든 원소의 합을 원소 개수로 나눈 값.

    Raises:
        ValueError: numbers가 비어 있을 경우.
    """
    if not numbers:
        raise ValueError("빈 시퀀스의 평균은 구할 수 없습니다.")

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(calculate_average([1, 2, 3, 4]))
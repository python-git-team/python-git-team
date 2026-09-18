def reverse_string(text: str) -> str:
    """문자열을 뒤집어 반환한다."""
    return text[::-1]


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string(""))
    print(reverse_string("한글"))
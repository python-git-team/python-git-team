from datetime import datetime


def format_date(date_text: str) -> str:
    """'YYYY-MM-DD' 형식 문자열을 한국어 날짜 표기로 전환한다.

    Args:
        date_text: 'YYYY-MM-DD' 형식의 문자열. 월/일은 두 자리여야 한다.

    Returns:
        '2026년 09월 14일' 형태의 문자열.

    Raises:
        ValueError: date_text가 형식에 맞지 않을 경우.
    """
    date = datetime.strptime(date_text, "%Y-%m-%d")

    return date.strftime("%Y년 %m월 %d일")

    if __name__ == "__main__":
        print(format_date("2026-09-17"))
from datetime import datetime


def format_date(date_text):
    date = datetime.strptime(date_text, "%Y-%m-%d")
    return date.strftime("%Y년 %m월 %d일")


if __name__ == "__main__":
    print(format_date("2026-09-14"))
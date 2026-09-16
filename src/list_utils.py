"""Utilities for working with lists."""


def remove_duplicates(items):
    """Return a new list without duplicates while preserving input order."""
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 3, 4]))

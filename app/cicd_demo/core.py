"""Core application logic."""

from collections.abc import Iterable


def greet(name: str) -> str:
    """Return a friendly message for a non-empty name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("名字不能为空")
    return f"你好，{cleaned_name}！CI/CD 运行成功。"


def add(numbers: Iterable[float]) -> float:
    """Add one or more numbers."""
    values = list(numbers)
    if not values:
        raise ValueError("至少需要一个数字")
    return sum(values)

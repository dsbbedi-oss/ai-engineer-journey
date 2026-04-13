def summarize_day(hours_studied: int, topic: str) -> str:
    return f"I studied {topic} for {hours_studied} hours today."


def total_hours(days: list[int]) -> int:
    return sum(days)


def average_hours(days: list[int]) -> float:
    return sum(days) / len(days)


if __name__ == "__main__":
    print(summarize_day(2, "Git and Python"))

    week = [1, 3, 2, 4]
    print("Total hours:", total_hours(week))
    print("Average hours:", average_hours(week))
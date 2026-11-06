from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    sorted_pairs_by_total,
)

# Задание 1: частоты слов
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

# Задание 2: темы
first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]

assert common_topics([], ["python", "sql"]) == []
assert all_topics([], ["python", "sql"]) == ["python", "sql"]

# Задание 3: запись
record = {"title": "Python", "hours": 4}
record["hours"] = 6
record["completed"] = False
assert record == {"title": "Python", "hours": 6, "completed": False}
pair = (record["title"], record["hours"])
name, hours = pair
assert name == "Python" and hours == 6

# Вариант 1: сводка и поиск
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
saved_copy = [r.copy() for r in records]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет такой") == []
assert totals_by_category([]) == {}

# Исходные записи не изменяются
assert records == saved_copy

# Дополнительно: список пар по убыванию суммы
assert sorted_pairs_by_total(records) == [
    ("основное", 7),
    ("дополнительное", 2),
]

print("Все проверки пройдены")

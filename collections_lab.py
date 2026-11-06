def word_counts(text):
    """Словарь «слово → количество»: нижний регистр, очистка .,!?;:, пропуск пустых."""
    counts = {}
    for word in text.split():
        cleaned = word.strip(".,!?;:").lower()
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(text):
    """Вывод пар по алфавиту."""
    counts = word_counts(text)
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Отсортированный список общих тем (через множество)."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Отсортированный список всех уникальных тем (через множество)."""
    return sorted(set(first) | set(second))


def totals_by_category(records):
    """Словарь сумм amount по категориям."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Названия записей указанной категории в исходном порядке."""
    result = []
    for record in records:
        if record["category"] == category:
            result.append(record["title"])
    return result


def sorted_pairs_by_total(records):
    """Дополнительно: список пар (category, total) по убыванию суммы, затем по имени."""
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))


if __name__ == "__main__":
    # Демонстрация задания 1
    text = input("Введите текст для подсчёта слов: ")
    print_word_counts(text)

    # Демонстрация задания 2
    first = input("Темы первого студента (через пробел): ").split()
    second = input("Темы второго студента (через пробел): ").split()
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")

    # Демонстрация задания 3
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False
    pair = (record["title"], record["hours"])
    name, hours = pair
    print(f"Запись: {record}")
    print(f"Пара: {name}, {hours}")

    # Демонстрация варианта 1
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    totals = totals_by_category(records)
    print("Сводка по категориям:")
    for cat in sorted(totals):
        print(f"  {cat}: {totals[cat]}")

    user_category = input("Введите категорию для поиска: ")
    print(f"Названия в категории '{user_category}': {titles_in_category(records, user_category)}")

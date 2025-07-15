import json

def load_problem(path):
    """
    Загружает задачу из JSON-файла.
    Формат задачи:
    {
        "id": "sum",
        "title": "Сумма двух чисел",
        "description": "...",
        "test_cases": [
            {"input": "2 3", "output": "5"},
            ...
        ],
        "time_limit": 1,
        "memory_limit": 64
    }
    """
    with open(path, encoding='utf-8') as f:
        problem = json.load(f)
    # Валидация основных полей
    required_fields = ['id', 'title', 'description', 'test_cases']
    for field in required_fields:
        if field not in problem:
            raise ValueError(f"Отсутствует обязательное поле задачи: {field}")
    if not isinstance(problem['test_cases'], list) or not problem['test_cases']:
        raise ValueError("Поле 'test_cases' должно быть непустым списком")
    for case in problem['test_cases']:
        if 'input' not in case or 'output' not in case:
            raise ValueError("Каждый тест-кейс должен содержать 'input' и 'output'")
    # Значения по умолчанию
    if 'time_limit' not in problem:
        problem['time_limit'] = 1
    if 'memory_limit' not in problem:
        problem['memory_limit'] = 64
    return problem
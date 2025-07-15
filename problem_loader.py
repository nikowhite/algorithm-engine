import json

def load_problem(path):
    """
    Loads a problem from a JSON file.
    Problem format:
    {
        "id": "sum",
        "title": "Sum of two numbers",
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
    # Validate required fields
    required_fields = ['id', 'title', 'description', 'test_cases']
    for field in required_fields:
        if field not in problem:
            raise ValueError(f"Missing required problem field: {field}")
    if not isinstance(problem['test_cases'], list) or not problem['test_cases']:
        raise ValueError("Field 'test_cases' must be a non-empty list")
    for case in problem['test_cases']:
        if 'input' not in case or 'output' not in case:
            raise ValueError("Each test case must contain 'input' and 'output'")
    # Default values
    if 'time_limit' not in problem:
        problem['time_limit'] = 1
    if 'memory_limit' not in problem:
        problem['memory_limit'] = 64
    return problem
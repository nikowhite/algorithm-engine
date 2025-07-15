import time

def run_test_cases(problem, solution_path, runner):
    """
    Runs the solution against all test cases of the problem.
    Returns a list of dictionaries with results for each test.
    """
    results = []
    for idx, case in enumerate(problem['test_cases']):
        input_data = case['input']
        expected_output = case['output'].strip()
        time_limit = problem.get('time_limit', 1)
        memory_limit = problem.get('memory_limit', 64)

        start_time = time.time()
        res = runner.run(
            solution_path,
            input_data,
            time_limit,
            memory_limit
        )
        elapsed = time.time() - start_time

        # Output comparison (strict, can be improved)
        actual_output = res.get('stdout', '').strip()
        passed = (actual_output == expected_output) and res.get('returncode', 1) == 0

        if res.get('returncode', 0) != 0:
            status = 'RUNTIME_ERROR'
        elif res.get('stderr', '') == 'Timeout':
            status = 'TIME_LIMIT_EXCEEDED'
        elif passed:
            status = 'OK'
        else:
            status = 'WRONG_ANSWER'

        results.append({
            'status': status,
            'error': res.get('stderr', '') if status != 'OK' else '',
            'output': actual_output,
            'expected': expected_output,
            'time': round(elapsed, 3)
        })
    return results
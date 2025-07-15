import argparse
import os
import sys
from problem_loader import load_problem
from runner import get_runner
from test_case import run_test_cases

def main():
    parser = argparse.ArgumentParser(description="Algorithmic Problem Engine")
    parser.add_argument('--problem', required=True, help='Путь к JSON-задаче')
    parser.add_argument('--solution', required=True, help='Путь к файлу решения')
    parser.add_argument('--lang', required=True, choices=['python', 'cpp', 'java'], help='Язык решения')
    parser.add_argument('--log', default=None, help='Путь к файлу логов (опционально)')
    args = parser.parse_args()

    if not os.path.exists(args.problem):
        print(f"Файл задачи не найден: {args.problem}")
        sys.exit(1)
    if not os.path.exists(args.solution):
        print(f"Файл решения не найден: {args.solution}")
        sys.exit(1)

    problem = load_problem(args.problem)
    runner = get_runner(args.lang)
    results = run_test_cases(problem, args.solution, runner)

    for idx, res in enumerate(results):
        print(f"Тест {idx+1}: {res['status']}")
        if res['status'] != 'OK':
            print(f"  Ошибка: {res.get('error', '')}")

    if args.log:
        with open(args.log, "w", encoding="utf-8") as logf:
            for idx, res in enumerate(results):
                logf.write(f"Тест {idx+1}: {res['status']}\n")
                if res['status'] != 'OK':
                    logf.write(f"  Ошибка: {res.get('error', '')}\n")

if __name__ == '__main__':
    main()
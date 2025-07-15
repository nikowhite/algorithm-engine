import argparse
import os
import sys
from problem_loader import load_problem
from runner import get_runner
from test_case import run_test_cases

def main():
    parser = argparse.ArgumentParser(description="Algorithmic Problem Engine")
    parser.add_argument('--problem', required=True, help='Path to the JSON problem file')
    parser.add_argument('--solution', required=True, help='Path to the solution file')
    parser.add_argument('--lang', required=True, choices=['python', 'cpp', 'java'], help='Solution language')
    parser.add_argument('--log', default=None, help='Path to log file (optional)')
    args = parser.parse_args()

    if not os.path.exists(args.problem):
        print(f"Problem file not found: {args.problem}")
        sys.exit(1)
    if not os.path.exists(args.solution):
        print(f"Solution file not found: {args.solution}")
        sys.exit(1)

    problem = load_problem(args.problem)
    runner = get_runner(args.lang)
    results = run_test_cases(problem, args.solution, runner)

    for idx, res in enumerate(results):
        print(f"Test {idx+1}: {res['status']}")
        if res['status'] != 'OK':
            print(f"  Error: {res.get('error', '')}")

    if args.log:
        with open(args.log, "w", encoding="utf-8") as logf:
            for idx, res in enumerate(results):
                logf.write(f"Test {idx+1}: {res['status']}\n")
                if res['status'] != 'OK':
                    logf.write(f"  Error: {res.get('error', '')}\n")

if __name__ == "__main__":
    main()
import subprocess
import sys
from .base import BaseRunner

class PythonRunner(BaseRunner):
    """
    Runs Python solutions.
    """
    def run(self, solution_path, input_data, time_limit, memory_limit):
        try:
            proc = subprocess.run(
                [sys.executable, solution_path],
                input=input_data.encode('utf-8'),
                capture_output=True,
                timeout=time_limit
            )
            return {
                'stdout': proc.stdout.decode('utf-8', errors='replace'),
                'stderr': proc.stderr.decode('utf-8', errors='replace'),
                'returncode': proc.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                'stdout': '',
                'stderr': 'Timeout',
                'returncode': -1
            }
        except Exception as e:
            return {
                'stdout': '',
                'stderr': f'Exception: {e}',
                'returncode': -2
            }
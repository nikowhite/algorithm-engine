import subprocess
import os
import tempfile
import shutil
from .base import BaseRunner

class JavaRunner(BaseRunner):
    """
    Runs Java solutions.
    The class name is expected to be Solution.
    """
    def run(self, solution_path, input_data, time_limit, memory_limit):
        temp_dir = tempfile.mkdtemp()
        try:
            # Copy solution file to temp directory
            solution_filename = os.path.basename(solution_path)
            temp_solution_path = os.path.join(temp_dir, solution_filename)
            shutil.copy(solution_path, temp_solution_path)

            # Compilation
            compile_proc = subprocess.run(
                ["javac", temp_solution_path],
                capture_output=True,
                timeout=10,
                cwd=temp_dir
            )
            if compile_proc.returncode != 0:
                return {
                    'stdout': '',
                    'stderr': compile_proc.stderr.decode('utf-8', errors='replace'),
                    'returncode': compile_proc.returncode
                }

            # Execution (expects Solution class with main method)
            run_proc = subprocess.run(
                ["java", "-cp", temp_dir, "Solution"],
                input=input_data.encode('utf-8'),
                capture_output=True,
                timeout=time_limit,
                cwd=temp_dir
            )
            return {
                'stdout': run_proc.stdout.decode('utf-8', errors='replace'),
                'stderr': run_proc.stderr.decode('utf-8', errors='replace'),
                'returncode': run_proc.returncode
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
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
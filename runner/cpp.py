import subprocess
import os
import tempfile
import shutil
from .base import BaseRunner

class CppRunner(BaseRunner):
    """
    Runs C++ solutions.
    """
    def run(self, solution_path, input_data, time_limit, memory_limit):
        temp_dir = tempfile.mkdtemp()
        exe_path = os.path.join(temp_dir, "solution.exe")
        compile_cmd = ["g++", solution_path, "-O2", "-std=c++17", "-o", exe_path]
        try:
            # Compilation
            compile_proc = subprocess.run(
                compile_cmd,
                capture_output=True,
                timeout=10
            )
            if compile_proc.returncode != 0:
                return {
                    'stdout': '',
                    'stderr': compile_proc.stderr.decode('utf-8', errors='replace'),
                    'returncode': compile_proc.returncode
                }
            # Execution
            run_proc = subprocess.run(
                [exe_path],
                input=input_data.encode('utf-8'),
                capture_output=True,
                timeout=time_limit
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
from .python import PythonRunner
# from .cpp import CppRunner
# from .java import JavaRunner

def get_runner(lang):
    """
    Returns the appropriate Runner for the language.
    """
    if lang == 'python':
        return PythonRunner()
    # elif lang == 'cpp':
    #     return CppRunner()
    # elif lang == 'java':
    #     return JavaRunner()
    else:
        raise ValueError(f"Unknown language: {lang}")
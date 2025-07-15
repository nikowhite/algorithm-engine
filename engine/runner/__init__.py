from .python import PythonRunner
# from .cpp import CppRunner
# from .java import JavaRunner

def get_runner(lang):
    """
    Возвращает соответствующий Runner по языку.
    """
    if lang == 'python':
        return PythonRunner()
    # elif lang == 'cpp':
    #     return CppRunner()
    # elif lang == 'java':
    #     return JavaRunner()
    else:
        raise ValueError(f"Неизвестный язык: {lang}")
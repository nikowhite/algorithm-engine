class BaseRunner:
    """
    Базовый класс для запуска решений на разных языках.
    """
    def run(self, solution_path, input_data, time_limit, memory_limit):
        """
        Запускает решение с заданным входом, лимитами времени и памяти.
        Возвращает словарь:
        {
            'stdout': str,
            'stderr': str,
            'returncode': int
        }
        """
        raise NotImplementedError("Метод run должен быть реализован в подклассе")
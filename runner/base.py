class BaseRunner:
    """
    Base class for running solutions in different languages.
    """
    def run(self, solution_path, input_data, time_limit, memory_limit):
        """
        Runs the solution with the given input, time and memory limits.
        Returns a dictionary:
        {
            'stdout': str,
            'stderr': str,
            'returncode': int
        }
        """
        raise NotImplementedError("The run method must be implemented in the subclass")
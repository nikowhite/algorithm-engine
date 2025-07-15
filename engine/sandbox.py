import sys

def set_limits(time_limit, memory_limit):
    """
    Устанавливает ограничения времени и памяти для дочернего процесса.
    Работает только на Unix-подобных системах.
    Для Windows требуется сторонний sandbox.
    """
    if sys.platform.startswith('win'):
        # На Windows ограничения не реализованы
        return
    try:
        import resource
        # Ограничение по времени (CPU time, в секундах)
        resource.setrlimit(resource.RLIMIT_CPU, (time_limit, time_limit))
        # Ограничение по памяти (в байтах)
        mem_bytes = memory_limit * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
    except ImportError:
        pass
    except Exception as e:
        print(f"Не удалось установить ограничения: {e}", file=sys.stderr)
import sys

def set_limits(time_limit, memory_limit):
    """
    Sets time and memory limits for the child process.
    Works only on Unix-like systems.
    For Windows, a third-party sandbox is required.
    """
    if sys.platform.startswith('win'):
        # Not implemented on Windows
        return
    try:
        import resource
        # CPU time limit (in seconds)
        resource.setrlimit(resource.RLIMIT_CPU, (time_limit, time_limit))
        # Memory limit (in bytes)
        mem_bytes = memory_limit * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
    except ImportError:
        pass
    except Exception as e:
        print(f"Failed to set limits: {e}", file=sys.stderr)
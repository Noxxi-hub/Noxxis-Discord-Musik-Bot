"""Playify startup with single-instance lock."""
import os
import sys
import fcntl

LOCK_PATH = "/tmp/playify.lock"

def acquire_lock():
    """Try to acquire an exclusive lock. Returns the lock file or None if already locked."""
    try:
        lock_fd = open(LOCK_PATH, "w")
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        # Write PID so we can identify the running instance
        lock_fd.write(str(os.getpid()))
        lock_fd.flush()
        return lock_fd
    except (IOError, OSError):
        return None

def release_lock(lock_fd):
    """Release the lock and clean up."""
    if lock_fd:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
        lock_fd.close()
        try:
            os.unlink(LOCK_PATH)
        except OSError:
            pass

if __name__ == "__main__":
    lock = acquire_lock()
    if lock is None:
        print("ERROR: Playify is already running! Only one instance allowed.", file=sys.stderr)
        sys.exit(1)

    print(f"Lock acquired (PID {os.getpid()}). Starting Playify...")

    try:
        from src.playify.app import run
        run()
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    finally:
        release_lock(lock)

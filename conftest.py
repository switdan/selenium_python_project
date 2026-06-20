import os
import sys
import subprocess
import time
from pathlib import Path

MAX_WAIT_SECONDS = 10
CHECK_INTERVAL = 0.5


def open_report(path: Path):
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform.startswith("linux"):
        subprocess.run(["xdg-open", str(path)], check=False)
    elif sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)


def pytest_unconfigure(config):
    """
    Pytest hook that opens the generated HTML report after all tests finish.
    Skips execution on distributed workers and polls for the file up to MAX_WAIT_SECONDS.

    :param config: Pytest configuration object containing runtime options
    """
    if hasattr(config, "workerinput"):
        return

    report_path = config.getoption("htmlpath")
    if not report_path:
        return

    path = Path(report_path).resolve()

    timeout = time.time() + MAX_WAIT_SECONDS

    while time.time() < timeout:
        if path.exists():
            open_report(path)
            return
        time.sleep(CHECK_INTERVAL)
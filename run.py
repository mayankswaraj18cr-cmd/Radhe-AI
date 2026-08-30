from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


def main() -> int:
    load_dotenv(Path(__file__).with_name('.env'))
    print('Radhe AI — Hybrid Cognitive LLM Platform')
    print('Environment:', os.getenv('RADHE_ENV', 'development'))
    print('Status: ready for orchestration and reasoning workflows.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

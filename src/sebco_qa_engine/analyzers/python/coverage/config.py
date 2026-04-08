"""Configuration dataclass for CoverageAnalyzer.

Keeping config separate from the analyzer itself makes it easy to
construct, serialize and pass around without importing the full analyzer.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CoverageConfig:
    """Runtime configuration for the coverage analyzer.

    Parameters
    ----------
    run_tests:
        When ``True``, the analyzer first executes ``coverage run`` to
        collect coverage data, then ``coverage report``.  Set to ``False``
        only when a ``.coverage`` file already exists (e.g. produced by a
        prior ``pytest --cov`` step in the same job).
    test_command:
        Command forwarded to ``coverage run -m`` when ``run_tests=True``.
        Defaults to ``["pytest"]``.
    run_extra_args:
        Additional arguments forwarded verbatim to ``coverage run``
        (e.g. ``["--source=src"]``).
    extra_args:
        Additional arguments forwarded verbatim to ``coverage report``
        (e.g. ``["--include=src/*"]``).
    timeout:
        Maximum seconds to wait for each ``coverage`` subprocess.
        ``None`` means no timeout.

    Examples
    --------
    Default — runs tests then reports:

        >>> cfg = CoverageConfig()

    Report-only (pre-existing .coverage file):

        >>> cfg = CoverageConfig(run_tests=False)

    Custom test command:

        >>> cfg = CoverageConfig(test_command=["pytest", "tests/unit"])
    """

    run_tests: bool = True
    test_command: list[str] = field(default_factory=lambda: ["pytest"])
    run_extra_args: list[str] = field(default_factory=list)
    extra_args: list[str] = field(default_factory=list)
    timeout: int | None = 300

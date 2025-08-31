"""Logging configuration for proselint."""

import logging
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime


class ColoredFormatter(logging.Formatter):
    """Custom formatter with color support for terminal output."""
    
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
    }
    RESET = '\033[0m'
    
    def format(self, record):
        """Format log record with colors if outputting to terminal."""
        if sys.stderr.isatty():
            levelname = record.levelname
            if levelname in self.COLORS:
                record.levelname = f"{self.COLORS[levelname]}{levelname}{self.RESET}"
        return super().format(record)


def setup_logging(
    level: str = "WARNING",
    log_file: Optional[Path] = None,
    verbose: bool = False
) -> logging.Logger:
    """
    Set up logging configuration for proselint.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional path to log file
        verbose: If True, use more detailed format
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("proselint")
    logger.setLevel(getattr(logging, level.upper(), logging.WARNING))
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stderr)
    
    if verbose:
        format_string = (
            "%(asctime)s - %(name)s - %(levelname)s - "
            "%(filename)s:%(lineno)d - %(message)s"
        )
    else:
        format_string = "%(levelname)s: %(message)s"
    
    console_formatter = ColoredFormatter(format_string)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - "
            "%(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        name: Logger name (defaults to 'proselint')
    
    Returns:
        Logger instance
    """
    if name:
        return logging.getLogger(f"proselint.{name}")
    return logging.getLogger("proselint")


class CheckLogger:
    """Context manager for logging check execution."""
    
    def __init__(self, check_name: str, logger: Optional[logging.Logger] = None):
        """Initialize check logger."""
        self.check_name = check_name
        self.logger = logger or get_logger("checks")
        self.start_time = None
    
    def __enter__(self):
        """Enter context - log check start."""
        self.start_time = datetime.now()
        self.logger.debug(f"Starting check: {self.check_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context - log check completion or error."""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        if exc_type:
            self.logger.error(
                f"Check {self.check_name} failed after {elapsed:.3f}s: {exc_val}"
            )
        else:
            self.logger.debug(
                f"Check {self.check_name} completed in {elapsed:.3f}s"
            )
        
        # Don't suppress exceptions
        return False


# Initialize default logger
_default_logger = setup_logging()


def log_performance(func):
    """Decorator to log function performance."""
    def wrapper(*args, **kwargs):
        logger = get_logger("performance")
        start = datetime.now()
        
        try:
            result = func(*args, **kwargs)
            elapsed = (datetime.now() - start).total_seconds()
            logger.debug(f"{func.__name__} completed in {elapsed:.3f}s")
            return result
        except Exception as e:
            elapsed = (datetime.now() - start).total_seconds()
            logger.error(f"{func.__name__} failed after {elapsed:.3f}s: {e}")
            raise
    
    return wrapper
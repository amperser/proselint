"""Custom exceptions for proselint."""

from typing import Optional


class ProselintError(Exception):
    """Base exception for all proselint errors."""
    pass


class ConfigError(ProselintError):
    """Error loading or parsing configuration."""
    
    def __init__(self, message: str, path: Optional[str] = None):
        """Initialize config error with optional path."""
        self.path = path
        super().__init__(f"Config error{f' in {path}' if path else ''}: {message}")


class CheckError(ProselintError):
    """Error running a specific check."""
    
    def __init__(self, check_name: str, message: str):
        """Initialize check error."""
        self.check_name = check_name
        super().__init__(f"Check '{check_name}' failed: {message}")


class FileProcessingError(ProselintError):
    """Error processing a file."""
    
    def __init__(self, filepath: str, message: str):
        """Initialize file processing error."""
        self.filepath = filepath
        super().__init__(f"Error processing '{filepath}': {message}")
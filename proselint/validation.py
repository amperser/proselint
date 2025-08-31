"""Input validation utilities for proselint."""

from typing import Any, Optional, Union
import re
from pathlib import Path

from proselint.errors import ProselintError


def validate_text_input(text: Any, max_size: int = 10 * 1024 * 1024) -> str:
    """
    Validate and sanitize text input.
    
    Args:
        text: Input to validate
        max_size: Maximum allowed size in bytes
    
    Returns:
        Validated and sanitized text
    
    Raises:
        ProselintError: If input is invalid
    """
    if text is None:
        raise ProselintError("Input text cannot be None")
    
    if not isinstance(text, str):
        try:
            text = str(text)
        except Exception as e:
            raise ProselintError(f"Cannot convert input to string: {e}")
    
    # Check size
    byte_size = len(text.encode('utf-8', errors='ignore'))
    if byte_size > max_size:
        raise ProselintError(
            f"Input exceeds maximum size of {max_size} bytes (got {byte_size} bytes)"
        )
    
    # Remove null bytes and other control characters
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Ensure text ends with newline for consistency
    if text and not text.endswith('\n'):
        text += '\n'
    
    return text


def validate_file_path(path: Union[str, Path]) -> Path:
    """
    Validate file path.
    
    Args:
        path: File path to validate
    
    Returns:
        Validated Path object
    
    Raises:
        ProselintError: If path is invalid
    """
    if isinstance(path, str):
        path = Path(path)
    
    if not isinstance(path, Path):
        raise ProselintError(f"Invalid path type: {type(path)}")
    
    # Resolve to absolute path to prevent traversal attacks
    try:
        path = path.resolve()
    except Exception as e:
        raise ProselintError(f"Cannot resolve path: {e}")
    
    # Check if file exists
    if not path.exists():
        raise ProselintError(f"File does not exist: {path}")
    
    # Check if it's a file (not directory)
    if not path.is_file():
        raise ProselintError(f"Path is not a file: {path}")
    
    # Check if readable
    if not path.stat().st_mode & 0o400:
        raise ProselintError(f"File is not readable: {path}")
    
    return path


def validate_position(position: int, text_length: int) -> int:
    """
    Validate and clamp position within text bounds.
    
    Args:
        position: Position to validate
        text_length: Length of text
    
    Returns:
        Valid position within bounds
    """
    if not isinstance(position, int):
        try:
            position = int(position)
        except (ValueError, TypeError):
            return 0
    
    # Clamp to valid range
    return max(0, min(position, text_length - 1))


def validate_check_path(check_path: str) -> bool:
    """
    Validate check path format.
    
    Args:
        check_path: Check path to validate
    
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(check_path, str):
        return False
    
    # Check path should be like "category.subcategory.check_name"
    # Only alphanumeric, underscore, and dots allowed
    if not re.match(r'^[a-z_][a-z0-9_]*(\.[a-z_][a-z0-9_]*)*$', check_path):
        return False
    
    # Maximum depth of 5 levels
    if check_path.count('.') > 4:
        return False
    
    return True


def validate_config_value(key: str, value: Any) -> bool:
    """
    Validate configuration value.
    
    Args:
        key: Configuration key
        value: Configuration value
    
    Returns:
        True if valid, False otherwise
    """
    if key == 'max_errors':
        return isinstance(value, int) and 0 < value <= 10000
    
    elif key == 'checks':
        if not isinstance(value, dict):
            return False
        
        for check_key, check_enabled in value.items():
            if not isinstance(check_key, str) or not isinstance(check_enabled, bool):
                return False
            if not validate_check_path(check_key):
                return False
        
        return True
    
    # Unknown key - allow but log warning
    return True


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe use.
    
    Args:
        filename: Filename to sanitize
    
    Returns:
        Sanitized filename
    """
    # Remove path components
    filename = Path(filename).name
    
    # Remove dangerous characters
    filename = re.sub(r'[^\w\s\-\.]', '', filename)
    
    # Limit length
    if len(filename) > 255:
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        max_name_len = 250 - len(ext)
        filename = name[:max_name_len] + ('.' + ext if ext else '')
    
    return filename or 'unnamed'
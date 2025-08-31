# Proselint MCP Server

An MCP (Model Context Protocol) server wrapper for [proselint](https://github.com/amperser/proselint), a linter for prose.

## Installation

1. Ensure proselint is installed:
```bash
pip install proselint
```

2. Install the MCP server dependencies:
```bash
cd mcp-server
npm install
```

3. Build the TypeScript code:
```bash
npm run build
```

## Usage

### Running the server

```bash
npm start
```

Or for development:
```bash
npm run dev
```

### Available Tools

The MCP server exposes three tools:

#### 1. `lint_text`
Check text for style issues using proselint.

**Parameters:**
- `text` (string, required): The text to lint

**Example:**
```json
{
  "name": "lint_text",
  "arguments": {
    "text": "The reason is because this is very unique."
  }
}
```

#### 2. `lint_file`
Check a file for style issues using proselint.

**Parameters:**
- `filepath` (string, required): Path to the file to lint

**Example:**
```json
{
  "name": "lint_file",
  "arguments": {
    "filepath": "/path/to/document.md"
  }
}
```

#### 3. `configure_proselint`
Get or update proselint configuration.

**Parameters:**
- `action` (string, required): Either "get" or "set"
- `config` (object, optional): Configuration object (only for "set" action)

**Examples:**

Get current configuration:
```json
{
  "name": "configure_proselint",
  "arguments": {
    "action": "get"
  }
}
```

Set configuration:
```json
{
  "name": "configure_proselint",
  "arguments": {
    "action": "set",
    "config": {
      "checks": {
        "misc.scare_quotes": false,
        "typography.symbols": true
      },
      "max_errors": 100
    }
  }
}
```

## Integration with Claude Desktop

To use this MCP server with Claude Desktop, add the following to your Claude Desktop configuration file:

### macOS
Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "proselint": {
      "command": "node",
      "args": ["/path/to/proselint/mcp-server/dist/index.js"]
    }
  }
}
```

### Windows
Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "proselint": {
      "command": "node",
      "args": ["C:\\path\\to\\proselint\\mcp-server\\dist\\index.js"]
    }
  }
}
```

## Output Format

The server returns proselint results in JSON format, containing:
- Error messages and suggestions
- Line and column positions
- Check identifiers
- Severity levels
- Replacement suggestions (when available)

## Requirements

- Node.js 18 or higher
- Python 3.9 or higher
- proselint Python package

## License

MIT
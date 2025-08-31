#!/usr/bin/env bash
set -euo pipefail
cat "$HOME/.mcp/servers.json" | jq '{ mcpServers: . }'

#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ErrorCode,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import { exec, spawn } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs/promises';
import * as path from 'path';
import * as os from 'os';
import { fileURLToPath } from 'url';

const execAsync = promisify(exec);
const __dirname = path.dirname(fileURLToPath(import.meta.url));

interface ProselintResult {
  status: string;
  data?: {
    errors: Array<{
      check_path: string;
      message: string;
      line: number;
      column: number;
      start_pos: number;
      end_pos: number;
      severity: string;
      replacements: string | null;
    }>;
  };
}

class ProselintServer {
  private server: Server;
  private pythonCommand: string = 'python';

  constructor() {
    this.server = new Server(
      {
        name: 'proselint-mcp',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.detectPythonCommand();
    this.setupHandlers();
  }

  private async detectPythonCommand(): Promise<void> {
    // Try to find the best Python command
    const commands = ['python3', 'python', 'py'];
    
    for (const cmd of commands) {
      try {
        const { stdout } = await execAsync(`${cmd} --version`);
        if (stdout.includes('Python 3.')) {
          this.pythonCommand = cmd;
          console.error(`Using Python command: ${cmd}`);
          break;
        }
      } catch {
        // Continue to next command
      }
    }
  }

  private setupHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'lint_text',
          description: 'Check text for style issues using proselint',
          inputSchema: {
            type: 'object',
            properties: {
              text: {
                type: 'string',
                description: 'The text to lint',
              },
            },
            required: ['text'],
          },
        },
        {
          name: 'lint_file',
          description: 'Check a file for style issues using proselint',
          inputSchema: {
            type: 'object',
            properties: {
              filepath: {
                type: 'string',
                description: 'Path to the file to lint',
              },
            },
            required: ['filepath'],
          },
        },
        {
          name: 'configure_proselint',
          description: 'Get or update proselint configuration',
          inputSchema: {
            type: 'object',
            properties: {
              action: {
                type: 'string',
                enum: ['get', 'set'],
                description: 'Action to perform on configuration',
              },
              config: {
                type: 'object',
                description: 'Configuration object (only for "set" action)',
              },
            },
            required: ['action'],
          },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      if (!args) {
        throw new McpError(
          ErrorCode.InvalidParams,
          'Arguments are required'
        );
      }

      switch (name) {
        case 'lint_text':
          return await this.lintText(args.text as string);
        
        case 'lint_file':
          return await this.lintFile(args.filepath as string);
        
        case 'configure_proselint':
          return await this.configureProselint(
            args.action as string,
            args.config as any
          );
        
        default:
          throw new McpError(
            ErrorCode.MethodNotFound,
            `Unknown tool: ${name}`
          );
      }
    });
  }

  private async lintText(text: string): Promise<any> {
    try {
      // Create temporary file in OS temp directory
      const tempDir = os.tmpdir();
      const tempFile = path.join(tempDir, `proselint-${Date.now()}.txt`);
      await fs.writeFile(tempFile, text, 'utf8');

      try {
        // Run proselint with timeout
        const { stdout } = await execAsync(
          `${this.pythonCommand} -m proselint --json "${tempFile}"`,
          { timeout: 30000 }
        );
        
        // Parse JSON output
        const result = JSON.parse(stdout);
        
        // Clean up temp file
        await fs.unlink(tempFile);
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      } catch (error: any) {
        // Clean up temp file even on error
        await fs.unlink(tempFile).catch(() => {});
        
        // Parse error output if it's JSON
        if (error.stdout) {
          try {
            const result = JSON.parse(error.stdout);
            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify(result, null, 2),
                },
              ],
            };
          } catch {
            // If not JSON, return as text
            return {
              content: [
                {
                  type: 'text',
                  text: error.stdout || error.message,
                },
              ],
            };
          }
        }
        throw error;
      }
    } catch (error: any) {
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to lint text: ${error.message}`
      );
    }
  }

  private async lintFile(filepath: string): Promise<any> {
    try {
      // Check if file exists
      await fs.access(filepath);
      
      // Validate file path
      const resolvedPath = path.resolve(filepath);
      
      // Run proselint with timeout
      const { stdout } = await execAsync(
        `${this.pythonCommand} -m proselint --json "${resolvedPath}"`,
        { timeout: 30000 }
      );
      
      // Parse JSON output
      const result = JSON.parse(stdout);
      
      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify(result, null, 2),
          },
        ],
      };
    } catch (error: any) {
      // Try to parse error output if it's JSON
      if (error.stdout) {
        try {
          const result = JSON.parse(error.stdout);
          return {
            content: [
              {
                type: 'text',
                text: JSON.stringify(result, null, 2),
              },
            ],
          };
        } catch {
          // If not JSON, return as text
          return {
            content: [
              {
                type: 'text',
                text: error.stdout || error.message,
              },
            ],
          };
        }
      }
      
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to lint file: ${error.message}`
      );
    }
  }

  private async configureProselint(action: string, config?: any): Promise<any> {
    try {
      if (action === 'get') {
        // Get current configuration
        const { stdout } = await execAsync(
          `${this.pythonCommand} -m proselint --dump-config`,
          { timeout: 10000 }
        );
        const currentConfig = JSON.parse(stdout);
        
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(currentConfig, null, 2),
            },
          ],
        };
      } else if (action === 'set') {
        if (!config) {
          throw new McpError(
            ErrorCode.InvalidParams,
            'Configuration object required for "set" action'
          );
        }
        
        // Find proselint config path
        const homeDir = os.homedir();
        const configPath = path.join(homeDir, '.proselintrc');
        
        // Write new configuration
        await fs.writeFile(configPath, JSON.stringify(config, null, 2));
        
        return {
          content: [
            {
              type: 'text',
              text: `Configuration saved to ${configPath}`,
            },
          ],
        };
      } else {
        throw new McpError(
          ErrorCode.InvalidParams,
          `Invalid action: ${action}. Use "get" or "set"`
        );
      }
    } catch (error: any) {
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to configure proselint: ${error.message}`
      );
    }
  }

  async run() {
    try {
      // Verify proselint is installed
      await execAsync(`${this.pythonCommand} -m proselint --version`);
    } catch (error) {
      console.error('Warning: proselint may not be installed correctly');
      console.error('Install with: pip install proselint');
    }
    
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Proselint MCP server running on stdio');
  }
}

const server = new ProselintServer();
server.run().catch(console.error);
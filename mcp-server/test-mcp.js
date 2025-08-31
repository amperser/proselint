#!/usr/bin/env node

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { spawn } from 'child_process';

async function testMCPServer() {
  console.log('Starting proselint MCP server test...\n');
  
  // Start the server process
  const serverProcess = spawn('node', ['dist/index.js'], {
    stdio: ['pipe', 'pipe', 'pipe'],
  });
  
  // Create transport and client
  const transport = new StdioClientTransport({
    command: 'node',
    args: ['dist/index.js'],
  });
  
  const client = new Client({
    name: 'test-client',
    version: '1.0.0',
  }, {
    capabilities: {}
  });
  
  try {
    // Connect to server
    await client.connect(transport);
    console.log('✓ Connected to server\n');
    
    // List available tools
    const tools = await client.listTools();
    console.log('Available tools:');
    tools.tools.forEach(tool => {
      console.log(`  - ${tool.name}: ${tool.description}`);
    });
    console.log();
    
    // Test lint_text tool
    console.log('Testing lint_text tool...');
    const textResult = await client.callTool('lint_text', {
      text: 'The reason is because this is very unique.'
    });
    console.log('Result:', JSON.stringify(textResult, null, 2));
    console.log();
    
    // Test lint_file tool
    console.log('Testing lint_file tool...');
    const fileResult = await client.callTool('lint_file', {
      filepath: './test.txt'
    });
    console.log('Result:', JSON.stringify(fileResult, null, 2));
    console.log();
    
    // Test configure_proselint tool (get)
    console.log('Testing configure_proselint tool (get)...');
    const configResult = await client.callTool('configure_proselint', {
      action: 'get'
    });
    console.log('Current config (truncated):', 
      JSON.stringify(JSON.parse(configResult.content[0].text), null, 2).substring(0, 200) + '...');
    console.log();
    
    console.log('✓ All tests passed!');
    
  } catch (error) {
    console.error('Test failed:', error);
    process.exit(1);
  } finally {
    // Clean up
    await client.close();
    serverProcess.kill();
  }
}

testMCPServer().catch(console.error);
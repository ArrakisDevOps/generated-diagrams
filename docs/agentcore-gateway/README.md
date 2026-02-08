# AgentCore Gateway

This directory contains diagrams illustrating the AgentCore Gateway architecture pattern - a centralized gateway that provides unified access to various tools and services through different protocols and endpoints.

## Architecture Components

- **Agent**: The requesting client using MCP (Model Control Protocol)
- **AgentCore Gateway**: Central hub that routes requests to appropriate services  
- **Endpoints**: Different service types (API, MCP Server, AWS Lambda, Smithy Model)
- **Tools**: Individual tools accessible through each endpoint
- **Benefits**: Key advantages of the gateway pattern

## Files

### Scripts
- `agentcore-gateway-graphviz.py` - **Main script** with correct styling (black fill, colored borders)
- `agentcore-gateway-with-icons.py` - Enhanced version using real PNG icons from icons directory
- `agentcore-gateway-simple.py` - Simplified oval version (alternative clean style)

### Generated Diagrams
- `agentcore-gateway-graphviz.png` - Main diagram matching original design (70KB)
- `agentcore-gateway-with-icons.png` - Enhanced version with real icons (84KB)
- `agentcore-gateway-simple.png` - Simple oval style (71KB)

### Icon Assets
- `icons/` - Directory containing AI/VR/Bot icon assets in PNG and EPS formats

## Running

```bash
# Generate the main diagram (recommended - matches original exactly)
python3 agentcore-gateway-graphviz.py

# Generate enhanced version with real icons
python3 agentcore-gateway-with-icons.py

# Generate simplified oval version
python3 agentcore-gateway-simple.py
```

## Key Styling Features

The main script (`agentcore-gateway-graphviz.py`) implements the correct visual design:

### ✅ **Fixed Styling Issues**
1. **Black rectangle fills** (not gradient fills)
2. **Colored borders** with proper gradient colors 
3. **Rounded rectangles** (not ovals)
4. **Complete layout** with all labels and benefits
5. **Proper positioning** matching the original design

### 🎨 **Visual Design**
- **Dark background**: `#0f0f23` (very dark blue/black)
- **Rectangle fills**: Black with colored borders
- **Typography**: Arial font family with proper sizing
- **Arrows**: White with proper arrowheads
- **Icons**: Brain and agent emojis (or real PNG icons in enhanced version)

## Architecture Benefits Illustrated

1. **Time to value**: Simplified access to existing APIs and data
2. **Security**: Inbound/outbound authentication and access control  
3. **Serverless**: Scales on demand without infrastructure management
4. **Built-in tool search**: Tools automatically indexed and searchable

## Color Coding

- **Purple borders**: AgentCore Gateway (central hub), Agent
- **Red borders**: API Endpoints (RESTful services)
- **Blue borders**: MCP Server (MCP protocol services)
- **Green borders**: AWS Lambda (serverless functions)
- **Yellow borders**: Smithy Model (model-based services)
- **Gray borders**: Individual tools and utilities

## Icon Assets

The `icons/` directory contains professional AI/VR/Bot icon sets in multiple formats:
- **PNG files**: For direct use in diagrams
- **EPS files**: Vector format for high-quality scaling
- **Multiple styles**: Both black and white versions available
- **Categories**: Brain icons, robot icons, technology symbols

The enhanced version (`agentcore-gateway-with-icons.py`) demonstrates how to incorporate these real icon assets instead of using emoji characters.
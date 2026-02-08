# Agent Guidelines for FromSolo2Squad

This repository contains Python scripts for generating multi-agent AI architecture diagrams for AWS meetup presentations. This guide provides coding agents with essential information for working effectively in this codebase.

## Project Overview

**Purpose**: Educational diagram generation toolkit for multi-agent AI presentations  
**Technology Stack**: Python 3, GraphViz, Diagrams library  
**Target Audience**: AWS meetups and developer education  
**Output Format**: PNG diagrams for presentations

## Build/Test/Lint Commands

Since this is a Python diagram generation project without formal build tooling:

### Running Scripts
```bash
# Execute diagram generation scripts directly
python3 docs/agent-components/agent-components-diagrams.py
python3 docs/agent-components/agent-components-graphviz.py

# Or run with executable permissions
./docs/agent-components/agent-components-diagrams.py
```

### Dependencies Installation
```bash
# Install required Python packages
pip install graphviz diagrams

# On macOS, also install graphviz system package
brew install graphviz
```

### Running Single Script
```bash
# To run a specific diagram generation script:
cd docs/[category-folder]
python3 [script-name].py
```

### Validation
```bash
# Check Python syntax
python3 -m py_compile [script-name].py

# Run with pylint (if available)
pylint [script-name].py
```

## Project Structure

```
FromSolo2Squad/
├── docs/                           # All diagram generation code
│   ├── agent-components/           # Agent architecture diagrams
│   ├── multi-agent-orchestrator/   # Orchestrator pattern diagrams
│   ├── multi-agent-router/        # Router pattern diagrams
│   └── prompt-chaining/           # Prompt chaining workflows
├── LICENSE                        # MIT License
├── README.md                      # Project description
└── AGENTS.md                      # This file
```

## Code Style Guidelines

### File Organization
- **Executable scripts**: All `.py` files should have shebang `#!/usr/bin/env python3`
- **File naming**: Use kebab-case: `agent-components-diagrams.py`
- **Output naming**: Match script name: `agent-components-diagrams.png`

### Python Code Conventions

#### Imports
```python
#!/usr/bin/env python3
#
# script-name.py
#
# Script generates a diagram for AWS meetup presentation.
#
# pylint: disable=pointless-statement, expression-not-assigned

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.aws.ml import Sagemaker
from graphviz import Digraph
```

#### Formatting & Style
- **Indentation**: 4 spaces (no tabs)
- **Line length**: Keep reasonable (under 88 chars when possible)
- **String quotes**: Use double quotes for user-facing strings, single for internal
- **Comments**: Include purpose comments for complex diagram configurations

#### Variable Naming
```python
# Configuration dictionaries - snake_case
graph_attr = {...}
edge_attr = {...}
node_styles = {...}

# Style dictionaries - descriptive names
green_style = {...}
white_style = {...}

# Diagram elements - descriptive names
user = Users("User Request")
agent_core = RekognitionImage("Agent Core")
```

#### GraphViz Patterns
```python
# Standard GraphViz setup
dot = Digraph(
    "Diagram Title",
    graph_attr={
        "nodesep": "1.0",
    },
    format="png",
)

dot.attr(bgcolor='transparent')
dot.attr('edge', color='white')
dot.attr(rankdir="LR")
```

#### Diagrams Library Patterns
```python
# Standard diagrams library setup
with Diagram(
    "\n\nDiagram Title\n\n",
    filename="output-filename",
    show=False,
    graph_attr=graph_attr,
    edge_attr=edge_attr,
):
    # Diagram elements here
```

### Error Handling
- **Minimal error handling**: Scripts are meant for controlled execution
- **Pylint suppressions**: Use specific suppressions as needed
- **Dependencies**: Assume required packages are installed

### Documentation
- **File headers**: Include purpose and description
- **Inline comments**: Document complex styling or layout decisions
- **README files**: Each directory should have explanatory README.md

## Diagram Generation Best Practices

### Color Schemes
- **Background**: Transparent (`bgcolor='transparent'`)
- **Edges**: White (`color='white'`)
- **Primary nodes**: Green (`#8BC34A`)
- **Secondary nodes**: White with black text

### Layout Principles
- **Direction**: Left-to-right (`rankdir="LR"`)
- **Node separation**: Use `nodesep` for spacing
- **Edge styling**: Bidirectional where appropriate (`dir="both"`)

### Naming Conventions
- **Scripts**: `[category]-[type].py` (e.g., `agent-components-graphviz.py`)
- **Outputs**: Match script name without `.py`
- **Directories**: kebab-case matching diagram categories

## Multi-Format Support

Each diagram concept should support multiple formats:
1. **Python Diagrams**: AWS-specific icons (`*-diagrams.py`)
2. **GraphViz**: Custom styling (`*-graphviz.py`)  
3. **Draw.io**: XML format (`*-drawio.xml`)
4. **Mermaid**: Text-based (`*-mermaid.mmd`)

## Development Workflow

1. **Create scripts**: Start with GraphViz for layout control
2. **Generate outputs**: Run scripts to create PNG files
3. **Test rendering**: Verify diagrams are presentation-ready
4. **Document**: Add README.md explaining the diagram concept
5. **Multiple formats**: Create equivalent diagrams in other formats

## Architecture Patterns

This project documents four key multi-agent patterns:

1. **Agent Components**: Core agent architecture
2. **Multi-Agent Orchestrator**: Coordinator-worker pattern  
3. **Multi-Agent Router**: Request routing mechanisms
4. **Prompt Chaining**: Sequential LLM processing

## File Permissions

- **Python scripts**: Should be executable (`chmod +x *.py`)
- **Generated files**: Standard read permissions
- **README files**: Standard documentation permissions

## Git Practices

- **Commit both**: Include both source scripts and generated outputs
- **Descriptive messages**: Reference which diagram is being modified
- **Small commits**: One diagram concept per commit when possible

This project prioritizes clear visual communication of complex AI concepts through well-styled, presentation-ready diagrams.
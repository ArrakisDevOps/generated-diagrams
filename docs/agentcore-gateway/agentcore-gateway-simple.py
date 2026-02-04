#!/usr/bin/env python3
#
# agentcore-gateway-simple.py
#
# Script generates a simplified AgentCore Gateway diagram (oval version).
#
# pylint: disable=pointless-statement, expression-not-assigned

from graphviz import Digraph

# Create simplified diagram
dot = Digraph(
    "AgentCore Gateway Simple",
    graph_attr={
        "bgcolor": "#0f0f23",
        "rankdir": "LR",
        "nodesep": "1.5",
        "ranksep": "2.0",
        "fontname": "Arial",
        "splines": "ortho",
        "pad": "0.8",
    },
    format="png",
)

# Define oval-based styles
purple_gateway_oval = {
    "style": "filled",
    "fillcolor": "#4c1d95",
    "color": "#8b5cf6",
    "penwidth": "4",
    "fontcolor": "white",
    "fontname": "Arial Bold",
    "fontsize": "16",
    "width": "3.5",
    "height": "2.5",
    "shape": "ellipse",
}

agent_oval = {
    "style": "filled",
    "fillcolor": "#312e81",
    "color": "#8b5cf6",
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "ellipse",
}

red_oval = {
    "style": "filled",
    "fillcolor": "#7f1d1d",
    "color": "#ef4444",
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "ellipse",
}

blue_oval = {
    "style": "filled",
    "fillcolor": "#1e3a8a",
    "color": "#3b82f6",
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "ellipse",
}

green_oval = {
    "style": "filled",
    "fillcolor": "#14532d",
    "color": "#10b981",
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "ellipse",
}

yellow_oval = {
    "style": "filled",
    "fillcolor": "#92400e",
    "color": "#fbbf24",
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "ellipse",
}

tool_oval = {
    "style": "filled",
    "fillcolor": "#374151",
    "color": "#6b7280",
    "penwidth": "2",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "12",
    "shape": "ellipse",
}

# Create nodes
dot.node("agent", "Agent", _attributes=agent_oval)
dot.node("gateway", "🧠\nAgentCore\nGateway", _attributes=purple_gateway_oval)

# Endpoints
dot.node("api_endpoint", "API Endpoint", _attributes=red_oval)
dot.node("mcp_server", "MCP Server", _attributes=blue_oval)
dot.node("aws_lambda", "AWS Lambda", _attributes=green_oval)
dot.node("smithy_model", "Smithy Model", _attributes=yellow_oval)

# Tools
dot.node("tool1", "Tool", _attributes=tool_oval)
dot.node("tool2", "Tool", _attributes=tool_oval)
dot.node("tool3", "Tool", _attributes=tool_oval)
dot.node("tool4", "Tool", _attributes=tool_oval)

# Layout
with dot.subgraph() as left:
    left.attr(rank="same")
    left.node("agent")

with dot.subgraph() as center:
    center.attr(rank="same")
    center.node("gateway")

with dot.subgraph() as endpoints:
    endpoints.attr(rank="same")
    endpoints.node("api_endpoint")
    endpoints.node("mcp_server")
    endpoints.node("aws_lambda")
    endpoints.node("smithy_model")

with dot.subgraph() as tools:
    tools.attr(rank="same")
    tools.node("tool1")
    tools.node("tool2")
    tools.node("tool3")
    tools.node("tool4")

# Connections
dot.edge("agent", "gateway", color="white", penwidth="3", arrowhead="vee")
dot.edge("gateway", "api_endpoint", color="white", penwidth="2", arrowhead="vee")
dot.edge("gateway", "mcp_server", color="white", penwidth="2", arrowhead="vee")
dot.edge("gateway", "aws_lambda", color="white", penwidth="2", arrowhead="vee")
dot.edge("gateway", "smithy_model", color="white", penwidth="2", arrowhead="vee")

dot.edge("api_endpoint", "tool1", color="white", penwidth="2", arrowhead="vee")
dot.edge("mcp_server", "tool2", color="white", penwidth="2", arrowhead="vee")
dot.edge("aws_lambda", "tool3", color="white", penwidth="2", arrowhead="vee")
dot.edge("smithy_model", "tool4", color="white", penwidth="2", arrowhead="vee")

# Render
dot.render("agentcore-gateway-simple", view=False)
print("Simple AgentCore Gateway diagram generated: agentcore-gateway-simple.png")
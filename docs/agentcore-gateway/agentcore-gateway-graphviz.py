#!/usr/bin/env python3
#
# agentcore-gateway-graphviz.py
#
# Script generates AgentCore Gateway diagram for AWS meetup presentation.
# Uses black fills with gradient border colors and proper icons.
#
# pylint: disable=pointless-statement, expression-not-assigned

from graphviz import Digraph

# Create main diagram with proper dark theme
dot = Digraph(
    "AgentCore Gateway",
    graph_attr={
        "bgcolor": "#0f0f23",  # Very dark background
        "rankdir": "LR",
        "nodesep": "1.0",
        "ranksep": "1.5",
        "fontname": "Arial",
        "fontsize": "28",
        "fontcolor": "white",
        "splines": "ortho",
        "pad": "0.5",
        "margin": "0.5",
    },
    format="png",
)

# Define styles with BLACK FILL and GRADIENT BORDERS
# This is the key fix - black fill, colored borders

# Central Gateway - large rounded rectangle
gateway_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#8b5cf6",    # Purple border
    "penwidth": "4",
    "fontcolor": "white",
    "fontname": "Arial Bold",
    "fontsize": "20",
    "width": "3.0",
    "height": "4.5",
    "shape": "box",        # Rounded rectangle
}

# Agent - small rounded rectangle
agent_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#8b5cf6",    # Purple border
    "penwidth": "2",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "box",
}

# API Endpoint - red border
red_endpoint_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#ef4444",    # Red border
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

# MCP Server - blue border  
blue_endpoint_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#3b82f6",    # Blue border
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

# AWS Lambda - green border
green_endpoint_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#10b981",    # Green border
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

# Smithy Model - yellow/orange border
yellow_endpoint_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#fbbf24",    # Yellow border
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

# Tools - gray border
tool_style = {
    "style": "filled,rounded",
    "fillcolor": "black",  # Black fill
    "color": "#6b7280",    # Gray border
    "penwidth": "2",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "box",
}

# Label styles for text elements
title_style = {
    "style": "invis",
    "fontcolor": "white",
    "fontname": "Arial Bold",
    "fontsize": "36",
}

section_label_style = {
    "style": "invis",
    "fontcolor": "#8b5cf6",
    "fontname": "Arial",
    "fontsize": "18",
}

service_label_style = {
    "style": "invis",
    "fontcolor": "#9ca3af",
    "fontname": "Arial",
    "fontsize": "14",
}

mcp_label_style = {
    "style": "invis",
    "fontcolor": "#9ca3af",
    "fontname": "Arial Bold",
    "fontsize": "16",
}

benefit_title_style = {
    "style": "invis",
    "fontcolor": "#8b5cf6",
    "fontname": "Arial Bold",
    "fontsize": "16",
}

benefit_desc_style = {
    "style": "invis",
    "fontcolor": "#9ca3af",
    "fontname": "Arial",
    "fontsize": "13",
}

# Create nodes - Using available icons and proper text

# Title at the top with icon
dot.node("title", "🧠 AgentCore Gateway", _attributes=title_style)

# Top right section label  
dot.node("apis_label", "APIs, tools, resources", _attributes=section_label_style)

# Left side - Agent with proper icon
dot.node("agent_icon", "Agent", _attributes=agent_style)

# MCP protocol labels
dot.node("mcp_icon", "📋 MCP", _attributes=mcp_label_style)
dot.node("mcp_actions", "List tools,\nInvoke tool,\nSearch", _attributes=service_label_style)

# Central AgentCore Gateway with brain icon inside
dot.node("gateway", "🧠\n\nAgentCore\nGateway", _attributes=gateway_style)

# Right side endpoints with proper black fill and colored borders
dot.node("api_endpoint", "API Endpoint", _attributes=red_endpoint_style)
dot.node("mcp_server", "MCP Server", _attributes=blue_endpoint_style)
dot.node("aws_lambda", "AWS Lambda", _attributes=green_endpoint_style)
dot.node("smithy_model", "Smithy Model", _attributes=yellow_endpoint_style)

# Right side tools with black fill and gray borders
dot.node("tool1", "Tool", _attributes=tool_style)
dot.node("tool2", "Tool", _attributes=tool_style)
dot.node("tool3", "Tool", _attributes=tool_style)
dot.node("tool4", "Tool", _attributes=tool_style)

# Service descriptions
dot.node("restful_desc", "RESTful services", _attributes=service_label_style)
dot.node("mcp_desc", "MCP servers", _attributes=service_label_style)
dot.node("lambda_desc", "AWS Lambda functions", _attributes=service_label_style)
dot.node("smithy_desc", "Smithy model servers", _attributes=service_label_style)

# Bottom benefits section
dot.node("benefit1_title", "Time to value", _attributes=benefit_title_style)
dot.node("benefit1_desc", "Simplify access to\nexisting APIs, data", _attributes=benefit_desc_style)

dot.node("benefit2_title", "Secure", _attributes=benefit_title_style)
dot.node("benefit2_desc", "Inbound, outbound auth,\naccess control", _attributes=benefit_desc_style)

dot.node("benefit3_title", "Serverless", _attributes=benefit_title_style)
dot.node("benefit3_desc", "Scales on demand,\nno infra management", _attributes=benefit_desc_style)

dot.node("benefit4_title", "Built-in tool search", _attributes=benefit_title_style)
dot.node("benefit4_desc", "Tools automatically indexed\nand searchable", _attributes=benefit_desc_style)

# Layout management with subgraphs for proper positioning

# Top section
with dot.subgraph() as top:
    top.attr(rank="min")
    top.node("title")
    top.node("apis_label")

# Left side elements
with dot.subgraph() as left:
    left.attr(rank="same")
    left.node("agent_icon")
    left.node("mcp_icon")
    left.node("mcp_actions")

# Center gateway
with dot.subgraph() as center:
    center.attr(rank="same")
    center.node("gateway")

# Right side endpoints 
with dot.subgraph() as endpoints:
    endpoints.attr(rank="same")
    endpoints.node("api_endpoint")
    endpoints.node("mcp_server")
    endpoints.node("aws_lambda")
    endpoints.node("smithy_model")

# Tools section
with dot.subgraph() as tools:
    tools.attr(rank="same")
    tools.node("tool1")
    tools.node("tool2")
    tools.node("tool3")
    tools.node("tool4")

# Service descriptions
with dot.subgraph() as services:
    services.attr(rank="same")
    services.node("restful_desc")
    services.node("mcp_desc")
    services.node("lambda_desc")
    services.node("smithy_desc")

# Bottom benefits section
with dot.subgraph() as benefits:
    benefits.attr(rank="max")
    benefits.node("benefit1_title")
    benefits.node("benefit1_desc")
    benefits.node("benefit2_title")
    benefits.node("benefit2_desc")
    benefits.node("benefit3_title")
    benefits.node("benefit3_desc")
    benefits.node("benefit4_title")
    benefits.node("benefit4_desc")

# Main flow connections with proper white arrows
dot.edge("agent_icon", "gateway", 
         color="white", penwidth="3", arrowhead="vee", arrowsize="1.0")

# Gateway to endpoints - main connections
dot.edge("gateway", "api_endpoint", 
         color="white", penwidth="3", arrowhead="vee", arrowsize="1.0")
dot.edge("gateway", "mcp_server", 
         color="white", penwidth="3", arrowhead="vee", arrowsize="1.0")
dot.edge("gateway", "aws_lambda", 
         color="white", penwidth="3", arrowhead="vee", arrowsize="1.0")
dot.edge("gateway", "smithy_model", 
         color="white", penwidth="3", arrowhead="vee", arrowsize="1.0")

# Endpoints to tools
dot.edge("api_endpoint", "tool1", 
         color="white", penwidth="2", arrowhead="vee", arrowsize="0.8")
dot.edge("mcp_server", "tool2", 
         color="white", penwidth="2", arrowhead="vee", arrowsize="0.8")
dot.edge("aws_lambda", "tool3", 
         color="white", penwidth="2", arrowhead="vee", arrowsize="0.8")
dot.edge("smithy_model", "tool4", 
         color="white", penwidth="2", arrowhead="vee", arrowsize="0.8")

# Invisible edges for positioning labels properly
dot.edge("mcp_icon", "agent_icon", style="invis")
dot.edge("mcp_actions", "mcp_icon", style="invis")

# Position service descriptions next to tools
dot.edge("tool1", "restful_desc", style="invis")
dot.edge("tool2", "mcp_desc", style="invis")
dot.edge("tool3", "lambda_desc", style="invis")
dot.edge("tool4", "smithy_desc", style="invis")

# Position benefit descriptions under titles
dot.edge("benefit1_title", "benefit1_desc", style="invis")
dot.edge("benefit2_title", "benefit2_desc", style="invis")
dot.edge("benefit3_title", "benefit3_desc", style="invis")
dot.edge("benefit4_title", "benefit4_desc", style="invis")

# Render the diagram
dot.render("agentcore-gateway-graphviz", view=False)
print("AgentCore Gateway diagram generated with correct styling: agentcore-gateway-graphviz.png")
print("Key fixes applied:")
print("- Black fill for all rectangles")
print("- Gradient border colors") 
print("- Rounded rectangle shapes")
print("- Complete layout matching original")
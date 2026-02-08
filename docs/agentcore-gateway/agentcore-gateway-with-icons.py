#!/usr/bin/env python3
#
# agentcore-gateway-with-icons.py
#
# Enhanced version using actual PNG icons from the icons directory
# This version incorporates real brain and agent icons instead of emojis
#
# pylint: disable=pointless-statement, expression-not-assigned

from graphviz import Digraph
import os

# Get the absolute path to icons directory
icons_dir = os.path.join(os.path.dirname(__file__), "icons", "AI VR Bot", "Solid", "PNG")

# Create main diagram
dot = Digraph(
    "AgentCore Gateway with Icons",
    graph_attr={
        "bgcolor": "#0f0f23",
        "rankdir": "LR", 
        "nodesep": "1.0",
        "ranksep": "1.5",
        "fontname": "Arial",
        "fontsize": "28",
        "fontcolor": "white",
        "splines": "ortho",
        "pad": "0.5",
    },
    format="png",
)

# Icon paths - using available icons
brain_icon = os.path.join(icons_dir, "Icon_80px_Brain_1_white.png")
agent_icon = os.path.join(icons_dir, "Icon_80px_Robot_1_white.png") 
chip_icon = os.path.join(icons_dir, "Icon_80px_Chip_white.png")

# Node styles with BLACK FILL and COLORED BORDERS
gateway_style = {
    "style": "filled,rounded",
    "fillcolor": "black",
    "color": "#8b5cf6",
    "penwidth": "4",
    "fontcolor": "white",
    "fontname": "Arial Bold",
    "fontsize": "20",
    "width": "3.0",
    "height": "4.5",
    "shape": "box",
    "image": brain_icon if os.path.exists(brain_icon) else "",
    "imagescale": "true",
    "labelloc": "b",  # Place label below image
}

agent_style = {
    "style": "filled,rounded", 
    "fillcolor": "black",
    "color": "#8b5cf6",
    "penwidth": "2",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14",
    "shape": "box",
    "image": agent_icon if os.path.exists(agent_icon) else "",
    "imagescale": "true",
    "labelloc": "b",
}

# Endpoint styles with black fill, colored borders
red_style = {
    "style": "filled,rounded",
    "fillcolor": "black",
    "color": "#ef4444", 
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

blue_style = {
    "style": "filled,rounded",
    "fillcolor": "black",
    "color": "#3b82f6",
    "penwidth": "3", 
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

green_style = {
    "style": "filled,rounded",
    "fillcolor": "black",
    "color": "#10b981",
    "penwidth": "3",
    "fontcolor": "white", 
    "fontname": "Arial",
    "fontsize": "16",
    "shape": "box",
}

yellow_style = {
    "style": "filled,rounded",
    "fillcolor": "black",
    "color": "#fbbf24",
    "penwidth": "3",
    "fontcolor": "white",
    "fontname": "Arial", 
    "fontsize": "16",
    "shape": "box",
}

tool_style = {
    "style": "filled,rounded",
    "fillcolor": "black",
    "color": "#6b7280",
    "penwidth": "2",
    "fontcolor": "white",
    "fontname": "Arial",
    "fontsize": "14", 
    "shape": "box",
}

# Text label styles
title_style = {
    "style": "invis",
    "fontcolor": "white",
    "fontname": "Arial Bold", 
    "fontsize": "36",
}

section_style = {
    "style": "invis",
    "fontcolor": "#8b5cf6",
    "fontname": "Arial",
    "fontsize": "18",
}

label_style = {
    "style": "invis", 
    "fontcolor": "#9ca3af",
    "fontname": "Arial",
    "fontsize": "14",
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

# Create nodes with proper icons and styling

# Title
dot.node("title", f"🧠 AgentCore Gateway", _attributes=title_style)

# Top right label
dot.node("apis_label", "APIs, tools, resources", _attributes=section_style)

# Left side
dot.node("agent", "Agent", _attributes=agent_style)
dot.node("mcp_label", "📋 MCP", _attributes=label_style)
dot.node("mcp_actions", "List tools,\\nInvoke tool,\\nSearch", _attributes=label_style)

# Central gateway with brain icon
dot.node("gateway", "AgentCore\\nGateway", _attributes=gateway_style)

# Endpoints 
dot.node("api_endpoint", "API Endpoint", _attributes=red_style)
dot.node("mcp_server", "MCP Server", _attributes=blue_style) 
dot.node("aws_lambda", "AWS Lambda", _attributes=green_style)
dot.node("smithy_model", "Smithy Model", _attributes=yellow_style)

# Tools
dot.node("tool1", "Tool", _attributes=tool_style)
dot.node("tool2", "Tool", _attributes=tool_style)
dot.node("tool3", "Tool", _attributes=tool_style)
dot.node("tool4", "Tool", _attributes=tool_style)

# Service descriptions
dot.node("restful", "RESTful services", _attributes=label_style)
dot.node("mcp_servers", "MCP servers", _attributes=label_style)
dot.node("lambda_funcs", "AWS Lambda functions", _attributes=label_style)
dot.node("smithy_servers", "Smithy model servers", _attributes=label_style)

# Bottom benefits
dot.node("benefit1_title", "Time to value", _attributes=benefit_title_style)
dot.node("benefit1_desc", "Simplify access to\\nexisting APIs, data", _attributes=benefit_desc_style)

dot.node("benefit2_title", "Secure", _attributes=benefit_title_style) 
dot.node("benefit2_desc", "Inbound, outbound auth,\\naccess control", _attributes=benefit_desc_style)

dot.node("benefit3_title", "Serverless", _attributes=benefit_title_style)
dot.node("benefit3_desc", "Scales on demand,\\nno infra management", _attributes=benefit_desc_style)

dot.node("benefit4_title", "Built-in tool search", _attributes=benefit_title_style)
dot.node("benefit4_desc", "Tools automatically indexed\\nand searchable", _attributes=benefit_desc_style)

# Layout with subgraphs
with dot.subgraph() as top:
    top.attr(rank="min")
    top.node("title")
    top.node("apis_label")

# Main flow connections
dot.edge("agent", "gateway", color="white", penwidth="3", arrowhead="vee")

dot.edge("gateway", "api_endpoint", color="white", penwidth="3", arrowhead="vee")
dot.edge("gateway", "mcp_server", color="white", penwidth="3", arrowhead="vee")
dot.edge("gateway", "aws_lambda", color="white", penwidth="3", arrowhead="vee")
dot.edge("gateway", "smithy_model", color="white", penwidth="3", arrowhead="vee")

dot.edge("api_endpoint", "tool1", color="white", penwidth="2", arrowhead="vee")
dot.edge("mcp_server", "tool2", color="white", penwidth="2", arrowhead="vee") 
dot.edge("aws_lambda", "tool3", color="white", penwidth="2", arrowhead="vee")
dot.edge("smithy_model", "tool4", color="white", penwidth="2", arrowhead="vee")

# Positioning edges
dot.edge("mcp_label", "agent", style="invis")
dot.edge("mcp_actions", "mcp_label", style="invis")
dot.edge("tool1", "restful", style="invis")
dot.edge("tool2", "mcp_servers", style="invis")
dot.edge("tool3", "lambda_funcs", style="invis")
dot.edge("tool4", "smithy_servers", style="invis")

# Benefits positioning
dot.edge("benefit1_title", "benefit1_desc", style="invis")
dot.edge("benefit2_title", "benefit2_desc", style="invis") 
dot.edge("benefit3_title", "benefit3_desc", style="invis")
dot.edge("benefit4_title", "benefit4_desc", style="invis")

# Render
dot.render("agentcore-gateway-with-icons", view=False)
print(f"Enhanced AgentCore Gateway diagram generated: agentcore-gateway-with-icons.png")
print(f"Icons directory: {icons_dir}")
print(f"Brain icon exists: {os.path.exists(brain_icon)}")
print(f"Agent icon exists: {os.path.exists(agent_icon)}")
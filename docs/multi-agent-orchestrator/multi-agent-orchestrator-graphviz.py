#!/usr/bin/env python3
#
# multi-agent-orchestrator-graphviz.py
#
# Script generates a small diagram for AWS meetup presentation.
#
# pylint: disable=pointless-statement, expression-not-assigned

from graphviz import Digraph

dot = Digraph(
    "Multi Agent Orchestrator",
    graph_attr={
        # "splines": "ortho",
        "nodesep": "1.0",
    },
    format="png",
)

dot.attr(bgcolor='transparent')
dot.attr('edge', color='white')
# Ranks for layout
dot.attr(rankdir="LR")
dot.attr("node", shape="rectangle")

# Node styles
green_style = {
    "style": "filled",
    "fillcolor": "#8BC34A",
    "fontcolor": "white",
    "fontsize": "20",
    "shape": "rectangle",
    "color": "transparent",
}
white_style = {
    "style": "filled",
    "fillcolor": "white",
    "fontcolor": "black",
    "fontsize": "20",
    "shape": "rectangle",
    "color": "transparent",
}

with dot.subgraph() as o:
    o.node("orc", "Orchestrator", **green_style)
    o.edge("orc", "w1")
    o.edge("orc", "w2")
    o.edge("orc", "w3")

with dot.subgraph() as w:
    w.attr(rank='same')
    w.node('w1', "Worker", **green_style)
    w.node('w2', "Worker", **green_style)
    w.node('w3', "Worker", **green_style)
    w.edge('w1', 'w2', style='invis')
    w.edge('w2', 'w3', style='invis')


with dot.subgraph() as s:
    s.node("syn", "Synthesizer", **green_style)
    s.edge("w1", "syn")
    s.edge("w2", "syn")
    s.edge("w3", "syn")

# Render the diagram
dot.render("multi-agent-orchestrator-graphviz", view=True)

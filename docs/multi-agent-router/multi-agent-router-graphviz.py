#!/usr/bin/env python3
#
# multi-agent-router-graphviz.py
#
# Script generates a small diagram for AWS meetup presentation.
#
# pylint: disable=pointless-statement, expression-not-assigned

from graphviz import Digraph

dot = Digraph(
    "Multi Agent Router",
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
    o.node("orc", "Router", **green_style)
    o.edge("orc", "l1")

with dot.subgraph() as w:
    w.attr(rank='same')
    w.node('l1', "LLM", **green_style)
    w.node('l2', "LLM", **green_style)
    w.node('l3', "LLM", **green_style)
    w.edge('l1', 'l2', style='invis')
    w.edge('l2', 'l3', style='invis')


with dot.subgraph() as s:
    s.node("out", "Output", **green_style)
    s.edge("l1", "out")

# Render the diagram
dot.render("multi-agent-router-graphviz", view=True)

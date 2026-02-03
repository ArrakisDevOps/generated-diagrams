#!/usr/bin/env python3
#
# prompt-chaining-graphviz.py
#
# Script generates a small diagram for AWS meetup presentation.
#
# pylint: disable=pointless-statement, expression-not-assigned

from graphviz import Digraph

dot = Digraph(
    "Prompt Chaining Diagram",
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
red_style = {
    "style": "filled",
    "fillcolor": "red",
    "fontcolor": "black",
    "fontsize": "20",
    "shape": "rectangle",
    "color": "transparent",
}

dot.node("input", "Input", **green_style)
dot.node('l1', "LLM 1", **green_style)
dot.node('l2', "LLM 2", **green_style)
dot.node("l3", "LLM 3", **green_style)
dot.edge("input", "l1")
dot.edge("l1", "l2")
dot.edge("l2", "g")
dot.edge("g", "l3")
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('g', "Gate", **green_style)
    s.node('f', "Fail", **red_style)
    s.edge("g", "f")


# Render the diagram
dot.render("prompt-chaining-graphviz", view=True)

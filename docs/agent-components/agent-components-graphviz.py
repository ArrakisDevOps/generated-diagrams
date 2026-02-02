from graphviz import Digraph

dot = Digraph(
    "Agent Components",
    graph_attr={
        "splines": "ortho",
        "nodesep": "1.0",
    },
    format="png",
)

dot.attr(bgcolor="transparent")
dot.attr("edge", color="white")
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

with dot.subgraph() as u:
    u.node("User", "User\nRequest", **white_style)
    u.edge(
        "User",
        "Core",
        dir="both",
    )
with dot.subgraph() as s:
    s.attr(rank="same")
    s.node("Memory", "Memory\nModule", **green_style)
    s.node("Core", "Agent Core", **green_style)
    s.node("Tools", "Tool(s)", **green_style)
    s.edge("Memory", "Core", style="invis")
    s.edge("Core", "Tools", style="invis")
    s.edge("Core", "Memory", dir="both")
    s.edge("Core", "Tools", dir="both")
with dot.subgraph() as p:
    p.node("Planning", "Planning\nModule", rank="same", **green_style)
    p.edge("Core", "Planning", dir="both")

# Render the diagram
dot.render("agent-components-graphviz", view=True)

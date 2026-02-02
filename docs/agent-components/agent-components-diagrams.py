#!/usr/bin/env python3
#
# agent-components.py
#
# Script generates a small diagram for AWS meetup presentation.
#
# pylint: disable=pointless-statement, expression-not-assigned

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.aws.database import ElasticacheForMemcached
from diagrams.aws.ml import RekognitionImage
from diagrams.aws.ml import Sagemaker
from diagrams.onprem.compute import Server

graph_attr = {
    "concentrate": "true",
    "splines": "curved",
    "bgcolor": "transparent",
    "labelloc": "t",
    "labeljust": "l",
    "fontsize": "24",
    "align": "right",
}

edge_attr = {
    "minlen": "1",
    "color": "white",
    # "headport": "w",
}

with Diagram(
    "\n\nAgent components\n\n",
    filename="agent-components-diagrams",
    show=False,
    graph_attr=graph_attr,
    edge_attr=edge_attr,
):
    user = Users("User Request")
    memory = ElasticacheForMemcached("Memory Module")
    agent = RekognitionImage("Agent Core")
    tool = Server("Tool(s)")
    plan = Sagemaker("Planning Module")

    user >> Edge(dir="both") >> agent
    agent >> Edge(dir="both") >> memory
    agent >> Edge(dir="both") >> tool
    agent >> Edge(dir="both") >> plan

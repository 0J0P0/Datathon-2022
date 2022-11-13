import networkx as nx
from read_write import *
import matplotlib.pyplot as plt


"""Modul containing the functions that creates a Graph with the solutions of 
the paths and saves the graph in an .png image."""

PathGraph: TypeAlias = nx.Graph()


def paint_nodes_and_show(file_name: str) -> None:
    """Paints the nodes and the edges of the paths and displays 
    the paths in an interactive screen."""
    
    labels = {}  # labels for output and input drivers.
    color_map = []
    node_sizes = []

    for index, attributes in PathGraph.nodes.data():
        if attributes['type'] == 'driver':
            color_map.append('red')
            node_sizes.append(50)
            if attributes['inout']:
                labels[index] = "$I$"
            else:
                labels[index] = "$O$"
        elif attributes['type'] == 'aux': 
            color_map.append('white')
            node_sizes.append(0)
        else:
            color_map.append('blue')
            node_sizes.append(50)

    nx.draw(PathGraph, nx.get_node_attributes(PathGraph, 'pos'), node_color=color_map, width=0.5,
            node_size=node_sizes, with_labels=False, node_shape="s")

    nx.draw_networkx_labels(PathGraph, nx.get_node_attributes(PathGraph, 'pos'), labels, font_size=10)
    plt.savefig(file_name)


def get_attributes_pin(pin: Pin) -> dict:
    """Returns a dictionary with the attributes of the Pin."""
    return {'type': 'pin', 'id': pin.id, 'pos': pin.pos}


def get_attributes_aux_nodes(pos: Coord) -> dict:
    """Returns a dictionary with tha attributes of the auxiliar node."""
    return {'type': 'aux', 'pos': pos}


def get_attributes_driver(driver: Driver) -> dict:
    """Returns a dictionary with the attributes of the Driver."""
    return {'type': 'driver', 'id': driver.id, 'pos': driver.pos, 'inout': (driver.input)}


def add_nodes(paths: List[Path]) -> None:
    """Adds the nodes to the graph PathGraph. """
    for path in paths:
        # Drivers nodes.
        att1: dict = get_attributes_driver(path.dri_in)
        att2: dict = get_attributes_driver(path.dri_out)
        PathGraph.add_node(path.dri_in.pos, **att1)
        PathGraph.add_node(path.dri_out.pos, **att2)

        # Coordenates of the auxiliar node (only for visual purposes).
        pos1 = (path.pins[0].pos[0], path.dri_in.pos[1])
        pos2 = (path.pins[-1].pos[0], path.dri_out.pos[1])
        att3: dict = get_attributes_aux_nodes(pos1)
        att4: dict = get_attributes_aux_nodes(pos2)
        PathGraph.add_node(pos1, **att3)
        PathGraph.add_node(pos2, **att4)

        # Pins nodes.
        for i in range (len(path.pins)):
            att5: dict = get_attributes_pin(path.pins[i])
            PathGraph.add_node(path.pins[i].pos, **att5)
            if i < len(path.pins)-1: 
                pos3 = (path.pins[i+1].pos[0], path.pins[i].pos[1])
                att6: dict = get_attributes_aux_nodes(pos3)
                PathGraph.add_node(pos3, **att6)


def add_edges(paths) -> None: 
    """Adds the edges to the graph PathGraph. """
    for path in paths:
        # Drivers edges.
        edge1 = (path.pins[0].pos[0], path.dri_in.pos[1])
        PathGraph.add_edge(path.dri_in.pos, edge1)
        PathGraph.add_edge(edge1, path.pins[0].pos)
        edge2 = (path.pins[-1].pos[0], path.dri_out.pos[1])
        PathGraph.add_edge(path.dri_out.pos, edge2)
        PathGraph.add_edge(edge2, path.pins[-1].pos)

        # Pins edges.
        for i in range(len(path.pins)-1):
            edge3 = (path.pins[i+1].pos[0], path.pins[i].pos[1])
            if (path.pins[i].pos != edge3):
                PathGraph.add_edge(path.pins[i].pos, edge3)
            if (edge3 != path.pins[i+1].pos):
                PathGraph.add_edge(edge3, path.pins[i+1].pos)


def add_nodes_and_edges(paths: List[Path]) -> None:
    """Adds all the nodes (both pins and drivers) and all the edges to 
    the graph PathGraph."""

    # Addition of nodes.
    add_nodes(paths) 

     # Addition of  edges
    add_edges(paths)
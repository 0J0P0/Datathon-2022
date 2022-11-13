import networkx as nx
import matplotlib.pyplot as plt
from read_write import *


PinsGraph: TypeAlias = nx.Graph()


def get_attributes_pin(pin: Pin) -> dict:
    """ Returns a dictionary with the attributes of the pin """
    return {'type': 'pin', 'id': pin.id, 'pos': pin.pos}


def get_attributes_driver(driver: Driver) -> dict:
    """ Returns a dictionary with the attributes of the driver """
    return {'type': 'driver', 'id': driver.id, 'pos': driver.pos, 'inout': (driver.input)}


def get_attributes_false_nodes(pos: Coord) -> dict: 
    return {'type': 'false', 'pos': pos}


def add_nodes_and_edges(paths: List[Path]) -> None:
    """ Adds all the nodes (both pins and drivers) and all the edges to 
    the graph PinsGraph """

    # add the nodes
    for path in paths:
        
        att1: dict = get_attributes_driver(path.dri_in)
        att2: dict = get_attributes_driver(path.dri_out)
        PinsGraph.add_node(path.dri_in.pos, **att1)
        PinsGraph.add_node(path.dri_out.pos, **att2)

        pos1 = (path.pins[0].pos[0], path.dri_in.pos[1])
        pos2 = (path.pins[-1].pos[0], path.dri_out.pos[1])

        att3: dict = get_attributes_false_nodes(pos1)
        att4: dict = get_attributes_false_nodes(pos2)

        PinsGraph.add_node(pos1, **att3)
        PinsGraph.add_node(pos2, **att4)

        for i in range (len(path.pins)):
            att5: dict = get_attributes_pin(path.pins[i])
            PinsGraph.add_node(path.pins[i].pos, **att5)
            if i < len(path.pins)-1: 
                pos3 = (path.pins[i+1].pos[0], path.pins[i].pos[1])
                att6: dict = get_attributes_false_nodes(pos3)
                PinsGraph.add_node(pos3, **att6)


    # add the edges
    for path in paths:

        edge1 = (path.pins[0].pos[0], path.dri_in.pos[1])
        PinsGraph.add_edge(path.dri_in.pos, edge1)
        PinsGraph.add_edge(edge1, path.pins[0].pos)

        edge2 = (path.pins[-1].pos[0], path.dri_out.pos[1])
        PinsGraph.add_edge(path.dri_out.pos, edge2)
        PinsGraph.add_edge(edge2, path.pins[-1].pos)

        for i in range(len(path.pins)-1):
           
            edge3 = (path.pins[i+1].pos[0], path.pins[i].pos[1])
            PinsGraph.add_edge(path.pins[i].pos, edge3)
            PinsGraph.add_edge(edge3, path.pins[i+1].pos)


def paint_nodes_and_show() -> None:
    """ Paints the nodes and the edges of the graph PinsGraph and displays 
    the graph in an interactive screen """
    color_map = []
    node_sizes = []
    labels = {}

    for index, node in PinsGraph.nodes.data():
        print(index)
        if node['type'] == 'driver':
            color_map.append('red')
            node_sizes.append(50)
            if node['inout']:
                labels[index] = "$I$"
            else:
                labels[index] = "$O$"
        elif node['type'] == 'false': 
            color_map.append('white')
            node_sizes.append(0)
        else:
            color_map.append('blue')
            node_sizes.append(50)

    nx.draw(PinsGraph, nx.get_node_attributes(PinsGraph, 'pos'), node_color=color_map, width=0.5,
            node_size=node_sizes, with_labels=False, node_shape="s")

    nx.draw_networkx_labels(PinsGraph, nx.get_node_attributes(PinsGraph, 'pos'), labels, font_size=10)
    plt.show()
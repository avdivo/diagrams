from diagrams import Diagram, Edge, Node

with Diagram('My Diagram', direction='TB'):
    n1 = Node('n1', style='filled', fillcolor='#40e0d0')
    n2 = Node('n2')
    n3 = Node('n3')
    n4 = Node('n4')
    n5 = Node('n5')
    n6 = Node('n6')

    n1 >> n2
    n1 >> n3
    n1 >> n4
    n1 >> n5
    n3 - n4
    n5 >> Edge(label='This is a label', color='red') >> n6
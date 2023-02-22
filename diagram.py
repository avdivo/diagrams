import sqlite3

from diagrams import Diagram, Edge, Node

"""

type 'mozg'             - бирюзовый
name 'time', 'time_p'   - желтый
name 'time_0', 't0'     - зеленый
name 'print'            - синий
name 'пло'              - красный (оттенок)
name 'хоро'             - серый

"""

conn = sqlite3.connect('Li_db_v1_4.db')
cursor = conn.cursor()

nodes = cursor.execute("SELECT ID, name, type FROM tochki")

for i in nodes.fetchall():


n = []
with Diagram('My Diagram', direction='TB'):
    n.append(Node('n1', style='filled', fillcolor='cadetblue', fontsize="20pt"))
    n.append(Node('n2', style='filled', fillcolor='lemonchiffon', fontsize="20pt"))
    n.append(Node('n3', style='filled', fillcolor='aqua', fontsize="20pt"))
    n.append(Node('n4', style='filled', fillcolor='limegreen', fontsize="20pt"))
    n.append(Node('n5', style='filled', fillcolor='salmon', fontsize="20pt"))
    n.append(Node('n6', style='filled', fillcolor='silver', fontsize="20pt"))

    for i in n:
        for j in n:
            i - j
            j >> i

    # n1 >> n2
    # n1 >> n3
    # n1 >> n4
    # n1 >> n5
    # n3 - n4
    # n5 >> Edge(label='This is a label', color='red') >> n6
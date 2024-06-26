# -*- coding: utf-8 -*-
"""47_Exp 5-Network.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sglPaMnUm3BICLUrS8aw3Udp46ren_3H
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(17,0.5)
nx.draw(G)

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(["A", "B", "C" , "D" , "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"])

# Add edges
G.add_edges_from([("P","F"),("P","H"),("P","I"),("P","J"),("P","K"),("P","L"),("P","M"),("P","N"),("P","G"),("J","K"),("K","L"),("L","M"),
 ("F","O"),("F","Q"),("F","O"),("F","A"),("F","B"),("Q","O"),("Q","C"),("Q","D"),("Q","E"),
  ("A","F"),("A","D"),("A","E"),("E","D"),("D","B"),
                  ("C","O"),("C","Q"),("C","D"),("C","B"),
                  ("B","C"),("B","F"),("B","D"),("B","E")])

# Visualize the graph
nx.draw(G, with_labels=True)
plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Generate a random graph with 10 nodes and a 50% probability of an edge between any two nodes
G = nx.gnp_random_graph(10, 0.5)

# Print the nodes in the graph to see their names
print("Nodes in the graph:", G.nodes())

# Define a dictionary to store labels for specific nodes
labeldict = {}
labeldict[0] = "shopkeeper"  # Assuming the node names are integers; adjust as needed
labeldict[1] = "angry man with parrot"
labeldict[2] = "new label"

# Visualize the graph with node labels
nx.draw(G, labels=labeldict, with_labels=True)

# Show the plot
plt.show()

nx.clustering(G)

nx.degree(G)

nx.degree_centrality(G)

sorted(nx.degree_centrality(G).values())
m_influential=nx.degree_centrality(G)
for w in sorted(m_influential,key=m_influential.get,reverse=True):
  print(w,m_influential[w])

nx.eigenvector_centrality(G)

nx.betweenness_centrality(G)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

#G = nx.Graph()
#G = nx.path_graph(4, create_using=nx.DiGraph)
G1= nx.Graph(G)

#nx.graph

nx.draw(G,with_labels=True)

pos=nx.spring_layout(G)
betCent=nx.betweenness_centrality(G,normalized=True,endpoints=True)
node_color=[20000.0*G.degree(v)for v in G]
node_size=[v*10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G,pos=pos,with_labels=False,node_color=node_color,node_size=node_size)
sorted(betCent,key=betCent.get,reverse=True)[:5]

#closeness centrality
closeness_centrality=nx.centrality.closeness_centrality(G)
(sorted(closeness_centrality.items(),key=lambda item:item[1],reverse=True))[:8]

node_size=[v*50 for v in closeness_centrality.values()]
plt.figure(figsize=(15,8))
nx.draw_networkx(G,pos=pos,node_size=node_size,with_labels=False,width=0.15)
plt.axis("off")

#bridges
nx.has_bridges(G)


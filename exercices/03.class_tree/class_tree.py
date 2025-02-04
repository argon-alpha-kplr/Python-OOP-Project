# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree
import os


# Fonction pour créer un arbre à partir d'un dictionnaire Python
def json_dict_from_file():
    local_path=os.path.dirname(os.path.abspath(__file__))
    json_data= json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    json_str = json.dumps(json_data)
    json_data=(unidecode(json_str))
    json_dict=json.loads(json_data)

    return json_dict

#Fonction récursive pour parcourir un dictionnaire Python et créer des noeuds dans un arbre
def creat_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            new_node_id= f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            creat_tree_from_dict(tree, new_node_id, value)

        else:
            leaf_node_id =f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)


# Fonction principale
def main():
    my_tree = Tree()
    my_tree.create_node(tag="Racine", identifier="racine")

    json_dict=json_dict_from_file()
    creat_tree_from_dict(my_tree, "racine", json_dict)

    #Afficher l'arbre de classes
    my_tree.show()

 # Code principal
if __name__=='__main__':
    main()
from xml.etree import ElementTree

RED = 0
GREEN = 1
BLUE = 2

result = [0,0,0]

def set_weight(color, level):
    if color == 'red':
        result[RED] += level
    elif color == 'green':
        result[GREEN] += level
    elif color == 'blue':
        result[BLUE] += level


def walk_tree(root, level=2):
    for node in root:
        color = node.attrib['color']
        set_weight(color, level)
        walk_tree(node, level=level+1)



#tree = ElementTree.parse('example1.xml')
#root = tree.getroot()

root = ElementTree.fromstring(input())

set_weight(root.attrib['color'], 1)
walk_tree(root)
print(*result)
from collections import defaultdict
create_node=lambda:defaultdict(create_node,{"ec":0}) #ec is count of words end at node.

class Trie:
    def __init__(self, *words):
        self.root = create_node()
        for word in words:
            self.add(word)

    def add(self, word):
        cur_node = self.root
        for letter in word:
            cur_node = cur_node[letter]
        cur_node["ec"] +=1

    def __contains__(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node:
                return False
            cur_node = cur_node[letter]
        return cur_node["ec"]>0
    
    def __getitem__(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node:
                return 0
            cur_node = cur_node[letter]
        return cur_node["ec"]

    def delete(self, word,all=False):
        cur_node = self.root
        nodes = [cur_node]
        for letter in word:
            cur_node = cur_node[letter]
            nodes.append(cur_node)
        if all:
            del cur_node["ec"]
        else:
            cur_node["ec"]-=1
            if cur_node["ec"]<1:
                del cur_node["ec"]
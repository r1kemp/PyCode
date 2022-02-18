# 
#  https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3
#
#  https://github.com/kamyu104/GoogleKickStart-2020
#

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.count = 1

    def increment(self):
        self.count += 1

    def.get_count(self):
        return self.count;

class Trie(object):
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
                node.increment()
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

    def add_up(self):
        node=self.root


def read_ints():
    return (int(x) for x in input().split(' '))

def read_ints_list():
    return [int(x) for x in input().split(' ')]

T, = read_ints()

for t in range(1, T+1):
    N, K = read_ints()

    trie = Trie()

    for _ in range(N):
        trie.insert(input())



    print(f"Case #{t}: {opt}")






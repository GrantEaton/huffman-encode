from heapq import heappush, heappop
from collections import Counter
import node as node


def get_encode(root):
    codes_map = {}
    get_encode_helper(root, codes_map, "")
    return codes_map

def get_encode_helper(node, codes_map, code):
    if type(node.left[1]) is str:
       codes_map[node.left[1]] = code
    else:
       get_encode_helper(node.left[1], codes_map, code + "0")
    if type(node.right[1]) is str:
       codes_map[node.right[1]] = code
    else:
       get_encode_helper(node.right[1], codes_map, code + "1")


text = "hello my name is grant and i want you to compress this string!"

c = Counter(text)
heap = []
most_common = c.most_common()
for entry in most_common:
    heappush(heap, tuple(reversed(entry)))

while (len(heap) != 1):
    left = heappop(heap)
    right = heappop(heap)
    n = node.Node(left[0] + right[0], left, right)
    heappush(heap, (n.val, n))

print get_encode(heap[0][1])

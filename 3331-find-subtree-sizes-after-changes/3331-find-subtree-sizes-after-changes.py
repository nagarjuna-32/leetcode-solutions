from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build original tree adjacency list
        orig_tree: List[List[int]] = [[] for _ in range(n)]
        for node in range(1, n):
            orig_tree[parent[node]].append(node)

        # Track closest ancestor with each character along current DFS path
        last_seen: List[int] = [-1] * 26
        new_parent = parent[:]

        def reassign_parents(node: int) -> None:
            char_idx = ord(s[node]) - ord("a")
            prev_ancestor = last_seen[char_idx]

            if prev_ancestor != -1 and node != 0:
                new_parent[node] = prev_ancestor

            last_seen[char_idx] = node
            for child in orig_tree[node]:
                reassign_parents(child)
            last_seen[char_idx] = prev_ancestor

        reassign_parents(0)

        # Build modified tree and compute subtree sizes
        mod_tree: List[List[int]] = [[] for _ in range(n)]
        for node in range(1, n):
            mod_tree[new_parent[node]].append(node)

        ans = [0] * n

        def calc_subtree_size(node: int) -> int:
            size = 1
            for child in mod_tree[node]:
                size += calc_subtree_size(child)
            ans[node] = size
            return size

        calc_subtree_size(0)
        return ans
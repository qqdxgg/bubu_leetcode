from typing import List


class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        def dfs(a: int, fa: int) -> bool:
            ok = True  # 变量ok代表以dfs传入的第一个参数为根节点的子树所有节点颜色是否一样
            for b in g[a]:
                if b != fa:
                    t = dfs(b, a)
                    ok = ok and colors[a] == colors[b] and t  # t的参与保证下面ok的功能
                    size[a] += size[b]
            if (
                ok
            ):  # 只有a以下任一子树所有节点颜色都一样才表明此时的size[a]的值可以用于更新ans
                nonlocal ans
                ans = max(ans, size[a])
            return ok

        size = [1] * len(colors)
        g = [[] for _ in range(len(colors))]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0
        dfs(0, -1)
        return ans


edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
colors = [1, 2, 3, 3, 3]
s = Solution()
print(s.maximumSubtreeSize(edges, colors))

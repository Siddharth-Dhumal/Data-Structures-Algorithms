class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_map = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crs_map[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if crs_map[crs] == []:
                return True
            visited.add(crs)
            for pre in crs_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            crs_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
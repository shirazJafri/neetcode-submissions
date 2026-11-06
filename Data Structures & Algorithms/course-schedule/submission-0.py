class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Maintain an adjacency list to build our graph
        # course -> [prereqs]
        prereq_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # Visited set to keep track of cycles i.e. if course seen again in recursive stack
        visiting = set()

        def dfs(course):
            # Base Cases
            if course in visiting:
                # Cycle detected
                return False
            if not prereq_map[course]:
                # No pre-reqs for the course - all clear
                return True

            visiting.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    # If any course fails - return False immediately
                    return False
            visiting.remove(course)  # Finished visiting this particular course and its prereqs
            prereq_map[course] = []  # All recursive calls return safely, clear up prereqs
            return True

        # Have to iterate over all courses incase of disconnected graphs
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

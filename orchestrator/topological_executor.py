from typing import Dict, List


class TopologicalExecutor:

    def resolve(self, graph: Dict[str, List[str]]) -> List[str]:

        resolved = []
        unresolved = set(graph.keys())

        while unresolved:
            progress = False

            for node in list(unresolved):
                deps = graph[node]

                if all(dep in resolved for dep in deps):
                    resolved.append(node)
                    unresolved.remove(node)
                    progress = True

            if not progress:
                raise RuntimeError(
                    f"Cannot resolve execution graph. Cyclic or missing dependency: {unresolved}"
                )

        return resolved

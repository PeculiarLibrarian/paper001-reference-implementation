"""
Replay Diff Engine
Compares two execution runs for semantic drift.
"""


class ReplayDiff:

    @staticmethod
    def diff(run_a: dict, run_b: dict):

        a_snap = run_a.get("snapshots", [])
        b_snap = run_b.get("snapshots", [])

        differences = []

        max_len = max(len(a_snap), len(b_snap))

        for i in range(max_len):

            a = a_snap[i] if i < len(a_snap) else None
            b = b_snap[i] if i < len(b_snap) else None

            if a != b:
                differences.append({
                    "step": i,
                    "a": a,
                    "b": b
                })

        return {
            "equal": len(differences) == 0,
            "differences": differences
        }

# Intuition:
# - Sort the strings and use as key, append to the list held in value
#
# Retro:
# - Worked on first submission, only trip-up on first run was that sorted(s) creates
#   a list of characters which needed to be joined
# - I'm surprised this is a Medium
# - Anecdotally, according to submitting different ways, `not groups.get()` is faster
#   than `if not in groups`

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if not groups.get(key):
                groups[key] = []
            groups[key].append(s)
        return groups.values()

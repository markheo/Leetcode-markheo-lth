class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        l = len(s)
        if l == 1:
            return False
        if l == 2:
            if "".join(reversed(s)) == goal:
                return True
            return False
        else:
            if s == goal:
                cnt = 0
                tmp = list(set(list(s)))
                if len(tmp) == 1:
                    return True
                elif len(tmp) == l//2:
                    return True
                return False
            else:
                cnt = 0
                lst1 = []
                lst2 = []
                for idx in range(l):
                    if s[idx] != goal[idx]:
                        cnt += 1
                        if s[idx] not in lst1:
                            lst1.append(s[idx])
                        if goal[idx] not in lst2:
                            lst2.append(goal[idx])
                lst2.reverse()
                if (lst1 == lst2) and (cnt == 2):
                    return True
                return False
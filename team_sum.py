def dividePlayers(skill):
    skill.sort()
    n = len(skill)
    total = sum(skill)
    teams = n // 2
    if total % teams != 0:
        return -1
    team_sum = total // teams
    chemistry = 0
    i, j = 0, n - 1
    while i < j:
        if skill[i] + skill[j] != team_sum:
            return -1
        chemistry += skill[i] * skill[j]
        i += 1
        j -= 1
    return chemistry
print(dividePlayers([3,2,5,1,3,4]))
print(dividePlayers([1,1,2,3]))
print(dividePlayers([3,4]))
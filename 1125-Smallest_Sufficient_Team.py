"""
- dynamic programming - knapsack (0/1) with bits
- similar: 691-Stickers to Spell Word
"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        
        for i, skills in enumerate(people):
            person_skill_ser = 0
            for skill in skills:
                if skill in key:
                    person_skill_ser |= 1 << key[skill]
            tasks = list(dp.keys())
            for skill_ser in tasks:
                skill_with_person_ser = skill_ser | person_skill_ser
                if skill_with_person_ser == skill_ser: continue
                if skill_with_person_ser not in dp or len(dp[skill_ser]) + 1 < len(dp[skill_with_person_ser]):
                    dp[skill_with_person_ser] = dp[skill_ser] + [i]
        return dp[(1 << len(req_skills)) - 1]
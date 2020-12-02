class Team:
    def __init__(self, name, team_count):
        self.name = name
        self.team_count = team_count
        self.votes = [0]*team_count
    
    def __lt__(self, other):
        i = 0
        while i < self.team_count and self.votes[i] == other.votes[i]:
            i += 1
        
        if i < self.team_count:
            return self.votes[i] < other.votes[i]
        else:
            return self.name > other.name
        
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = dict()
        n = len(votes[0])
        for team in votes[0]:
            teams[team] = Team(team, n)
            
        for votes_ in votes:
            for rank, team in enumerate(votes_):
                teams[team].votes[rank] += 1
        
        teams_list = [val for key, val in teams.items()]
        
        teams_list.sort(reverse = True)
        
        rankings = ''
        for team in teams_list:
            rankings += team.name
        return rankings
                

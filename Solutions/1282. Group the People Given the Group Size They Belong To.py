class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_id = defaultdict(list)
        for Id, size in enumerate(groupSizes):
            size_id[size].append(Id)
        
        groups = []
        for size, ids in size_id.items():
            n = len(ids)
            subgroups = [ids[i:i+size] for i in range(0,n,size)]
            groups.extend(subgroups)
        
        return groups

class Solution:
    def minDeletions(self, s: str) -> int:
        def get_next_empty_slot(i):
            empty_slot = i
            while empty_slot > 0 and arr[empty_slot] != 0:
                empty_slot -= 1
            return empty_slot
        
        char_counts = collections.Counter(s).values()
        freq_counts = list(collections.Counter(char_counts).items())
        
        arr_len = max(freq_counts, key = lambda x: x[0])[0] + 1
        
        arr = [0]*arr_len
        
        for k, v in freq_counts:
            arr[k] = v
            
        delete_count = 0
        empty_i = arr_len-1
        for i in range(arr_len-1, -1, -1):
            if arr[i] > 1:
                for _ in range(arr[i] - 1):
                    
                    empty_i = get_next_empty_slot(min(i, empty_i))
                    delete_count += (i - empty_i)
                    arr[empty_i] = 1
        return delete_count
  

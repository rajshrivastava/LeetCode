class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int ptr = 0;
        for(auto& it: nums){
            if(it!=0){
                nums[ptr] = it;
                ptr++;
            }   
        }
        
        for(int i=ptr;i<nums.size();i++)
            nums[i]=0;
        
    }
};

class SparseVector:
    def __init__(self, nums: List[int]):
        self.csr = {}
        for i,v in enumerate(nums):
            if v!=0:
                self.csr[i] = v
    
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        def dot(v1, v2):
            product = 0
            for k,v in v1.items():
                if k in v2:
                    product += v*v2[k]
            return product
        if len(self.csr) < len(vec.csr):
            return dot(self.csr, vec.csr)
        else:
            return dot(vec.csr, self.csr)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

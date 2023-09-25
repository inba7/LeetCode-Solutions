class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        left = 0
        right = len(products) - 1
        
        for i in range(len(searchWord)):
            ch = searchWord[i]
            while left <= right and (len(products[left]) <= i or products[left][i] != ch):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != ch):
                right -= 1
            
            if left > right:
                res.append([])
            else:
                res.append(products[left:min(left + 3, right + 1)])
        return res
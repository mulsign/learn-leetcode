class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
    
    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1]*num)
    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0
        else:
            return self.nums[-1] // self.nums[-k-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k

productOfNumbers = ProductOfNumbers();
productOfNumbers.add(3);        # [3]
productOfNumbers.add(0);        # [3,0]
productOfNumbers.add(2);        # [3,0,2]
productOfNumbers.add(5);        # [3,0,2,5]
productOfNumbers.add(4);        # [3,0,2,5,4]
productOfNumbers.getProduct(2); # 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); # 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); # 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        # [3,0,2,5,4,8]
productOfNumbers.getProduct(2); # 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 


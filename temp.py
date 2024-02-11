class Main:
    def main(self,n) -> int:
        self.answer = 0
        return self.reverseNum(1100000011)
    

    def reverseNum(self, num: int) -> int:
        if num == 0:
            return self.answer
        if num%10 == 0:
            self.answer += 1
        return self.reverseNum(num//10)
    
    def reverseWithArgs(self, num: int, result: int) -> int:
        if num == 0:
            return result
        result = result * 10 + num%10
        return self.reverseWithArgs(num//10, result)
    
    
    def isPalindrome(self,num) -> bool:
        if num == self.reverseNum(num):
            return True
        return False

obj = Main()
print(obj.main(1824))

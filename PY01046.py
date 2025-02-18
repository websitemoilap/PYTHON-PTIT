def TowerOfHanoi(n , cot1, cot2, cot3):
   if n==1:
      print(cot1,"->",cot2)
      return
   TowerOfHanoi(n-1, cot1, cot3, cot2)
   print(cot1,"->",cot2)
   TowerOfHanoi(n-1, cot3, cot2, cot1)
 
n = int(input())
TowerOfHanoi(n,'A','C','B')

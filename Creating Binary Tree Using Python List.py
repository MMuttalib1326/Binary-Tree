# Creating Binary Tree Using Python List

class BinaryTree:
    def __init__(self,size):
        self.customList=size*[None]
        self.LastUsedIndex=0
        self.maxsize=size
# Insertion
    def insertNode(self,value):
        if self.LastUsedIndex+1==self.maxsize:
            return"The Binary Tree Is Full"
        self.customList[ self.LastUsedIndex+1] = value
        self.LastUsedIndex+=1
        return"The Value has Been Succefully Inserted"
# Searching
    def searchNode(self,Nodevalue):
        for i in range(len(self.customList)):
            if self.customList[i]==Nodevalue:
                return"Success"
        return "Not Found" 
# preOrder Traversal of Binary Tree(Python List)
    def preordertraversal(self,index):
        if index>self.LastUsedIndex:
            return
        print(self.customList[index])
        self.preordertraversal(index*2)
        self.preordertraversal(index*2+1)

# InOrder Traversal of Binary Tree(Python List)
    def inordertraversal(self,index):
        if index>self.LastUsedIndex:
            return
        self.inordertraversal(index*2)
        print(self.customList[index])
        self.inordertraversal(index*2+1)
# PostOrder Traversal of Binary Tree(Python List)
    def postordertraversal(self,index):
        if index>self.LastUsedIndex:
            return
        self.postordertraversal(index*2)
        self.postordertraversal(index*2+1)
        print(self.customList[index])   
# LevelOrderTraversal
    def levelordertraversal(self,index):
        for i in range(index,self.LastUsedIndex+1):
            print(self.customList[i])
# Delete a node from Binary Tree(python list)
    def deleteNode(self,value):
        if self.LastUsedIndex==0:
            return"There is Not any node to delete "
        for i in range(1,self.LastUsedIndex+1):
            if self.customList[i]==value:
                self.customList[i]==self.customList[self.LastUsedIndex]
                self.customList[self.LastUsedIndex]=None
                self.LastUsedIndex-=1
                return"The node has been succefully deleted"
# Delete Entire Binary Tree(python List)
    def deleteBT(self):
        self.customList=None
        return"The BT has been successfully deleted"
                       



            

newBT=BinaryTree(8)
print(newBT.insertNode("drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
#print(newBT.searchNode("Hot")) 
#newBT.preordertraversal(1)
#newBT.inordertraversal(1)
#newBT.postordertraversal(1)
#newBT.levelordertraversal(1)
#print(newBT.deleteNode("Cold"))
#newBT.preordertraversal(1)
print(newBT.deleteBT())
newBT.levelordertraversal(1)


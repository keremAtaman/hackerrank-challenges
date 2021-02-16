import unittest
import math
inputs = [
    [[[1,1],[1,1]],2],
    [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],2],
    [[[1,2,3,4],[7,8,9,10],[13,14,15,16],[19,20,21,22],[25,26,27,28]],7]
]
outputs=[
    [[1,1],[1,1]],
    [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]],
    [[28,27,26,25],[22,9,15,19],[16,8,21,13],[10,14,20,7],[4,3,2,1]]
]

class Test(unittest.TestCase):
    def testExactMatch(self,inputs, function, expectedOutputs):
        """Tests if each entry of inputs passed to the function maps to corresponding entry of expectedOutputs
        Essentiallty, this function does function(inputs[i]) == outputs[i]

        Args:
            inputs (list): The set of inputs, where inputs[0] is the first set of inputs
            function (function): The function that maps inputs to outputs
            expectedOutputs (list): The set of expected outputs, where expectedOutputs[0] is the first set of expected outputs
        """
        for i in range(len(inputs)):
            function_output =function(inputs[i]) 
            self.assertEqual(function_output,expectedOutputs[i],"For the input " +str(inputs[i])+" the expected value was " 
            + str(outputs[i]) + " but got " + str(function_output)+ " instead")

class RingMember:
    row_idx:int = 0
    col_idx:int = 0
    cw_next_member = None
    ccw_next_member = None 
    ring_member_after_r_cw_rotations = None

    def __init__(self,row_idx,col_idx):
        self.row_idx = row_idx
        self.col_idx = col_idx

    def get_coords(self):
        return [self.row_idx,self.col_idx]

class Ring:
    ring_id:int = 0
    min_row_idx:int = 0
    max_row_idx:int = 0
    min_col_idx:int = 0
    max_col_idx:int = 0
    num_members:int=0
    r=0

    last_processed_left_side_member = None
    last_processed_right_side_member = None

    #list of ring members, in order of appearence in the matrix
    ring_members = []
    #shows which member was processed last
    id_of_member_to_process:int = 0

    def get_coords_of_member_to_print(self, row_idx,col_idx):
        #this function keeps the previously printed member in memory to make all prints after the first one require only a single step
        member = self.ring_members[self.id_of_member_to_process]
        member_after_rotation = member
        #this is the first entry
        if(self.id_of_member_to_process==0):
            #keep going cw until the member to process is found
            for _ in range(self.r):
                member_after_rotation = member_after_rotation.cw_next_member
            self.last_processed_left_side_member = member
            self.last_processed_right_side_member = member
        #we are not dealing with the last row
        elif(row_idx != self.max_row_idx):
            #we are dealing with the leftmost column
            if(col_idx == self.min_col_idx):
                member_after_rotation = self.last_processed_left_side_member.ring_member_after_r_cw_rotations.ccw_next_member
                self.last_processed_left_side_member = member
            else:
                member_after_rotation = self.last_processed_right_side_member.ring_member_after_r_cw_rotations.cw_next_member
                self.last_processed_right_side_member = member
        #last row
        else:
            member_after_rotation = self.last_processed_left_side_member.ring_member_after_r_cw_rotations.ccw_next_member
            self.last_processed_left_side_member = member

        
        #cleanup and return
        self.id_of_member_to_process+=1
        member.ring_member_after_r_cw_rotations = member_after_rotation
        return member_after_rotation.get_coords()


    def __init__(self,num_rows,num_cols,ring_id,r):
        self.ring_id = ring_id
        self.min_row_idx = ring_id
        self.min_col_idx = ring_id
        self.max_row_idx = num_rows - ring_id -1
        self.max_col_idx = num_cols - ring_id -1
        #how many elements there are in this ring
        self.num_members = 2 *(self.max_col_idx - self.min_row_idx +1) + 2*(self.max_row_idx - self.min_col_idx +1) - 4
        #what is the amount of element position change in this ring after all the ccw rotations?
        self.r = r%self.num_members
        self.ring_members = []
        self.id_of_member_to_process = 0

        #populate ring members
        for row in range(self.min_row_idx,self.max_row_idx+1):
            #this is one of the middle rows of a ring, which only has two elements in it
            if (row not in [self.min_row_idx,self.max_row_idx]):
                #process the left side 
                #add ccw to previous and cw to current
                new_member = RingMember(row,self.min_col_idx)
                self.last_processed_left_side_member.ccw_next_member = new_member
                new_member.cw_next_member = self.last_processed_left_side_member

                self.last_processed_left_side_member = new_member
                self.ring_members.append(new_member)

                #process right side
                #CW to previous and ccw to current
                new_member = RingMember(row,self.max_col_idx)
                self.last_processed_right_side_member.cw_next_member = new_member
                new_member.ccw_next_member = self.last_processed_right_side_member

                self.last_processed_right_side_member = new_member
                self.ring_members.append(new_member)

            #this is the first row of the ring
            elif row == self.min_row_idx:
                #take care of the first element, make it the "last processed element" of the left and right sides
                new_member = RingMember(self.min_row_idx,self.min_col_idx)

                self.last_processed_right_side_member = new_member
                self.last_processed_left_side_member = new_member
                self.ring_members.append(new_member)
                for col in range(self.min_col_idx+1,self.max_col_idx+1):
                    new_member = RingMember(row,col)

                    new_member.ccw_next_member = self.last_processed_right_side_member
                    self.last_processed_right_side_member.cw_next_member = new_member

                    self.last_processed_right_side_member = new_member
                    self.ring_members.append(new_member)
 
            #this is the last row of the ring
            else:
                new_member = None
                #take care of all elements of the row
                for col in range(self.min_col_idx,self.max_col_idx+1):
                    new_member = RingMember(row,col)

                    new_member.cw_next_member = self.last_processed_left_side_member
                    self.last_processed_left_side_member.ccw_next_member = new_member

                    self.last_processed_left_side_member = new_member
                    self.ring_members.append(new_member)
                #take care of the last element's ccw shenanigans
                new_member.ccw_next_member = self.last_processed_right_side_member
                self.last_processed_right_side_member.cw_next_member = new_member

        #reset the last processed members
        self.last_processed_left_side_member = None
        self.last_processed_right_side_member = None

#TODO: gives ring_id 1 for coords [4,1] of a 5by4, should give 0 instead          
def find_ring_id(row_idx,col_idx,row_midway_idx,col_midway_idx,max_row_idx,max_col_idx,max_ring_id):
    row_idx = row_idx if row_idx<=row_midway_idx else max_row_idx - row_idx
    col_idx = col_idx if col_idx<=col_midway_idx else max_col_idx - col_idx
    return min(row_idx,col_idx,max_ring_id)

    

def function(input_):
    matrix=input_[0]
    r=input_[1]

    num_rows = len(matrix)
    max_row_idx = num_rows-1
    row_midway_idx = math.ceil(max_row_idx/2)
    num_cols = len(matrix[0])
    max_col_idx = num_cols-1
    col_midway_idx = math.ceil(max_col_idx/2)
    #rings are the # of circumferences of rotation. Find the # of rings required and create them
    num_rings = math.floor(min(num_rows,num_cols)/2)
    max_ring_id = num_rings - 1
    dict_rings = {}
    for i in range(num_rings):
        dict_rings[i] = Ring(num_rows,num_cols,i,r)

    result = []
    for row_idx in range(num_rows):
        row = []
        for col_idx in range(num_cols):
            ring_id = find_ring_id(row_idx,col_idx,row_midway_idx,col_midway_idx,max_row_idx,max_col_idx,max_ring_id)
            #get the element to print next
            [element_row,element_col] = dict_rings[ring_id].get_coords_of_member_to_print(row_idx,col_idx)
            row.append(matrix[element_row][element_col])
        result.append(row)
    return result
        


    

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)
    print("Done")
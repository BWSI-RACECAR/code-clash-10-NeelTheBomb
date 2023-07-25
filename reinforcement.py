class Solution:
    def create_action_dict(self, num_players, num_actions):
            #type num: two integer values
            #return type: int dictionary
            Dict = {}
            count = 0
            for i in range((num_players)):
                for j in range((num_actions)):
                    count = count + 1
                    tup = ()
                    for b in range(len(num_players)):
                        tup = tup + 0
                    tup[i] = j
                    print(tup)
                    Dict[count] = tup
            print(Dict)
            return Dict
                    
                         
            
            #TODO: Write code below to return a dictionary with the solution to the prompt.
            pass
    
def main():
    input1 = input()
    input1= int(input1)
    input2= input()
    input2=int (input2)
    tc1 = Solution()
    ans = tc1.create_action_dict(input1, input2)
    print(ans)

if __name__ == "__main__":
    main()

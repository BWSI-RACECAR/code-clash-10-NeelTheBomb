class Solution:
    def create_action_dict(self, num_players, num_actions):
            #type num: two integer values
            #return type: int dictionary
            Dict = {}
            for i in range(num_actions**num_actions):
                Dict[i] = [ ]
                for j in range(num_players):
                    Dict[i].append(i // (num_actions**j) %num_actions)
                Dict[i] = tuple(Dict[i])
                Dict[Dict[i]] = i
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

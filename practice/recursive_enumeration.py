def generate_permutations(items):
    def backtrack(current, remaining):
        # base case
        if not remaining: # used all elements
            print(current) # process result, add to result list or whatever
            return
        
        for i, item in enumerate(remaining):
            current.append(item) # make a choice

            # Explore further with that choice
            backtrack(current, remaining[:i] + remaining[i+1:])

            # Backtrack, undo choice
            current.pop()
    
    backtrack([], items)

generate_permutations([1, 2, 3, 4])
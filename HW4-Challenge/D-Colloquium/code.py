"""
Understanding the Problem:

We are given a sequence of scheduled talks, each categorized 
as 'T' (Theory), 'S' (System), or 'A' (AI).
The department wants to split these talks into two sections 
to maximize student attention.
Students' attention spans depend on the diversity of the last three talks in a section:
- 20 minutes if all three are from the same category.
- 40 minutes if two categories are present.
- 60 minutes if all three are from different categories.

The goal is to assign each talk to one of the two sections to maximize the total attention time.

How is Attention Time Calculated?
- For each talk, consider the current and the two preceding talks in its section.
- Count the number of unique categories among these talks.
- Assign attention time based on the count:
  - 1 unique category: 20 minutes
  - 2 unique categories: 40 minutes
  - 3 unique categories: 60 minutes

Key Observations:
- Talks must be assigned in order; we cannot rearrange them.
- Each talk can only be assigned to one section.
- The attention time for a talk depends on its section's recent history.

Plan of Attack:
1. Use dynamic programming to track the maximum attention time for different states.
2. Define a state by the last two 
    categories in each section: (sec1_old, sec1_new, sec2_old, sec2_new).
3. For each talk, iterate through all existing states 
    and consider assigning the talk to either section.
   - Update the section's history accordingly.
   - Calculate the attention time for the new state.
   - Keep the maximum attention time for each state.
4. After processing all talks, the maximum value among all states is the answer.

Why Use Dynamic Programming?
- To efficiently explore all possible assignments without redundant computations.
- To handle the large input size (up to 10^5 talks) within time constraints.

Time Complexity:
- At each step, we consider a manageable number of states due to the limited number of categories.
- Overall complexity is O(n), where n is the number of talks.

This approach ensures an optimal and scalable solution for large inputs.

References:
https://stackoverflow.com/questions/71539851/dynamic-programming-problem-maximize-the-sum-of-the-value-of-all-positions
"""



n = int(input())
s = input().strip()

chars = {'T': 1, 'S': 2, 'A': 3}
atten = {1: 20, 2: 40, 3: 60}


dp = {}
ini_state = (0, 0, 0, 0) 
dp[ini_state] = 0

for ch in s:
    c = chars[ch]
    new_dp = {}

    for (sec1_ol, sec1_ne, sec2_ol, sec2_ne), tot_atten in dp.items():
        
        
        # Assign to section 1 
        nh1_old, nh1_new = sec1_ne, c
        catgs = set()
        
        if sec1_ol: catgs.add(sec1_ol)
        if sec1_ne: catgs.add(sec1_ne)
        
        catgs.add(c)
        att = atten[len(catgs)]  

        hist1, hist2 = (nh1_old, nh1_new), (sec2_ol, sec2_ne)
        if hist1 <= hist2:
            state = (nh1_old, nh1_new, sec2_ol, sec2_ne)
        else:
            state = (sec2_ol, sec2_ne, nh1_old, nh1_new)

        new_total = tot_atten + att
        new_dp[state] = max(new_dp.get(state, 0), new_total)

        
        
        # Assign to section 2 
        nh2_old, nh2_new = sec2_ne, c
        catgs = set()
        
        
        
        if sec2_ol: catgs.add(sec2_ol)
        if sec2_ne: catgs.add(sec2_ne)
        
        
        
        catgs.add(c)
        att = atten[len(catgs)]  

        hist1, hist2 = (sec1_ol, sec1_ne), (nh2_old, nh2_new)
        if hist1 <= hist2:
            state = (sec1_ol, sec1_ne, nh2_old, nh2_new)
        else:
            state = (nh2_old, nh2_new, sec1_ol, sec1_ne)

        
        new_total = tot_atten + att
        new_dp[state] = max(new_dp.get(state, 0), new_total)

    dp = new_dp


print(max(dp.values()))

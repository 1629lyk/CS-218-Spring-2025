# E. Black Family Tree

**Time limit per test:** 1 second  
**Memory limit per test:** 256 megabytes

---

The tapestry looked immensely old; it was faded and looked as though Doxys had gnawed it in places. Nevertheless, the golden thread with which it was embroidered still glinted brightly enough to show them a sprawling family tree dating back (as far as Harry could tell) to the Middle Ages. Large words at the very top of the tapestry read:

> The Noble and Most Ancient House of Black  
> 'Toujours pur'

> 'You're not on here!' said Harry, after scanning the bottom of the tree.  
> 'I used to be there,' said Sirius, pointing at a small, round, charred hole in the tapestry, rather like a cigarette burn. 'My sweet old mother blasted me off after I ran away from home - Kreacher's quite fond of muttering the story under his breath.'  
> 'You ran away from home?'  
> 'When I was about sixteen,' said Sirius. 'I'd had enough.'

— *Rowling, J.K.. Harry Potter and the Order of Phoenix*

---

The Noble and Most Ancient House of Black was one of the largest, oldest, and wealthiest pure-blooded wizarding families in Great Britain. Many famous Wizards and Witches were from this family. Sirius Black, Harry Potter's godfather, was the last male member of the family. Both Ron's father and mother are relatives of the Black family.

The Black family tree was displayed in the drawing room of the family home at 12 Grimmauld Place in London, England, on an intricate tapestry, as an ornate mural. Very unfortunately, however, the family was very arrogant and placed great importance on blood purity, considering themselves akin to royalty in the wizarding world (some even became Voldemort's followers). A few members of the family disagreed with their family. Harry's godfather Sirius Black, for example, joined the Order of the Phoenix to fight against Voldemort. Because of this, his name was wiped out from the family tree (one of the black dots on the tree). A few other "traitors" were also wiped out.

Given the family tree of the Black family and the names of the traitors who have been wiped out from the tree, your task is to compute the maximum number of family members still connected with each other without any traitors.

---

## Input
- The first line contains two integers 𝑛 and 𝑚, which is the number of people in the family tree, and the number of traitors. All the family members are labeled from 0 to 𝑛−1.
- The next 𝑛−1 lines each contain one integer 𝑝𝑖, which is the parent of the 𝑖-th person in the family for 1 ≤ 𝑖 ≤ 𝑛−1. The root is always labeled with 0.
- The next 𝑚 lines each contain one integer 𝑡𝑖, which is a traitor that had been wiped out from the family tree.

## Output
- Output one integer: the maximum number of family members that are connected with each other.

---

## Examples

### Input
```
7 2
0
0
1
1
1
2
2
4
```

### Output
```
4
```

---

### Input
```
10 4
0
0
1
2
3
2
5
3
2
0
3
5
9
```

### Output
```
3
```

---

## Notes

- For 50% of the test data, 𝑛 ≤ 100.
- For 100% of the test data, 𝑛 ≤ 10^6.

---

## Example 1 Explained

- There are 7 people in the family tree and 2 traitors.
- The parent information builds the tree structure.
- Traitors are nodes 2 and 4.
- The largest number of connected members (excluding traitors and their descendants) is 4: members 0, 1, 3, and 5.

---

## An Unimportant Note:

The house of Black's, located at 12 Grimmauld Place, was offered by Sirius Black as the headquarter of the Order of Phoenix (an organization to fight against Voldemort). After Sirius Black died, he left the house for Harry Potter.
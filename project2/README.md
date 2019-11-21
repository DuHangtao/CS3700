# Project 2

### High Level Approach
- We started with reading the entire project description very carefully because it tells us what we should do in detail.
- We started the project based on the milestone, first read through the instructions, and then write helpers functions upon request. Then, change some part of the code based on the milestone. Then add simple revoke function.
- We implemented aggregation and disaggregation.
- But to finish the lv6 tests, we add some helper functions and global variables to pass the final tests.   
- We expanded the forwarding table to include the various attributes and implement the five rules for selecting a path.


### Challenges
- We needed to understand how router works very well before we started coding.
- We took a long time to design the structure of self.routes.
- When we implement the aggregation and disaggregation, we took a while to think about how to loop through the entire routes and check if they can be aggregated.

### Test:
- We used print statement to print the routes so that we can make sure routes table is updated or revoke correctly after update or revoke.
- We also used print statement to check the element when we have two for loops in the coalesce function.
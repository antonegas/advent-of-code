# advent-of-code
All my advent of code solutions for 2024

# Notes
- main.py for a given day is almost always my initial solution and main2.py is my attempt at making it more efficient.

# Fun Facts
- Day 6 it took one extra hour to solve part 2 because I placed an obstruction on the starting position. I'm guessing that I was unlucky with my input because I have seen solutions which don't account for this.
- Day 7 took about 30 minutes extra because I used ljust instead of rjust to pad my binary strings.
- Day 7's main2.py is about 210x faster than main.py, by determining which equations are not valid and terminating the search quicker.
- Day 10 part 1 took a long time because I read the description wrong and solved part 2 instead.
- Day 14's main2.py should be more general as some inputs didn't follow the logic of main.py
- Day 24 part 2 was solved manually at first using graphviz (online) and some helper functions. The automatic solution uses some assumptions about the input to fix the adder.
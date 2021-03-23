![Finantial Data](Resources/image.jpg)

# Changelog

## **03/22/2021**
- Started the analysis for the finantial data
- python script in [main.py](main.py)
- Determined total number of months and total amount of profit/losses
- Created the [pseudo-code](Resources/pseudo_average_profit.md) for changes in profit/losses and the average
- Implemented the script to calculate average profit/losses per month
- Bugs found:
    - [X] delta_profit list has 85 elements, should be 86
        - actually, 85 elements is correct
        - 87 rows of data - 1 header row - 1st month can't be calculated = 85 elements
- After further testing no bugs or logical errors found
- Implemented code that creates [results.txt](results.txt) and prints it out on the console



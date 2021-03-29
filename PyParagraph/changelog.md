![Paragraph Analysis](Resources/header.jpg)

# Changelog

## **03/24/2021**
- code in [main.py](main.py)
- added user input, error handler for non-existing files
- added word count, code works but tested against MS-Word word count and there is a disparity
    - The disparity is caused by "enhancer-promoter" MS-Word interprets it as 2 words, which shouldn't, code works fine
- added, tested and debugged:
    - sentence count
    - average letters by word
    - average words by sentence
- added format to the output

## **03/25/2021**
- added user input to keep analyzing paragraphs
- created results txt file
- changed print to terminal code to match the txt file
- added some user instructions
- testing stage finished, commented variables that skip user inputs
- analysis done on both paragraphs provided
    - [] paragraph_2 has blank lines need to adjust logic to avoid errors

## **03/29/2021**
- changed the regex to (?<=[.!?]) seems to work better, still an error with abbreviations

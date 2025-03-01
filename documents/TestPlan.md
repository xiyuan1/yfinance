# TEST PLAN
## Introduction
### Objective
The objective of this assignment is to improve our abilities of reading other people’s code. We also hope to learn new testing strategies and how to document them. 
Another objective is to get exposed to the Open Source projects and learn the process of how to contribute to them properly and in the best way possible. 

### Team Members
| Member Names        | Role   |
|:-------------------:|:------:|
| Anastasia Borissova | Tester |
| Khang Nguyen        | Tester |
| Xiyuan Shen         | Tester |
| Wilson Quon         | Tester |
| Qian Yu             | Tester |

### Research
**Issues:**
1. **No "calendar" attribute in yf.Ticker object #562.** It appears that the the .calendar attribute is not returning the next earnings event: AttributeError: 'Ticker' object has no attribute 'calendar' Tried a few different tickers, but it does not work with "MSFT", the example ticker

**PRs:**

We did not find any github PRs related to our assigned section of code.

### Problems found during the Research phase


### Planned Tests
1. check if the variable ‘cal’ gets an empty pandas DataFrame, in other words, check if the variable 'cal' is not receiving proper data.
2. check if the code properly handles when the variable ‘cal’ gets a pandas DataFrame that contains only NaNs.
3. check if cal[‘earningsDate’] is being properly converted to a readable datetime format using to_datetime().
4. check if self._calendar.index is being set properly by camel2title().

## Risks


## Test Approach
Read and understand the code assigned to us, and develop tests that address the functionality of the code block. No automation.

## Test Environment
A new server is required for the web server, the application and the database. 

## Test Deliverables
| Member Names        | Task                                           | Date/Milestone      |
|:-------------------:|:----------------------------------------------:|:-------------------:|
| Anastasia Borissova | Test 1 report sheet and software fixing for it | March 28, 2021      |
| Khang Nguyen        | Test 2 report sheet and software fixing for it | March 28, 2021      |
| Xiyuan Shen         | Test 3 report sheet and software fixing for it | March 28, 2021      |
| Wilson Quon         | Test 4 report sheet and software fixing for it | March 28, 2021      |
| Qian Yu             | Test 5 report sheet and software fixing for it | March 28, 2021      |

## Software Fixing

We did not find any github PRs that implements a solution to the problem identifies by our tests.

#### Quick Fix?
- Issue #1: Have a quick test that checks if dataframe is empty. If empty, pass. Otherwise, continue execution of the function
- Issue #2:
- Issue #3:
- Issue #4:

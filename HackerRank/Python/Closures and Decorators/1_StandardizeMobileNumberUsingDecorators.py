"""

Monday 25th April 2016

Hackerrank - Closures and Decorators - Standardize Mobile Number Using Decorators

Let's dive into decorators! You are given NN mobile numbers. Sort them in ascending order then print them in the standard format shown below:


+91 xxxxx xxxxx

The given mobile numbers may have +91+91, 9191 or 00 written before the actual 1010 digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer NN, the number of mobile phone numbers.
NN lines follow each containing a mobile number.

Output Format

Print NN mobile numbers on separate lines in the required format.


"""

n = int(input())
numbers = [input() for i in range(n)]

def sort_number_list(function):
    def list_wrap(inputlist):
        print (*sorted(function(inputlist)), sep = '\n')
    return (list_wrap)


@sort_number_list
def number_formatter(pn):
    return (['+91 ' + i[-10:-5] + ' ' + i[-5:] for i in pn])

number_formatter(numbers)






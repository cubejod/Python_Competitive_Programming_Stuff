'''
tips
don't waste all ur time on 1 problem even if u think u can do it
get easy problems first to not get penalty points
make sure your code resets variables to the right number, sometimes u need to reset to 1 instead of 0
if you have two loops nested in a loop, remove one and it'll still be O(n^2), u need to remove both
think about data structures and problem solving techniques that might apply to a problem
think about algorithms that might apply to a problem
draw problem out, you might find a solve or find that your solve doesn't work
'''

# reverse list in 1 line
a=[1,2,3,4]
a=a[::-1]
#a is now [4,3,2,1]

#sort based on non first element (this is based on 2nd)
a=[[1,9,9,9],[9,1,1,1]]
#change index of x if not second
a.sort(key = lambda x: x[1])
#prints [[9, 1, 1, 1], [1, 9, 9, 9]]

#bisect_left gives index of leftmost place that a number should be inserted in sorted list
#bisect_right gives rightmost index
import bisect
print(bisect.bisect_left([1,2,3,4,5,5,5,5,5,5], 5))  # 4
print(bisect.bisect_right([1,2,3,4,5,5,5,5,5,5], 5)) # 10

#eval evaluates expressions if you need to for some wack formatting problem
x = 5
print(eval('x * 3'))
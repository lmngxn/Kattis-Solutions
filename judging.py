n = int(input())
DOM_results = {}
for _ in range(n): #read the results from DOMjudge into a dictionary
    result = input()
    DOM_results[result] = DOM_results.get(result, 0) + 1
counter = 0
for _ in range(n): #check the results from Kattis to see how many match with DOMjudge
    check = input()
    if check in DOM_results:
        DOM_results[check] -= 1
        counter += 1
        if DOM_results[check] == 0: #delete record once 0 so will not appear in the first if statement
            del DOM_results[check]
print(counter)

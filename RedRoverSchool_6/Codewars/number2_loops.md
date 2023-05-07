1) Expected Behaviour

Function should return a dictionary/Object/Hash with "status" as a key, whose value can : "busy" or "available" depending on the truth value of the argument is_busy.

But as you will see after clicking RUN or ATTEMPT this code has several bugs, please fix them.

```
def get_status(is_busy):
    n = "busy" if is_busy elese "available"
    dict = {"status":n}
    return n
 ```
 ___________________________________________________________
 
2) - Each of the numbers in the array refers to the position of a letter in the string, in increasing order.

- Spaces are not places, you need the actual letters. No spaces.

- The returned word should be all lowercase letters.

- if you can't find one of the letters using the index numbers, return "No mission today"

 ```
def missing(nums, s):
    nums.sort()
    s = s.split()
    s = ''.join()
    output = ''
    for i in nums:
        if i >=len(s):
            retutn "No mission today"
        output +=s [i]
        
return output.lower()
    
 ```
 
 s = s.split (тут мы строку переделали в лист)
 
 s = ''.join() (тут мы лист обратно переделали в строку но без пробелов уже)
 
 
 ________________________________________
 
3)  Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta" --> "alpha beta gamma delta alpha beta gamma delta"

Words will be separated by a single space. There will be no leading or trailing spaces in the string. An empty string (0 words) is a valid input.
    
 ```
 def remove_consecutive_duplicates(s : str) -> str:
    s = s.split (" ")
    lst = [s[0]]
    for i in range(1, len(s)):
        if s [i] != lst[-1]:
            lst.append(s[i])
    return ' '.join(lst)
    
 ```
 
 ___________________________________________
 
 4. Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"

capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100. The input will be a lowercase string with no spaces and an array of digits.

```
def capitalize(s, ind):
    word = ''
    for i in range(len(s)):
        if i in ind:
            word += s[i].upper()
        else:
            word += s[i]
    return word
```



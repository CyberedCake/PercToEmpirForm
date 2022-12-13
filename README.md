# Percentage to Empirical Formula :books:
This program will automatically convert your percentages into an empirical formula.

It does not show you the work required because... that would be *cheating*, but it's a good way to check your work.

Also, feel free to fork it just don't claim yourself to be the original creator of it.

# Please also note
This program is old, as of August 18th, I will be updating it for the last time, just cleaning some things up and committing some unused files from the last school year. I'm not entirely proud of this project, but it is the first ever "big" thing I worked on in Python, so I guess it is going to be messy and hard-to-read, but oh well. If someone wants to attempt to make this any better, you can by forking it, and despite what it says above, you don't really have to give credit: just fork it on GitHub and you'll be good :thumbsup:.

# Requirements
This script requires elements.txt in the same directory as the python script. I might have found a better way to do this but we'll see, for now, just put it in the same directory.

Also, this project requires ['pyautogui'](https://github.com/asweigart/pyautogui).

# Pictures & More Information
## Empirical Formula
![image](https://user-images.githubusercontent.com/61170080/207385898-68195192-e9e6-4b8c-a885-f4229468d952.png)
<br>
Above is an image of the script being used. <strong>Please note! This script is not perfect, I have encountered some edge cases where the outputted number is not correct!</strong>
<br> <br>
In order to use the calculator, you must input your text in the following format:
<br>
`%element%=%grams%, %element 2%=%grams 2%`
<br>
<strong>Example:</strong> `carbon=62.02, hydrogen=10.43, oxygen=27.55`
<br> <br>
Sometimes, in my Chemistry class, we had to multiply numbers to get rid of the decimal places. Below is an example of that on paper:
<br>
![image](https://user-images.githubusercontent.com/61170080/207388223-e43b8cb1-dfff-494d-8b19-4f7aa7b086cb.png)
<br>
The calculator will automatically decide if it should try to multiply the numbers in order to remove the decimal. The same example from the paper in the calculator:
<br>
![image](https://user-images.githubusercontent.com/61170080/207388327-f334060e-9a10-429d-bfa8-e61fa1bb90ff.png)
<br>
The calculator will indicate whether the number has been multiplied by telling you below the Empirical formula.
<br>
Sometimes, the calculator can't (or doesn't know how to) multiply a number, which is where this message will sometimes come in.
<br>
![image](https://user-images.githubusercontent.com/61170080/207388544-d81788d9-09a2-43c8-90aa-326d1df7617e.png)
<br>
This number, in our Chemistry class, could be multiplied by `x3` to get closer to the real answer, and that would be acceptable; however, since computers are precise, it doesn't think it would work out, and thus doesn't multiply it.

## Empirical + Molecular Formula
![image](https://user-images.githubusercontent.com/61170080/207387385-392cf709-5da5-4c27-af7e-b7c54ed6ca8b.png)
<br>
If you wish to fine the molecular formula as well, you can add a `|%molecular mass%` to the end of your statement, for example:
<br>
`oxygen=60, sulfur=40, |240`
<br>
After using this, the output will tell you how the number was multiplied with a blue number with a 'x' in front of it (representing multiplication)

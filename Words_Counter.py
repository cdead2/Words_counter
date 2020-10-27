import huepy
def Counter(word):
    with open(word,'r') as file:
        file=str(file.read())
        file=file.strip()
        c=file.split(' ')
    if len(c) <=1:
        return f"The file(Letter) has  {len(c)} word "
    else:
        return f"The file(Letter) has  {len(c)} words"
print(huepy.green("""

1>Choose no 1 for word counter
2>choose no 2 for char counter 


"""))



def chcount(word):
    with open(word,'r') as file:
        file=str(file.read())
        file=file.strip()
        c=list(file)
        l=len(c)
        return f"The file (Letter) has {l} char "


ch=input("choose > ")
if ch =='1':
    print(huepy.yellow("="*40+" Word Counter "+"="*40))
    print(Counter(input(huepy.yellow(" input a file : "))))
    input("Press enter to exit")
elif ch =='2':
    print(huepy.yellow("="*40+" char Counter "+"="*40))
    print(chcount(input("Input a file : ")))
    input('Press enter to exit ')

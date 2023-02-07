def renswap(S):
    S = S.split()[::-1]
    L = []
    for i in S:
        L.append(i)
    L = " ".join(L)
    print(L.swapcase())
    return()

#inputed = input("Enter a Sentence: ")
#renswap(inputed)

from prac import student

student1 = student("Jim", "A.I.", "4.7", False)

print(student1.name)
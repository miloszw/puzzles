## mostly pen and paper

A = ['one','two','three','four','five','six','seven','eight','nine']
B = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
C = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def lettercount(List):
    return sum(map(len, List))

h = len('hundred')
a = len('and')

count = 900*(h+a) + 100*lettercount(A) + 10*(9*lettercount(A) + lettercount(B) + 10*lettercount(C)) - 9*a + len('onethousand')

print count

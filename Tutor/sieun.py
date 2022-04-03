def test(x, g):
    delta = 1e-5
    if(abs(x/g - g) < delta): return g
    else: return test(x, (g+x/g)/2)

print('2의 제곱근', test(2,1))
print('3의 제곱근', test(3,1))

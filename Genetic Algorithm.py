from random import randint,choices
MUT_PROB = .05
N = 8
S = 6

def init_pop(n,s=4):
    ans = [None]*n
    for i in range(n):
        ans[i] = ''.join([str(randint(0,1)) for i in range(s)])
    return ans

def fitness(sol):
    x = sum([int(sol[len(sol)-1-i])*(2**i) for i in range(len(sol))])
    return 15*x-x*x

def fit_ratio(pop):
    fits = list(map(fitness,pop))
    tot = sum(fits)
    return [(pop[i],fits[i],fits[i]/tot*100) for i in range(len(pop))]

def crossover(father,mother):
    return [father[:2]+mother[2:],mother[:2]+father[2:]]

def mutate(gen):
    global MUT_PROB
    sz = len(gen[0])
    bits = list(''.join(gen))
    lim = int(1/MUT_PROB)
    for i in range(len(bits)):
        if randint(0,lim)==0:
            bits[i] = str(1-int(bits[i]))

    newgen = []
    for i in range(len(gen)):
        newgen.append(''.join(bits[i*sz:(i+1)*sz]))
    return newgen

def iterate(pop,n):
    for i in range(n):
        fr = fit_ratio(pop)
        print(max([s[1] for s in fr]))
        w = [s[1] for s in fr]
        parents = choices(pop,weights=w,k=len(pop))
        new_gen = []
        for i in range(len(pop)//2):
            new_gen += crossover(parents[2*i],parents[2*i+1]) 
        pop = mutate(new_gen)
    return pop

pop = init_pop(N)
print(pop)
ans = iterate(pop,30)

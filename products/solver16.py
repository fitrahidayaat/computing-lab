import json
from django.template import loader
from django.http import HttpResponse
import pycosat

from pprint import pprint
solusi = []
jumSol = 0
petunjuk = 0

n = 4
n1 = 17
n2 = 16
def v(i, j, d):
    return 16*16 * (i - 1) + 16 * (j - 1) + d

def sudoku_clauses():
    global n1
    res = []

    #Setidaknya ada satu angka di setiap entri:
    for r in range(1, n1):
        for c in range(1, n1):
            l=[]
            for d in range(1, n1):
                l.append(v(r,c,d))
            res.append(l)

    #Setiap angka muncul paling banyak satu kali di setiap baris:
    for c in range(1, n1):
        for d in range(1, n1):
            for r in range(1, n2):
                for i in range(r+1,n1):
                    res.append([-v(r, c, d), -v(i, c, d)])

    #Setiap angka muncul paling banyak satu kali di setiap kolom:
    for r in range(1, n1):
        for d in range(1, n1):
            for c in range(1, n2):
                for i in range(c+1,n1):
                    res.append([-v(r, c, d), -v(r, i, d)])

    #Setiap angka muncul paling banyak sekali dalam setiap sub-grid sqrt(n)xsqrt(n):
    for d in range(1, n1):
        for i in range(n):
            for j in range(n):
                for c in range(1, n+1):
                    for r in range(1, n):
                        for k in range(r + 1, n+1):
                            for l in range(1,n+1):
                                res.append([-v((n*i+r), (n*j+c), d), -v((n*i+k), (n*j+l), d)])
    return res

def ShowBoard(s):
   global solusi
   solusi.append([])
   for x in range(0,n2):
        solusi[jumSol-1].append([])
        for y in range(0,n2):
            solusi[jumSol-1][x].append(s[x][y])

def solve2(sudoku):
    clauses = sudoku_clauses()
    global petunjuk
    petunjukC = 0
    for i in range(1, n1):
        for j in range(1, n1):
            d = sudoku[i - 1][j - 1]
            # untuk setiap given.
            if d:
                petunjukC+=1
                petunjuk=petunjukC
                clauses.append([v(i, j, d)])

    def read_cell(i, j):
        # mengembalikan i,j
        for d in range(1, n1):
            if v(i, j, d) in sol:
                return d
    # memulai SAT solver
    #print(len(clauses))
    #pprint(clauses)
    sol = set(pycosat.solve(clauses))
    #print(sol)
    checker = len(sol)
    counter = 0
    global solusi
    global jumSol
    temp = []
    for i in range(n2):
        temp.append([])
        for j in range(n2):
            temp[i].append(0)
    tempSol = temp
    if checker == 5:
        #print('Sudoku tidak memiliki solusi')
        jumSol=counter
        return False
    while (checker != 5):
        if(counter==10):
           break
        counter+=1
        jumSol=counter
        #print(counter)
        #print(sol)
        #sol = pycosat.solve(cnf)

        for i in range(1, n1):
            for j in range(1, n1):
                tempSol[i - 1][j - 1] = read_cell(i, j)
        #print(tempSol)
        #print('Answer: '+str(counter))
        #print(numclause)
        #print()
        ShowBoard(tempSol)
        #solusi[].append(tempSol)
        tempSol=temp
        clauses.append([-x for x in sol])
        sol = set(pycosat.solve(clauses))
        checker=len(sol)
    return True

def solve(grid16):
    clauses = sudoku_clauses()
    for i in range(1,n1):
        for j in range(1, n1):
            d = grid16[i - 1][j - 1]
            if d:
                clauses.append([v(i, j, d)])

    # solve SAT problem
    sol = set(pycosat.solve(clauses))
    if (len(sol)==5):
        return False
    def read_cell(i, j):
        # return solution
        for d in range(1, n1):
            if v(i, j, d) in sol:
                return d

    for i in range(1, n1):
        for j in range(1, n1):
            grid16[i - 1][j - 1] = read_cell(i, j)
    #print(grid16)
    return True

def readAPuzzle(lst):
    grid=[]
    for i in range(16):
        grid.append(lst[16*i:16*(i+1)])

    return grid

def hasil(request):
    global valid
    valid = True

    #Get input
    get_lst16 = request.GET.getlist("grid")
    lst2 = []

    for x in get_lst16:
        if (x == ''):
            x = int(0)
            lst2.append(x)
        elif(x.isalpha() == True):
            valid = False
            lst2.append(x)
        elif(x.isdigit()== True):
            if(int(x) > 16):
                valid = False
                lst2.append(x)
            elif(int(x) > 0):
                x = int(x)
                lst2.append(x)
            else:
                valid = False
                lst2.append(x)
        else:
            valid = False
            lst2.append(x)

    grid_orig16 = readAPuzzle(lst2)
    #grid yang akan diproses
    grid16 = grid_orig16

    #output
    global solusi
    solusi = []
    out16 = ""
    add = ""
    
    if(valid == False):
        out16 = "Input Not Valid"
        valid = True
    elif solve2(grid_orig16):
        if(grid_orig16 == solusi[0]):
            add = "Sudoku Yang Dikerjakan Benar"
        grid16 = solusi
        out16 = "Solusi Sudoku:"
        valid = True
    elif(petunjuk == 16**2):
        out16 = "Sudoku Yang Dikerjakan Salah"
        valid = True
    else:
        out16 = "Sudoku tidak memiliki solusi!"
        valid = True

    ctx = {
        'grid_orig16': json.dumps(grid_orig16),
        'grid16': json.dumps(grid16),
        'out16': out16,
        'add': add,
        'jumSol': json.dumps(jumSol)
    }
    content = loader.render_to_string('products/answer16.html', ctx)
    return HttpResponse(content)
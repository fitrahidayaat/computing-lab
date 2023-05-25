import json
from django.template import loader
from django.http import HttpResponse
from pprint import pprint
import pycosat

solusi = []
jumSol = 0
petunjuk = 0
valid = True

n = 2
n1 = 5
n2 = 4

def v(i, j, d):
    return 4*4 * (i - 1) + 4 * (j - 1) + d

def sudoku_clauses():
    global n1
    res = []

    #Setidaknya ada satu angka di setiap entri:
    for r in range(1, n1):
        for c in range(1, n1):
            l = []
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
                clauses.append([v(i, j, d)])
                petunjukC+=1
                petunjuk=petunjukC

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

    global solusi
    global jumSol
    counter = 0
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
        if(counter == 100):
           break
        counter += 1
        jumSol = counter
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
        tempSol = temp
        clauses.append([-x for x in sol])
        sol = set(pycosat.solve(clauses))
        checker=len(sol)
    return True

def solve(grid4):
    clauses = sudoku_clauses()
    for i in range(1,n1):
        for j in range(1, n1):
            d = grid4[i - 1][j - 1]
            if d:
                clauses.append([v(i, j, d)])

    # solve SAT problem
    sol = set(pycosat.solve(clauses))
    if (len(sol) == 5):
        return False
    def read_cell(i, j):
        # return solution
        for d in range(1, n1):
            if v(i, j, d) in sol:
                return d

    for i in range(1, n1):
        for j in range(1, n1):
            grid4[i - 1][j - 1] = read_cell(i, j)
    #print(grid4)
    return True

def readAPuzzle(lst):
    grid = []
    for i in range(4):
        grid.append(lst[4*i:4*(i+1)])

    return grid

def jawaban(request):
    global valid
    valid = True

    #Get input
    get_lst4 = request.GET.getlist("grid")
    lst2 = []

    for x in get_lst4:
        if (x == ''):
            x = int(0)
            lst2.append(x)
        elif(x.isalpha() == True):
            valid = False
            lst2.append(x)
        elif(x.isdigit()== True):
            if(int(x) > 4):
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

    grid_orig4 = readAPuzzle(lst2)
    #grid yang akan diproses
    grid4 = grid_orig4

    #output
    global solusi
    solusi = []
    out4 = ""
    add = ""

    if(valid == False):
        out4 = "Input Not Valid"
        valid = True
    elif solve2(grid_orig4):
        if(grid_orig4 == solusi[0]):
            add = "Sudoku Yang Dikerjakan Benar"
        grid4 = solusi
        out4 = "Solusi Sudoku:"
        valid = True
    elif(petunjuk == 4**2):
        out4 = "Sudoku Yang Dikerjakan Salah"
        valid = True
    else:
        out4 = "Sudoku tidak memiliki solusi!"
        valid = True

    ctx = {
        'grid_orig4': json.dumps(grid_orig4),
        'grid4': json.dumps(grid4),
        'out4': out4,
        'add': add,
        'jumSol': json.dumps(jumSol)
    }
    content = loader.render_to_string('products/answer4.html', ctx)
    return HttpResponse(content)

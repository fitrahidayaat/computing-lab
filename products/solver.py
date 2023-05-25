import json
from django.template import loader
from django.http import HttpResponse
from pprint import pprint
import pycosat

solusi = []
jumSol = 0
petunjuk = 0

n = 3
n1 = 10
n2 = 9

def v(i, j, d):
    return 81 * (i - 1) + 9 * (j - 1) + d

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
                petunjukC += 1
                petunjuk = petunjukC
                clauses.append([v(i, j, d)])

    def read_cell(i, j):
        # mengembalikan i,j
        for d in range(1, n1):
            if v(i, j, d) in sol:
                return d
    # memulai SAT solver
    sol = set(pycosat.solve(clauses))
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
        jumSol = counter
        return False
    while (checker != 5):
        if(counter == 100):
           break
        counter += 1
        jumSol = counter

        for i in range(1, n1):
            for j in range(1, n1):
                tempSol[i - 1][j - 1] = read_cell(i, j)

        ShowBoard(tempSol)
        #solusi[].append(tempSol)
        tempSol = temp
        clauses.append([-x for x in sol])
        sol = set(pycosat.solve(clauses))
        checker = len(sol)
    return True

def solve(grid):
    clauses = sudoku_clauses()
    for i in range(1, 10):
        for j in range(1, 10):
            d = grid[i - 1][j - 1]
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
            grid[i - 1][j - 1] = read_cell(i, j)
    return True

def readAPuzzle(lst):
    grid = []
    for i in range(9):
        grid.append(lst[9*i:9*(i+1)])
    return grid

def answer(request):
    global valid
    valid = True
    #Get input
    get_lst = request.GET.getlist("grid")
    lst2 = []

    for x in get_lst:
        if (x == ''):
            x = int(0)
            lst2.append(x)
        elif(x.isalpha() == True):
            valid = False
            lst2.append(x)
        elif(x.isdigit()== True):
            if(int(x) > 9):
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

    grid_orig = readAPuzzle(lst2)
    #grid yang akan diproses
    grid = grid_orig
    
    #output
    global solusi
    solusi = []
    out = ""
    add = ""

    if (valid == False):
        out = "Input Not Valid"
        valid = True
    elif solve2(grid_orig):
        if(grid_orig == solusi[0]):
            add = "Sudoku Yang Dikerjakan Benar"
        grid = solusi
        out = "Solusi Sudoku:"
        valid = True
    elif(petunjuk == 9**2):
        out = "Sudoku Yang Dikerjakan Salah"
        valid = True
    else:
        out = "Sudoku tidak memiliki solusi!"
        valid = True

    ctx = {
        'grid_orig': json.dumps(grid_orig),
        'grid': json.dumps(grid),
        'out': out,
        'add': add,
        'jumSol': json.dumps(jumSol)
    }
    content = loader.render_to_string('products/answer.html', ctx)
    return HttpResponse(content)

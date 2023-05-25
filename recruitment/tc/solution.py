n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = arr[-1]
for i in range(n - 1):
  ans = min(ans, abs(arr[i] - arr[i + 1]))
print(ans)
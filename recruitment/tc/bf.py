n = int(input())
arr = list(map(int, input().split()))

ans = 10**9
for i in range(n):
  for j in range(i + 1, n):
    ans = min(ans, abs(arr[i] - arr[j]))

print(ans)
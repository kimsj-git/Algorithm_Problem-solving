papers = [1, 3]
def papers_dp(n):
    for i in range(2, n+1):
        papers.append(papers[i-1] + papers[i-2] * 2)
    return papers[n-1]


N = int(input())
result = papers_dp(N)
print(result % 10007)
def evaluateExp(exp: str) -> int:
    MOD = 1000000007
    n = len(exp)
    dp = [[[-1] * 2 for _ in range(n)] for _ in range(n)]

    def dfs(i, j, isTrue):
        if i>j: return 0
        if i==j:
            if isTrue: return 1 if exp[i] == 'T' else 0
            else: return 1 if exp[i] == 'F' else 0
        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]
        ways = 0
        for k in range(i+1,j,2):
            LT = dfs(i,k-1,1)
            RT = dfs(k+1,j,1)
            LF = dfs(i,k-1,0)
            RF = dfs(k+1,j,0)
            if isTrue:
                if exp[k] == '&':
                    ways = (ways + (LT * RT) % MOD) % MOD
                elif exp[k] == '|':
                    ways = (ways + ((LT * RT) % MOD + (LF * RT) % MOD + (RF * LT) % MOD) % MOD) % MOD
                elif exp[k] == '^':
                    ways = (ways + ((LT * RF) % MOD + (RT * LF) % MOD) % MOD) % MOD
            else:
                if exp[k] == '&':
                    ways = (ways + ((LF * RF) % MOD + (LF * RT) % MOD + (RF * LT) % MOD) % MOD) % MOD
                elif exp[k] == '|':
                    ways = (ways + (LF * RF) % MOD) % MOD
                elif exp[k] == '^':
                    ways = (ways + ((LF * RF) % MOD + (RT * LT) % MOD) % MOD) % MOD

        dp[i][j][isTrue] = ways
        return ways
    return dfs(0,n-1,1)
            


# Tabulation
def evaluateExp(exp: str) -> int:
    MOD = 1000000007
    n = len(exp)
    dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            for isTrue in [0,1]:
                if i==j:
                    if isTrue:
                        dp[i][j][isTrue] = 1 if exp[i] == 'T' else 0
                    else:
                        dp[i][j][isTrue] = 1 if exp[i] == 'F' else 0
                    continue
                ways = 0
                for k in range(i+1, j, 2):
                    LT = dp[i][k-1][1]
                    RT = dp[k+1][j][1]
                    LF = dp[i][k-1][0]
                    RF = dp[k+1][j][0]
                    if isTrue:
                        if exp[k] == '&':
                            ways = (ways + (LT * RT) % MOD) % MOD
                        elif exp[k] == '|':
                            ways = (ways + ((LT * RT) % MOD + (LF * RT) % MOD + (RF * LT) % MOD) % MOD) % MOD
                        elif exp[k] == '^':
                            ways = (ways + ((LT * RF) % MOD + (RT * LF) % MOD) % MOD) % MOD
                    else:
                        if exp[k] == '&':
                            ways = (ways + ((LF * RF) % MOD + (LF * RT) % MOD + (RF * LT) % MOD) % MOD) % MOD
                        elif exp[k] == '|':
                            ways = (ways + (LF * RF) % MOD) % MOD
                        elif exp[k] == '^':
                            ways = (ways + ((LF * RF) % MOD + (RT * LT) % MOD) % MOD) % MOD

                dp[i][j][isTrue] = ways

    return dp[0][n-1][1]

def solve_with_backtracking(n):
    def is_safe(board, row, col):
        # Check current row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        
        # Check upper diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check lower diagonal
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        
        return True

    def backtrack(col):
        if col == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'  # Backtrack

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

def solve_with_branch_and_bound(n):
    def backtrack(col, used_rows, used_diag1, used_diag2):
        if col == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            d1 = row - col  # Diagonal 1 (top-left to bottom-right)
            d2 = row + col  # Diagonal 2 (top-right to bottom-left)
            
            # Branch and Bound: Skip invalid positions
            if not used_rows[row] and not used_diag1[d1] and not used_diag2[d2]:
                board[row][col] = 'Q'
                used_rows[row] = True
                used_diag1[d1] = True
                used_diag2[d2] = True
                
                backtrack(col + 1, used_rows, used_diag1, used_diag2)
                
                # Backtrack
                board[row][col] = '.'
                used_rows[row] = False
                used_diag1[d1] = False
                used_diag2[d2] = False

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    used_rows = [False] * n
    used_diag1 = [False] * (2 * n - 1)
    used_diag2 = [False] * (2 * n - 1)
    
    backtrack(0, used_rows, used_diag1, used_diag2)
    return solutions

def print_solutions(solutions, n, method):
    print(f"\n{method} - Found {len(solutions)} solutions for {n}-Queens:")
    for i, solution in enumerate(solutions[:2], 1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    n = 8
    
    # Solve with pure backtracking
    backtracking_solutions = solve_with_backtracking(n)
    print_solutions(backtracking_solutions, n, "Backtracking")
    
    # Solve with branch and bound
    bb_solutions = solve_with_branch_and_bound(n)
    print_solutions(bb_solutions, n, "Branch and Bound")
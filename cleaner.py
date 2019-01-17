

def cleaner(arr, r, c):
    nowR = 0
    nowC = 0
    max_seq = r*c
    #1 east, 2 south, 3 west, 4 north
    direction = 1
    clean_seq = 1

    for seq in range(1, max_seq+1):
        if direction == 1:
            for col in range(c):
                if arr[nowR][col] != 0:
                    continue
                if col+1 == c or arr[nowR][col+1] != 0:
                    direction =2
                arr[nowR][col] = clean_seq
                clean_seq +=1
                nowC = col

        if direction == 2:
            for row in range(r):
                if arr[row][nowC] != 0:
                    continue
                if row+1 == r or arr[row+1][nowC] != 0:
                    direction =3

                arr[row][nowC] = clean_seq
                clean_seq +=1
                nowR=row
        if direction == 3:
            for col in reversed(range(c)):
                if arr[nowR][col] != 0:
                    continue
                if col-1 == 0 or arr[nowR][col-1] != 0:
                    direction =4
                arr[nowR][col] = clean_seq
                clean_seq +=1
                nowC=col

        if direction == 4:
            for row in reversed(range(r)):
                if arr[row][nowC] != 0:
                    continue
                if row-1 == 0 or arr[row-1][nowC] != 0:
                    direction =1
                arr[row][nowC] = clean_seq
                clean_seq +=1
                nowR=row

    print(arr)
if __name__ == '__main__':
    cleaner([[0,0,0],[0,0,0],[0,0,0], [0,0,0]], 4, 3)
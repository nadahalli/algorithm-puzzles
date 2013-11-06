def num_handshakes(n):
    if n == 0:
        return 1
    sum = 0
    for i in range(n/2):
        left_points = i * 2
        left = num_handshakes(left_points)
        right_points = n - 2 - left_points
        right = num_handshakes(right_points)
        print left, right
        sum += left * right
    return sum

print num_handshakes(10)

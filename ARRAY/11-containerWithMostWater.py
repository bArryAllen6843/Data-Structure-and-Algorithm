def maxArea(height) -> int:
    max_water = 0
    n = len(height)
    l, h = 0, n - 1

    while l < h:
        hl, hh = height[l], height[h]
        curr_water = min(hl, hh) * (h - l)

        if curr_water > max_water:
            max_water = curr_water
        if hl <= hh:
            l += 1
        if hh <= hl:
            h -= 1
    return max_water


a = [7, 4, 0, 9]
print(maxArea(a))

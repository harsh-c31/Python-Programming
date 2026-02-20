def max_stamina(heights):
    n=len(heights)
    max_xor=0
    for i in range(n):
        curr=heights[i]
        for j in range(i+1,n):
            if heights[j]>heights[j-1]:
                curr=curr^heights[j]
            else:
                break
        max_xor=max(max_xor,curr)
    return max_xor
n = int(input())
heights = list(map(int, input().split()))

print(max_stamina(heights))
            
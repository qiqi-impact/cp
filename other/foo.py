def closest_left_larger(arr):
    ret = [None] * len(arr)

    st = []
    for i in range(len(arr)-1, -1, -1):
        while st and arr[i] > arr[st[-1]]:
            cur = st.pop()
            ret[cur] = i
        st.append(i)
    return ret

print(closest_left_larger([4,3,1,2,4,8,6,7]))

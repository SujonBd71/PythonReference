# Deque is double ended linked list push and pop on both side as O(1)


from collections import deque

st = deque()
st.append("d")
st.append("e")
st.appendleft("a")
st.insert(2, "X")

print(st)

st.insert(0, "#")
print(st)

def basic_test():
    st = set()
    st.add(12)
    st.add(13)
    st.add(34)

    #this is dublicate and will be igonred
    st.add(13)

    print(st)

    st.discard(12)
    print(st)

    


basic_test()

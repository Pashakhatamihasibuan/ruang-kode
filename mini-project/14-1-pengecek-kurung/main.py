def seimbang(s):
    st = []
    for c in s:
        if c in "([{":
            st.append(c)
        elif c in ")]}":
            if not st:
                return False
            buka = st.pop()
            if "([{".index(buka) != ")]}".index(c):
                return False
    return not st

for s in ["(a[b]{c})", "(]", "((x)"]:
    print(s, "->", seimbang(s))

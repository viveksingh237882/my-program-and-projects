def div(a,b):
    print(a/b)

    def samrt (fun):
        def inner(a,b):
            if a<b:
                a,b=b,a
            return(fun)
        return(inner)
    div=samrt(div)
    div(2,4  )
    print(div)
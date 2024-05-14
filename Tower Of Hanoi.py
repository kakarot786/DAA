def towerOfHanoi(n,source,auxiliary,target):
    if n == 1:
        print("Move disk 1 from Source", source, "to Target", target)
        return
    else:
        towerOfHanoi(n-1,source,target,auxiliary)
        print("Move disk", n, "from Source", source, "to Auxiliary", auxiliary)
        towerOfHanoi(n-1,auxiliary,source,target)


towerOfHanoi(4,"A", "B", "C")

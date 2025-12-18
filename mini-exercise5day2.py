def md_bullets(items:list[str])-> list[str]:
    """turn ['a','b'] into ['- a','- b']"""
    newlist=[]
    for i in items:
        newlist.append("- "+i)
    return newlist
print(md_bullets(["s",'fds']))
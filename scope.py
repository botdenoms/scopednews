import sys

def listScopes():
    ''' List scope text present in the scopes file'''
    with open('scope.txt', 'r') as f:
        lns = f.readlines()
        if len(lns) == 0:
            print('scope list is empty \nRun scope -a|A "scope text ..."')
        for ln in lns:
            print(ln.strip())

def allScopes():
    ''' retuns a List of all scopes present in the scopes file'''
    with open('scope.txt', 'r') as f:
        lns = f.readlines()
        if len(lns) == 0:
            return []
        else:
            return [s.strip() for s in lns]

def addScope(list=[], append=True):
    ''' add a scope item(s) into the scope list'''
    if len(list) > 0:
        if append:
            with open('scope.txt', 'a') as f:
                for sr in list:
                    f.write(sr + '\n')
                    if len(sr) > 7:
                        print('Added : ', sr[:10], '...')
                    else:
                        print('Added : ', sr)
                print(len(list),  "scopes added")
        else:
            with open('scope.txt', 'w') as f:
                for sr in list:
                    f.write(sr + '\n')
    else:
        print('Scope list is empty \nRun scope -a|A "scope text ..."')
    pass

def removeScopes(items=[]):
    ''' Remove scope item(s) from the scopes list'''
    if len(items) == 0:
        with open('scope.txt', 'w') as f:
                f.write('')
        print('Removed all items form the scopes list')
    else:
        srcs = allScopes()
        if len(srcs) == 0:
            print('scope list is empty \nRun scope -a|A "scope text ..."')
            return
        for src in items:
            try:
                i = srcs.index(src)
                srcs.pop(i)
                if len(src) > 7:
                        print(src[:10], ": Removed")
                else:
                    print(src, ": Removed")
            except:
                if len(src) > 7:
                        print(src[:10], ": is NOT in the list")
                else:
                    print(src, ": is NOT in the list")
        addScope(srcs, False)

def cleanScopes():
    ''' Remove duplicate scopes item(s) from the scopes list'''
    srcs = allScopes()
    if len(srcs) == 0:
        print('scope list is empty \nRun scope -a|A "scope text ..."')
    else:
        srcnw = set(srcs)
        addScope(srcnw, False)

def main():
    args = sys.argv[1:]

    if len(args) > 0:
        try:
            if args[0].lower() == '-a':
                #  add new source(s)
                addScope(args[1:])
            if args[0].lower() == '-d':
                # remove source(s) from the list
                if args[1].lower() == '-all':
                    removeScopes([])
                else:
                    removeScopes(args[1:])
            if args[0].lower() == '-clean' or args[0].lower() == '-c':
                #  clean the sources list removing duplicates
                cleanScopes()
        except Exception as e:
            print("Error: ", e.args)
            print("Use the flag -a or -A followed by the scope text in quotes")
            print('scope -a|A " scope text here "')
    else:
        listScopes()

if __name__ == '__main__':
    main()

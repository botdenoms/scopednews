import sys

def listSources():
    ''' List sources present in the sources file'''
    with open('sources.txt', 'r') as f:
        lns = f.readlines()
        if len(lns) == 0:
            print('Sources list is empty \nRun sources -a|A source.com source1.com ...')
        for ln in lns:
            print(ln.strip())

def allSources():
    ''' retuns a List of sources present in the sources file'''
    with open('sources.txt', 'r') as f:
        lns = f.readlines()
        if len(lns) == 0:
            return []
        else:
            return [s.strip() for s in lns]

def addSources(list=[], append=True):
    ''' add a source item(s) into the sources list'''
    if len(list) > 0:
        if append:
            with open('sources.txt', 'a') as f:
                for sr in list:
                    f.write(sr + '\n')
                    print('Added : ', sr)
                print(len(list),  "sources added")
        else:
            with open('sources.txt', 'w') as f:
                for sr in list:
                    f.write(sr + '\n')
    else:
        print('Sources list is empty \nRun sources -a|A source.com source1.com ...')
    pass

def removeSources(items=[]):
    ''' Remove source item(s) from the sources list'''
    if len(items) == 0:
        with open('sources.txt', 'w') as f:
                f.write('')
        print('Removed all items form the sources list')
    else:
        srcs = allSources()
        if len(srcs) == 0:
            print('Sources list is empty \nRun sources -a|A source.com source1.com ...')
            return
        for src in items:
            try:
                i = srcs.index(src)
                srcs.pop(i)
                print(src, ": Removed")
            except:
                print(src, ": is NOT in the list")
        addSources(srcs, False)

def cleanSources():
    ''' Remove duplicate & not working source item(s) from the sources list'''
    srcs = allSources()
    if len(srcs) == 0:
        print('Sources list is empty \nRun sources -a|A source.com source1.com ...')
    else:
        srcnw = set(srcs)
        addSources(srcnw, False)

def main():
    args = sys.argv[1:]

    if len(args) > 0:
        try:
            if args[0].lower() == '-a':
                #  add new source(s)
                addSources(args[1:])
            if args[0].lower() == '-d':
                # remove source(s) from the list
                if args[1].lower() == '-all':
                    removeSources([])
                else:
                    removeSources(args[1:])
            if args[0].lower() == '-clean' or args[0].lower() == '-c':
                #  clean the sources list removing duplicates
                cleanSources()
        except Exception as e:
            print("Error: ", e.args)
            print("Use the flag -a or -A followed by the urls separated by space")
    else:
        listSources()

if __name__ == '__main__':
    main()

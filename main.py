import scope as sc
import sources as src
import scraper as scr


# load the scope key words --> [" "]
scopes = sc.allScopes()
print(len(scopes), 'scopes found')
# load the sources in the sources list --> [" "]
sources = src.allSources()
print(len(sources), 'sources found')

# found <-- 0
found = 0
hits = []
# hits_set = set()

# for each source in sources:
for source in sources:
    # fetch source --> [(text, url)...]
    print(source)
    resp = scr.fetchSource(source)
    if resp == None:
        print("Error in fetching source:", source)
        continue
    highlights = scr.sourceLinkMiner(resp)

    # for (text, url) in [(text, url)...]
    for hlt in highlights:
        # if text == None:
        if hlt[0] == None:
            # for scope n scopes:
            for scope in scopes:
                # if scope in url: --> true
                if scope.lower() in hlt[1].lower():
                    # dump (None, url) to bd
                    hits.append((hlt[0], hlt[1], source))
                    # hits_set.add((hlt[0], hlt[1], source))
                    # found ++
                    found += 1
                    # break
                    break
        # else:
        else:
            # for scope n scopes:
            for scope in scopes:
                # if scope in text: --> true
                if scope.lower() in hlt[0].lower():
                    # dump (None, url) to bd
                    hits.append((hlt[0], hlt[1], source))
                    # hits_set.add((hlt[0], hlt[1], source))
                    # found ++
                    found += 1
                    # break
                    break
                # else:
                else:
                    # if scope in url: --> true
                    if scope.lower() in hlt[1].lower():
                        # dump (None, url) to bd
                        hits.append((hlt[0], hlt[1], source))
                        # hits_set.add((hlt[0], hlt[1], source))
                        # found ++
                        found += 1
                        break
                        # break
#  print found
print('Found:', found, 'Succesful hits')

# print('Found:', len(hits_set), 'Unique hits')

# print('List:', len(hits), 'Set:', len(hits_set))

# for i, hit in enumerate(hits_set):
#     print(str(i).rjust(3, ' '), "Title: ", hit[0])
#     print(''.rjust(3, ' '),"url: ", hit[1])
#     print(''.rjust(3, ' '),"Source: ", hit[2])

for i, hit in enumerate(hits):
    print(str(i).rjust(3, ' '), "Title: ", hit[0])
    print(''.rjust(3, ' '),"url: ", hit[1])
    print(''.rjust(3, ' '),"Source: ", hit[2])

# write the hits to the output file or db

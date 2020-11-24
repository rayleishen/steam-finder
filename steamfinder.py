import urllib.request
count = 0
line_count = 0


datafile = (open("data.txt", "r"))
megalist = datafile.read()
words = megalist.split()

print ("UNUSED STEAM URLS")
print ("-----------------")
print
print

for i in words:
    count += 1

    if len(i) >= 3:
        
        page = urllib.request.urlopen("https://steamcommunity.com/id/" + i)
        
        line_count = 0
        for line in page:
            if line != "\n":
                line_count += 1

        if line_count == 334:
            print (i)

print ("-----------------")
print ("Datafile finished")



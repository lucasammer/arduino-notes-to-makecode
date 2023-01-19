import os

def progress(prog):                       # The simplest progress bar ever
    print(flush=True)
    if(prog>0.99):
        print("[====================]")
    elif(prog>=0.90):
        print("[==================..]")
    elif(prog>=0.80):
        print("[================....]")
    elif(prog>=0.70):
        print("[==============......]")
    elif(prog>=0.60):
        print("[============........]")
    elif(prog>=0.50):
        print("[==========..........]")
    elif(prog==0.40):
        print("[========............]")
    elif(prog>=0.30):
        print("[======..............]")
    elif(prog>=0.20):
        print("[====................]")
    elif(prog>=0.10):
        print("[==..................]")
    elif(prog>=0):
        print("[....................]")
    elif(prog<0):
        print("[--------------------]")

filename = input("enter filename: ")
progress(-1)

# read the file
with open(filename, "r") as f:
    content = f.read()

# split the file into array of actions
contentArr = []
temp = ""
for i in range(len(content)):
    char = content[i]
    if(char == ";"):
        contentArr.append(temp)
        temp = ""
    elif(char == "\n"):
        continue
    else:
        temp += char
    
# reset out.js
out = open("out.js", "w")
out.write("")

# write to out.js
out = open("out.js", "a")
for i in range(len(contentArr)):
    progress((i+1)/len(contentArr))
    cont = contentArr[i]
    cont = cont.replace(");", "")
    if(cont.startswith("tone")):
        tone = cont.replace('tone(buzzerPin, ', '')
        tone = tone.replace(")", "")
        r = "music.ringTone(" + tone + ")"
        out.write(r)
    elif(cont.startswith("delay")):
        time = cont.replace('delay(', '')
        time = time.replace(")", "")
        time = int(time)
        time *= 1000                            # Converting from milliseconds to microseconds
        time = str(time)
        r = "control.waitMicros(" + time + ")"
        out.write(r)
    else:
        out.write("music.stopAllSounds()")
    out.write("\n")

print(flush=True)
print('saved to: "'  + os.getcwd() + '\\out.js"')
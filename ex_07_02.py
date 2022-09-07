# This program is the exercise as described in Chapter 7 from "Python for Everybody" on freeCodeCamp.org
# https://www.py4e.com/code3/mbox.txt (mbox.txt)
# https://www.py4e.com/code3/mbox-short.txt (mbox-short.txt)

fn = input('Enter File Name: ')

if fn == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")

else:

    try:
        fh = open(fn)
    except:
        print('File cannot be opened:', fn)
        quit()

    count = 0
    fcon = 0
    for lx in fh:
        if lx.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            fcon = fcon + float(lx[19:])
            fav = fcon / count
    print('There are', count, 'X-DSPAM-Confidence values in:', fn)
    print('The average of these values is:', fav)





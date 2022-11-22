import random

NO_OF_CHARS = 500
def getNextState(pat, M, state, x):
	if state < M and x == ord(pat[state]):
		return state+1

	i=0
	for ns in range(state,0,-1):
		if ord(pat[ns-1]) == x:
			while(i<ns-1):
				if pat[i] != pat[state-ns+1+i]:
					break
				i+=1
			if i == ns-1:
				return ns
	return 0

def computeTF(pat, M):
	global NO_OF_CHARS

	TF = [[0 for i in range(NO_OF_CHARS)]\
		for _ in range(M+1)]

	for state in range(M+1):
		for x in range(NO_OF_CHARS):
			z = getNextState(pat, M, state, x)
			TF[state][x] = z

	return TF

def search(pat, txt):
    global NO_OF_CHARS
    U = len(pat)
    N = len(txt)
    TU = computeTF(pat, U)
    state = 0
    status = 'l'
    for i in range(N):
        state = TU[state][ord(txt[i])]
        if state == U:
            if txt[i-U+6] == '1' and status == 'l':
               print("Unlocked at index: " + format(i-U+1))
               status = 'u'
            elif txt[i-U+6] == '4' and status == 'u':
                print("Locked at index: " + format(i-U+1))
                status = 'l'

# manually enter the digits for the lock            
def manual():
    unlock = "20489"
    inp = input("Enter A Code: ")
    translated = inp.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./=-+_!@#$%^&*() :;[]{\}|`~'})
    print(translated)
    search(unlock, translated)

#automatically tests and trys to break the lock
def tester():
    status = "Locked!"
    tap = ""
    Ct = 0
    unlock = "204891"
    while status == "Locked!":
        tap = tap + random.choice(["0","1","2","3","4","5","6","7","8","9"])
        if len(tap) == 24:
            print(tap)
            if unlock in tap:
                status = "Unlocked!"
                print("It took " + str((Ct * 12)) + " entries till Lock was broken!")
            tap = ""
            Ct = Ct + 1

def main():
    loop = True
    while loop:
        inp = input("Enter 1 for manual entry:\nEnter 2 for forced entry:\nEnter 3 to exit:\n")
        if inp == "1":
            loop = False
            manual()
        elif inp == "2":
            loop = False
            tester()
        elif inp == "3":
            loop = False

main()
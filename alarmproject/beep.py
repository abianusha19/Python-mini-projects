import winsound

def beep(n):
    for x in range(n):
        winsound.PlaySound("papa_telephone.wav",winsound.SND_FILENAME)
    return


beep(1)
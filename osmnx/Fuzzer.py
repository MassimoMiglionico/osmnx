def file_fuzzer(selected_file_address, FuzzFactor=250, launch=True):
    import math, subprocess, time, random

    #INITIALISATION
    # try:
    #     selected_file_address = str(selected_file_address)
    # except e:
    #     return "File input is not a string"

    path = selected_file_address
    file_name = path.split("\\")[-1]
    extension = file_name.split(".")[-1]

    program_to_test = r"C:\Users\massi\AppData\Local\Programs\Microsoft VS Code\Code.exe" #programme en version beta à tester

    print(type(selected_file_address))
    #stocker les donées binaires du fichier choisi
    buffer = bytearray(open(selected_file_address, 'rb').read())

    #nombre de réécritures dans le buffer
    # plus le FuzzFactor est grand moins il y a de réécritures
    numwrites = random.randrange(math.ceil((float(len(buffer)) / FuzzFactor)))+1

    #phase de fuzzing (Code de Charlie Miller)

    for i in range(numwrites):
        rbytes = random.randrange(256) #byte aleatoire
        readnum = random.randrange(len(buffer)) #indice aléatoire dans le buffer
        buffer[readnum] = rbytes #remplacement du byte present


    #fichier de sortie
    output_file = r"C:\Users\massi\Desktop\output." + extension

    try:
        open(output_file, 'wb').write(buffer)
    except PermissionError: # catch les PermissionError à l'ouverture
        return

    if launch:
        #lire le fichier de sortie
        process = subprocess.Popen([program_to_test, output_file])

        #mettre fin au processus de lecture du fichier


        time.sleep(1)
        crashed = process.poll()
        if not crashed:
            process.terminate
        else:
            print('Un crash a eu lieu ...')

file_fuzzer(r"C:\Users\massi\Desktop\test.py", FuzzFactor=10)
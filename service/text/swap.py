def swap(body: str, password: str) -> str:
    master = list(body)

    step = int(len(password)/4)

    for i, v in enumerate(master):
        for j, b in enumerate(password):
            if v == b:
                if j < step or (j >= 2*step and j < 3*step):
                    master[i] = password[j+step]
                else:
                    master[i] = password[j-step]

    master = ''.join(master)
    return master
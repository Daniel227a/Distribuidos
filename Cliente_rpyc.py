import rpyc

if __name__ == "__main__":
    while True:
        conn = rpyc.connect("localhost", 8000)
        vote = input("quem ganha a partida ? city ou real: ")
        conn.root.vote(vote)
        votes = conn.root.get_votes()
        print(f"Contagem de votos: {votes}")
        conn.close()

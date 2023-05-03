import rpyc
from rpyc.utils.server import ThreadedServer

class VoteService(rpyc.Service):
    votes = {"city": 0, "real": 0}

    def exposed_vote(self, candidate):
        self.votes[candidate] += 1
        print(f"Voto recebido para {candidate}")
    
    def exposed_get_votes(self):
        return self.votes

if __name__ == "__main__":
    server = ThreadedServer(VoteService, port=8000)
    server.start()

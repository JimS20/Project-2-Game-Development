class train:
    def __init__ (self,posetion,watingpassangers,waitingcontainers):
        self.p=posetion
        self.wp=waitingcontainers
        self.wc=waitingcontainers

class trein:
    def __init__(self,position):
        self.p=position
        self.pas=0
        self.con=0
    def travelto(self,station):
        self.p=station
        self.passenger=station.wp
        self.wp=0



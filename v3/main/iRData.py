import irsdk

class iRData(object):
    ir = irsdk.IRSDK()
    ir.startup()#test_file='datavuelta4.bin')
    playerID = ir['PlayerCarIdx']

    if ir['WeekendInfo']['TrackID']:
        trackID = ir['WeekendInfo']['TrackID']
    if ir['DriverInfo']['Drivers'][playerID]['CarID']:
        carID = ir['DriverInfo']['Drivers'][playerID]['CarID']
    if ir['WeekendInfo']['SeriesID']:
        seriesID = ir['WeekendInfo']['SeriesID']
    else:
        seriesID = 0
    totalLaps = ir['SessionInfo']['Sessions'][0]['SessionLaps']
    maxIncidents = ir['WeekendInfo']['WeekendOptions']['IncidentLimit']
    myIncidents = ir['PlayerCarMyIncidentCount']
    sessions = ir['SessionInfo']['Sessions']
    lap = ir['Lap']

    
    def getSesion(self):
        if len(self.ir['SessionInfo']['Sessions']) == 3:
            return 2
        elif len(self.ir['SessionInfo']['Sessions']) == 2:
            return 1
        elif len(self.ir['SessionInfo']['Sessions']) == 1:
            return 0
    
    def getSesionLaps(self):
        return self.ir['SessionInfo']['Sessions'][iRData.getSesion(self)]['SessionLaps']

    def getParticipantes(self):
        return self.ir['SessionInfo']['Sessions'][iRData.getSesion(self)]['ResultsPositions']
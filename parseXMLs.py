import os
import xml.etree.ElementTree as ET
import time

path = 'Results'

class Vote(object):
   def __init__(self, party, vote):
      self.party = party
      self.vote = vote
   #def __repr__(self):
   #   return "<PARTY: %s, VOTES: %s>" % (self.party, self.vote)


for filename in os.listdir(path):
   if not filename.endswith('.xml'): continue
   fullname = os.path.join(path, filename)
   tree = ET.parse(fullname)
   print filename
   
   for result in tree.findall("./constituencyResult/results"):

      votingData = []
      partyName = []
      partyVotes = []
      
      for party in result.iter('partyCode'):
         partyName.append(party.text)

      for votes in result.iter('votes'):
         partyVotes.append(votes.text)
      
      if len(partyName)!=len(partyVotes):
         print "Party Code inconsistent with Votes data, skipping file..."
      else :
         print "XML file data consistent, sorting data..."

         for item in range(len(partyName)):
            votingData.append(Vote(partyName[item], partyVotes[item]))

         votingData.sort(key=lambda Vote: int(Vote.vote), reverse=True)
         
         for item in votingData:
            print item.party + " " + item.vote
   #time.sleep(1)
            
    

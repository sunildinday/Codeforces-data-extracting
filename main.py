import requests
def get_submission_list(handle):	
	url="http://codeforces.com/api/user.status?handle=";
	url+=(handle)
	status={} #used to get the number of problem which got accpeted,wrong answer or tle etc 
	data=requests.get(url)
	submission=data.json()
	i=1
	if submission['status']=="OK":
		result=submission['result']
		for rslt in result:
			with open("Submission.txt","a") as file:
				file.write(str(i)+"\n")
				problem=rslt['problem']
				if problem.has_key('name'):
					file.write("Problem Name: "+(problem['name']).encode('utf8')+"\n")
				else:
					file.write("Else")	
				if 'index' in problem:
					file.write("Problem Index: "+(problem['index']).encode('utf8')+"\n")
				if 'participantType' in problem:
					file.write("ParticipantType: "+(problem['participantType']).encode('utf8')+"\n")	
				if 'verdict' in rslt:
					file.write("Problem Verdict: "+(rslt['verdict']).encode('utf8')+"\n")	
					if rslt['verdict'] in status:
						status[rslt['verdict']]+=1
					else:
						status[rslt['verdict']]=1	
				file.write("\n\n\n")
				i+=1
	else:
		print "Connection Error.............."	
	return status
def get_status(status):
	if len(status)>0:
		with open('status.txt',"a") as file:
			file.write("\t\t\t\t\t\t\t\t\t\t\Status\n")
			file.write("Verdict\t\t\t\t\t\tCount\t\t\n")
			for key,value in status.iteritems():
				file.write(str(key)+"\t\t\t\t"+str(value))
				file.write("\n\n")	

	else:
		print "No Submission to show"	
def main():
	handler=raw_input('Enter the Handler')#like sunil.dinday
	status=get_submission_list(handler)
	if(int(raw_input("Do you want to get Status of your submission : If yes press any number except 0"))):
		get_status(status)		
if __name__=='__main__' :
	main()
	
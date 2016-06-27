import requests

def get_submission_list(handle):	
	url="http://www.codeforces.com/api/use";
	url+=str(handle)
	data=requests.get("http://codeforces.com/api/user.status?handle=sunil.dinday")
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
				file.write("\n\n\n")
				i+=1
	else:
		print "Connection Error.............."	



get_submission_list("sunil.dinday")
from firebase import firebase

firebase = firebase.FirebaseApplication('https://scarlethacks-e6978.firebaseio.com/')

#Format of database:
#
#
# scarlethacks-e6978
#     users
#         -KyhtgcjKX7vVKnUbjCi
#             hap:104
#		  -SDF324Jht7vVKnUbjCi
#             hap:39
#		  -WERU4456JFH67ffdcas
#             hap:17
#		  -AWsl4ldsFak257dSaQk
#             hap:29

#adding data:
result = firebase.post('/users', {hap:1002})


#NEW FORMAT:
#
#
# scarlethacks-e6978
#     users
#         -KyhtgcjKX7vVKnUbjCi
#             hap:104
#		  -SDF324Jht7vVKnUbjCi
#             hap:39
#		  -WERU4456JFH67ffdcas
#             hap:17
#		  -AWsl4ldsFak257dSaQk
#             hap:29
#		  -LQOSfsdio234sisDFe9
#             hap:1002

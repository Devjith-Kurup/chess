square = {'a1': '  wR  ', 'a2': '  w*  ', 'a3': '      ' , 'a4': '      ', 'a5': '      ', 'a6': '      ', 'a7': '  b*  ', 'a8': '  bR  ', 'b1': '  wN  ', 'b2': '  w*  ', 'b3': '      ', 'b4': '      ', 'b5': '      ', 'b6': '      ', 'b7': '  b*  ', 'b8': '  bN  ', 'c1': '  wB  ', 'c2': '  w*  ', 'c3': '      ', 'c4': '      ', 'c5': '      ', 'c6': '      ', 'c7': '  b*  ', 'c8': '  bB  ', 'd1': '  wQ  ', 'd2': '  w*  ', 'd3': '      ', 'd4': '      ', 'd5': '      ', 'd6': '      ', 'd7': '  b*  ', 'd8': '  bK  ', 'e1': '  wK  ', 'e2': '  w*  ', 'e3': '      ', 'e4': '      ', 'e5': '      ', 'e6': '      ', 'e7': '  b*  ', 'e8': '  bQ  ', 'f1': '  wB  ', 'f2': '  w*  ', 'f3': '      ', 'f4': '      ', 'f5': '      ', 'f6': '      ', 'f7': '  b*  ', 'f8': '  bB  ', 'g1': '  wN  ', 'g2': '  w*  ', 'g3': '      ', 'g4': '      ', 'g5': '      ', 'g6': '      ', 'g7': '  b*  ', 'g8': '  bN  ', 'h1': '  wR  ', 'h2': '  w*  ', 'h3': '      ', 'h4': '      ', 'h5': '      ', 'h6': '      ', 'h7': '  b*  ', 'h8': '  bR  '}
alphaCoord = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

whiteCaptured = []
blackCaptured = []

def chessBoard():
	print('\n  ________________________________________________________')	
	for x in range(8):
		num = 8-x
		print(str(8-x) + ' |', end = '')
		for y in range(8):
			print(square[alphaCoord[y] + str(num)], end = '')
			print('|', end = '')
		print('\n  _________________________________________________________')
	print('   ', end = '')
	for alpha in alphaCoord:
		print('   ' + alpha + '   ', end = '')
	print('\n')
	
def movePiece(player, opponent, Captured):
	while True:
		
		print('___________________________________________________________________\n')
		if player == 'w':
			print("White's turn:\n")
		elif player == 'b':
			print("Black's turn:\n")

		try:
			moveFrom = input("Coordinates of piece to move: ")
			moveTo = input("Coordinates to place the piece: ")

			if moveFrom not in square.keys() or moveTo not in square.keys():
				print("\nGive correct coordinates!")
				continue 
				
			if player not in square[moveFrom]:
				print("\nYour piece isnt there!")
				continue
			
			if moveFrom == moveTo:
				print("\nYou cant place your piece where it already is!")
				continue

			alphaCoord_moveFrom = moveFrom[0]
			alphaCoord_moveTo = moveTo[0]
			numCoord_moveFrom = int(moveFrom[1])
			numCoord_moveTo = int(moveTo[1])
			movePiece = True
			
			if '*' in square[moveFrom] or 'N' in square[moveFrom] or 'K' in square[moveFrom]:
				if alphaCoord.index(alphaCoord_moveTo) >= alphaCoord.index(alphaCoord_moveFrom)+3:
					print("\nInvalid move!")
					continue

			#Pawn			
			if '*' in square[moveFrom]:
				if player == 'w':
					if alphaCoord_moveFrom == alphaCoord_moveTo:
						if numCoord_moveFrom == 2 and numCoord_moveFrom+2 == numCoord_moveTo:
							for num in range(numCoord_moveFrom+1, numCoord_moveTo+1):
								if square[alphaCoord_moveFrom + str(num)] != '      ':
										print("\n"+square[alphaCoord_moveFrom+str(num)]+"is in the way at "+alphaCoord_moveFrom+str(num)+"!")
										movePiece = False
										break
							if alphaCoord_moveTo != 'a':
								if 'b*' in square[alphaCoord[alphaCoord.index(alphaCoord_moveTo)-1]+'4']:
									enPassant = True
							elif alphaCoord_moveTo != 'h':
								if 'b*' in square[alphaCoord[alphaCoord.index(alphaCoord_moveTo)+1]+'4']:
									enPassant = True
						elif numCoord_moveFrom+1 == numCoord_moveTo:
							if square[moveTo] != '      ':
								print("\n"+square[moveTo]+"is in the way at "+moveTo+"!")
								continue
						else:
							print("\nInvalid move!")
							continue 
					elif numCoord_moveFrom+1 == numCoord_moveTo:
						if alphaCoord_moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1] or alphaCoord_moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+1]:
							if square[moveTo] == '      ':
								print("\nNo piece at " + moveTo + " to capture!")
								continue
					else:
						print("\nInvalid move!")
						continue
				elif player == 'b':
					if alphaCoord_moveFrom == alphaCoord_moveTo:
						if numCoord_moveFrom == 7 and numCoord_moveTo+2 == numCoord_moveFrom:
							for num in reversed(range(numCoord_moveTo, numCoord_moveFrom)):
								if square[alphaCoord_moveFrom + str(num)] != '      ':
									print("\n"+square[alphaCoord_moveFrom+str(num)]+"is in the way at "+alphaCoord_moveFrom+str(num)+"!")
									movePiece = False
									break
							if alphaCoord_moveTo != 'a':
								if 'w*' in square[alphaCoord[alphaCoord.index(alphaCoord_moveTo)-1]+'5']:
									enPassant = True
							elif alphaCoord_moveTo != 'h':
								if 'w*' in square[alphaCoord[alphaCoord.index(alphaCoord_moveTo)+1]+'5']:
									enPassant = True
						elif numCoord_moveTo+1 == numCoord_moveFrom:
							if square[moveTo] != '      ':
								print("\n"+square[moveTo]+"is in the way at "+moveTo+"!")
								continue
						else:
							print("\nInvalid move!")
							continue
					elif numCoord_moveFrom == numCoord_moveTo+1:
						if alphaCoord_moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1] or alphaCoord_moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+1]:
							if square[moveTo] == '      ':
								print("\nNo piece at " + moveTo + " to capture!")
								continue
					else:
						print("\nInvalid move!")
						continue
				if numCoord_moveTo == 1 or numCoord_moveTo == 8:
					while True:
						promotedPiece =  input("\n'N' for Knight\n'B' for Bishop\n'R' for Rook\n'Q' for Queen\nPromote Pawn to: ").upper()
						if promotedPiece not in ['N', 'B', 'R', 'Q']:
							print("\nGive correct notation!")
							continue
						square[moveFrom] = '  ' + player + promotedPiece + '  '
						break

			#Knight
			elif 'N' in square[moveFrom]:
				if moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+1]+str(numCoord_moveFrom+2) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1]+str(numCoord_moveFrom+2) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+1]+str(numCoord_moveFrom-2) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1]+str(numCoord_moveFrom-2) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+2]+str(numCoord_moveFrom+1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+2]+str(numCoord_moveFrom-1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-2]+str(numCoord_moveFrom+1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-2]+str(numCoord_moveFrom-1):
					movePiece = True
				else:
					print("\nInvalid move!")
					continue     

			#Bishop
			elif 'B' in square[moveFrom]:
				if alphaCoord_moveFrom == alphaCoord_moveTo or numCoord_moveFrom == numCoord_moveTo:
					print("\nInvalid move!")
					continue
				else:
					if alphaCoord.index(alphaCoord_moveTo) > alphaCoord.index(alphaCoord_moveFrom):
						alphaIncrement = 1
					elif alphaCoord.index(alphaCoord_moveTo) < alphaCoord.index(alphaCoord_moveFrom):
						alphaIncrement = -1
					if numCoord_moveTo > numCoord_moveFrom:
						numIncrement = 1
					elif numCoord_moveTo < numCoord_moveFrom:
						numIncrement = -1
					alphaCoord_tempSquare = alphaCoord.index(alphaCoord_moveFrom)
					numCoord_tempSquare = numCoord_moveFrom
					while True:
						alphaCoord_tempSquare += alphaIncrement
						numCoord_tempSquare += numIncrement
						if alphaCoord_tempSquare == -1 or alphaCoord_tempSquare == 8 or numCoord_tempSquare == 0 or numCoord_tempSquare == 9:
							print("\nInvalid move!")
							movePiece = False
							break
						tempSquare = alphaCoord[alphaCoord_tempSquare] + str(numCoord_tempSquare)
						if tempSquare == moveTo:
							alphaCoord_tempSquare = alphaCoord.index(alphaCoord_moveFrom)
							numCoord_tempSquare = numCoord_moveFrom
							while True:
								alphaCoord_tempSquare += alphaIncrement
								numCoord_tempSquare += numIncrement
								if alphaCoord_tempSquare == -1 or alphaCoord_tempSquare == 8 or numCoord_tempSquare == 0 or numCoord_tempSquare == 9:
									print("\nInvalid move!")
									movePiece = False
									break
								tempSquare = alphaCoord[alphaCoord_tempSquare] + str(numCoord_tempSquare)
								if tempSquare == moveTo:
									break
								elif square[tempSquare] != '      ':
									print("\n"+square[tempSquare]+"is in the way at "+tempSquare+"!")
									movePiece = False
									break
							break

			#Rook	
			elif 'R' in square[moveFrom]:
				if alphaCoord_moveFrom == alphaCoord_moveTo:
					if numCoord_moveFrom < numCoord_moveTo:
						limit = range(numCoord_moveFrom+1, numCoord_moveTo)
					else:
						limit = reversed(range(numCoord_moveTo+1, numCoord_moveFrom))	
					for num in limit:
						if square[alphaCoord_moveTo + str(num)] != '      ':
							movePiece = False
							print("\n"+square[alphaCoord_moveFrom+str(num)]+"is in the way at "+alphaCoord_moveFrom+str(num)+"!")
							break	
				elif numCoord_moveFrom == numCoord_moveTo:
					if alphaCoord.index(alphaCoord_moveFrom) < alphaCoord.index(alphaCoord_moveTo):
						limit = range(alphaCoord.index(alphaCoord_moveFrom)+1, alphaCoord.index(alphaCoord_moveTo))	
					else:
						limit = reversed(range(alphaCoord.index(alphaCoord_moveTo)+1, alphaCoord.index(alphaCoord_moveFrom)))
					for alpha in limit:
						if square[alphaCoord[alpha]+str(numCoord_moveTo)] != '      ':
							movePiece = False
							print("\n"+square[alphaCoord[alpha]+str(numCoord_moveFrom)]+"is in the way at "+alphaCoord[alpha]+str(numCoord_moveFrom)+"!")
							break			
				else:
					print("\nInvalid move!")
					continue
				
			#Queen
			elif 'Q' in square[moveFrom]:
				if alphaCoord_moveFrom == alphaCoord_moveTo:
					if numCoord_moveFrom < numCoord_moveTo:
						limit = range(numCoord_moveFrom+1, numCoord_moveTo)
					else:
						limit = reversed(range(numCoord_moveTo+1, numCoord_moveFrom))	
					for num in limit:
						if square[alphaCoord_moveTo + str(num)] != '      ':
							movePiece = False
							print("\n"+square[alphaCoord_moveFrom+str(num)]+"is in the way at "+alphaCoord_moveFrom+str(num)+"!")
							break	
				elif numCoord_moveFrom == numCoord_moveTo:
					if alphaCoord.index(alphaCoord_moveFrom) < alphaCoord.index(alphaCoord_moveTo):
						limit = range(alphaCoord.index(alphaCoord_moveFrom)+1, alphaCoord.index(alphaCoord_moveTo))	
					else:
						limit = reversed(range(alphaCoord.index(alphaCoord_moveTo)+1, alphaCoord.index(alphaCoord_moveFrom)))
					for alpha in limit:
						if square[alphaCoord[alpha]+str(numCoord_moveTo)] != '      ':
							movePiece = False
							print("\n"+square[alphaCoord[alpha]+str(numCoord_moveFrom)]+"is in the way at "+alphaCoord[alpha]+str(numCoord_moveFrom)+"!")
							break			
				else:
					if alphaCoord.index(alphaCoord_moveTo) > alphaCoord.index(alphaCoord_moveFrom):
						alphaIncrement = 1
					elif alphaCoord.index(alphaCoord_moveTo) < alphaCoord.index(alphaCoord_moveFrom):
						alphaIncrement = -1
					if numCoord_moveTo > numCoord_moveFrom:
						numIncrement = 1
					elif numCoord_moveTo < numCoord_moveFrom:
						numIncrement = -1
					alphaCoord_tempSquare = alphaCoord.index(alphaCoord_moveFrom)
					numCoord_tempSquare = numCoord_moveFrom
					while True:
						alphaCoord_tempSquare += alphaIncrement
						numCoord_tempSquare += numIncrement
						if alphaCoord_tempSquare == -1 or alphaCoord_tempSquare == 8 or numCoord_tempSquare == 0 or numCoord_tempSquare == 9:
							print("\nInvalid move!")
							movePiece = False
							break
						tempSquare = alphaCoord[alphaCoord_tempSquare] + str(numCoord_tempSquare)
						if tempSquare == moveTo:
							alphaCoord_tempSquare = alphaCoord.index(alphaCoord_moveFrom)
							numCoord_tempSquare = numCoord_moveFrom
							while True:
								alphaCoord_tempSquare += alphaIncrement
								numCoord_tempSquare += numIncrement
								if alphaCoord_tempSquare == -1 or alphaCoord_tempSquare == 8 or numCoord_tempSquare == 0 or numCoord_tempSquare == 9:
									print("\nInvalid move!")
									movePiece = False
									break
								tempSquare = alphaCoord[alphaCoord_tempSquare] + str(numCoord_tempSquare)
								if tempSquare == moveTo:
									break
								elif square[tempSquare] != '      ':
									print("\n"+square[tempSquare]+"is in the way at "+tempSquare+"!")
									movePiece = False
									break
							break
			
			#King
			elif 'K' in square[moveFrom]:
				if moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+1]+str(numCoord_moveFrom) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1]+str(numCoord_moveFrom) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)]+str(numCoord_moveFrom+1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)]+str(numCoord_moveFrom-1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)+1]+str(numCoord_moveFrom+1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1]+str(numCoord_moveFrom+1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1]+str(numCoord_moveFrom-1) or moveTo == alphaCoord[alphaCoord.index(alphaCoord_moveFrom)-1]+str(numCoord_moveFrom+1):
					movePiece = True
				else:
					print("\nInvalid move!")
					continue
			
		except: 
			print("\nInvalid move!")
			continue
		
		else:
			if movePiece == True:		
				if player in square[moveTo]:
					print("\nYou cant capture your own piece!")
					continue
				elif opponent in square[moveTo]:
					Captured.append(square[moveTo])
					print("\n" + square[moveFrom] + "captured" + Captured[-1] +"!")
					print(Captured)
				square[moveTo] = square[moveFrom]
				square[moveFrom] = '      '
				chessBoard()
				break

print("-------------------------------CHESS-------------------------------")
chessBoard()

while True:
	movePiece('w', 'b', whiteCaptured)
	movePiece('b', 'w', blackCaptured)
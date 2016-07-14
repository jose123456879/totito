A="A"
B="B"
C="C"
D="D"
E="E"
F="F"
G="G"
H="H"
I="I"
turnos=1
win=False
print("bienvenidos a totito")
for judio in range (5):
	if win ==False and turnos <=5:
		print(A+"_|_"+B+"_|_"+C+"\n"+D+"_|_"+E+"_|_"+F+"\n"+G+" | "+H+" | "+I)
		print("turno J1")
		jugador1=input("ingrese una casilla: ")
		if jugador1==A and A!="O":
			A="X"
		if jugador1==B and B!="O":
			B="X"
		if jugador1==C and C!="O":
			C="X"
		if jugador1==D and D!="O":
			D="X"
		if jugador1==E and E!="O":
			E="X"
		if jugador1==F and F!="O":
			F="X"	
		if jugador1==G and G!="O":
			G="X"
		if jugador1==H and H!="O":
			H="X"
		if jugador1==I and I!="O":
			I="X"
		if A=="X" and B=="X" and C=="X":
			win=True
			print("ganador J1")
		if D=="X" and E=="X" and F=="X":
			win=True
			print("ganador J1")
		if G=="X" and H=="X" and I=="X":
			win=True
			print("ganador J1")
		if A=="X" and D=="X" and G=="X":
			win=True
			print("ganador J1")
		if B=="X" and E=="X" and H=="X":
			win=True
			print("ganador J1")
		if A=="X" and E=="X" and I=="X":
			win=True
			print("ganador J1")
		if G=="X" and E=="X" and C=="X":
			win=True
			print("ganador")
		if win==False and turnos<=4:	
			print(A+"_|_"+B+"_|_"+C+"\n"+D+"_|_"+E+"_|_"+F+"\n"+G+" | "+H+" | "+I)
			print("Turno J2")
			jugador2=input("ingrese una casilla: ")
			jugador2=="O"
			if jugador2==A and A!="X":
				A="O"		
			if jugador2==B and B!="X":
				B="O"
			if jugador2==C and C!="X":
				C="O"	
			if jugador2==D and D!="X":
				D="O"						
			if jugador2==E and E!="X":
				E="O"			
			if jugador2==F and F!="X":
				F="O"		
			if jugador2==G and G!="X":
				G="O"	
			if jugador2==H and H!="X":
				H="O"
			if jugador2==I and I!="X":
				I="O"	
			if A=="O" and B=="O" and C=="O":
				win=True
				print("ganador J2")
			if D=="O" and E=="O" and F=="O":
				win=True
				print("ganado J2")
			if G=="O" and H=="O" and I=="O":
				win=True
				print("ganado J2")
			if A=="O" and D=="O" and G=="O":
				win=True
				print("ganador J2")
			if B=="O" and E=="O" and H=="O":
				win=True
				print("ganador J2")
			if A=="O" and E=="O" and I=="O":
				win=True
				print("ganador J2")
			if G=="O" and E=="O" and C=="O":
				win=True
				print("ganador J2")				 
			if judio>5:
				print("EMPATE")
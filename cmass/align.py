from cmmi import *

def alignCM_(atomicCoor, cenMass):
	atomicCoor_aligned = []
	for i in range(len(atomicCoor)):
		atom = []
		for j in range(len(atomicCoor[i])):
			if i in range(1, 4):
				atom.append(float(atomicCoor[i][j]) - cenMass[i - 1])
			else:
				atom.append(atomicCoor[i][j])
		atomicCoor_aligned.append(atom)
	return atomicCoor_aligned

def alignCM(atomicCoor, cenMass):
	molecule_aligned = []
	for atom in atomicCoor:
		atom_aligned = atom
		for i in range(1, 4):
			atom_aligned[i] = round(atom_aligned[i] - cenMass[i - 1], 3)
		molecule_aligned.append(atom_aligned)
	return molecule_aligned

def combine(words): #list
	row = f'{words[0]:7s}{words[1]:6s}{words[2]:4s}{words[3]:4s}{words[4]:2s}{words[5]:8s}{words[6]:9s}{words[7]:7s}{words[8]:9s}{words[9]:5s}{words[10]:16s}{words[11]:3s}\n'
	return row #string


def copyfile(fileA, fileB):
	with open(fileA, 'r') as ifile:
		data = ifile.readlines()
	with open(fileB, 'w') as ofile:
		ofile.writelines(data)

def main():

	import sys
	originPDB = sys.argv[1]
	alignedPDB = 'pdb/aligned.pdb'


	atomicCoor = readPDB(originPDB)
	atomicMass = readTOPs()
	molecule, missing = createMole(atomicCoor, atomicMass)
	cenMass, totMass = calulateCM(molecule)
	
	data = alignCM(atomicCoor, cenMass)
	counter = 0
	with open(originPDB,'r') as fileA:
		with open(alignedPDB, 'a+') as fileB:
			for row in fileA:
				words = row.split()
				if words[0] == 'ATOM':
					words[6] = str(data[counter][1])
					words[7] = str(data[counter][2])
					words[8] = str(data[counter][3])       		
					if len(words) == 12: 
						pass
					else:
						word = words[9]
						words[9] = word[:4]
						words.insert(10, word[4:])
					line = combine(words)
					counter += 1
					fileB.write(line)
				else:
					fileB.write(row)

if __name__ == '__main__':
	main()
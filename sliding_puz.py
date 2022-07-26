def slide_puzzle(ar):
	
	def main(o_ar):
		c_ar = o_ar
		mt_pos = [];
		childs = [];
		for i in c_ar:
			for j in i:
				if j == 0:
					mt_pos.append(c_ar.index(i));
					mt_pos.append(i.index(j));
		
		if mt_pos[0] != 0:
			childs.append(c_ar[mt_pos[0] - 1][mt_pos[1]]);
		if mt_pos[1] != 0:
			childs.append(c_ar[mt_pos[0]][mt_pos[1] - 1])
		if mt_pos[0] != (len(c_ar) - 1):    
			childs.append(c_ar[mt_pos[0] + 1][mt_pos[1]]);
		if mt_pos[1] != (len(c_ar[mt_pos[1]]) - 1):
			childs.append(c_ar[mt_pos[0]][mt_pos[1] + 1])

		def find_comp(o_ar, mt_pos, child, child_pos):
			comp_ar = o_ar;
			#print(child)
			#print(child_pos)
			comp_ar[child_pos[0]][child_pos[1]] = 0;
			comp_ar[mt_pos[0]][mt_pos[1]] = child;			
			print(comp_ar)
		
		for child in childs:
			child_pos = [];
			for i in c_ar:
				for j in i:
					if j == child:
						child_pos.append(c_ar.index(i));
						child_pos.append(i.index(j));			
			find_comp(o_ar, mt_pos, child, child_pos);
			
		#print(mt_pos)
		#print(childs)
		print(c_ar)
	main(ar)
	#print(ar)

slide_puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])


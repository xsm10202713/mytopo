#!/usr/bin/python

(n, k) = (8, 4)
out_file_name = "bcube_4_8"

n_servers = n**(k+1)

n_switches = n**k * (k+1)

def next(tp):
	for i in range(0, k+1):
		tp[i] += 1
		if tp[i]>=n:
			tp[i] = 0
		else:
			return tp
	return None

def get_id(tp):
	# print 'getting_id of ', tp
	s = 0
	for i in range(0, k+1):
		s = s * n + tp[i]
	return s

def get_switch_id(tp, dimension):
	# print 'getting switch id of ', tp, dimension
	return get_id([0] + tp[:dimension] + tp[dimension+1:]) * (k+1) + dimension

tp = [0] * (k+1)

out_file = open(out_file_name,'w')
out_file.write(str(n_servers + n_switches) + " " + str(n_switches * n) + " " + str(2) + " " + str(n_servers)+ '\n' )
while tp:
	for i in range(0, k+1):
		if tp[i] == 0:
			neighbor = tp[:]
			switch_id = get_switch_id(tp, i)
			for a in range(0, n):
				neighbor[i] = a
				out_file.write(str(get_id(neighbor)) + " " + str(switch_id + n_servers) + '\n')

	tp = next(tp)
out_file.close()
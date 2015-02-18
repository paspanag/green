from datetime import date, timedelta
import subprocess
import time

display =  [[0,1,1,1,2,3,4,3,2,1,1,1,0,1,1,1,2,3,4,3,2,1,1,1,0,1,1,1,2,3,4,2,3,1,1,1,0,1,1,1,2,3,4,3,2,1,1,1,0,1,1,1], \
			[1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1], \
			[1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1], \
			[1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0], \
			[2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1,0,1,1,1,0,1,1,1,2,1,1,1], \
			[3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1,1,0,1,0,1,1,1,2,3,2,1,1], \
			[4,3,2,1,1,1,0,1,1,1,2,3,4,3,2,1,1,1,0,1,1,1,2,3,4,3,2,1,1,1,0,1,1,1,2,3,4,3,2,1,1,1,0,1,1,1,2,3,4,3,2,1]]

DATE_START = date(2014,2,16)

def matrix_evaluator(row, col, matrix_value):
	days_past = 7 * col + row
	current_date = DATE_START + timedelta(days=days_past)
	commit_date = current_date.strftime("%Y-%m-%d")
	while matrix_value > 0:
		print '%s,%s - %s\n' % (row, col, commit_date)
		with open('update_file','a') as update_file:
			update_file.write('%s,%s - %s\n' % (row, col, commit_date))
		subprocess.call(["git", "commit", "-am", '"update update file"', "--date", commit_date])
		matrix_value -= 1

	return current_date


def matrix_traverse(row, col, matrix, mat_val_func):

	if col >= len(matrix[0]):
		return row,col

	# print "row - %s, col - %s, date - %s, value - %s" % (row, col, matrix_evaluator(row, col, matrix, start_date), matrix[row][col])
	matrix_evaluator(row, col, matrix[row][col])

	col = col + 1 if (row + 1 ) % len(matrix) == 0 else col

	return matrix_traverse((row + 1) % len(matrix), col, matrix, mat_val_func)

subprocess.call(["touch", "update_file"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", '"added update_file"'])
matrix_traverse(0,0,display, matrix_evaluator)
subprocess.call(["git", "push", "origin"])
from random import randint
import os

class GameBoard(object):
	def __init__(self):
		self.board = []
		for i in range(16):
			self.board.append([0])
			
		self.r0 = self.board[0:4]
		self.r1 = self.board[4:8]
		self.r2 = self.board[8:12]
		self.r3 = self.board[12:16]
		
		self.c0 = [self.board[0], self.board[4], self.board[8], self.board[12]]
		self.c1 = [self.board[1], self.board[5], self.board[9], self.board[13]]
		self.c2 = [self.board[2], self.board[6], self.board[10], self.board[14]]
		self.c3 = [self.board[3], self.board[7], self.board[11], self.board[15]]
		
		
		
	def generate(self):
		i = randint(0, 15)
		cnt = 0
		while self.board[i][0] != 0:
			i += 1
			if i > 15:
				i = 0
			cnt += 1
			if cnt >= 16:
				return False
		else:
			self.board[i][0] = 2
		return True
	
	def check_up(self, c):
		cur = [-1]
		j = 0
		
		while j < 4:
			if c[j][0] == 0:
				j += 1
				continue
			if cur[0] == c[j][0]:
				cur[0] *= 2
				c[j][0] = 0
				cur = c[j]
				j = 0
				continue
			else:
				cur = c[j]

			j += 1
		vs = map(lambda x: x[0], filter(lambda x: x[0] != 0, c))
		if len(vs) == 4:
			return False
		
		vs.reverse() #so that popping the first value.
		for cur in c:
			if len(vs) == 0:
				cur[0] = 0
			else:
				cur[0] = vs.pop()

		return True
	
	def check_down(self, c):
		cur = [-1]
		j = 3
		while j >= 0:
			if c[j][0] == 0:
				j -= 1
				continue
			if cur[0] == c[j][0]:
				cur[0] *= 2
				c[j][0] = 0
				cur = c[j]
				j = 3
				continue
			else:
				cur = c[j]
			j-=1
		vs = map(lambda x: x[0], filter(lambda x: x[0] != 0, c))
		if len(vs) == 4:
			return False
		for cur in c[-1::-1]:
			if len(vs) == 0:
				cur[0] = 0
			else:
				cur[0] = vs.pop()
		return True
	
	def shift_up(self):
		flg = False
		flg = self.check_up(self.c0) or flg
		flg = self.check_up(self.c1) or flg
		flg = self.check_up(self.c2) or flg
		flg = self.check_up(self.c3) or flg
		return flg
	def shift_down(self):
		flg = False
		flg = self.check_down(self.c0) or flg
		flg = self.check_down(self.c1) or flg
		flg = self.check_down(self.c2) or flg
		flg = self.check_down(self.c3) or flg
		return flg
	def shift_left(self):
		flg = False
		flg = self.check_up(self.r0) or flg
		flg = self.check_up(self.r1) or flg
		flg = self.check_up(self.r2) or flg
		flg = self.check_up(self.r3) or flg
		return flg
	def shift_right(self):
		flg = False
		flg = self.check_down(self.r0) or flg
		flg = self.check_down(self.r1) or flg
		flg = self.check_down(self.r2) or flg
		flg = self.check_down(self.r3) or flg
		return flg
	
	def play(self):
		self.generate()
		self.generate()
		self.show()
		while True:
			d = raw_input()
			if d == 'w':
				if self.shift_up():
					self.generate()
			elif d == 's':
				if self.shift_down():
					self.generate()
			elif d == 'a':
				if self.shift_left():
					self.generate()
			elif d == 'd':
				if self.shift_right():
					self.generate()
			#os.system('cls')
			self.show()
	
	def show(self):
		for r in xrange(4):
			for c in xrange(4):
				print '%d '%self.board[r*4+c][0],
			print
		
if __name__ == '__main__':
	gb = GameBoard()
	gb.play()

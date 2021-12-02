class Submarine:
    depth = 0
    position = 0
    aim = 0

    def down(self, i):
        self.aim += i
    
    def up(self, i):
        self.aim -= i

    def forward(self, i):
        self.position += i
        self.depth += self.aim * i

    def final_position(self):
        return self.depth * self.position

f = open('input-2.csv','r')
lines = f.readlines()

sub = Submarine()

for line in lines:
    direction, distance = line.split(' ')
    print('direction {} with distance {}'.format(direction,int(distance)))
    if direction == 'forward':
        sub.forward(int(distance))
    elif direction == 'down':
        sub.down(int(distance))
    elif direction == 'up':
        sub.up(int(distance))

print(sub.final_position())
    

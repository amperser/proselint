"""Run the demo."""

from subprocess import Popen, PIPE

p0 = Popen(["cat", "proselint/demo.md"], stdout=PIPE)
p1 = Popen(["proselint", "--stdin"], stdin=p0.stdout, stdout=PIPE)
p0.stdout.close()
p2 = Popen(["proselint", "--demo"], stdout=PIPE)

output1 = [line.split(':')[1:] for line in p1.communicate()[0].decode().split('\n')]
output2 = [line.split(':')[1:] for line in p2.communicate()[0].decode().split('\n')]

assert(output1 == output2)


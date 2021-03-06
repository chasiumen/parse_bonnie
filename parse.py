#!/usr/bin/python

import subprocess


#execute shell command
def ex(cmd):
    p =subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out.rstrip()


####Variables######
HOST=ex('hostname')
infile = HOST + '.out'
base = 'cat ' + infile

grep1 = '| grep -i ' + HOST + '| head -1 | '
grep2 = '| grep -i latency' + '| head -1 | '


#seq out base_command
seq_out = base + grep1
seq_lat = base + grep2
#seq_out commands
cout_perch=seq_out + 'awk \'{print $3 }\' ' 
cout_block=seq_out + 'awk \'{print $5 }\' '
cout_rw=seq_out + 'awk \'{print $7 }\' '


cout_percha_lat=seq_lat + 'awk \'{print $2 }\' '
cout_block_lat=seq_lat + 'awk \'{print $3 }\' '
cout_rw_lat=seq_lat + 'awk \'{print $4 }\' '

#seq in commands
cin_perch=seq_out + 'awk \'{print $9 }\' ' 
cin_block=seq_out + 'awk \'{print $11 }\' '

cin_percha_lat=seq_lat + 'awk \'{print $5 }\' '
cin_block_lat=seq_lat + 'awk \'{print $ 6}\' '

#bonnie test
mem1='16384'
mem2='1024'

print "Checking hostanme..."
if HOST == 'h1':
    print HOST + ' ['+ mem1 + ']'
    print "Benchmark test starts...."
    bonnie ='bonnie -d /tmp -r ' + mem1 + ' > ' + infile
    ex(bonnie)
    print "Benchmark completed"
else:
    print HOST + ' ['+ mem2 + ']'
    print "Benchmark test starts...."
    bonnie ='bonnie -d /tmp -r ' + mem2 + ' > ' + infile
    ex(bonnie)
    print "Benchmark completed"

print "parsing...."
#RUN COMMANDS#
#seq out char
out_cha=ex(cout_perch)
out_cha_lat=ex(cout_percha_lat)
#seq block
out_block=ex(cout_block)
out_block_lat=ex(cout_block_lat)
#seq w/r
out_wr=ex(cout_rw)
out_wr_lat=ex(cout_rw_lat)


#seq in char
in_cha=ex(cin_perch)
in_cha_lat=ex(cin_percha_lat)
#seq in block
in_block=ex(cin_block)
in_block_lat=ex(cin_block_lat)


### OUTPUT ###


print HOST
print out_cha
print out_cha_lat
print out_block
print out_block_lat

#seq w/r
print out_wr
print out_wr_lat

#seq in char
print in_cha
print in_cha_lat

#seq in block
print in_block
print in_block_lat




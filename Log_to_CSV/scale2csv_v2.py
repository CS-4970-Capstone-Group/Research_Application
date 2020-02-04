#!/usr/bin/python
#Code created by Noah Marchal and edited by Brad Boutaugh
import sys
import os
import os.path
import struct 

print("")

print("This tool converts scale log files into CSV files.")


file_struct_fmt = '=III' # int, int, int
file_struct_len = struct.calcsize(file_struct_fmt)
file_struct_unpack = struct.Struct(file_struct_fmt).unpack_from

entry_struct_fmt = '=bIII' # int[5], float, byte[255]
entry_struct_len = struct.calcsize(entry_struct_fmt)
entry_struct_unpack = struct.Struct(entry_struct_fmt).unpack_from

file_magic = 0xa2ea54c1
BCG_novalue = 0xffffffff

#timerHz = 32.8
#timerHz = 30629.13907289332
timerHz = 33492.3494619704


#if len(sys.argv) != 2:
#    print("Usage: scale2csv.py [filename]")
#    sys.exit(0)
#
#Apply the local directory for which this program is located in your system
#Example r"C:\Users\brad\My_Dir"
directory = r""
for filename in os.listdir(directory):
    if filename.endswith(".LOG"):
        #filename = sys.argv[1]
        #filename="REC0.LOG"

        if not os.path.isfile(filename):
            print("File doesn't exist: " + filename)


        outfilename = filename + ".csv"

        outfile = open(outfilename, "w+")




        results = []
        with open(filename, "rb") as infile:
            data = infile.read(file_struct_len)
            if not data:
                sys.exit(0)
            s = file_struct_unpack(data)
        #    print s


            if s[0] != file_magic:
                print("invalid file?")
                sys.exit(0)

            outfile.write("\"start time\", %d\n" % s[1])
            outfile.write("\"stop time\", %d\n" % s[2])

            outfile.write("\"Time (s)\",\"BCG\",\"ECG ch1\",\"ECG ch2\"\n")


            reconstructedTimer = 0
            lastTimer = 0
            while True:
                data = infile.read(entry_struct_len)
                if not data: break
                s = entry_struct_unpack(data)
                results.append(s)
        #        print "  " + str(s)
                print("  " + str(s))

                timerIncrease = (s[0] - lastTimer) % 256
                reconstructedTimer += timerIncrease



                if s[1] == BCG_novalue:
                    outfile.write("%f," ",%d,%d\n" % (reconstructedTimer/timerHz,s[2],s[3]) )
                else:
                    outfile.write("%f,%d,%d,%d\n" % (reconstructedTimer/timerHz,s[1],s[2],s[3]) )

                lastTimer = s[0]

        outfile.close()
        


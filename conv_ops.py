# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  script will determine output shape and operation ocunt of a convolution layer
# Parameters:
# c_in: input channel count
# h_in : input height count
# w_in :input width count
# n_filt : number of filters in the covolution layer 
# h_filt : filter height count
# w_filt : filter width count 
# s : stride of covolution filters
# p: amount of padding on each of the four input map sides 
# Output:
#  outputs channel count, height count, width count, number of additions performed, number of multiplications performed, number of divisions performed
#
# Written by Anushka Devarajan
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137

# helper functions

# initialize script arguments
c_in= float('nan') #input channel count
h_in = float('nan') #input height count
w_in = float('nan') #input width count
n_filt =float('nan') # number of filters in the covolution layer 
h_filt = float('nan') #filter height count
w_filt = float('nan') #filter width count 
s = float('nan') #stride of covolution filters
p = float('nan') #amount of padding on each of the four input map sides 

# parse script arguments
if len(sys.argv)==9:
    c_in= float(sys.argv[1])
    h_in= float(sys.argv[2])
    w_in= float(sys.argv[3])
    n_filt=float(sys.argv[4])
    h_filt = float(sys.argv[5])
    w_filt = float(sys.argv[6])
    s = float(sys.argv[7])
    p = float(sys.argv[8])
else:
   print(\
    'Usage: '\
    'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
   )
   exit()


# write script below this line
c_out= n_filt
h_out = (h_in+2*p-h_filt)/s + 1
w_out = (w_in+2*p -w_filt)/s +1
adds= n_filt*h_out*w_out*c_in*h_filt*w_filt
muls= n_filt*h_out*w_out*c_in*h_filt*w_filt
divs=0


#outputs
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
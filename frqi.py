from helper_funcs import *
from qiskit import QuantumCircuit

def cFRQI(a,compression):
    a = convertToAngles(a,1) # convert grayscale to angles
    
    n = len(a)
    k = ilog2(n)
    
    a = 2*a 
    a = sfwht(a)
    a = grayPermutation(a) 
    
    idx = list(range(0,n))
    
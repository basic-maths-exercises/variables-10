import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_arrayValues(self) : 
       for j in range(11) : 
          self.assertTrue( timesTable[j]==j*table, "One of more of the values in the timesTable array has not been set correctly" )
          
    def test_variablesExist(self) : 
       self.assertTrue( "table" in globals(), "no variable called table has been defined" )
       self.assertTrue( "timesTable" in globals(), "no variable called timesTable has been defined" )
       self.assertTrue( len(timesTable)==11, "the timesTable array has the wrong length" )
       
   def test_variable_used(self) : 
       self.assertTrue( "i" in globals(), "the loop vairable must be called i" )
       self.assertTrue( i==10, "the loop variable must be called i" )

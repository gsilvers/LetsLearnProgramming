import unittest
from ..linked_list import linked_list
import io
import sys

class Test_TestLinkedList(unittest.TestCase):
    def test_constructor_works(self):
        test_list = linked_list()

    def test_empty_list(self):
        test_list = linked_list()
        test_list.size = 0
    
    def test_add_one_node(self):
        test_list = linked_list()
        test_list.add('Greg')
        assert(test_list.has('Greg') == 1)
    
    def test_add_two_node(self):
        test_list = linked_list()
        test_list.add('Greg')
        test_list.add('Sierra')
        assert(test_list.has('Greg') == True)
        assert(test_list.has('Sierra') == True)
        assert(test_list.has('Molly') == False)

    def test_print(self):
        expected_value = """ROOT
Greg
Sierra
"""
        test_list = linked_list()
        test_list.add('Greg')
        test_list.add('Sierra')
        captured_output = io.StringIO() 
        sys.stdout = captured_output  
        test_list.list_print()
        sys.stdout = sys.__stdout__ 
        print("testval")
        print(captured_output.getvalue())
        print("expected val")
        print(expected_value)
        assert(captured_output.getvalue() == expected_value)
        

if __name__ == '__main__':
    unittest.main()
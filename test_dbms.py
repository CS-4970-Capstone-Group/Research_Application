import research_dbms as db
import pytest
import unittest
# coding=utf-8

class TestClass:
    def test_insert(self):
        assert db.Research_DBMS.insert_person(self,'Qisheng','160','80','30','110','69','Asia','Male','True','True') == 1
    
    def test_wrong_input(self):
        assert db.Research_DBMS.insert_person(self,1,2,'80','30','110','69','Asia','Male','True','True') == 0
    
    def test_correct_search(self):
        assert db.Research_DBMS.search_person(self, '1017') == 1
    
    def test_invalid_search(self):
        assert db.Research_DBMS.search_person(self,1017)== -1
    
    def test_delete_correct(self):
        assert db.Research_DBMS.delete_person(self,'1017') ==1
    
    def test_delete_invalid(self):
        assert db.Research_DBMS.delete_person(self,1017) == -1
    
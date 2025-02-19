# Copyright (c) 2025, Salman Sami Khan and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase
from frappe.tests.utils import FrappeTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class TestLibraryMember(FrappeTestCase):
    def test_full_name_correctly_set(self):
        test_member = frappe.new_doc("Library Member")
        test_member.first_name = 'John'
        test_member.last_name = 'Doe'
        test_member.save()
        
        self.assertEqual(test_member.full_name, 'John Doe')

class UnitTestLibraryMember(UnitTestCase):
	"""
	Unit tests for LibraryMember.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestLibraryMember(IntegrationTestCase):
	"""
	Integration tests for LibraryMember.
	Use this class for testing interactions between multiple components.
	"""

	pass

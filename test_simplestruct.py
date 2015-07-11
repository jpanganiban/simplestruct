# -*- coding: utf-8 -*-
import unittest
import simplestruct as structs


class StructTestCase(unittest.TestCase):

    def test_class(self):
        class Type(structs.Struct):
            pass

        self.assertIsNotNone(Type)
        self.assertIsNotNone(Type())

    def test_instantiation_correct_value_type(self):

        class Type(structs.Struct):
            id = int

        self.assertEqual(Type(id=1).id, 1)

    def test_instantiation_incorrect_value_type(self):

        class Type(structs.Struct):
            id = int

        with self.assertRaises(TypeError):
            Type(id="1")

    def test_instantiation_None_type(self):

        class Type(structs.Struct):
            id = int

        self.assertIsNone(Type(id=None).id)

    def test_instance_setter_correct_value_type(self):

        class Type(structs.Struct):
            id = int

        t = Type()
        t.id = 1

        self.assertEqual(t.id, 1)

    def test_instance_setter_None(self):

        class Type(structs.Struct):
            id = int

        t = Type()
        t.id = None

        self.assertIsNone(t.id)

    def test_instance_setter_incorrect_value_type(self):

        class Type(structs.Struct):
            id = int

        t = Type()

        with self.assertRaises(TypeError):
            t.id = "1"

    def test_compound_type_correct_value_type(self):

        class Address(structs.Struct):
            country = str

        class Person(structs.Struct):
            address = Address

        a = Address(country="PH")
        p = Person(address=a)

        self.assertEqual(p.address, a)
        self.assertEqual(p.address.country, "PH")

    def test_compound_type_incorrect_value_type(self):

        class Address(structs.Struct):
            country = str

        class Person(structs.Struct):
            address = Address

        with self.assertRaises(TypeError):
            Person(address="PH")

    def test_compound_type_None_value(self):

        class Address(structs.Struct):
            country = str

        class Person(structs.Struct):
            address = Address

        self.assertIsNone(Person(address=None).address)

    def test_composite_correct_value_type(self):

        class Person(structs.Struct):
            sibling_names = [str]

        Person(sibling_names=["peter", "mary", "john"])

    def test_composite_incorrect_value_type(self):

        class Person(structs.Struct):
            sibling_names = [str]

        with self.assertRaises(TypeError):
            Person(sibling_names=[1, 2, 3])

    def test_composite_no_type(self):

        class Person(structs.Struct):
            stuff = []

        Person(stuff=[1, "jesse", 2, {}])

    def test_composite_struct_correct_value_type(self):

        class Address(structs.Struct):
            country = str

        class Person(structs.Struct):
            addresses = [Address]

        Person(addresses=[Address(country="PH"), Address(country="US")])

    def test_composite_struct_incorrect_value_type(self):

        class Address(structs.Struct):
            country = str

        class Person(structs.Struct):
            addresses = [Address]

        with self.assertRaises(TypeError):
            Person(addresses=["PH", "US"])

    def test_type_tuple_correct_value_type(self):

        class Person(structs.Struct):
            age_and_gender = (int, str)

        Person(age_and_gender=(24, "M"))

    def test_type_tuple_incorrect_value_type(self):

        class Person(structs.Struct):
            age_and_gender = (int, str)

        with self.assertRaises(TypeError):
            Person(age_and_gender=(24, 12312))

    def test_type_tuple_None_value(self):

        class Person(structs.Struct):
            age_and_gender = (int, str)

        self.assertIsNone(Person(age_and_gender=None).age_and_gender)

    def test_type_tuple_partial_None_value(self):

        class Person(structs.Struct):
            age_and_gender = (int, str)

        self.assertEqual(
            Person(age_and_gender=(21, None)).age_and_gender,
            (21, None)
        )

    def test_type_list_just_list(self):

        class Person(structs.Struct):
            stuff = list([str])

        self.assertEqual(
            Person(stuff=["a", "b", 1]).stuff,
            ["a", "b", 1]
        )

if __name__ == "__main__":
    unittest.main()

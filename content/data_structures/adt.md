Title: Abstract Data Types vs Data Structures
Date:   2014-09-19
Category: DataTypes
Tags: datastructures,meta,datatypes,basics
Slug: adt
Authors: rixx
Summary: Abstract Data Types are not the same as Data Structures, and understanding this difference is important for understanding of the following articles detailling data types, data structures and their implementations.

**tl;dr:** ADT: definition of a stack as `data + push + pop + peek`. Data Structure: implementation of a stack as `linked list + push() + pop() + peek()`.

There is a difference between ADT (abstract data types) and data structures. Understanding it is necessary for getting the following articles about both abstract data structures and data types.

## Abstract Data Types
*Abstract Data Types* are defined by actions that may be performed on them. They are only a model of data objects and their methods. You could think of it as an interfaces (in Java terminology). 

One ADT may easily have a dozen different implementations. They might differ only in the implementation of an algorithm, or use completely different data structures.

**Examples:** A list is an ADT, commonly defined by the actions `insert`, `get` and `delete` (phrasing may differ). Another ADT is the stack, defined by the operations `push`, `pop` and sometimes `peek`.

## Data Structures
*Data Structures* are ways of organizing data so that it may be used efficiently. Data structures paired with the necessary functions or methods can serve as implementation for an ADT. Data Structures in popular programming languages include for example strings, integers, lists, dictionaries and floats.

**Examples:** A linked list can be an implementation of a list or a stack, depending on the corresponding methods.



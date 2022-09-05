<center>
<img src="image.jpeg">
</center>

# Fundamentals of Programming Languages

[Syllabus](docs/syllabus.pdf)

<!--
NOTES:
* do type stuff in C
* move grammar and implementation stuff to the end of the course with prolog semantics
* move functional programming after Asteroid types
* nice material on python gc: https://stackify.com/python-garbage-collection/
-->

## Introduction

#### Why study programming languages?
* Communalities/differences
* Programming paradigms
* Language evolution/design

#### Meet our languages:
* Asteroid - Object-Based, Imperative, Functional
* Prolog - Logic

#### Lecture Notes
* [Intro & Language Classes](notes/csc301-ln001.pdf)



## Programming & Types

#### Asteroid
* The basics
* **Lecture Notes**:
  * [Asteroid Basics](notes/csc301-ln002.pdf)

#### Types and Type Systems
* Type checking
    * static vs dynamic
* Type hierarchies
* Type inference
* **Lecture Notes**:
    * [Types](notes/csc301-ln003.pdf)

#### Exploring more of Asteroid's Types
* Primitive types
* Lists & Tuples
* Constructed types
* **Lecture Notes**:
    * [Asteroid Types](notes/csc301-ln004.pdf)

#### Functional Programming with Asteroid
* Functional programming is defined by two things:
    * Programs consist of recursive definitions of functions
    * Functions are first-class citizens of the language
* Pattern matching - A functional programming invention
    * Lists & Tuples
    * Constructed data types
* Special Patterns
    * Wild card patterns
    * Constraint patterns
    * Type match patterns
    * Conditional patterns
* Multi-dispatch with pattern matching
    * A declarative way to think about function definitions
* Recursion
    * Recursion on lists
* Higher-order programming - Another functional programming invention
    * The `lambda` function
    * `map` and `reduce`
    * Function currying
        * working with partially evaluated functions
* **Lecture Notes**
    * [Pattern Matching](notes/csc301-ln013.pdf)
    * [Higher-Order Programming](notes/csc301-ln014.pdf)

#### Polymorphism
* Ad-hoc polymorphism
* Subtype polymorphism
* Parametric polymorphism
* Duck typing
* **Lecture Notes**:
   * [Polymorphism](notes/csc301-ln019.pdf)

#### Logic Programming with Prolog
* First-order logic
  * Predicates and quantification
  * Modus ponens
* Logic programs
  * Facts and rules
  * Proof trees
  * Arithmetic
  * IO
* **Lecture Notes**:
  * [Logic as a Programming Language](notes/csc301-ln020.pdf)
  * [Rules](notes/csc301-ln021.pdf)
  * [Arithmetic & I/O](notes/csc301-ln022.pdf)
  * [Advanced Concepts](notes/csc301-ln023.pdf)



## Memory

#### Parameter passing
* Pass by value
* Pass by reference
* **Lecture Notes**:
   * [Parameter Passing](notes/csc301-ln018.pdf)

#### Recursion
* How do programming language implement recursive functions?
* The runtime stack and stack frames
   * Using a debugger to look at the runtime stack
* **Lecture Notes**:
   * [Stack & Frames](notes/csc301-ln016.pdf)

#### Memory management
* Typical process memory
* Explicit Memory Management vs. Garbage Collection
* **Lecture Notes**:
   * [Process Memory & Memory Management](notes/csc301-ln017.pdf)



## Theory and Implementation

#### Language specification
* Programming Language Specification
    * Syntax
       * Grammars
       * Ambiguous grammars
       * Parse tree/derivation trees
    * Semantics
       * Interpretations of the parse tree
* **Lecture Notes**:
    * [Formal Language Specification](notes/csc301-ln009.pdf)
    * [Grammars in Action](notes/csc301-ln010.pdf)
    * [Grammars & Semantics](notes/csc301-ln011.pdf)

#### Programming Language Implementation
* Interpreters vs Compilers
* Lexical Analysis
    * Lex
* Syntax Analysis
   * Yacc
   * Recursive descent parsing
* Example: a simple calculator language
* **Lecture Notes**:
  * [Programming Language Implementation](notes/csc301-ln012.pdf)

#### Formal semantics
* Semantics via abstract interpretation
  * Operational semantics
  * Building abstract interpreters using Prolog
* **Lecture Notes**:
  * [Simple Operational Semantics](notes/csc301-ln024.pdf)
  <!-- * [The Semantics of Variables](notes/csc301-ln025.pdf) -->


These lecture notes are released under the [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode)

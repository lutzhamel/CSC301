# CSC301 - Fundamentals of Programming Languages

1. Why study [programming languages](https://en.wikipedia.org/wiki/Programming_language)?
    * Communalities/differences
    * [Programming paradigms](https://en.wikipedia.org/wiki/Programming_paradigm)
    * Language evolution/design
    * Meet our languages:
        * [Asteroid](https://www.asteroid-lang.org) - Object-Based, Imperative, Functional
        * [Prolog](https://www.swi-prolog.org) - Logic
    * **Lecture Notes**:
        * [Intro & Language Classes](notes/csc301-ln001.pdf)
1. [Asteroid](https://github.com/lutzhamel/asteroid)
    * [The basics](https://github.com/lutzhamel/asteroid/blob/master/Asteroid%20User%20Guide.md)
    * **Lecture Notes**:
        * [Asteroid Basics](notes/csc301-ln002.pdf)
1. Interlude - [Types and type systems](https://en.wikipedia.org/wiki/Type_system)
    * Type checking
        * static vs dynamic
    * Type hierarchies
    * Type inference
    * **Lecture Notes**:
        * [Types](notes/csc301-ln003.pdf)
1. More on [Rust](https://www.rust-lang.org)
    * [Objects and traits](https://en.wikipedia.org/wiki/Trait_(computer_programming))
    * [Generics](https://en.wikipedia.org/wiki/Generic_programming)
    * [Pattern matching](https://en.wikipedia.org/wiki/Pattern_matching) oriented programming
    * The Rust standard library: [std](https://doc.rust-lang.org/std/index.html)
        * Strings
        * I/O
    * [Higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function)
    * [Iterators](https://en.wikipedia.org/wiki/Iterator) (internal/external)
    * **Lecture Notes**:
        * [Objects and Traits](notes/csc301-ln004.pdf)
        * [Generics](notes/csc301-ln005.pdf)
        * [Pattern Matching](notes/csc301-ln006.pdf)
        * [The Standard Library](notes/csc301-ln007.pdf)
        * [Higher-Order Functions & Iterators](notes/csc301-ln008.pdf)
1. Interlude - Language specification & Implementation
    * [Programming Language Specification](https://en.wikipedia.org/wiki/Programming_language_specification)
        * [Syntax](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
           * [Grammars](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Grammars)
           * [Ambiguous grammars](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Ambiguity)
           * [Parse tree/derivation trees](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Parsing)
        * [Semantics](https://en.wikipedia.org/wiki/Semantics_(computer_science))
           * Interpretations of the parse tree
    * [Programming Language Implementation](https://en.wikipedia.org/wiki/Programming_language_implementation)
        * Interpreters vs Compilers
        * [Lexical Analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
            * [Lex](https://en.wikipedia.org/wiki/Lex_(software))
        * [Syntax Analysis](https://en.wikipedia.org/wiki/Parsing)
           * [Yacc](https://en.wikipedia.org/wiki/Yacc)
           * [Recursive descent parsing](https://en.wikipedia.org/wiki/Recursive_descent_parser)
        * Example: a [simple calculator language](https://en.wikipedia.org/wiki/Bc_(programming_language))
    * **Lecture Notes**:
        * [Formal Language Specification](notes/csc301-ln009.pdf)
        * [Grammars in Action](notes/csc301-ln010.pdf)
        * [Grammars & Semantics](notes/csc301-ln011.pdf)
        * [Programming Language Implementation](notes/csc301-ln012.pdf)
1. Haskell
      * The Basics
         * [Getting Started](https://en.wikibooks.org/wiki/Haskell/Getting_set_up)
         * [Variables and Functions](https://en.wikibooks.org/wiki/Haskell/Variables_and_functions)
         * [Truth Values](https://en.wikibooks.org/wiki/Haskell/Truth_values)
         * [Type Basics](https://en.wikibooks.org/wiki/Haskell/Type_basics)
         * [Lists and Tuples](https://en.wikibooks.org/wiki/Haskell/Lists_and_tuples)
         * [Type Basics II](https://en.wikibooks.org/wiki/Haskell/Type_basics_II)
         * [I/O](http://book.realworldhaskell.org/read/io.html)
      * Diving a Bit Deeper
         * [Recursion](https://en.wikibooks.org/wiki/Haskell/Recursion)
         * [Lists II (map)](https://en.wikibooks.org/wiki/Haskell/Lists_II)
         * [Lists III (folds, comprehensions)](https://en.wikibooks.org/wiki/Haskell/Lists_III)
         * [Type Declarations](https://en.wikibooks.org/wiki/Haskell/Type_declarations)
         * [Pattern matching](https://en.wikibooks.org/wiki/Haskell/Pattern_matching)
         * [Control structures](https://en.wikibooks.org/wiki/Haskell/Control_structures)
      * **Lecture Notes**:
         * [Basics](notes/csc301-ln013.pdf)
         * [Lists and Tuples](notes/csc301-ln014.pdf)
         * [Functions](notes/csc301-ln015.pdf)
1. Interlude - [Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
    * How do programming language implement recursive functions?
    * The runtime stack and stack frames
       * Using a debugger to look at the runtime stack
    * **Lecture Notes**:
       * [Stack & Frames](notes/csc301-ln016.pdf)
1. Interlude - [Memory management](https://en.wikipedia.org/wiki/Memory_management)
    * Typical process memory
    * Explicit Memory Management vs. Garbarge Collection
    * [Parameter passing](https://courses.cs.washington.edu/courses/cse341/98sp/general/parameters.html)
       * Pass by value
       * Pass by reference
    * **Lecture Notes**:
       * [Process Memory & Memory Management](notes/csc301-ln017.pdf)
       * [Parameter Passing](notes/csc301-ln018.pdf)
1. Interlude - [Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
    * Ad-hoc polymorphism
    * Subtype polymorphism
    * Parametric polymorphism
    * Duck typing
    * **Lecture Notes**:
       * [Polymorphism](notes/csc301-ln019.pdf)
1. [Prolog](https://en.wikipedia.org/wiki/Prolog)
    * [First-order logic](https://en.wikipedia.org/wiki/First-order_logic)
      * [Predicates](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic)) and [quantification](https://en.wikipedia.org/wiki/Quantifier_(logic))
      * [Modus ponens](https://en.wikipedia.org/wiki/Modus_ponens)
    * [Logic programs](https://en.wikipedia.org/wiki/Logic_programming)
      * Facts and rules
      * Proof trees
      * Arithmetic
      * IO
    * **Lecture Notes**:
      * [Logic as a Programming Language](notes/csc301-ln020.pdf)
      * [Rules](notes/csc301-ln021.pdf)
      * [Arithmetic & I/O](notes/csc301-ln022.pdf)
      * [Advanced Concepts](notes/csc301-ln023.pdf)
1. Interlude - Formal semantics
    * Semantics via abstract interpretation
      * Operational semantics
    * Building abstract interpreters using Prolog
1. Semester Review

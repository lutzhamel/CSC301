# CSC301 - Foundations of Programming Languages

1. Why study [programming languages](https://en.wikipedia.org/wiki/Programming_language)?
    * Communalities/differences
    * [Programming paradigms](https://en.wikipedia.org/wiki/Programming_paradigm)
    * Language evolution/design
    * Meet our languages:
        * [Rust](https://www.rust-lang.org) - OO/Imperative
        * [Haskell](https://www.haskell.org) - Functional
        * [Prolog](https://www.swi-prolog.org) - Logic
    * **Lecture Notes**:
        * [Intro & Languages Classes](notes/csc301-ln001.pdf)
1. [Rust](https://www.rust-lang.org)
    * [The basics](https://stevedonovan.github.io/rust-gentle-intro/1-basics.html)
    * **Lecture Notes**:
        * [Rust Basics](notes/csc301-ln002.pdf)
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
1. Interlude - [Language specification](https://en.wikipedia.org/wiki/Programming_language_specification)
    * Syntax
        * Grammars
        * Parse tree/derivation trees
    * Semantics
        * interpretations of the parse tree
    * Ambiguous grammars
    * Building language Processors
        * Lexical analysis
        * Recursive descent parsing
        * Adding actions
        * Example: a simple calculator language
1. Interlude - Language Tools
    * Tool chains
    * Interpreters vs compilers
    * Debuggers
1. Interlude - Memory management
    * Typical process memory
    * Parameter passing
      * Pass by value
      * Pass by reference
1. Haskell
    * Lists and tuples
    * Types and type classes
    * Functions and pattern matching
    * Let, where, and case
    * Recursion/thinking recursively
    * Higher order functions (mapping)
    * Algebraic data types
    * Functional IO
1. Interlude - Recursion
    * How do programming language implement recursive functions?
    * The runtime stack and stack frames
      * Using a debugger to look at the runtime stack
1. Interlude - Polymorphism
    * Duck typing
    * Subtype polymorphism
    * Parametric polymorphism
1. Prolog
    * First-order logic
      * Predicates and quantification
      * Modus ponens
    * Logic programs
      * Facts and rules
    * Querying/executing a program
      * Proof trees
    * Arithmetic
    * IO
1. Interlude - Scoping
    * scoping rules
    * name spaces
    * static vs. dynamic scoping
1. Interlude - Formal semantics
    * Semantics via abstract interpretation
      * Operational semantics
    * Building abstract interpreters using Prolog
1. Semester Review

# zksdk

This repository is for the project of building a zero-knowledge sdk

## Problem Statement

> Recent break-throughs allow the use of zero-knowledge proofs to protect sensitive data and therefore mitigate multiple security risks. They are not widely utilised because there exists no simple interface which allows non-expert software developers to utilise these assertions in their applications.

~~Recent break-throughs allow the use of zero-knowledge proofs in real-world applications. Such proofs can assert the correctness of a computation while keeping the data hidden. Yet, zero-knowledge proofs are _currently_ not widely utilised because there exists no simple interface which allows non-expert (security) software developers to utilise these assertions in their applications.~~
  
## Solution

> We develop a simple and universal interface that allows any non-expert software developer to include assertions of zero-knowledge in their applications. This interface allows interchangeable access to our highly optimised ZK libraries as well as existing libraries.

~~We develop a simple interface that allows any non-expert software developer to include assertions of zero-knowledge in their applications. As such, this interface allows the connection to existing ZK libraries without *any* cryptographic / security knowledge.~~ 

~~We develop a simple, easy-to-use API/SDK that allows a software developer to include zero-knowledge proofs in their applications.~~

'simple' --> Use without expert knowledge
'universal' --> Support of wide range of programming lanuages

 ### What exactly do we want to build?
 
 API, SDK, Libraries, Products
 
 #### Short Term - MVP

  API --- interface to existing libraries
 
 ##### Features
  * Support of a small range of programming languages
      - C, C++, Go
  * Utilising existing ZK libraries
  * Restricted set of operations ('specialised') 
  * Non-optimised
  * Non-production code ('proof of concept') 
 
 ##### Market Monopolisation
   * Security Professionals
   * Blockchain
 
 #### Long Term
 
  SDK --- software development kits 
 
  ##### Features
   * Support of a wide range of programming languages
   * Building our own ZK libraries
   * 'universal' computations
   * Highly optimised
   * Secure software programming 
     - certified, standardised
     - side-channel security
     - secure under sql injections, buffer overflows, path traveral attacks, integer overflow attacks, ...
 
  ##### Market Monopolisation
   * Any software programmer
   * Any software field/area

## One Liners

  * Zero-Knowledge Proofs --- Now accessible for everyone 
  * Zero. Knowledge. Proofs. We turned the impossible into something super simple.
  * Zero-Knowledge Proofs --- Now, super simple
  * Zero-Knowledge Proofs --- Complex? Now, super simple!
  
## Customer Development
  
## License 

Learning result: software developers (security minded) want to see the code they are working on

  * Common Creatives: Non-Disclosure License (CC NC) --- restricts the use of the software to non-commercial use
      - pitfalls: someone may release a non-commercial product using our sdk
    
  * Open-sourced limited versions (closed-source of the rest of the library)
     a) limiting efficiency
     b) open-sourcing only parts of the software - counter-intuitive?
     c) limiting functionality - closed-source of other functionality? 
      - pitfalls: doesn't necessarily solve the trust problem?

  * Black box model --- closed source
    - pitfalls: might hinder software developers from using the software; trust issues; outreach 

# Unknowns

## Stuff that isn't fully figured out just yet
* Package manager, maintaining, and deprecating
    * Should be in a way that makes it simple to install packages
    * Need maintenance and auditing to make packages official
* Creating linkable files
    * For now can just require all source files, but having some kind of archive format would be good for modifying a program after its release
    * Needs to respect access specifiers, guarantees, assumptions, and platform independence
* Exact memory management algorithm
    * Want to use arenas/bump pointers for extreme speed
    * Since the compiler should know a lot of information about the program at compile time, it should be able to leverage this to make memory management as quick as possible.
    * For now can just literally just malloc and free until a better algorithm is done





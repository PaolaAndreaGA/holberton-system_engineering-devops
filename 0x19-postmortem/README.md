# Postmortem

## Issue Summary

When we did the monty project in the first part we faced a series of failures since we were not very familiar with the concept we were going to implement, the instructions lacked relevant information for the overall development of the project.

## Timeline (all in PST)

1:00 P.M: Creation of the code in main.c , monty.h
3:00 P.M: Creation of add.c, freeoptions.c nop.c opcode.c pall.c
pint.c pop.c swap.c utilities.c
5:00 P.M: Verification of project operation and error in the libraries.
6:00 P.M: Review of possible solutions on Google, Stackoverflow and with peers from different cohorts.
8:00 P.M: Added _GNU_SOURCE and _POSIX_C_SOURCE 200809L and the Monty project worked without errors.

## Root Cause

### What does #define _gnu_source do?

If you define _GNU_SOURCE , you will get:  **access to lots of nonstandard GNU/Linux extension functions**.  **access to traditional functions which were omitted from the POSIX standard**  (often for good reason, such as being replaced with better alternatives, or being tied to particular legacy implementations)

### What does #define _POSIX_SOURCE mean?

It allows you to use functions that are not part of the standard C library but are part of the POSIX.1 (IEEE Standard 1003.1) standard. Using the macros described in  [feature_test_macros](http://man7.org/linux/man-pages/man7/feature_test_macros.7.html)  allows you to control the definitions exposed by the system header files.

As far as I know  `_POSIX_SOURCE`  is obsolete and you should use  `_POSIX_C_SOURCE`  instead.

For example, if you want to use  [`strndup`](https://linux.die.net/man/3/strndup), you have to use

## Correct and Preventative Measures

I believe that this problem would not have occurred if we had documented all the bugs and incompatibilities that the project had with the operating system with which we were working, since our version did not recognize some commands that were being handled in our code.
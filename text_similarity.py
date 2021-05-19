text_1 = """
Python is a high-level programming language designed to be easy to read and simple to implement.
 It is open source, which means it is free to use, even for commercial applications.
Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET
 virtual machines.
Python is considered a scripting language, like Ruby or Perl and is often used for 
creating Web applications and dynamic Web content. It is also supported by a number 
of 2D and 3D imaging programs, enabling users to create custom plug-ins and extensions
 with Python.
"""

text_2 = """
Python is an interpreted, object-oriented programming language similar to PERL, 
that has gained popularity because of its clear syntax and readability. 
Python is said to be relatively easy to learn and portable, meaning its statements can be
 interpreted in a number of operating systems, including UNIX-based systems, 
 Mac OS, MS-DOS, OS/2, and various versions of Microsoft Windows 98. Python was created
  by Guido van Rossum, a former resident of the Netherlands, whose favorite comedy 
  group at the time was Monty Python's Flying Circus. The source code is freely available
   and open for modification and reuse. Python has a significant number of users.
"""
# Plagiarism Checker
# Steps to be performed on both text
# 1. Tokenize(Split) text and convert all text to lower
# 2. Remove stopwords ('is','are','this','the','a','of','by'....)
# 3. Convert both text to set type of data
# 4. Calculate similarity using jaccard


def pre_process(text):
    tokens = text.lower().split()
    stopwords = ['a','as','are','by','of','this','the','that','was','is',
                 'in','it','for','at','to','be','on','also','has','been','and',
                 'its','can','often','with','use','used']
    words = []
    for token in tokens:
        if token not in stopwords:
            words.append(token)
    return set(words)

set_1 = pre_process(text_1)
set_2 = pre_process(text_2)

sim = len(set_1.intersection(set_2)) / len(set_1.union(set_2))
print(round(sim, 2) * 100)


prompt_template = """
You are an expert at creating questions based on coding materials and documentation.
Your goal is to prepare  a coder or a programmer for there exam and coding tests.
Your do this by asking questions  about the text below:

--------------
{text}
--------------

Create questions that will prepare the coders or programmers for their tests.
Make sure not to lose any important information

Questions:
"""

refine_template = (
    """
You are an expert at creating practice questions based on coding material and documentation
Your goal is to help a coder or programmer prepare for coding test.
We have received some practice questions to a certain extent: {existing_answer}.
We have the option to refine the exisiting questions or add new ones.
(Only if necessary) with some more context below.

----------------
{text}
----------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the orignial questions.
QUESTIONS:
"""
)
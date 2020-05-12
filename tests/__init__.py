import os

# TODO: get git_branch into this URL
USE_LOCAL_FILES = True
# This is based on the package bbeing located in shexSpec/grammar-python-antlr/tests
schemas_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'shexTest', 'schemas'))
if not os.path.exists(schemas_base) or not USE_LOCAL_FILES:
    schemas_base = "https://api.github.com/repos/shexSpec/shexTest/contents/schemas"
git_branch = 'extends'

print(f"***** Schema test base is {schemas_base} *****")
print(f"***** git test branch: {git_branch}*****\n")



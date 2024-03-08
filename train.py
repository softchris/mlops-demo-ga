import os

# skould train model with sklearn
print("training model")
# TBC, call to persist as file 

if not os.path.exists("dist"):
    os.makedirs("dist")

with open('dist/hello.model', 'w') as f:
    f.write('I contain model info')

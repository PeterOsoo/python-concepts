try:
    f = open('testfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception

# except IOError as e:
#     print('First!')
# except Exception as e:
#     print('Second')
except Exception as e:
    print('Sorry File does not exist!')

    # else runs code that need to be eecuted when there is an error
else:
    print(f.read())
    f.close()
    # finally will run no matter what happens
finally:
    print("Executing Finally...")

print('End of program')

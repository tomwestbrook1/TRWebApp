# imports ....
import cgi
import cgitb
cgitb.enable(display=0, logdir='./Files/log') # unsure on args at this point

# vars ....
form = cgi.FieldStorage()
searchItem = form.getvalue('txtinput')

open_file = open('./Files/outputs', 'a')

open_file.write("Hello World")
open_file.write(searchItem)
open_file.close()


"""
def main():
    print("Hello World")

# functions

if __name__ == "__main__": 
    main()

"""
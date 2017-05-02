"""The mighty TePADiM -- extremely a work in progress.
To do:
Tweak line generation function so the user can set some of the
variables!

Exception handling. We should probably start doing that now...

Q to Quit when creating new list instead of choosing source file

More candles!
"""

import time
from random import randrange
import os


done = False

print_wait_time = 0.05 / 4
pause_wait_time = 0.05

possible_lines = []


def printer(text, wait_time):
	for char in range(len(text)):
		print(text[char], end = "")
		time.sleep(wait_time)
	print()

def display_lists():
	list_path = os.path.join(os.path.dirname(__file__), "lists\\")
	print()
	print("The following lists are available:")
	for file in os.listdir(list_path):
		if file.endswith(".txt"):
			print(file)
	print()
	return False

def create_list():
	#print local text files
	print("Text files in local directory:")
	print()
	for file in os.listdir(os.path.dirname(__file__)):
		if file.endswith(".txt"):
			print(file)
	print()
	#Get the length of the file to be scraped
	source_file = input("Enter the name of the .txt file to use (including extension, using full path if not in local directory): ")
	mani_first = open(source_file, "r", encoding = "utf-8")
	mani_read = mani_first.read()
	mani_length = len(mani_read)
	mani_first.close()

	#Open it again to read it bit by bit to a list, each with a 'new line' char added
	manifesto = open(source_file, "r", encoding = "utf-8")
	our_list = []

	print()
	print("Processing text... this may take a while.")
	print("Await the dump with patience.") #variations on this? Little idea...
	for i in range(mani_length):
	    phrase = ""
	    chars_read = 0
	    while chars_read < 100: #arbitrary number - it should never reach 100 chars before reaching a space
	        current_char = manifesto.read(1)
	        if chars_read > 35 and current_char == " ": #this number is the point it starts looking for a breakpoint: this is the variable for the player to tweak. 35 is a good sweet spot!
	            break
	        else:
	            phrase += current_char
	            chars_read += 1
	    phrase = phrase.strip()
	    if phrase != "":
	        our_list.append(phrase + "\n")

	manifesto.close()

	print(our_list)
	print()
	print("List generated.")

	#Finally, write each line in the list to a new text file
	print()
	output_name = input("Enter a filename to save the new list (must end .txt): ")
	list_index = 0
	#generate the filename using os
	file_name = os.path.join(os.path.dirname(__file__), "lists\\" + output_name)
	final = open(file_name, "w", encoding = "utf-8")

	while list_index < len(our_list):
	    final.write(our_list[list_index])
	    list_index += 1

	final.close() #This needs to return you to the menu at the end! #needs to go back to menu at end
	print()
	print("List saved.")
	print()

def read_lines():
	done = False
	lines = read_line_input()

	while done == False:
		print()
		print("List added. Enter Y to add another, or anything else to continue:")
		user_input = input()
		if user_input.lower() == "y":
			lines = lines + read_line_input()
		else:
			done = True

	return lines

def read_line_input():
	lines = []
	print("Enter the filename of the source list (including .txt):")
	user_input = input()
	file_path = os.path.join(os.path.dirname(__file__), "lists\\" + user_input)
	line_file = open(file_path, "r", encoding = "utf-8") #Or type Q to return to menu! Will probably need to move input out of the open() function to do so...
	for line in line_file:
		line = line.rstrip("\n") #strip newline chars
		line += " " #add a space at the end
		lines.append(line)
	line_file.close()
	return lines

def paragraph_maker(mini, maxi):
	global possible_lines
	output = ""
	#input here for length tweak variable
	tweet_length = randrange(mini, maxi)
	while len(output) < tweet_length:
	    output += possible_lines[randrange(len(possible_lines))]
	return output

def divine():
	global possible_lines
	possible_lines = read_lines()
	print()
	mini = int(input("Enter minimum paragraph length in characters (TePADiM likes 20): "))
	maxi = int(input("Enter the maximum paragraph length in chacters (TePADiM likes 500): "))
	while True:
		print()
		user_input = input("Press return to generate or type Q to quit: ")
		if user_input.lower() == "q":
			print()
			return False
		else:
		    paragraph_to_print = paragraph_maker(mini,maxi)
		    paragraph_to_print = paragraph_to_print.strip() #strip trailing spaces
		    paragraph_to_print = paragraph_to_print.replace("  ", " ") #replace any double spaces with singles
		    print()
		    print(paragraph_to_print)

def candle():
	seed = randrange(3)
	print()
	if seed == 0:
		printer("    (", print_wait_time)
		printer("     )", print_wait_time)
		printer("    ()", print_wait_time)
		printer("   |--|", print_wait_time)
		printer("   |  |", print_wait_time)
		printer(" .-|  |-.", print_wait_time)
		printer(":  |  |  :", print_wait_time)
		printer(":  '--'  :", print_wait_time)
		printer(" '-....-'", print_wait_time)
		printer("", print_wait_time)
		printer("", print_wait_time)
	elif seed == 1:
		printer("  / (", print_wait_time)
		printer(" ( 6 )", print_wait_time)
		printer(" _`)'_", print_wait_time)
		printer("(  |  )", print_wait_time)
		printer("|`\"-\")|", print_wait_time)
		printer("|   ( )", print_wait_time)
		printer("|    (_)", print_wait_time)
		printer("|     |", print_wait_time)
		printer("|     |o!O", print_wait_time)
		printer("", print_wait_time)
		printer("", print_wait_time)
	elif seed == 2:
		printer("                   . . ...", print_wait_time)
		printer("                .:::'.`:::::.", print_wait_time)
		printer("               ::::::  '::::::", print_wait_time)
		printer("              :::::: J6  ::::::", print_wait_time)
		printer("              :::::  HMw  :::::", print_wait_time)
		printer("              :::::  WNM  :::::", print_wait_time)
		printer("              :::::: MAM ::::::", print_wait_time)
		printer("               :::::.`;'.:::::", print_wait_time)
		printer("                   KKKRRMMA", print_wait_time)
		printer("                   KPPPP9NM", print_wait_time)
		printer("                   K7IIYINN", print_wait_time)
		printer("                   Klll1lNJ", print_wait_time)
		printer("                   Klll1lNR", print_wait_time)
		printer("                   Kl::1lJl", print_wait_time)
		printer("                   L:::1:J", print_wait_time)
		printer("                   L:::!:J", print_wait_time)
		printer("                   L:::::l", print_wait_time)
		printer("                   l:..::l    dWn.", print_wait_time)
		printer("             ,nnnnml:...:lmncJP',", print_wait_time)
		printer("  :::::::;mCCCc'pdPl:...:l9bqPyj'jm;:::::::::::::::", print_wait_time)
		printer("  ::::::OPCCcc.9b::;.....;::dP ,JCC9O::::::::::::::", print_wait_time)
		printer("  ::::' 98CCccc.9MkmmnnnmmJMP.JacOB8P '::::::::::::", print_wait_time)
		printer("  :::    `9qmCcccc\"\"YAAAY\"\"roseCmpP'    :::::::::::", print_wait_time)
		printer("  :::.     ``9mm,...     ...,mmP''     .:::::::::::", print_wait_time)
		printer("  :::::..       \"YTl995PPPT77\"      ..:::::::::::::", print_wait_time)
		printer("  :::::::::...                 ...:::::::::::::::::", print_wait_time)
		printer("  ::::::::::::::::.........::::::::::::::::::::::::", print_wait_time)
		printer("", print_wait_time)
		printer("", print_wait_time)

def print_title():

	logo_outer = "***********"
	logo_inner = "* TePADiM *"

	print()
	printer("████████╗███████╗██████╗  █████╗ ██████╗ ██╗███╗   ███╗", print_wait_time)
	printer("╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║████╗ ████║", print_wait_time)
	printer("   ██║ora█████╗  ██████╔╝███████║██║  ██║██║██╔████╔██║", print_wait_time)
	printer("   ██║cul██╔══╝  ██╔═══╝ ██╔══██║██║  ██║██║██║╚██╔╝██║", print_wait_time)
	printer("   ██║ ar███████╗██║ meth██║od██║██████╔╝██║██║ ╚═╝ ██║", print_wait_time)
	printer("   ╚═╝   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝     ╚═╝", print_wait_time)
	print()

	printer(logo_outer, print_wait_time)
	printer(logo_inner, print_wait_time)
	printer(logo_outer, print_wait_time)
	printer("Text Processing and Divination Method", print_wait_time)
	print()
	time.sleep(pause_wait_time)

def print_menu():
	print("Menu:")
	time.sleep(pause_wait_time)
	print("1: Create a new list")
	time.sleep(pause_wait_time)
	print("2: See available lists")
	time.sleep(pause_wait_time)
	print("3: Divine")
	time.sleep(pause_wait_time)
	print("4: About TePADiM")
	time.sleep(pause_wait_time)
	print("5: Light a candle")
	time.sleep(pause_wait_time)
	print("6: Quit")
	time.sleep(pause_wait_time)
	print()

def menu_input():
	global done
	printer("Choose an option:", print_wait_time)
	print()
	user_input = input()
	if user_input == "1":
	    print()
	    create_list()
	elif user_input == "2":
		display_lists()
	elif user_input == "3":
		display_lists()
		divine()
	elif user_input == "4":
		print()
		printer("TePADiM is an oracular method.", print_wait_time)
		printer("It loves to crash if you give it incorrect filenames.", print_wait_time)
		print()
	elif user_input == "5":
	    candle()
	elif user_input == "6":
		print()
		print("Bye!")
		time.sleep(3)
		done = True
	else:
		print()
		print("Enter a real option!")
		print()

def main():
	global done
	print_title()
	while not done:
		print_menu()
		menu_input()

main()

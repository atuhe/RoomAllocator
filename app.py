"""
Usage:
    RoomAllocator create_room <room_type> <room_name>...
    RoomAllocator add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
    RoomAllocator print_room <room_name>...
    RoomAllocator print_allocations [<filename>]
    RoomAllocator load_people
    RoomAllocator save_state [<database_name>]
    RoomAllocator load_state <sqlite_database>
    RoomAllocator 
    RoomAllocator (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from app.dojo import *

dojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class RoomAllocator (cmd.Cmd):
    intro = 'Welcome RoomAllocator Application for Andela Kenya Dojo!' \
        + ' (type help for a list of commands.)'
    prompt = '(RoomAllocator) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]
        dojo.create_room(room_type, room_name)


    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <person_type> [<wants_accommodation>]"""
        first_name = arg['<first_name>']
        last_name = arg['<last_name>']
        person_type = arg['<person_type>']
        person_name = first_name + " " + last_name
        wants_accommodation = arg['<wants_accommodation>']

        if wants_accommodation is None:
            wants_accommodation = "N"
        dojo.add_person(person_name, person_type, wants_accommodation)


    @docopt_cmd
    def do_print_room(self, arg):
        """ Usage: print_room <room_name>..."""
        room_name = arg["<room_name>"]
        dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<filename>]"""
        x = arg['<filename>']
        dojo.print_allocations(x)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [<database_name>]"""
        db_name = arg['<database_name>']
        dojo.save_state(db_name)

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""
        database_name = arg['<sqlite_database>']
        dojo.load_state(database_name)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()
opt = docopt(__doc__, sys.argv[1:])
RoomAllocator().cmdloop()
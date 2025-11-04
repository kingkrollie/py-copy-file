def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        print("invalid command")
        return

    if command[1] == command[2]:
        print("same files")
        return

    if command[0] == "cp":
        try:
            with (open(command[1], "r") as file_in,
                  open(command[2], "w") as file_out):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            print("source file not found")
    else:
        print("invalid command")
        return

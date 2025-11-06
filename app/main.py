def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        return

    if command[1] == command[2]:
        return
    try:
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return

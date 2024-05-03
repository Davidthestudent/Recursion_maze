from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class MyMaze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str = ''):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string,
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is empty.
        """
        if len(maze_str) == 0:
            raise ValueError
        else:
            # We internally treat this as a List[List[str]], as it makes indexing easier.
            self._maze = list(list(row) for row in maze_str.splitlines())
            self._row_range = len(self._maze)
            self._col_range = len(self._maze[0])
            self._exits: List[Tuple[int, int]] = []
            self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        if start_row < 0 or start_row >= self._row_range or start_col < 0 or start_col >= self._col_range:
            raise ValueError("Start row and col out of bounds") # checking if starting point is okay
        if self._maze[start_row][start_col] != PATH:  # check if we can step on the cell
            raise ValueError
        if self._maze[start_row][start_col] == PATH:
            self._max_recursion_depth = max(self._max_recursion_depth, depth)
            if start_row == 0 or start_col == 0 or start_row == self._row_range - 1 or start_col == self._col_range - 1:  # check if the cell is an exit
                if self._maze[start_row][start_col] != EXIT:  # if we did not mark it early
                    self._maze[start_row][start_col] = EXIT  # we mark it as an exit
                    self._exits.append((start_row, start_col))  # add exit as a tuple to the list

            else: # if it is not an exit
                self._max_recursion_depth += 1
                if depth == 0:  # if the depth is 0 it is a start
                    self._maze[start_row][start_col] = START
                else:  # we mark it as a visited
                    self._maze[start_row][start_col] = VISITED
            for x, y in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                # checking all the directions
                next_row, next_col = start_row + x, start_col + y
                if (0 <= next_row < self._row_range and 0 <= next_col < self._col_range
                        and self._maze[next_row][next_col] == PATH):
                    # checking if we are able to step into the other cell
                    self.find_exits(next_row, next_col, depth + 1)  # recursive call

        # TODO

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__
def main():
    maze_15x15 = "###############\n"
    maze_15x15 += "#   #        ##\n"
    maze_15x15 += "# ## # # ## # #\n"
    maze_15x15 += "# ##   # ## # #\n"
    maze_15x15 += "#  ###### # ## \n"
    maze_15x15 += "# # ##  # #   #\n"
    maze_15x15 += "# #  # # ## # #\n"
    maze_15x15 += "# # #     # # #\n"
    maze_15x15 += "# # # # # # # #\n"
    maze_15x15 += "  # # ## # #  #\n"
    maze_15x15 += "# # #     # # #\n"
    maze_15x15 += "# # ###### #  #\n"
    maze_15x15 += "# # # #   # # #\n"
    maze_15x15 += "#   #   # #   #\n"
    maze_15x15 += "###############\n"
    maze_20x20 = "####################\n"
    maze_20x20 += "      #            #\n"
    maze_20x20 += "## ## # # ## # ## # \n"
    maze_20x20 += " # ##   # ## # ## # \n"
    maze_20x20 += "##  ###### # ### # #\n"
    maze_20x20 += " # # ##  # #    #  #\n"
    maze_20x20 += "## #  # # ## # ## # \n"
    maze_20x20 += " # # #     # #     #\n"
    maze_20x20 += "## # # # # # # # # #\n"
    maze_20x20 += " # # # ## # # # ## #\n"
    maze_20x20 += "## # #     #     # #\n"
    maze_20x20 += " # # ###### # ## # #\n"
    maze_20x20 += "## # # #   # # ##  #\n"
    maze_20x20 += " #   #   # # #   # #\n"
    maze_20x20 += "## # ###### # ## # #\n"
    maze_20x20 += " # # # #   # # # # #\n"
    maze_20x20 += "#    #   # # #   #  \n"
    maze_20x20 += " ### ######## ######\n"
    maze_20x20 += "## # #     #     # #\n"
    maze_20x20 += "# # ##  # #    #  ##\n"
    ans_15 = [(4, 14), (9, 0)]
    ans_20 = [(2, 19), (3, 19), (6, 19), (16, 19), (19, 17), (19, 16), (19, 14), (19, 13), (19, 12), (19, 11), (19, 9), (19, 7), (19, 6), (19, 3), (19, 1), (17, 0), (15, 0), (1, 0)]
    # Initialize Maze objects
    maze_15 = MyMaze(maze_15x15)
    maze_20 = MyMaze(maze_20x20)

    # Find exits for 15x15 maze
    maze_15.find_exits(1, 1)
    print("Exits for 15x15 maze:", maze_15._exits)
    print(ans_15 == maze_15._exits)

    # Find exits for 20x20 maze
    maze_20.find_exits(1, 1)
    print("Exits for 20x20 maze:", maze_20._exits)
    print(ans_20 == maze_20._exits)


if __name__ == "__main__":
    main()



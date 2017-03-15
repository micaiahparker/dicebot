from discord.ext.commands import command, group
from .cog import Cog
from random import choice

def get_column(i, grid):
    return [row[i] for row in grid]

def check_row(row):
    return row == "XXX" or row == "OOO"

def get_diags(grid):
    return ("".join(str(grid[x][y]) for x, y in [(0, 0), (1, 1),(2, 2)]),
            "".join(str(grid[x][y]) for x, y in [(0, 2), (1, 1),(2, 0)]))

class Board:
    def __init__(self):
        self.grid = [
            [' ' for _ in range(3)] for _ in range(3)
        ]
        self.turn = None

    def move(self, player:int, x:int, y:int):
        if self.grid[x][y] != ' ':
            raise Exception("taken")
        else:
            self.grid[x][y] = ['X', 'O'][player]

    def is_draw(self):
        for row in self.grid:
            for col in row:
                if col == ' ':
                    return False
        return True

    def is_won(self):
        for row in self.grid:
            if check_row("".join(str(x) for x in row)):
                return True

        for i in range(3):
            for col in get_column(i, self.grid):
                if check_row("".join(str(x) for x in col)):
                    return True

        for row in get_diags(self.grid):
            if check_row("".join(str(x) for x in row)):
                return True

        return False

    def convert(self, s):
        if s == " ":
            return ":eggplant:"
        if s == "X":
            return ":x:"
        if s == "O":
            return ":o:"
        return s

    def __str__(self):
        return "\n".join(''.join(self.convert(col) for col in row) for row in self.grid)

class TicTacToe(Cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.players = []
        self.i_turn = None
        self.turn = 0
        self.board = Board()

    @group(pass_context=True)
    async def tic(self, ctx):
        """plays tic tac toe, neat huh"""
        if not ctx.invoked_subcommand:
            pass

    @tic.command(aliases=['board'])
    async def show(self):
        await self.bot.say(self.board)

    @tic.command(pass_context=True)
    async def start(self, ctx):
        if not self.players:
            self.players.append(ctx.message.author)
            await self.bot.reply('Players: {}'.format(', '.join(str(p) for p in self.players)))
        else:
            await self.bot.reply('Game already started')

    @tic.command(pass_context=True)
    async def accept(self, ctx):
        if len(self.players) == 1:
            self.players.append(ctx.message.author)
            await self.bot.reply('Players: {}'.format(', '.join(str(p) for p in self.players)))
            self.i_turn = choice([0, 1])
            self.turn = self.players[self.i_turn]
            await self.bot.reply("{}'s turn".format(self.turn))
        else:
            await self.bot.reply('Either game not started or max players')

    @tic.command(pass_context=True)
    async def move(self, ctx, x:int, y:int):
        if not ctx.message.author == self.turn:
            await self.bot.reply('Not ur turn')
            return None
        try:
            self.board.move(self.i_turn, x, y)
            if self.board.is_draw():
                await self.bot.say('Draw!')
                self.end_game()

            elif self.board.is_won():
                await self.bot.say(self.board)
                await self.bot.say("{} won!".format(self.turn))
                self.end_game()
            else:
                await self.change_turn()
        except Exception as e:
            await self.bot.reply('try again')

    @tic.command(aliases=['players'])
    async def get_players(self):
        await self.bot.reply(', '.join(str(p) for p in self.players))

    @tic.command(aliases=['turn'])
    async def get_turn(self):
        await self.bot.reply(self.turn)


    async def change_turn(self):
            self.i_turn = (self.i_turn + 1) % 2
            self.turn = self.players[self.i_turn]
            await self.bot.reply('ur turn')
            await self.bot.say(self.board)

    def end_game(self):
        self.board = Board()
        self.players = []
        self.turn = None
        self.i_turn = 0

def setup(bot):
    bot.add_cog(TicTacToe(bot))

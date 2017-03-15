from discord.ext.commands import command, group
from .cog import Cog
from random import choice

def get_column(grid):
    for row in grid:
        yield [row[i] for i in range(len(row))]

def check_row(self, row):
    return row == "XXX" or row == "OOO"

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
                if col == ' '
                    return False
        return True

    def is_won(self):
        for row in self.grid:
            if check_row("".join(str(x) for x in row)):
                return True

        for col in get_column(self.grid):
            if check_row("".join(str(x) for x in col)):
                return True

        return False

    def __str__(self):
        return "```{board}```".format(board="\n".join(' '.join(col for col in row) for row in self.grid))

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
            await self.bot.reply(self.board)

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
                await self.bot.reply('Draw!')
                self.end_game()

            elif self.board.is_won():
                await self.board.reply(self.board)
                await self.bot.reply("{} won!".format(self.turn))
            else:
                await self.change_turn()
        except Exception:
            await self.bot.reply('try again')

    async def change_turn(self):
            self.i_turn = (self.i_turn + 1) % 2
            self.turn = self.players[self.i_turn]
            await self.bot.reply('{}\'s turn'.format(self.turn))
            await self.bot.reply(self.board)

    def end_game(self):
        self.board = Board()
        self.players = []
        self.turn = None
        self.i_turn = 0

    @tic.command()
    async def get_players(self):
        await self.bot.reply(', '.join(str(p) for p in self.players))

    @tic.command()
    async def get_turn(self):
        await self.bot.reply(self.turn)

def setup(bot):
    bot.add_cog(TicTacToe(bot))

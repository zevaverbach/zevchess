from zevchess.commands import recalculate_FEN, create_FEN_from_tokens
import zevchess.ztypes as t


def test_recalculate_FEN():
    state = t.GameState()
    move = t.Move(
        piece="p",
        src="b2",
        dest="b4",
    )
    oldFEN = state.FEN
    board = t.Board.from_FEN(state.FEN)
    newFEN = recalculate_FEN(state, move, board)
    assert newFEN != oldFEN


def test_recalculate_FEN_same_rank():
    state = t.GameState(FEN="rnb1kbnr/pppppppp/8/8/1R3q2/8/PPPPPPPP/1NBQKBNR")
    move = t.Move(
        piece="R",
        src="b4",
        dest="f4",
        capture=1,
    )
    board = t.Board.from_FEN(state.FEN)
    newFEN = recalculate_FEN(state, move, board)
    assert newFEN == "rnb1kbnr/pppppppp/8/8/5R2/8/PPPPPPPP/1NBQKBNR"


def test_recalculate_FEN_castling_kingside():
    state = t.GameState(FEN="rnbqkbnr/pppppppp/8/8/5BN1/8/PPPPPPPP/RNBQK2R")
    move = t.Move(
        castle="k",
    )
    board = t.Board.from_FEN(state.FEN)
    newFEN = recalculate_FEN(state, move, board)
    assert newFEN == "rnbqkbnr/pppppppp/8/8/5BN1/8/PPPPPPPP/RNBQ1RK1"


def test_recalculate_FEN_castling_kingside_2():
    fen = "2kr3r/p2pQ2p/1p2p3/8/5b2/P7/1N3PPP/4K2R"
    state = t.GameState(FEN=fen)
    move = t.Move(
        castle="k",
    )
    board = t.Board.from_FEN(state.FEN)
    newFEN = recalculate_FEN(state, move, board)
    assert newFEN == "2kr3r/p2pQ2p/1p2p3/8/5b2/P7/1N3PPP/5RK1"


def test_recalculate_FEN_castling_queenside():
    state = t.GameState(FEN="rnbqkbnr/pppppppp/8/2B5/3N4/4Q3/PPPPPPPP/R3KBNR")
    move = t.Move(
        castle="q",
    )
    board = t.Board.from_FEN(state.FEN)
    newFEN = recalculate_FEN(state, move, board)
    assert newFEN == "rnbqkbnr/pppppppp/8/2B5/3N4/4Q3/PPPPPPPP/2KR1BNR"


def test_recalculate_FEN_castling_queenside_only_rook_on_home_row():
    state = t.GameState(FEN="rnbqkbnr/pppppppp/8/4B3/1N2QBN1/8/PPPPPPPP/R3K2R")
    board = t.Board.from_FEN(state.FEN)
    move = t.Move(
        castle="q",
    )
    newFEN = recalculate_FEN(state, move, board)
    assert newFEN == "rnbqkbnr/pppppppp/8/4B3/1N2QBN1/8/PPPPPPPP/2KR3R"


def test_create_FEN_from_tokens():
    assert (
        create_FEN_from_tokens(["R", "N", "B", "Q", "BLANK", "R", "K", "BLANK"])
        == "RNBQ1RK1"
    )


def test_create_FEN_from_tokens_2():
    assert (
        create_FEN_from_tokens(
            ["BLANK", "BLANK", "K", "R", "BLANK", "BLANK", "BLANK", "R"]
        )
        == "2KR3R"
    )


def test_create_FEN_from_tokens_3():
    assert (
        create_FEN_from_tokens(["BLANK", "BLANK", "K", "R", "BLANK", "B", "N", "R"])
        == "2KR1BNR"
    )

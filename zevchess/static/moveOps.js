import { getPieceAt } from './boardOps.js';

export function doTheMoveSentCastle(move, side, board) {
  const rank = side === "black" ? 8 : 1; // it's this side that castled
  if (move.castle === "k") {
    board.movePiece(`h${rank}`, `f${rank}`, true)
  } else {
    board.movePiece(`a${rank}`, `d${rank}`, true)
  }
}

export function doTheMoveSentEnPassant(move, board, side) {
  const [file, rankStr] = move.dest;
  const rank = parseInt(rankStr);
  const sq = side === "black" ? `${file}${rank + 1}` : `${file}${rank - 1}`;
  board.setPiece(sq, null);
}

export function doTheMoveReceived(move, board, side) {
  if (move.castle) {
    const rank = side === "black" ? 1 : 8; // it's the other side that castled
    if (move.castle === "k") {
      board.movePiece(`e${rank}`, `g${rank}`, true)
      board.movePiece(`h${rank}`, `f${rank}`, true)
    } else {
      board.movePiece(`e${rank}`, `c${rank}`, true)
      board.movePiece(`a${rank}`, `d${rank}`, true)
    }
    return
  }
  const enPassant = move.capture === 1 && getPieceAt(move.dest, board) == null
  board
    .movePiece(move.src, move.dest, true).then(() => {
      if (enPassant) {
        const [file, rankStr] = move.dest;
        const rank = parseInt(rankStr);
        const sq = side === "black" ? `${file}${rank - 1}` : `${file}${rank + 1}`;
        board.setPiece(sq, null);
      // TODO: change this since there will noly be move.promote == 1
      } else if (move.promotion_piece) {
        const pp = move.promotion_piece;
        const piece = pp.toUpperCase() === pp ? `w${pp.toLowerCase()}` : `b${pp}`;
        board.setPiece(move.dest, piece);
      }
  });
}

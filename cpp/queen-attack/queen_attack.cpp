#include "queen_attack.h"

namespace queen_attack
{
    chess_board::chess_board(std::pair<int, int> white, std::pair<int, int> black)
    {
        if (white == black)
        {
            throw std::domain_error("Queens cannot occupy the same position");
        }
        if (white.first < 0 || white.second < 0)
        {
            throw std::domain_error("White Queen position must be positive");
        }
        if (black.first < 0 || black.second < 0)
        {
            throw std::domain_error("Black Queen position must be positive");
        }

        if (white.first > 7 || white.second > 7)
        {
            throw std::domain_error("White Queen position must be on the board");
        }

        if (black.first > 7 || black.second > 7)
        {
            throw std::domain_error("Black Queen position must be on the board");
        }
        this->white_queen = white;
        this->black_queen = black;
    }

    std::pair<int, int> chess_board::white() const
    {
        return this->white_queen;
    }

    std::pair<int, int> chess_board::black() const
    {
        return this->black_queen;
    }

    bool chess_board::can_attack() const
    {
        if (this->white_queen.first == this->black_queen.first)
        {
            // Same row
            return true;
        }
        if (this->white_queen.second == this->black_queen.second)
        {
            // Same column
            return true;
        }
        if (std::abs(this->white_queen.first - this->black_queen.first) == std::abs(this->white_queen.second - this->black_queen.second))
        {
            // Diagonal
            return true;
        }
        return false;
    }
} // namespace queen_attack

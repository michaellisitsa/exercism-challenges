#include "nucleotide_count.h"
#include <iostream>

namespace nucleotide_count
{
    const std::map<char, int> count(std::string dna_strand)
    {
        std::map<char, int> nucleotide = {{'A', 0}, {'C', 0}, {'G', 0}, {'T', 0}};
        for (const char nucleotide_char : dna_strand)
        {
            // std::cout << nucleotide_char << std::endl;
            if (nucleotide.find(nucleotide_char) == nucleotide.end())
            {
                throw std::invalid_argument("Invalid nucleotide");
            }
            else
            {
                nucleotide[nucleotide_char]++;
            }
        }
        return nucleotide;
    }
} // namespace nucleotide_count

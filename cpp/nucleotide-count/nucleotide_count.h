#if !defined(NUCLEOTIDE_COUNT_H)
#define NUCLEOTIDE_COUNT_H
#include <string>
#include <map>

namespace nucleotide_count
{
    const std::map<char, int> count(std::string dna_strand);
} // namespace nucleotide_count

#endif // NUCLEOTIDE_COUNT_H
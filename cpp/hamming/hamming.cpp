#include "hamming.h"
#include <stdexcept>
namespace hamming
{
    int compute(std::string a, std::string b)
    {
        // Make sure strings are the same length
        if (a.length() != b.length())
        {
            throw std::domain_error("Strings must be the same length.");
        }

        // For loop index of the length of string
        int hammingDistance = 0;
        int length = a.length();
        for (int i = 0; i < length; i++)
        {
            // If the character code is not the same add 1 to the counter
            if (a[i] != b[i])
            {
                hammingDistance++;
            }
        }
        // Return the counter (make sure its a value.)
        return hammingDistance;
    }
} // namespace hamming

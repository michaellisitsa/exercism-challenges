#include "nth_prime.h"
#include <math.h>
#include <stdexcept>

namespace nth_prime
{

    bool isprime(int num)
    {
        if (num == 2)
        {
            return true;
        }
        else if (num == 1 || num % 2 == 0)
        {
            return false;
        }

        // Check if num is divisible by any number from 3 to sqrt(num)
        // Exclude all evens because they're divided by 2.
        for (int i = 3; i <= sqrt(num); i++)
        {
            if (num % i == 0)
            {
                return false;
            }
        }
        return true;
    }

    int nth(int n)
    {
        int number = 0;
        int count = 0;
        if (n < 1)
        {
            throw std::domain_error("Invalid input");
        }
        while (count < n)
        {
            if (isprime(++number))
            {
                ++count;
            }
        }
        return number;
    }
} // namespace nth_prime
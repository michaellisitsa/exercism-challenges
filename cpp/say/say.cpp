#include "say.h"
#include <iostream>
#include <string>
#include <unordered_map>
#include <map>
#include <cmath>

namespace say
{
    std::string in_english(unsigned long long number)
    {
        std::unordered_map<int, std::string> singleDigitMap = {
            {0, "zero"},
            {1, "one"},
            {2, "two"},
            {3, "three"},
            {4, "four"},
            {5, "five"},
            {6, "six"},
            {7, "seven"},
            {8, "eight"},
            {9, "nine"}};

        std::unordered_map<int, std::string> teenMap = {
            {10, "ten"},
            {11, "eleven"},
            {12, "twelve"},
            {13, "thirteen"},
            {14, "fourteen"},
            {15, "fifteen"},
            {16, "sixteen"},
            {17, "seventeen"},
            {18, "eighteen"},
            {19, "nineteen"}};

        std::unordered_map<int, std::string> tensMap = {
            {2, "twenty"},
            {3, "thirty"},
            {4, "forty"},
            {5, "fifty"},
            {6, "sixty"},
            {7, "seventy"},
            {8, "eighty"},
            {9, "ninety"}};

        std::map<int, std::string> ordersOfMagnitudeMap = {
            {1, "thousand"},
            {2, "million"},
            {3, "billion"}};

        if (number < 10)
        {
            std::string result = singleDigitMap[number];

            return result;
        }
        else if (number < 20)
        {
            return teenMap[number];
        }
        else if (number < 100)
        {
            if (number % 10 == 0)
            {
                return tensMap[number / 10];
            }
            return tensMap[number / 10] + "-" + in_english(number % 10);
        }
        else if (number < 1000)
        {
            if (number % 100 == 0)
            {
                return in_english(number / 100) + " hundred";
            }
            return in_english(number / 100) + " hundred " + in_english(number % 100);
        }
        else if (number < 1000000000000L)
        {
            for (auto const &magnitude : ordersOfMagnitudeMap)
            {
                unsigned long long magnitudeValue = std::pow(1000, magnitude.first);
                if (number < magnitudeValue * 1000)
                {
                    if (number % magnitudeValue == 0)
                    {
                        return in_english(number / magnitudeValue) + " " + magnitude.second;
                    }
                    return in_english(number / magnitudeValue) + " " + magnitude.second + " " + in_english(number % magnitudeValue);
                }
                else
                {
                    continue;
                }
            }
        }
        else
        {
            throw std::domain_error("Number is too large");
        }

        return "";
    }
}

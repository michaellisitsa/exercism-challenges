#include "grade_school.h"
#include <algorithm>
namespace grade_school
{

    const std::map<int, std::vector<std::string>> school::roster() const
    {
        std::map<int, std::vector<std::string>> newMap = {};

        for (auto const &[key, val] : _roster)
        {
            auto copy = _roster.at(key);
            std::sort(copy.begin(), copy.end());
            newMap[key] = copy;
        }
        return newMap;
    }

    void school::add(std::string name, int grade)
    {
        _roster[grade].push_back(name);
    }

    const std::vector<std::string> school::grade(int grade) const
    {
        if (_roster.find(grade) == _roster.end())
        {
            return {};
        }
        else
        {
            auto copy = _roster.at(grade);
            std::sort(copy.begin(), copy.end());
            return copy;
        }
    }
} // namespace grade_school

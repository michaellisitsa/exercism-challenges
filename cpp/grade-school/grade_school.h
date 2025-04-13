#if !defined(GRADE_SCHOOL_H)
#define GRADE_SCHOOL_H
#include <vector>
#include <string>
#include <map>

namespace grade_school
{
    class school
    {
        std::map<int, std::vector<std::string>> _roster;
        // class members and methods go here
    public:
        const std::map<int, std::vector<std::string>> roster() const;

    public:
        void add(std::string name, int grade);

    public:
        const std::vector<std::string> grade(int grade) const;
    };

} // namespace grade_school

#endif // GRADE_SCHOOL_H
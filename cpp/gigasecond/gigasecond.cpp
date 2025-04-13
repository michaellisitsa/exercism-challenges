#include "gigasecond.h"

namespace gigasecond
{
    using namespace boost::posix_time;

    ptime advance(const ptime &start)
    {
        return start + seconds(1000000000L);
    }
} // namespace gigasecond

///
//
// LibSourcey
// Copyright (c) 2005, Sourcey <https://sourcey.com>
//
// SPDX-License-Identifier: LGPL-2.1+
//
/// @addtogroup symple
/// @{


#include "scy/symple/event.h"
#include "scy/util.h"


using std::endl;


namespace scy {
namespace smpl {


Event::Event()
{
    setType("event");
    setTime(::time(0));
}


Event::Event(const Event& root)
    : Message(root)
{
    // if (find("type") == end())
        setType("event");
    if (find("time") == end())
        setTime(::time(0));
}


Event::Event(const json::value& root)
    : Message(root)
{
    // if (find("type") == end())
        setType("event");
    if (find("time") == end())
        setTime(::time(0));
}


Event::~Event()
{
}


bool Event::valid() const
{
    return Message::valid()
        && find("name") != end();
}


std::string Event::name() const
{
    return value("name", "");
}


time_t Event::time() const
{
    return static_cast<time_t>(value("time", double(0)));
}


void Event::setName(const std::string& name)
{
    (*this)["name"] = name;
}


void Event::setTime(time_t time)
{
    (*this)["time"] = static_cast<double>(time);
    // DateTimeFormatter::format(
    //    Timestamp::fromEpochTime(time),
    //    DateTimeFormat::ISO8601_FORMAT);
}


} // namespace smpl
} // namespace scy


/// @\}
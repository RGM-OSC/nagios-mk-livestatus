// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// ails.  You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

#ifndef Store_h
#define Store_h

#include "config.h"  // IWYU pragma: keep
#include <list>
#include <map>
#include <string>
#include "LogCache.h"
#include "TableColumns.h"
#include "TableCommands.h"
#include "TableContactgroups.h"
#include "TableContacts.h"
#include "TableDownComm.h"
#include "TableHostgroups.h"
#include "TableHosts.h"
#include "TableLog.h"
#include "TableServicegroups.h"
#include "TableServices.h"
#include "TableStateHistory.h"
#include "TableStatus.h"
#include "TableTimeperiods.h"
#include "mk/Mutex.h"
#include "nagios.h"
class InputBuffer;
class OutputBuffer;
class Table;

class Store {
    LogCache _log_cache;
    TableContacts _table_contacts;
    TableCommands _table_commands;
    TableHostgroups _table_hostgroups;
    TableHosts _table_hosts;
    TableHosts _table_hostsbygroup;
    TableServicegroups _table_servicegroups;
    TableServices _table_services;
    TableServices _table_servicesbygroup;
    TableServices _table_servicesbyhostgroup;
    TableTimeperiods _table_timeperiods;
    TableContactgroups _table_contactgroups;
    TableDownComm _table_downtimes;
    TableDownComm _table_comments;
    TableStatus _table_status;
    TableLog _table_log;
    TableStateHistory _table_statehistory;
    TableColumns _table_columns;

    typedef std::map<std::string, Table *> _tables_t;
    _tables_t _tables;

    mk::mutex _command_mutex;

public:
    Store();
    ~Store();
    void registerHostgroup(hostgroup *);
    void registerComment(nebstruct_comment_data *);
    void registerDowntime(nebstruct_downtime_data *);
    bool answerRequest(InputBuffer *, OutputBuffer *);

private:
    Table *findTable(std::string name);
    void answerGetRequest(const std::list<std::string> &lines, OutputBuffer *,
                          const char *);
    void answerCommandRequest(const char *);
};

#endif  // Store_h

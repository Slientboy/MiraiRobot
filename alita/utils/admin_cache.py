# Copyright (C) 2020 - 2021 ProgrammingError. All rights reserved. Source code available under the AGPL.
#
# This file is part of MiraiRobot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from time import perf_counter

from cachetools import TTLCache

# admins stay cached for one hour
ADMIN_CACHE = TTLCache(maxsize=512, ttl=(60 * 60), timer=perf_counter)

# Curriculum - Web application for creating and managing educational curricula
# Copyright (C) 2010  The Ministry of Education, Science and Culture, Iceland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    content = models.TextField() # Markdown field
    goals = models.TextField() # Markdown field
    evaluation = models.TextField() # Markdown field
    level = models.IntegerField()
    credits = models.IntegerField()
    modification_date = models.DateTimeField()
    #version_number = 
    prerequisites = models.TextField()
    school = models.ForeignKey(School)
    author = models.ForeignKey(User)
    certifier = models.ForeignKey(User, related_name='certification_set')
    def course_id(self):
        return ''

    def __unicode__(self):
        return ''

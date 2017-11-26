#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Wecker: rpi zero + led lights + wecker code = wake up light that 
#  is controlled by a mysql database, via a webgui.
#
#  Wecker stems from the dutch words wekker which means alarm clock and 
#  weckpot which is the pot in which I put my wekker.
#  
#  Copyright 2017 maxbaeten <m.j.j.baeten@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import time
import datetime
import schedule
import math

import wiringpi
import MySQLdb

import sqlparam

duration = sqlparam.sunrisetime*60

class SettingsDatabase(object):

    def __init__(self):
        """ Init SettingsDatabase class in wecker module """
        
        self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
        self.previouschecksum = 0;
        
        # Connect to Wekker database 
        self.sqldb = MySQLdb.connect(host=sqlparam.dbservername,    # host
                                     user=sqlparam.dbusername,      # username
                                     passwd=sqlparam.dbpw,          # pw
                                     db=sqlparam.dbname)            # data base
        
        # Set autocommit is True to keep updated from all changes
        self.sqldb.autocommit(True)
        
        # Create database cursor 
        self.cur = self.sqldb.cursor()
        
        
    def update_settings(self):
        """ Checks if settings in the database have been updated

        Returns:
            True if changes have been applied
            False if no changes have been applied
        
        """
        
        self.cur.execute("CHECKSUM TABLE Wecker.Settings;");
        for row in self.cur.fetchall():
            currentchecksum = row[1]
        
        if currentchecksum != self.previouschecksum:
            
            # Clear all scheduled tasks
            schedule.clear()
            
            for _day_it in self.days:
                _cmd_str = "SELECT * FROM Wecker.Settings WHERE day = '" + _day_it + "'"
                self.cur.execute(_cmd_str)
                
                # Extract the enable and desired wakeup time                
                for row in self.cur.fetchall():
                    _enable_val = row[1]
                    _time_val = row[2]
                
                # Subtract duration to obtain start of sunrise time and convert to a datetime.time
                _startsunrise_time = _time_val - datetime.timedelta(seconds=duration);
                _startsunrise_time = (datetime.datetime.min + _startsunrise_time).time();
                _startsunrise_time_str = str(_startsunrise_time);
                
                if _enable_val:
                    print "schedule.every()." + _day_it + ".at('" + _startsunrise_time_str[0:5] + "').do(ll.sunrise)";
                    eval( "schedule.every()." + _day_it + ".at('" + _startsunrise_time_str[0:5] + "').do(ll.sunrise)");
            
            self.previouschecksum = currentchecksum
        
        
class LedLights(object):

    def __init__(self):
        """ Init LedLights class in wecker module """
        
        self.pwm_pin = 18
        self.pinMode = 2
        self.zero_intensity = 0
        self.min_intensity = 1
        self.max_intensity = 1024
        
        # Initiate PWM control of LED lights
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pwm_pin, self.pinMode)
        wiringpi.pwmWrite(self.pwm_pin,self.zero_intensity)

    def sunrise(self):
        """ Simulate rise of the sun """
        
        ii = 0;
        
        while (ii < duration):
            
            # Calculate intensity
            if (ii < 660):
                _intensity = math.ceil(-66000./(ii-660)-100)
                _intensity = min(_intensity,self.max_intensity)
            else:
                _intensity = 1024;
                
            wiringpi.pwmWrite(self.pwm_pin,int(_intensity))

            ii += 1;
            time.sleep(1)
        
        wiringpi.pwmWrite(self.pwm_pin,self.zero_intensity)

if __name__ == '__main__':
    """ Main """

    # Initiate LED Lights
    ll = LedLights()

    # Initiate Database
    db = SettingsDatabase()
        
    while True:
        
        # Update settings from MySQL database
        db.update_settings()
        
        # Run all scheduled tasks (Blocking Call)
        schedule.run_pending()
        
        # Repeat in 10 seconds
        time.sleep(0.1)


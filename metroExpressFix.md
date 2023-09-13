  This is what you need to do!


  [m0 users, download this file](https://github.com/Helmstk1/CircuitPython/blob/master/files/adafruit-circuitpython-metro_m0_express-en_US-7.3.2.uf2)

  [m4 users, download this file](https://github.com/Helmstk1/CircuitPython/blob/master/files/adafruit-circuitpython-metro_m4_airlift_lite-en_US-7.3.2.uf2)

  Then everybody downloads the version 7 library bundle [here](https://github.com/Helmstk1/CircuitPython/blob/master/files/adafruit-circuitpython-bundle-7.x-mpy-20230912.zip)

  To get rid of version 8 ( the buggy one), you need to:
  * double click the reset button
  * drag and drop the .uf2 file onto the METROBOOT drive.
  * Once your board resets, unzip / expand that library bundle, and replace your version 8 libraries with the ones from version 7.
  * Reload VS code, and hit F5
  * You're done!

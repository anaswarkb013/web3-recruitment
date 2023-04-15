# web3-recruitment
## Overview
A Car class is created with collision detection and time to collision calculation using coordinates and speed. Car is implememted as a rectangle in 2D coordinate space. Collision takes place when rectnagle of one car touch or overlap rectangle of another.  

## Attributes
***make***(string): make of the car

***model***(string): model of the car

***year***(int): year the car was made

***speed_x***(int): current speed in x direction

***speed_y***(int): current speed in y direction

***x***(int): x coordinate of centre of the car (set to 0 by default)

***y***(int): y coordinate of centre of the car (set to 0 by default)

***width***(int): width of rectangle of the car (set to 5 by default)

***length***(int): length of rectangle of the car (set to 10 by default)

## Methods

***accelerate_x***(speed_increment): increments speed_x by speed_increment

***accelerate_y***(speed_increment): increments speed_y by speed_increment

***brake_x***(speed_decrement): decrements speed_x by speed_decrement

***brake_y***(speed_decrement): decrements speed_y by speed_decrement

***move***(): increment x by speed_x and y by speed_y

***detect_collision***(car2): returns true if both x and y coordinates of the cars are overlapping, else false

***time_to_collision***(car2): returns time to collision by checking both time for x overlap and y overlap. In case of no collision returns -1

# SmartSystemController
A smart system controller designed for distribution on low-cost hardware.

# Design
+ Virtual network associated with Controllers
+ Virtual NAS (or similar distributed storage)
+ Flow of data: Sensor --> Controller Private Network <--> Storage Private Network
+ Redundency with fail-over (either load-balancing or active-standby for reliability) in controllers and physical storage.

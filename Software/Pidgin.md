## Don't Use pidgin to connect Lync (Skype for Business)
## See ~/dotfile/Linux/Lync.md

Setup
=====
* $ app-fast install pidgin-libnotify -y
* Tools -> Plugins -> History -> Check
* Tools -> Plugins -> Message Notification -> Check -> Configure Plugin
    * Check "Raise conversation"
    * Check "Present conversation"
* Tools -> Plugins -> Libnotify Popups
* Buddies -> Show -> Offline Buddies

Connect to Skype for business (AKA Lync)
=====
* $ app-fast install pidgin-sipe -> Add
    * Chage Protocol to "Office Communicator"
    * Username -> `Joeky_Zhan@asus.com`
    * Login -> `ASUS\Joeky_Zhan`
    * Server[:Port]: Leave empty
    * Connection type: Auto
    * User Agent(Optional): UCCAPI/15.0.4420.1017 OC/15.0.4420.1017
    * Authentication scheme(Optional): TLS-DSK

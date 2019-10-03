# SQLite3_Application_Database
A little fun with SQLite and the Twilio API to manage and search through databases.


This application was created with python but it uses database management with SQLite. SQLite is essentially SQL with a few missing features as far as querying. This application allows users to submit applications online to a database. It automatically queries users depending on their G.P.A as I have found out from some current applications. This was mainly to get an understanding of SQL and databases without going through the trouble of running a server on my computer.

I did want to implement a resume upload feature however I learned through research that you shouldn't be uploading files to databases so everything in this project ended a bit early. I did think about converting information into a binary file and uploading it but I am currently working on a Node webapp so I want to try out MongoDB and see if I can do some fun stuff with that!

I also used the Twilio API for fun. It was a bit frustrating with the Keys and the documentation being vague but after some hours or so I figured out the issue with the python library. The twilio API only checks for valid phone numbers on my program.

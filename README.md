# Inspiration
Walking around our communities, we often find them ruined by scattered garbage and waste, that requires looking after and cleaning up. One solution to this was often community park clean-ups, however, they often tend to be very inconstant, and difficult to initialize

# What it does
ReBug utilizes a flask and JS backend to communicate with firebase where it stores the information collected about an event request that is submitted by a user. This allows ReBug to create multiple volunteering opportunities for volunteers to sign up for, where their data is also collected and stored in the database. Besides that, we are utilizing firebase in order to store the images taken by the users at each location and utilizing the Google Maps API to help get a more accurate description of the location of an event.

# How we built it
We built it primarily with Flask, to create the website, and Firebase to upload images, store volunteer information in the database, store garbage location, using the Google Maps API.

# Challenges we ran into
Building ReBug we faced many challenges as we were new to web dev, having to learn how flask works and how to apply it for our own use. Besides that, we have almost no experience with JS which meant that any simple JS task often took a long while to complete and would result in errors and bugs we would have to fix and debug. Aside from that, using firebase's storage is something new to us, which took us a while to figure out and definitely slowed us down.

# Accomplishments that we're proud of
Despite the various setbacks, we were able to reach a somewhat functioning prototype for ReBug, that allows users to submit clean-up requests, and volunteers to sign up for events submitting their personal information. Additionally, we were able to store all the data on firebase, as well as retrieve the event info off of the real-time database to display the different events for any volunteers under the volunteer/events section. Furthermore, we are also extremely proud of what we have learned, as this challenged us into learning the basics of flask and javascript in a short period of time, and were still able to apply them effectively to create a functioning product for our submission.

# What we learned
Doing this project, we learned a lot about web dev. All of us being complete beginners at web dev, and barely even working on a back end before, this forced us outside of our comfort zones allowing us to grow our web development skills especially with respect to back end development as well as how to tie the back end and front end together to create a functioning web app/website. We are also proud that we learned a lot about the basics of flask and javascript as well as other frameworks and languages that we researched and thought about using before starting the project (such as reactjs, typescript, ajax, and angular).

# What's next for ReBug
Switching to React to make ReBug look nicer, as well as more functional. Implementing a login system for volunteers, with a dashboard to track their volunteer hours. Adding ML to ensure that images submitted, contain garbage in them, and prevent duplicates of an image from being uploaded.

# Built With
css3 - firebase - flask - html5 - javascript - python

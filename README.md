# RunHub

## Inspiration
Ever since college started, we have had difficulty finding enough time in our schedule for exercise. In our minds, running is the best option for a quick workout. RunHub is the solution to this issue, gathering data on the user, whether it be previous runtime data or their schedule via Google Calendar, in order to recommend an optimal running schedule for the week.

## What it does
When a user registers for RunHub, they are prompted to add their user information. Afterwards, they must choose their running goal:
- Get Faster -> increase mile time
- Build Stamina -> increase mileage per day
- Stay Fit -> maintain a constant exercise schedule

After the user chooses their running goal, a machine algorithm will focus on the goal. In order for the algorithm to work, it is fed the user's running data over time.

## How we built it
We used Figma to brainstorm and design the app, IMBz LinuxOne for the data analysis and machine learning aspect of the project, and other applications:
- [thispersondoesnotexist.com](https://thispersondoesnotexist.com/) to create Ron's profile picture
- [visualcrossing.com](www.visualcrossing.com/weather/weather-data-services) access via scripting to gather weather data

## Challenges we ran into
We had difficulty implementing and configuring the machine learning algorithm, primarily because there was not much data that we could use. We tried to use a dataset provided by user @yoda on data.world (https://data.world/yoda/running-since-1999). However, it would be more beneficial to gather more data. As an alternative, we created a calendar heatmap to determine the user's mileage per day and seaborn to analyze their average mileage.

## Accomplishments that we're proud of
We are proud of being able to create potential ideas for the app within 24 hours. Also, this was both of our first hackathons, and although it was difficult to accomplish the tasks that we planned on finishing by the end of it, we are happy that we managed to configure an idea that could easily be fleshed out more.

## What we learned
We learned:
- accessing IBMz systems and using its Jupyter notebook for machine learning
- Python packages: matplotlib, calplot, numpy, pandas, selenium
- Machine Learning Related packages: tensorflow, seaborn
- Designing applications/websites through Figma
- Project Planning

## What's next for RunHub
We plan on finishing the machine learning algorithm first. Then, we hope to expand RunHub into other running-related services such as path recommendations, path difficulty, suggested nearby running clubs/events, street traffic analyzer, etc.

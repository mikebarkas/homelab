# AutoCorp
The AutoCorp app is an application to demonstrate running a web app and an api backend using k8s.

"Automobile Corporation" is a fictitious company that sells automobiles. The sample web app displays a list of vehicles and the list can be searched by make or mileage.
The web app consumes data from an API and the data is stored with Postgres. 

The purpose of this application is to gain experience running separate containerized applications using different
programming languages and running the application in a Kubernetes environment.

### Web App
The website application is a small program written in Python that contains a few URLs to display a list
of vehicles. The web app runs in a custom container I created.

Github code repo: <a href="https://github.com/mikebarkas/auto-corp-web" target="_blank">https://github.com/mikebarkas/auto-corp-web </a>

Container repo:   <a href="https://hub.docker.com/r/mikebarkas/auto-corp-web/tags" target="_blank">https://hub.docker.com/r/mikebarkas/auto-corp-web/tags </a>

### Backend API
The backend API is a simple program written in Go to provide data to the frontend Python app. The API runs in
a custom container I created. The data is stored in a Postgres database container.

Github code repo: <a href="https://github.com/mikebarkas/auto-corp-api" target="_blank"> https://github.com/mikebarkas/auto-corp-api </a>

Container repo:   <a href="https://hub.docker.com/r/mikebarkas/auto-corp-api/tags" target="_blank"> https://hub.docker.com/r/mikebarkas/auto-corp-api/tags </a>

----

This project is not complete. Future work is planned to update and improve its features. 

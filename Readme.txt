Cloud Deployment

GCP:
To deploy and run Flask application on Google Cloud Platform (GCP), we can use Google Cloud App Engine as well.
First we need to download google cloud sdk install it and initialize it using command gcloud init or else we could deploy app through gcp cloud shell as well.
if we don't have project in our gcp account we can create new one with command gcloud projects create your-project-id
then set project gcloud config set project your-project-id
Now the file directory of our app should have app.yaml, requirements.txt, main.py.
app.yaml can be created at root of directory and contains configuration of our app engine settings like python version, scaling options,
target cpu utilization threshold. requirements.txt is a must file contains dependencies.
Now we can deploy our app using command gcloud app deploy. Now we can enter region.
once deployed we can access application wih the url generated.
Also, we can monitor our app and check logs using the Google Cloud Console:
App Engine Dashboard & Logs Viewer.


AWS:
For deploying the flask application which I have created we can use aws elastic beanstalk service to handle the deployments and autoscaling (if required) of application.
There we will select create application option and give the details like environment platform that is python in our case and pass the zip file as application.
Or use commands through EB CL
eb init -p python-3.9 pythonProject -> eb create pythonProject-env (create and deploy environment)-> eb open (to open app in web browser)
And once ready we can monitor logs and performance using aws cloudwatch as well.

Method 2(AWS):
Also we can create an ec2 instance with linux(ubuntu os) with minimum configuration as our application is simple post api request. And with proper security group inbound rules to allow http/https connection and create a ipv4 public ip. Then launch the instance. And then download ssh key to run the application through terminal same as local

Similarly, For azure we can use app service where it will handle the complete deployment of application and scaling as well.
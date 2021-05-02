# Assignment
Step 1:
 The input file is stored in a git repository and is cloned in the cloud shell
Step 2:
 A data storage bucket is created for the task
Step 3:
 The arrays a and b are ingested into the storage bucket
Step 4:
 A cloud function is created for combining and sorting the arrays
Step 5:
 The cloud function is deployed using the defined name and the parameters should be defined as below:
  --entry-point=inputs \
  --runtime python37 \            #Defining the runtime
  --trigger-http \                #The function will be triggered by a http request
  --timeout 180s \                #Given the time restriction of 180 seconds
  --allow-unauthenticated         #To allow unauthenticated access

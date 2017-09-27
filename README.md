# Google Cloud Dataproc PoC

Simple PoC to exercise some aspects of training pipeline automation in Cloud Dataproc:
 - Execute PySpark job with zipped package.
 - Have a better idea for build/deployment strategies.
 - Receive parameters on job execution.
 - Output using BigQuery.
 - Input/Output using GCS.
 - Cluster creation/deletion.

Based on sample pyspark script to be uploaded to Cloud Storage and run on Cloud Dataproc.

Note this file is not intended to be run directly, but run inside a PySpark environment.

## Create cluster
```
gcloud dataproc clusters create <cluster-name>
```

## Delete cluster
```
gcloud dataproc clusters delete my-dataproc-cluster-name
```

## Submit a job
```
gcloud dataproc --project=prj-retraining jobs submit pyspark ./pyspark_sort.py --cluster=refactoring-tests --py-files=my_package.zip -- prj-retraining up
```

## Wait for job execution
```
gcloud dataproc --project=prj-retraining jobs wait 2cc32cc3-2cc3-2cc3-2cc3-7bbdb79fd007
```

## Create tunnel
```
gcloud compute --project "prj-retraining" ssh --zone "us-central1-f" "refactoring-tests-m" --ssh-flag="-D" --ssh-flag="10000" --ssh-flag="-N" --ssh-flag="-n"
```

## Run pylint
```
pylint -f colorized -r y *
```

# Smart Classroom Assistant 1

This project aims to create a serverless cloud application that utilizes PaaS resources from Amazon Web Services (AWS) to provide a face recognition service for classroom assistants. Users can send videos of students in the classroom, and the application performs face recognition on the students while retrieving their academic information.

## Problem Statement

Managing attendance and accessing academic information for students in a classroom can be a time-consuming and challenging task. By leveraging AWS's serverless architecture, this project aims to create an efficient and cost-effective solution for these problems.

## Design and Implementation

<img width="611" alt="image" src="https://user-images.githubusercontent.com/22538269/235815708-99c2c861-6a5d-49b7-ab26-dd51da0c3387.png">

### AWS Services Used

1. **AWS Lambda (Serverless computing)**: Utilized for processing input videos and performing face recognition on them.
2. **AWS S3 (Simple Storage Service)**: Used to store the input videos and the output CSV files containing the recognized students' academic information.
3. **AWS DynamoDB (No-sql database)**: Stores the academic information of the students.

### Architecture Description

1. The user uploads videos of students to the S3 input bucket using the `workload_generator.py` script.
2. When a new video is uploaded, an AWS Lambda function is triggered, which executes the `handler.py` script.
3. The `handler.py` script extracts the first frame of the video, performs face recognition on it, and retrieves the recognized student's academic information from the DynamoDB table.
4. The script stores the academic information in a CSV file and uploads it to the S3 output bucket.
5. The user can access the academic information of the recognized students in the CSV file.

## Autoscaling

AWS Lambda automatically scales the function instances based on the number of incoming requests, ensuring efficient processing of multiple videos simultaneously.

## Testing and Evaluation

The application was tested with multiple input videos and evaluated based on the accuracy of face recognition and the correctness of the retrieved academic information.

## Code

### Files

- `Dockerfile`: Used to build the Docker container for the Lambda function.
- `handler.py`: Contains the Lambda function's logic, including frame extraction, face recognition, and DynamoDB interaction.
- `workload_generator.py`: A Python script used to upload test videos to the S3 input bucket.
- `encoding`: Contains the face recognition model encodings.
- `academic-info.json`: A JSON file containing the academic information of the students.

### Usage

1. Build and upload the Docker image to AWS ECR.
2. Run `python workload_generator.py` to upload test videos to the S3 input bucket.
3. Monitor the Lambda function logs and check the S3 output bucket for the generated CSV files containing the recognized students' academic information.

## Team Members

- Pranav Toggi
- Riyank Mukhopadhyay

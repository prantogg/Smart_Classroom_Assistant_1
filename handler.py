from fileinput import filename
from boto3
import face_recognition
import cv2
import pickle
import os

input_bucket = "inputbucketproj2"
output_bucket = "outputbucketproj2"
aws_access_key_id = "AKIARULFMIFK2EMF5RWV"
aws_secret_access_key = "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"


# Function to read the 'encoding' file
def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data
"""
def download_from_s3(aws_access_key_id, aws_secret_access_key, bucket_name):
	s3 = boto3_client('s3', aws_access_key_id, aws_secret_access_key)
	s3.download_file(bucket_name,'test_0.mp4','/tmp/test_0.mp4')
"""
def capture_frame(file):
	path = "/tmp/"
	os.system("ffmpeg -i " + str(file) + " -r 1 " + str(path) + "image-%3d.jpeg")
	print(os.system("ls /tmp/"))

def dynamo_db(face):

  dynamodb = boto3_client.resource('dynamodb', region_name=region)

  table = dynamodb.Table('my-table')

  response = table.get_item(Key={
    'name': face
  })
  return response


def face_recognition_handler(event, context):	
	filename = event['Records'][0]['s3']['object']['key']
	
	s3_url = "https://inputbucketproj2.s3.amazonaws.com/" + str(filename)
	
	capture_frame(s3_url)

	image_path = "home/riyank/cse546-project-lambda-master/test_cases/test_case_1/outputimage-001.jpeg"

    with open('/tmp/encoding', 'rb') as f:
		all_face_encodings = pickle.load(f)

	# Grab the list of names and the list of encodings
	face_names = list(all_face_encodings["name"])

	face_encodings = np.array(list(all_face_encodings["encoding"]))
	#print("fe: ------------------", face_encodings)

	# Try comparing an unknown image
	unknown_image = face_recognition.load_image_file("/home/riyank/cse546-project-lambda-master/test_cases/test_case_1/outputimage-001.jpeg")

	unknown_face = face_recognition.face_encodings(unknown_image)


	result = face_recognition.compare_faces(face_encodings, unknown_face)

	# Print the result as a list of names with True/False
	names_with_result = list(zip(face_names, result))

	#Print the unknown_face name as - First_Name Last_Name
	face=None
	for name, v in names_with_result:
		if(v==True):
			face = name
	
	response = dynamo_db(face)
	f = open("output.csv", "w")
	f.write(response['name']+', '+response['major']+', '+response['year'])
	f.close()

	#Push output.csv to S3 output bucket
	client = boto3.client("s3")

	client.upload_file("output.csv", "outputbucket", filename+".txt")


	






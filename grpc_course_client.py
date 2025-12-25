import grpc

import course_service_pb2
import course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

request = course_service_pb2.GetCourseRequest(course_id="api-course")
print(f"Отправляю запрос с course_id: {request.course_id}")

response = stub.GetCourse(request)
print(response)

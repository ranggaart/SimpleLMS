from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from core.models import Course, CourseContent, CourseMember, User


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def testing(request):

    guru = User.objects.create_user(
        username="Agus_sumanto",
        email="agus@gmail.com",
        password="Rahasia",
        first_name="agus",
        last_name="sumanto",
    )

    Course.objects.create(
        name="Pemrograman Python",
        description="Belajar Python",
        price=500000,
        teacher=guru,
    )

    return HttpResponse("KOSONGAN")


def allCourse(request):
    courses = Course.objects.all().select_related("teacher")
    data_resp = []
    for course in courses:
        record = {
            "id": course.id,
            "name": course.name,
            "price": course.price,
            "teacher": {
                "id": course.teacher.id,
                "username": course.teacher.username,
                "fullname": f"{course.teacher.first_name} {course.teacher.last_name}",
            },
        }
        data_resp.append(record)

    return JsonResponse(data_resp, safe=False)


def userProfile(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = Course.objects.filter(teacher=user)
    data_resp = {
        "username": user.username,
        "email": user.email,
        "fullname": f"{user.first_name} {user.last_name}",
    }
    data_resp["courses"] = []
    for course in courses:
        course_data = {
            "id": course.id,
            "name": course.name,
            "price": course.price,
            "description": course.description,
        }
        data_resp["courses"].append(course_data)

    return JsonResponse(data_resp, safe=False)


from django.db.models import Count, Min, Max, Avg


def courseStats(request):
    courses = Course.objects.all()
    statistics = courses.aggregate(
        course_count=Count("*"),
        min_price=Min("price"),
        max_price=Max("price"),
        avg_price=Avg("price"),
    )

    cheapest_list = Course.objects.filter(price=statistics["min_price"])
    expensive_list = Course.objects.filter(price=statistics["max_price"])
    popular_list = Course.objects.annotate(member_count=Count("coursemember")).order_by(
        "-member_count"
    )[:3]
    unpopular_list = Course.objects.annotate(
        member_count=Count("coursemember")
    ).order_by("member_count")[:3]
    data_resp = {
        "course_count": statistics["course_count"],
        "min_price": statistics["min_price"],
        "max_price": statistics["max_price"],
        "avg_price": statistics["avg_price"],
        "cheapest_courses": [course.name for course in cheapest_list],
        "expensive_courses": [course.name for course in expensive_list],
        "popular_courses": [course.name for course in popular_list],
        "unpopular_courses": [course.name for course in unpopular_list],
    }

    return JsonResponse(data_resp, safe=False)


def userCourseStats(request):
    # total user yang ada
    total_user = User.objects.all().count()

    # Jumlah user yang membuat course (terlibat dalam setidaknya satu course)
    users_with_courses = (
        User.objects.filter(coursemember__isnull=False).distinct().count()
    )

    # Jumlah user yang tidak memiliki course
    users_without_courses = User.objects.filter(coursemember__isnull=True).count()

    # Rata-rata jumlah course yang diikuti 1 user
    avg_courses_per_user = (
        CourseMember.objects.values("user_id")
        .annotate(course_count=Count("course_id"))
        .aggregate(avg_course=Avg("course_count"))["avg_course"]
    )

    # User yang mengikuti course terbanyak
    top_user = (
        CourseMember.objects.values(
            "user_id", "user_id__username"
        )  # Menggunakan user_id__username
        .annotate(course_count=Count("course_id"))
        .order_by("-course_count")
        .first()
    )

    top_user_name = top_user["user_id__username"] if top_user else None

    # List user yang tidak mengikuti course sama sekali
    users_without_enrollments = User.objects.exclude(
        id__in=CourseMember.objects.values_list("user_id", flat=True)
    ).values_list("username", flat=True)

    # Data response
    data_resp = {
        "total_user": total_user,
        "users_with_courses": users_with_courses,
        "users_without_courses": users_without_courses,
        "avg_courses_per_user": avg_courses_per_user,
        "top_user": top_user_name,
        "users_without_enrollments": list(users_without_enrollments),
    }

    return JsonResponse(data_resp)

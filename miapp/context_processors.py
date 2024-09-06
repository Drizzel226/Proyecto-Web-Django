def user_name(request):
    if request.user.is_authenticated:
        return {'user_name': request.user.first_name}  # o request.user.username o request.user.get_full_name()
    return {}

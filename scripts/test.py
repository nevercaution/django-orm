from db.models import User


def run(*script_args):

	user_list = User.objects.all()

	for user in user_list:
		print('name : ', user.name)
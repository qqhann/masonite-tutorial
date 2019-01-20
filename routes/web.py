"""Web Routes."""

from masonite.helpers.routes import get, post
from masonite.routes import RouteGroup as group
from masonite.routes import Get, Post

ROUTES = [
    get('/', 'WelcomeController@show').name('welcome'),

    # Blog routes
    group([
        get('/', 'BlogController@show'),
        post('/create', 'BlogController@store').name('store'),
    ], prefix='/blog', name='blog.'),
    group([
        get('/', 'PostController@show'),
        get('/@id', 'PostController@single').name('single'),
        get('/@id/update', 'PostController@update').name('update'),
        post('/@id/update', 'PostController@store'),
    ], prefix='/post', name='post.'),
]

# auth
ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
    Get().route('/email/verify', 'ConfirmController@verify_show'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    Post().route('/password', 'PasswordController@send'),
    Get().route('/password/@token/reset', 'PasswordController@reset'),
    Post().route('/password/@token/reset', 'PasswordController@update'),
]

""" A PostController Module """

from masonite.request import Request
from masonite.view import View

from app.Post import Post


class PostController:
    """PostController
    """

    def show(self, view: View):
        posts = Post.all()

        return view.render('posts', {'posts': posts})

    def single(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('single', {'post': post})

    def update(self, request: Request, view: View):
        post = Post.find(request.param('id'))

        return view.render('update', {'post': post})

    def store(self, request: Request):
        post = Post.find(request.param('id'))

        post.title = request.input('title')
        post.body = request.input('body')

        post.save()

        return 'post updated'

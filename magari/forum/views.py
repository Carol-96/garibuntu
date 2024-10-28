from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumThread, ForumPost, ForumReply
from .forms import ThreadForm, PostForm, ReplyForm
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
from datetime import timedelta


# List of all threads
def thread_list(request):
    threads = ForumThread.objects.all()
    return render(request, 'thread_list.html', {'threads': threads})

# Detail view for a thread, showing posts
def thread_detail(request, thread_id):
    thread = get_object_or_404(ForumThread, pk=thread_id)
    posts = thread.posts.all()  # Fetch all replies using the related name

    context = {
        'thread': thread,
        'posts': posts,
    }
    return render(request, 'thread_detail.html', context)

# Detail view for a thread, showing Replies
def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)
    replies = post.replies.all()  # Fetch all replies using the related name

    context = {
        'post': post,
        'replies': replies,
    }
    return render(request, 'thread_detail.html', context)

# Create a new thread
@login_required
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user
            thread.save()
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'create_thread.html', {'form': form})

# Create a new post within a thread
@login_required
def create_post(request, thread_id):
    thread = get_object_or_404(ForumThread, id=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('forum:thread_detail', thread_id=thread.id)
    return redirect('forum:thread_detail', thread_id=thread.id)

# Create a reply to a specific post
@login_required
def create_reply(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.created_by = request.user
            reply.save()
            return redirect('forum:thread_detail', thread_id=post.thread.id)
    return redirect('forum:thread_detail', thread_id=post.thread.id)



# Moderating the Forum
def is_moderator(user):
    # Replace with your actual moderator check logic
    return user.is_staff or user.is_superuser

@user_passes_test(is_moderator)
def lock_thread(request, thread_id):
    thread = get_object_or_404(ForumThread, id=thread_id)
    thread.is_locked = True
    thread.save()
    return redirect('forum:thread_detail', thread_id=thread.id)

@user_passes_test(is_moderator)
def unlock_thread(request, thread_id):
    thread = get_object_or_404(ForumThread, id=thread_id)
    thread.is_locked = False
    thread.save()
    return redirect('forum:thread_detail', thread_id=thread.id)

@user_passes_test(is_moderator)
def delete_thread(request, thread_id):
    thread = get_object_or_404(ForumThread, id=thread_id)
    thread.is_deleted = True
    thread.save()
    return redirect('forum:thread_list')

# Enabling Thread/Post Editing by Users
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id, created_by=request.user)
    if timezone.now() > post.created_at + timedelta(minutes=15):
        return redirect('forum:thread_detail', thread_id=post.thread.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('forum:thread_detail', thread_id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/edit_post.html', {'form': form})